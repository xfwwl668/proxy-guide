# 06 · deploy-vercel 免费版

> 仓库：https://github.com/vvxw/deploy-vercel
> 一句话：零成本跑在 Vercel 上，但代价是：**没有 sing-box 内核**（协议是手写的 JS）、只走 WebSocket、**必须套反代才能用**。
> 这是 5 个项目里原理最特殊的一个，部署前先看懂它是怎么工作的。

## 技术原理（和前四个完全不同）

前四个跑的是真正的 sing-box 内核。这个不是：`index.js`（约 1000 行）里用纯 Node.js **手写**了 VLESS / Trojan / Shadowsocks 的协议解析，没有任何第三方代理内核（`package.json` 依赖只有 `ws`、`axios`、grpc 相关和 `systeminformation`）。

运行模型：
- Vercel 把所有请求打到 `index.js`（`vercel.json` 里 `routes` 全转发，`regions: ["sin1"]` 新加坡，函数最长跑 300 秒）；
- 只监听**一条** WebSocket 路径（默认 UUID 前 8 位），收到第一条消息后按特征字节分流：像 VLESS 的走 VLESS 解析、像 Trojan 的走 Trojan 解析、像 SS 地址头的走 SS 解析，对不上直接断开；
- 握手通过后，用 `net.connect()` 从 Vercel 实例向目标网站发起 TCP 连接，再把两边对接起来；
- 函数内部全是明文 HTTP/WS，TLS 由 Vercel 边缘或反代层终止——所以订阅链接里 `security=tls` 指的是外层。

附带功能（源码证实）：
- **防滥用**：硬编码屏蔽了 10 个测速域名（speedtest.net、fast.com 等），命中直接断开；
- **哪吒 agent**：用 grpc 手写了全套 proto（上报系统状态、终端、文件管理），`package.json` 叫 `nzws-js` 就是"哪吒+WebSocket 的 JS 实现"的意思。但 serverless 函数是按次调用的，常驻 `while(true)` 上报循环跑不起来——所以"哪吒不亮不用填"是结构性必然，不是 bug。

## 支持的协议（只有 3 种，全走 WS）

| 协议 | 订阅形式 | 说明 |
|---|---|---|
| VLESS | `vless://UUID@域名:443?type=ws&path=/xxxx` | `encryption=none`，UUID 即凭证，有校验 |
| Trojan | `trojan://UUID@域名:443?type=ws&path=/xxxx` | 密码即 UUID，校验 `sha224(UUID)`，有校验 |
| Shadowsocks | `ss://base64("none:UUID")@域名:443?plugin=v2ray-plugin…` | **method=`none`（无加密），且服务端不校验任何凭证**，全靠 WS 路径保密 |

没有 Reality、Hysteria2、TUIC、gRPC，没有 UDP。能接受"纯 WS + 无 UDP"再往下看。

## 适合谁

- 一分钱不想花、能接受折腾反代的人
- 只需要轻量浏览，对协议丰富度、UDP、稳定性要求不高的人
- 想研究"serverless 上怎么跑代理"的人（代码本身是很好的学习材料）

## 准备什么

- [ ] GitHub 账号、Vercel 账号、Cloudflare 账号（Workers 或 Snippets 用来反代）
- [ ] 一个你自己的域名（反代用）
- [ ] 生成一个 UUID（**必须改**，默认的是公开仓库里的公开值，不改等于把节点送人；且 WS 路径是 UUID 前 8 位，可被推算）

## 操作步骤

1. 点仓库 "Use this template" 建**私密仓库**（防 UUID 泄露）。
2. 改环境变量（二选一）：**直接改 `index.js` 里的默认值**，或去 Vercel 控制台 → Settings → Environment Variables 里设置（代码是 `process.env.X || 默认值`，两种都生效）。核心是要改 `UUID`，以及部署后要填的 `DOMAIN`。
3. （可选）用 AI 生成一个纯 html 页替换 `index.html`（伪装页，`/` 路径返回的就是它；当前是个英文环保主题占位页）。
4. Vercel → New Project → Import 该仓库 → Install Command 填 `npm install` → Deploy。想换地区改 `vercel.json` 的 `regions`（默认 `sin1` 新加坡）。
5. 用 Cloudflare Workers/Snippets 把你自己的域名反代到 `xxx.vercel.app`（README 里给了 Worker 脚本，路径透传即可），然后把**反代后的域名**填进 `DOMAIN`。
6. 访问 `https://你的反代域名/vercel` 拿订阅（base64 的三行节点）。

> 💡 README 还提到用 jshaman.com 混淆 `index.js` 再保存，这是为了躲 Vercel 的滥用检测，属于经验操作，源码层面无从证实。

## 为什么必须反代（源码层面）

- 不填 `DOMAIN` 时，代码会去抓 Vercel 出口 IP，生成 `IP:3000` + `security=none` 的明文订阅——Vercel 只通过自家边缘域名提供 443 入站，`IP:3000` 从公网根本连不上。**无论"墙不墙"，不填 DOMAIN 就没有可用节点**。
- 反代的 Worker 脚本和 `index.js` 是咬合的：脚本做路径透传，而 `index.js` 的路由（`/`、`/vercel`、WS 路径）全按路径判断、不校验 Host，所以透传路径就能工作；订阅里的 `sni`/`host` 填反代域名，由反代层终止 TLS。

## 成功标准（对照打勾）

- [ ] `https://你的反代域名/` 能打开伪装页
- [ ] `https://你的反代域名/vercel` 能拿到 base64 订阅，解开是 3 行节点
- [ ] 把节点 `address` 换成优选 IP/域名后（延迟更低），客户端能连通
- [ ] 按 [docs/07](07-客户端使用-订阅导入.md) 最后一节验证，确认真的能用

## 环境变量真相（以 `index.js` 源码为准）

| 变量 | 源码默认值 | 说明 |
|---|---|---|
| `UUID` | `d1cf4b9c-3e57-085d-b34a-797fcf601381` | **公开值，必须改**；三协议共用；同时决定默认 WS 路径 |
| `WSPATH` | UUID 前 8 位 | 三协议共用这一条 WS 路径 |
| `DOMAIN` | `your-domain.com` | **核心变量**，填反代后的域名；不填则订阅不可用 |
| `SUB_PATH` | `vercel` | 订阅路径：`https://DOMAIN/vercel` |
| `NAME` | `Vercel` | 节点名前缀，实际输出 `Vercel-国家-ISP`（取订阅时实时查 geoip） |
| `PORT` | `3000` | 仅函数内部监听，在 Vercel 上对外无意义 |
| `NEZHA_SERVER` / `NEZHA_KEY` | 空 | 任一为空则 agent 直接跳过；填了也大概率不亮（见上） |
| `AUTO_ACCESS` | `false` | ⚠️ 为 `true` 会把**含 UUID 的订阅链接** POST 给第三方 `oooo.serv00.net/add-url`，README 没提，**别开** |
| `SHOW_LOG` | 关闭 | 设任意值开启详细日志 |

小 bug：`getip()` 失败兜底时会拼出 `cahnge-your-domain.com`（拼写错误），网络抖动时可能产出垃圾订阅，重新取一次即可。

## 出问题怎么办

| 症状 | 先查 |
|---|---|
| 订阅是 `IP:3000` 明文链接 | `DOMAIN` 没填或没生效，填反代域名 |
| 反代域名打不开 | Worker 脚本里的 `xxx.vercel.app` 是否换成你自己的；Vercel 项目是否部署成功 |
| 节点超时 | 换优选 IP/域名填到 `address`；确认反代链路本身通（先 curl 反代域名） |
| 订阅偶尔变成垃圾域名 | `cahnge-your-domain.com` 拼写 bug，重取订阅 |
| 哪吒不亮 | 结构性问题，别折腾，空着就行 |
| Vercel 封号/项目被删 | 代理类项目违反 Vercel 可接受使用政策，有这个风险；换号或换方案 |

## 卸载 / 清理

Vercel 控制台删掉该 Project，GitHub 删掉仓库（私密仓库删之前确认 UUID 已作废）。

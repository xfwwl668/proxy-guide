# 03 · sbx-native 原生启动器

> 仓库：https://github.com/xfwwl668/sbx-native
> 一句话：没有 root、装不了 systemd 的免费容器也能跑——把 sing-box、cloudflared、哪吒全塞进**一个进程**里，用线程方式运行。

## 先理解原理（只看这一段也行）

普通方案是下载 3 个二进制文件各起一个进程。sbx-native 把它们编译成 `.so` 动态库，主程序（Java / Node.js / Python 任选其一）在**守护线程**里加载运行。所以 `ps` 只能看到一个进程，容器平台杀进程也只认这一个，特别适合 PaaS 免费容器（Koyeb、Render 等）。

启动后它会做这些事（源码 14 步，简述关键的）：
1. 从 `oooen.com`（失败换 `ssss.nyc.mn`）按架构下载 `sbx.so`（sing-box）、`bot.so`（cloudflared）、`v1.so`/`agent.so`（哪吒）；
2. 按你填的端口变量生成 sing-box 的 `config.json`；
3. 生成节点链接 → 写 `sub.txt`（base64 订阅）+ `list.txt`（明文）→ 打印到日志；
4. 起 HTTP 服务：`GET /sub` 返回订阅，`GET /` 返回伪装页；
5. **45 秒后删掉运行目录里除 `keypair.properties` 和 `sub.txt` 之外的一切**（包括刚下载的 `.so`）。

第 5 步是重点：**每次重启都要重新下载 `.so`**，下载源挂了或限流就起不来。这是单进程方案的代价。

## 适合谁

- 只有免费 PaaS 容器 / 无 root 主机的人
- 想一个进程搞定、不想管 systemd 的人
- 会选 Java / Node.js / Python 其中一种环境的人（**推荐 Java 版**，见下）

## 三个语言版怎么选（源码级差异）

协议层面三者 100% 一致，差异全在工程细节：

| 维度 | Java（推荐） | Python | Node.js（坑最多） |
|---|---|---|---|
| native 调用 | JNA | ctypes | koffi |
| 哪吒 v0（`NEZHA_PORT` 方式） | ✅ 支持 | ✅ 支持 | ❌ **不支持**，设了反而启动失败 |
| 端口合法性校验 | 严格（1–65535） | 字符串非空即算数 | 字符串非空即算数 |
| keypair/证书校验 | 校验公私钥是否匹配 | 用 SSL 真实校验 | 只判文件存在 |
| `.env` 文件 | 自带解析，**优先级高于系统环境变量** | 不读（文档明确说了） | 尝试读 dotenv，缺包则忽略 |
| HTTP 端口被占 | 打日志跳过，不启动 HTTP | 直接抛错退出 | 自动 +1 重试 5 次 |
| 保活上报地址 | `oooo.serv00.net` | `oooo.serv00.net` | `keep.gvrander.eu.org`（不一样） |
| WARP 分流 | netflix + openai | 只有 netflix | netflix + openai |

结论：**无脑选 Java 版**。Node 版功能最残（v0 哪吒是坏的），除非你的容器只有 Node 环境。

## 支持的协议（填端口才开）

| 协议 | 开关变量 | 认证 | 说明 |
|---|---|---|---|
| VMess + WS | 无（恒开，监听 `ARGO_PORT`） | UUID | 走 Argo 隧道对外；`DISABLE_ARGO=true` 时不生成节点 |
| VLESS + Reality | `REALITY_PORT` | UUID | flow `xtls-rprx-vision`，SNI `www.iij.ad.jp`，密钥存 `keypair.properties` 复用 |
| Hysteria2 | `HY2_PORT` | 密码=UUID | 自签证书，客户端开"跳过证书验证" |
| TUIC | `TUIC_PORT` | UUID | 同上，拥塞控制 bbr |
| AnyTLS | `ANYTLS_PORT` | 密码=UUID | 同上 |
| SOCKS5 | `S5_PORT` | 用户名 UUID 前 8 位，密码后 12 位 | 不走 TLS，别暴露到公网 |

另有一个 WireGuard（Warp）**出站**，只做分流（Netflix 必走，YouTube 按需），不是对外服务的协议。

## 准备什么

- [ ] 一个能跑 Java 17+ / Node 16+ / Python 3 的容器或主机
- [ ] 生成一个 UUID（必须自己改，见下）
- [ ] （可选）哪吒面板、Argo 固定隧道、TG 推送，同其他项目

## 操作步骤

按仓库的 [JAVA.md](https://github.com/xfwwl668/sbx-native/blob/main/JAVA.md) / NODE.md / PYTHON.md 来，大流程：

```bash
# Java 版示例
# 1. 上传 java/ 目录，mvn package 打出 server-1.0.jar（或直接用仓库 Actions 构建好的）
# 2. 设置环境变量后运行
UUID=你生成的uuid PORT=3000 java -jar server-1.0.jar
```

## 成功标准（对照打勾）

- [ ] 日志里打印出绿色节点链接（base64 那串）
- [ ] 浏览器打开 `http://你的域名:3000/sub` 能拿到订阅
- [ ] 客户端导入后节点可用（HY2/TUIC/AnyTLS 记得开"跳过证书验证"）

## 环境变量真相（源码为准，文档有错）

| 变量 | 源码默认值 | 真相 |
|---|---|---|
| `UUID` | Java `53b16e96-…` / Python、Node `0a6568ff-…` | **三版各不相同**，且都是公开值，必须自己改；空字符串会被视为"没填"而回退默认值 |
| `CFIP` | Java `cf.877774.xyz` / Python `spring.io` / Node `saas.sin.fan` | 三版各不相同，文档统一写 `saas.sin.fan` 只对 Node 版成立 |
| `FILE_PATH` | Java `.tmp` / Python `.cache` / Node `.npm` | 三版各不相同 |
| `SHOW_LOG` | `true` | `false`/`disable`/`no` 才关日志；**主 README 写成 `DSHOW_LOG` 是拼写错误**，按源码的 `SHOW_LOG` 填 |
| `PORT` | `3000` | HTTP 订阅端口 |
| `ARGO_PORT` | `8001` | 固定隧道 token 模式需与 CF 后台一致 |
| `SUB_PATH` | `sub` | 订阅路径 |
| `DISABLE_ARGO` | `false` | `true` 则不下 cloudflared、不生成 vmess 节点 |
| `AUTO_ACCESS` | `false` | 保活开关，`true` 才上报（上报地址见上表，Node 版不一样） |
| `YT_WARPOUT` | `false` | `true` 强制 YouTube 走 Warp |

完整变量表见 [docs/09](09-环境变量总表.md)。

## 出问题怎么办

| 症状 | 先查 |
|---|---|
| 启动后 45 秒 `.so` 被删，下次起不来 | 下载源是否可达（`oooen.com` / `ssss.nyc.mn`）；离线环境别用这个项目 |
| Node 版哪吒 agent 起不来 | 是否设了 `NEZHA_PORT`——Node 版 v0 是坏的，改用 v1（只填 SERVER+KEY）或换 Java 版 |
| `/sub` 返回空 | 是否用了 `REALITY_PORT=abc` 这类非法端口：py/node 会生成 keypair 但不加 inbound，java 直接忽略 |
| 端口冲突 | Java 版会静默跳过 HTTP（日志里找），py 版直接退出，node 版自动 +1 |
| HY2/TUIC 连不上 | 客户端"跳过证书验证"开了没（自签证书） |

## 卸载 / 清理

杀掉主进程即可（单进程，无残留服务）。删掉运行目录（`.tmp`/`.cache`/`.npm`，看你用的哪版）。

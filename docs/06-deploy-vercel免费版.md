# 06 · deploy-vercel 免费版

> 仓库：https://github.com/vvxw/deploy-vercel（已验证存在）
> 一句话：部署到 Vercel 白嫖，支持 VLESS WS+TLS、Trojan WS+TLS、Shadowsocks WS。
> 代价是步骤最多：还要配 Cloudflare Worker 反代。

> ⚠️ 原版表格里写的 `vvqx/deploy-vercel` 是错的（404），正确的是 `vvxw/deploy-vercel`。

## 适合谁

- 没 VPS、没游戏机，只想白嫖的人
- 能接受折腾 Cloudflare Worker 反代的人
- 对速度要求不高、能接受免费额度限制的人

## 准备什么

- [ ] GitHub 账号、Vercel 账号、Cloudflare 账号（都要）
- [ ] 生成一个 UUID
- [ ] 一个自己的域名（可选，反代绑定自定义域名用，没有就用 workers.dev 的）

## 为什么需要反代？

Vercel 分配的 `*.vercel.app` 域名在部分地区可能无法直接访问，
所以要套一层 Cloudflare Worker 反代，再绑自己的域名（或 workers.dev 域名）给客户端用。

流程：客户端 → CF Worker（反代）→ Vercel 节点 → 优选域名/IP → 目标网站

## 操作步骤

### 步骤 1：Fork 仓库

1. 打开 https://github.com/vvxw/deploy-vercel
2. 点右上角 **Use this template**（或 Fork）
3. 建一个新仓库，**建议私有**，名字随意

### 步骤 2：改环境变量

1. 打开 `index.js`
2. 改第 1~30 行的环境变量（UUID、DOMAIN、WSPATH 等，不用的留空）
3. 保存

### 步骤 3：替换伪装网页（可选但建议）

1. 用 AI 生成一个纯 HTML 网页（假装是个普通网站）
2. 替换掉 `index.html`
3. 保存

### 步骤 4：部署到 Vercel

1. 打开 Vercel 控制台 → **New Project**
2. Import 你的仓库，默认配置
3. Install Command 设为 `npm install`
4. 点 **Deploy**，等部署完成，记下分配的 `xxx.vercel.app` 域名

### 步骤 5：CF Worker 反代

1. Cloudflare 控制台 → Workers → **Create Worker**，起个名
2. 粘贴反代代码（把 `xxx-xxx.vercel.app` 换成你的 Vercel 域名）：

```js
export default {
  async fetch(request, env) {
    let url = new URL(request.url);
    if (url.pathname.startsWith('/')) {
      var arrStr = [
        'xxx-xxx.vercel.app', // 你的 Vercel 域名
      ];
      url.protocol = 'https:'
      url.hostname = getRandomArray(arrStr)
      let new_request = new Request(url, request);
      return fetch(new_request);
    }
    return env.ASSETS.fetch(request);
  },
};

function getRandomArray(array) {
  const randomIndex = Math.floor(Math.random() * array.length);
  return array[randomIndex];
}
```

3. 点 **Deploy**，等约 1 分钟，复制 Worker 的 URL（如 `abc.workers.dev`）
4. （可选）有自己域名的话：Workers → Settings → Custom Domain 绑定
5. 把反代后的域名填回 `index.js` 的 `DOMAIN` 变量，重新部署 Vercel

> 原版提到用 jshaman 混淆 index.js，这是可选的防扫操作，不混淆也能跑。

## 成功标准

- [ ] Vercel 部署成功，`xxx.vercel.app` 能打开伪装网页
- [ ] Worker URL 能打开同样的伪装网页（说明反代通了）
- [ ] 订阅链接可访问，客户端导入后出现 3 种协议的节点
- [ ] 按 [docs/07](07-客户端使用-订阅导入.md) 最后一节验证可用

## 环境变量

| 变量 | 说明 |
|---|---|
| `UUID` | ★ 节点身份证 |
| `DOMAIN` | 反代后的域名（Worker 域名或自定义域名） |
| `WSPATH` | WS 路径 |
| `SUB_PATH` | 订阅路径 |
| `NAME` | 节点名称 |
| `PORT` | 端口 |
| `NEZHA_SERVER` / `NEZHA_KEY` | 哪吒监控 🔑 |
| `AUTO_ACCESS` | 自动保活 |
| `SHOW_LOG` | 显示日志 |

## 出问题怎么办

| 症状 | 先查 |
|---|---|
| Vercel 部署失败 | 看部署日志，多为 `index.js` 变量格式问题 |
| 反代后打不开 | 检查 Worker 是否部署成功、域名填对没 |
| 延迟变高 | 免费 CF Worker 绕路正常；换优选域名试试 |
| 反代域名被墙 | 换个 Worker 域名或自定义域名，重新部署 |

## 免费额度提醒

- Cloudflare Workers 免费版：每天 10 万次请求，个人用一般够
- Vercel 免费版有流量和构建时长限制，超了会限速或停服
- 别指望免费方案有多稳，挂了就重建一个

## 卸载 / 清理

Vercel 控制台删项目，Cloudflare 删 Worker 即可。

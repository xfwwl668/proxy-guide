# 02 · Sing-box 一键脚本（新手推荐）

> 仓库：https://github.com/xfwwl668/Sing-box（已验证存在）
> 一句话：复制粘贴一条命令，VLESS Reality + VMESS WS+Argo + HY2 + TUIC 四个协议一次装好。

## 适合谁

- 有 VPS（Ubuntu / CentOS / Debian / Alpine）的人
- 有 Serv00 / CT8 游戏机的人
- 第一次部署，只想最快跑起来的人

## 准备什么

- [ ] 一台 VPS（需要 root 权限），或 Serv00 / CT8 账号
- [ ] 生成一个 UUID（在线搜 "UUID 生成器"，复制一个）
- [ ] （可选）哪吒面板地址 + KEY，想监控才需要
- [ ] （可选）Argo 固定隧道的域名 + 凭据，想长期稳定才需要；不填就用临时隧道

## 操作步骤

### VPS 一键安装

```bash
# 最简：全默认
bash <(curl -Ls https://raw.githubusercontent.com/xfwwl668/Sing-box/main/sing-box.sh)

# 带参数：指定端口和优选
PORT=443 CFIP=www.visa.com.tw CFPORT=443 bash <(curl -Ls https://raw.githubusercontent.com/xfwwl668/Sing-box/main/sing-box.sh)
```

### Serv00 / CT8 一键安装

```bash
# 交互式（会问你几个问题）
bash <(curl -Ls https://raw.githubusercontent.com/xfwwl668/Sing-box/main/sb_serv00.sh)

# 全自动（不问问题，用默认值）
bash <(curl -Ls https://raw.githubusercontent.com/xfwwl668/Sing-box/main/sb4.sh)
```

带参数的全自动示例（把 `xxx` 换成你自己的）：

```bash
CHAT_ID=xxx \
BOT_TOKEN=xxx \
NEZHA_SERVER=nz.example.com \
NEZHA_PORT=5555 \
NEZHA_KEY=xxx \
ARGO_DOMAIN=abc.2go.com \
ARGO_AUTH='xxx' \
bash <(curl -Ls https://github.com/xfwwl668/Sing-box/releases/download/00/sb4.sh)
```

> ⚠️ 上面的 `xxx` 是**密钥**，填你自己的，别用别人的，也别截图发出来。

## 成功标准（对照打勾）

- [ ] 脚本跑完没报错，输出了订阅链接（类似 `http://你的IP:端口/sub`）
- [ ] 浏览器能打开订阅链接，看到一串节点信息（不是空白页）
- [ ] 客户端导入订阅后，节点列表里出现了 4 个协议的节点
- [ ] 选一个节点测延迟，能返回数字（不是超时）
- [ ] 按 [docs/07](07-客户端使用-订阅导入.md) 最后一节验证，确认真的能用

## 环境变量（常用）

| 变量 | 必填 | 说明 | 示例 |
|---|---|---|---|
| `UUID` | ★ | 节点身份证，每节点唯一 | 随手生成一个 |
| `PORT` | | 订阅服务端口 | `443` |
| `CFIP` | | 优选域名/IP | `www.visa.com.tw` |
| `CFPORT` | | 优选端口 | `443` |
| `NEZHA_SERVER` | | 哪吒面板地址 | `nz.example.com` |
| `NEZHA_PORT` | | 哪吒 v0 的 agent 端口；v1 留空 | `5555` |
| `NEZHA_KEY` | | 哪吒密钥 🔑 | 从哪吒后台获取 |
| `ARGO_DOMAIN` | | 固定隧道域名，不填用临时的 | `abc.2go.com` |
| `ARGO_AUTH` | | 隧道凭据 🔑 | 从 CF 后台获取 |
| `SUB_TOKEN` | | 订阅链接密码 | 随手设一个 |
| `CHAT_ID` / `BOT_TOKEN` | | TG 推送 🔑 | 按需填写 |

完整变量表见 [docs/09](09-环境变量总表.md)。

## 出问题怎么办

| 症状 | 先查 |
|---|---|
| 脚本报错 | 看报错信息；检查 VPS 系统版本是否在支持列表 |
| 订阅链接打不开 | 检查端口是否放行、服务是否在运行 |
| 节点超时 | 换优选域名（`CFIP`），或换个协议试试 |
| 哪吒不显示 | 对照 [排错手册](08-排错手册.md) 的哪吒一节 |

## 卸载 / 清理

脚本一般会在输出里告诉你卸载方式；VPS 上直接删掉相关进程和文件即可。
Serv00 上删掉对应目录，进程会随账号过期自动清理。

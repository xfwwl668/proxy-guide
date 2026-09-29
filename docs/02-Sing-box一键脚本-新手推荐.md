# 02 · Sing-box 一键脚本（新手推荐）

> 仓库：https://github.com/xfwwl668/Sing-box
> 一句话：复制粘贴一条命令，多个协议一次装好。但注意：**这是三套不同的脚本**，VPS、免费主机、游戏机各用各的，别混着抄命令。

## 先搞清楚：三套脚本，别用错

| | VPS 版 `sing-box.sh` | Serv00/CT8 版 `sb4.sh` / `sb_serv00.sh` | 游戏机版（go/nodejs/python/java 目录） |
|---|---|---|---|
| 运行环境 | 自己的 VPS | Serv00、CT8 这类免费主机 | 游戏面板机（Pterodactyl 等） |
| 权限要求 | **要 root** | 不要 root | 不要 root |
| 交互方式 | 交互式菜单 | `sb4.sh` 全自动 / `sb_serv00.sh` 交互式 | 改各语言入口文件里的变量后运行 |
| 进程管理 | systemd 服务 | nohup 后台 | nohup 后台 |
| 协议 | vless-reality / vmess-ws-tls(argo) / hy2 / tuic | vmess-ws / vmess-ws-tls(argo) / hy2 / tuic（**无 vless-reality**） | 默认只输出 vmess-argo（见下） |

> ⚠️ **URL 真相**：仓库 README 里的一键命令拉的是 `eooce/sing-box` 的脚本，不是 `xfwwl668/Sing-box` 本仓库的快照，跑起来用的是上游代码。且 README 提到的 `2.sh`、`tu.sh`、`00_vm.sh` 在本仓库里**根本不存在**。下面给的命令以仓库实际文件为准。

## 适合谁

- 有 VPS（Ubuntu / Debian / CentOS / Alpine / Fedora / Rocky）且有 root 的人 → VPS 版
- 有 Serv00 / CT8 免费主机账号的人 → Serv00 版
- 有游戏面板机的人 → 游戏机版
- 第一次部署，只想最快跑起来的人

## 准备什么

- [ ] VPS（需要 root），或 Serv00 / CT8 账号，或游戏面板机
- [ ] 生成一个 UUID（在线搜 "UUID 生成器"，复制一个）——**Serv00 版特别注意**：它的默认 UUID 是用户名 md5 派生的，可预测，**必须手动改掉**；且它的 tuic 密码硬编码是 `admin123`，全网统一，知道的人都能连你的 tuic 端口
- [ ] （可选）哪吒面板地址 + KEY，想监控才需要
- [ ] （可选）Argo 固定隧道的域名 + 凭据，想长期稳定才需要；不填就用临时隧道

## 操作步骤

### VPS 一键安装（要 root）

```bash
# 最简：全默认（PORT 随机，UUID 随机生成）
bash <(curl -Ls https://raw.githubusercontent.com/xfwwl668/Sing-box/main/sing-box.sh)

# 带参数：指定端口和优选（PORT 后面连续 3 个端口也要可用）
PORT=443 CFIP=www.visa.com.tw CFPORT=443 bash <(curl -Ls https://raw.githubusercontent.com/xfwwl668/Sing-box/main/sing-box.sh)
```

**端口逻辑**（源码证实，NAT 小鸡重点看）：
- `PORT` → vless-reality
- `PORT+1` → 订阅（nginx，明文 http，路径带随机密码）
- `PORT+2` → tuic
- `PORT+3` → hysteria2
- `8001`（固定）→ vmess-ws，cloudflared 用临时隧道对外

所以 `PORT=443` 要求 443、444、445、446 全可用。NAT 机装完后**必须手动**把订阅端口和节点端口改到面板允许的范围内，否则不通。

### Serv00 / CT8 一键安装（不要 root）

```bash
# 全自动（不问问题，用默认值）
bash <(curl -Ls https://raw.githubusercontent.com/xfwwl668/Sing-box/main/sb4.sh)

# 交互式（会问你几个问题）
bash <(curl -Ls https://raw.githubusercontent.com/xfwwl668/Sing-box/main/sb_serv00.sh)
```

**端口逻辑**：脚本会自动整理面板端口为 **1 个 TCP + 2 个 UDP**（多了删、少了随机加）。TCP 跑 vmess-ws（Argo 隧道也指向它），两个 UDP 分别跑 tuic 和 hy2。

带参数的全自动示例（把 `xxx` 换成你自己的）：

```bash
UUID=你生成的uuid \
NEZHA_SERVER=nz.example.com \
NEZHA_PORT=5555 \
NEZHA_KEY=xxx \
ARGO_DOMAIN=abc.2go.com \
ARGO_AUTH='xxx' \
bash <(curl -Ls https://raw.githubusercontent.com/xfwwl668/Sing-box/main/sb4.sh)
```

> ⚠️ 上面的 `xxx` 是**密钥**，填你自己的，别用别人的，也别截图发出来。

### 游戏机版

对应目录（`go/`、`nodejs/`、`python/`、`java/`）即对应环境：下载该目录下的文件上传到面板机，改好变量后运行。`start.sh` 主体是 base64 混淆过的，不用管，看头 17 行的变量就行。

**默认只开 vmess-argo**：`TUIC_PORT`、`HY2_PORT`、`REALITY_PORT` 默认是 40000/50000/60000，等于默认值时**不输出**对应节点（单端口面板机上开了也连不上，所以脚本干脆不输出）。想要多协议就改成面板实际分配的端口。

> ⚠️ go 版的 `PORT`（订阅端口）是写死的 3000，环境变量改不动；nodejs/python 版正常读取。

## 成功标准（对照打勾）

- [ ] 脚本跑完没报错，输出了节点链接或订阅链接
- [ ] 订阅链接能打开（VPS 版是 `http://IP:PORT+1/随机密码`，Serv00 版是 `https://用户名.serv00.net/子TOKEN`）
- [ ] 客户端导入后，节点列表出现了对应协议的节点
- [ ] 选一个节点测延迟，能返回数字（不是超时）
- [ ] 按 [docs/07](07-客户端使用-订阅导入.md) 最后一节验证，确认真的能用

## "解锁 GPT 和奈飞"到底真不真

- **VPS 版 / 游戏机版：真**。配置里有 WireGuard（Warp）出站，netflix 和 openai 相关域名走 Warp。
- **Serv00 版：不真**。只有 s14/s15/s16 主机才加 Warp，且只分流 google/youtube，**没有 netflix、没有 openai 规则**。README 那句"默认解锁"是照抄 VPS 版的。

## 保活（Serv00 版容易掉线才需要看）

- `sb4.sh` 会自动在 Serv00 上再建一个 nodejs 保活站（`/start` 拉起、`/stop` 停止、`/status` 查状态），但这是**站内保活**——保活程序和节点在同一台机器上，机器挂了它也挂。
- `keep_00.sh` 是外部保活：放你自己的 VPS 上，cron 每 2 分钟检查端口、Argo、哪吒，连续失败 3 次就 TG 告警并尝试远程重装。注意它有个 bug：`CFPORT` 变量名拼成了 `CFIPPORT`，外部传入的 `CFPORT` 不生效；且要求把 Serv00 账号密码明文写进脚本。
- `keep.sh` 是简化版，但**有语法错误**，别用。

## 出问题怎么办

| 症状 | 先查 |
|---|---|
| VPS 脚本一运行就退出 | 是否 root？脚本开头检查 `$EUID`，非 root 直接退出 |
| NAT 小鸡节点不通 | PORT 后面 3 个端口是否在面板放行范围内 |
| Serv00 节点突然全挂 | 面板端口是否被回收；用 keep_00.sh 查 Argo/哪吒状态 |
| 订阅链接打不开 | VPS 版查 nginx 是否在 PORT+1 监听；Serv00 版查 php 站点和 SUB_TOKEN |
| 哪吒不显示 | 对照 [排错手册](08-排错手册.md) 的哪吒一节；Serv00 的 agent 名是按 `S+序号` 匹配的 |
| hy2/tuic 连不上 | 客户端"跳过证书验证"是否开了（自签证书，CN=bing.com） |

## 卸载 / 清理

- VPS 版：`systemctl stop/disable sing-box argo`，再删 `/etc/sing-box` 和脚本文件；注意脚本装过 `iptables -F`（全放行），卸载后按需恢复防火墙。
- Serv00 版：删掉对应目录和面板站点即可；`keep_00.sh` 的 cron 别忘了清。

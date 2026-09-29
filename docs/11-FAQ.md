# 11 · FAQ（精简 10 问）

## Q1：哪个项目最适合新手？

**A：** Sing-box 一键脚本（docs/02）。复制粘贴一条命令就行。

## Q2：哪个最稳定？

**A：** 没有"最稳定"，只有"适合你网络的"。一般来说：有 VPS 用 Sing-box；
免费平台里 sbx-native 的 6 协议组合容错率高一些。延迟高先看[排错手册](08-排错手册.md)。

## Q3：哪个最隐蔽？

**A：** sbx-native 的无子进程 FFI 方式**相对**隐蔽。但隐蔽≠免检测，别拿它当护身符。

## Q4：哪个适合免费平台？

**A：** 看你有什么：PaaS 选 sbx-native，游戏机选 paper-pro / java-plugins-plus，
啥都没有又想白嫖选 deploy-vercel（Vercel + CF Worker，步骤最多）。

## Q5：无子进程是什么意思？

**A：** 传统方式是启动 sing-box 二进制文件，会产生子进程；sbx-native 用 FFI 直接调动态库，
只有一个主进程。进程特征少一点，**相对**不容易被基于进程的检测发现。

## Q6：Argo 临时隧道和固定隧道怎么选？

**A：** 测试用临时的（零配置）；长期用固定的（要填 `ARGO_DOMAIN` + `ARGO_AUTH`）。
临时隧道每次重启域名会变，订阅要重新更新。

## Q7：哪吒 v0 和 v1 怎么配？

**A：** v0：`NEZHA_SERVER` 填 host，`NEZHA_PORT` 填 agent 端口；
v1：`NEZHA_SERVER` 填 `host:port`，`NEZHA_PORT` 留空。`NEZHA_KEY` 去哪吒面板后台拿。

## Q8：能解锁流媒体吗？

**A：** 不保证。原版说"默认已解锁"过于绝对，IP 干净程度看运气，被标记的 IP 该不行还是不行。

## Q9：假人插件怎么加？

**A：** paper-pro：替换主文件后，把假人插件 jar 放 `plugins/`；
java-plugins-plus：本插件和假人插件都放 `plugins/`，共存。
推荐：Citizens / Dummy Players / FakePlayer。

## Q10：连不上先干嘛？

**A：** 按这个顺序：订阅链接浏览器能打开吗 → 换网络试试 → 更新订阅 → 换节点测速 →
对照[排错手册](08-排错手册.md)。还不行就开 `SHOW_LOG=true` 看日志，
求助时记得给密钥打码。

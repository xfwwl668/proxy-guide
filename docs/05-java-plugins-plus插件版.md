# 05 · java-plugins-plus 插件版

> 仓库：https://github.com/eooce/java-plugins-plus
> 一句话：和 paper-pro **同一套代理代码**，但做成了 Minecraft 插件——不用换服务端主文件，jar 丢进 `plugins/`（Fabric 丢 `mods/`）就行。
> 已有 MC 服、不想动主文件的人选这个。

## 模块结构（一句话版）

Maven 多模块工程，但别被吓到，记住三层就行：

| 模块 | 作用 |
|---|---|
| `common` | **全部逻辑**：`AppService.java`（约 1200 行，代理核心，唯一依赖 JNA） |
| `paper` / `bungee` / `velocity` / `fabric` | 薄外壳：各平台的插件入口类，干的事都是"启动 AppService" |
| `universal` | 无源码，把上面全打成**一个通用 jar**（`EssentialsX-1.21.11.jar`） |

一个 jar 四处通用原理：jar 里同时装着四套入口类和三套描述文件（`plugin.yml` / `bungee.yml` / `fabric.mod.json`，Velocity 靠注解），各平台加载器只认自己的那份。Actions 也只发布这一个 universal jar。

## 启动机制

```
服务端启动 → 加载插件
  Paper/Spigot/Purpur: 插件 onEnable()
  BungeeCord:          插件 onEnable()
  Velocity:            监听 ProxyInitializeEvent
  Fabric:              ModInitializer.onInitialize()
→ EssentialsXService.start() → AppService.start()
→ 起守护线程跑代理，主线程睡 30 秒后打印假的 MC 开服日志
→ 守护线程永久阻塞（插件线程不退出）
```

> ⚠️ **伪装日志**：启动 30 秒后它会打印十几行假的 MC 日志（`Preparing spawn area: x%`、`Done preparing level "world"`），用来掩盖代理启动痕迹。看到这种日志别以为服没开好——那是它装的。

运行目录藏在 `world/` 里（借世界存档文件夹藏文件），45 秒后除 `keypair.properties` 和 `sub.txt` 外全删——和 paper-pro 一样的清理逻辑。

## 适合谁

- 已经有一个 MC 服务器在跑，不想换主文件的人
- 服务端是 BungeeCord / Velocity / Fabric（paper-pro 只支持 Paper 系）的人
- 接受"配置靠改源码重新构建"的人

## 准备什么

- [ ] 一个在运行的 MC 服务端（Paper / Spigot / Purpur / BungeeCord / Velocity / Fabric 任一）
- [ ] 点仓库 "Use this template" 建**私密仓库**
- [ ] 生成一个 UUID（必须改）

## 操作步骤

1. 用模板建私密仓库，在 Actions 页面点启用。
2. 打开 `common/src/main/java/com/example/essentialsx/common/AppService.java`，第 46–69 行，把环境变量**默认值**改成你自己的（UUID 必须改）。
3. push 到 main，Actions 自动 `mvn clean package`（约 2 分钟），去 Release 的 `Latest Build` 下载 `EssentialsX-1.21.11.jar`。
4. Paper/Spigot/Purpur/BungeeCord/Velocity → 丢进 `plugins/`；Fabric → 丢进 `mods/`。
5. 重启服务端，代理自动跑。拿订阅方式同 paper-pro：控制台 45 秒内复制 / `world/sub.txt` / TG / `UPLOAD_URL`。

### 为什么改源码、私密仓库？

JVM 环境变量在面板机上一般不可控，所以配置是**改源码默认值 → Actions 构建 → 把配置"烤进" jar**。UUID、密钥都会进 jar，必须私密仓库。注意：`.env` 文件也行（`env()` 会先读工作目录的 `.env`），但插件场景下一般没法放文件，所以 README 教的是改源码。

## 成功标准（对照打勾）

- [ ] Actions 构建成功，Release 里有 jar
- [ ] 服务端重启后插件列表里能看到它加载
- [ ] 45 秒内在控制台拿到订阅，或 `world/sub.txt` 生成
- [ ] 客户端导入后节点可用

## 环境变量（源码默认值）

| 变量 | 源码默认值 | 说明 |
|---|---|---|
| `UUID` | `9ac16559-f9a7-4296-bd77-b837d10fc9d2` | 公开值，必须改；Socks 用户名取前 8 位、密码取后 12 位 |
| `CFIP` / `CFPORT` | `saas.sin.fan` / `443` | vmess 节点优选 |
| `FILE_PATH` | `world` | 藏身世界存档目录 |
| `ARGO_PORT` | `8001` | vmess-ws 固定监听 |
| `ARGO_DOMAIN` / `ARGO_AUTH` | 空 | 都空→临时隧道（从 boot.log 正则抓 `*.trycloudflare.com`）；都填→固定隧道 |
| `DISABLE_ARGO` | `false` | `true` 则无 vmess 节点 |
| `S5_PORT` / `HY2_PORT` / `TUIC_PORT` / `ANYTLS_PORT` / `REALITY_PORT` | 空 | 填 1–65535 才启用 |
| `NEZHA_SERVER` / `NEZHA_PORT` / `NEZHA_KEY` | 空 | SERVER+KEY 有、PORT 空→v1；PORT 也有→v0（443/8443/2096/2087/2083/2053 自动加 `--tls`） |
| `UPLOAD_URL` / `PROJECT_URL` | 空 | 都填→上报订阅 URL；只填前者→上报节点列表 |
| `BOT_TOKEN` / `CHAT_ID` | 空 | 都填才 TG 推送 |
| `AUTO_ACCESS` | `false` | `true` 且 `PROJECT_URL` 非空→向 `oooo.serv00.net/add-url` 保活 |
| `YT_WARPOUT` | `false` | `false` 时自动探测 youtube，不可达才加 Warp 分流 |
| `NAME` | 空 | 空则节点名用 `国家-ISP`（调 api.ip.sb / ip-api.com 获取） |
| `SHOW_LOG` | 显示 | `false`/`disable`/`no` 才屏蔽（平台日志不受影响） |

> ⚠️ README 里列的 `ANYREALITY_PORT`，**源码里根本不存在**（grep 计数为 0），是文档多写的功能，别填。

`.so` 下载源：主 `00666.xyz`，备 `oooen.com`（文件名伪装：`sbx.so`=sing-box、`bot.so`=cloudflared、`agent.so`/`v1.so`=哪吒）。

## 出问题怎么办

| 症状 | 先查 |
|---|---|
| 插件没加载 | 放对目录没（Fabric 是 `mods/`，不是 `plugins/`）；服务端版本是否支持 |
| 构建失败 | 改源码时是否改坏了 Java 语法（引号/逗号） |
| 拿不到订阅 | 同 paper-pro：45 秒清屏，查 `world/sub.txt` 或配 TG |
| 和 paper-pro 选哪个 | 已有服→插件版；从零搭 Paper 服→主文件版；功能一样 |

## 卸载 / 清理

删掉 jar，重启服务端。删 `world/` 下的 `sub.txt`、`keypair.properties`。

# 04 · paper-pro 游戏机主文件版

> 仓库：https://github.com/eooce/paper-pro
> 一句话：魔改版 PaperMC 服务端——代理启动器代码直接编译进 `server.jar` 本体，开服即自动跑代理。
> 和 sbx-native 的 Java 版是**同一套代码**（方法名 61 个重合），区别只在"宿主"：这里宿主是游戏服务端本身。

## 启动机制（源码证实的调用链）

```
java -jar server.jar
 → PaperBootstrap.boot()
 → 起守护线程跑代理（io.papermc.paper.sbx.App）
 → 主线程睡 30 秒（等你复制订阅）
 → 清屏
 → 强制把 eula.txt 写成 eula=true
 → 正常启动 MC 服务端
```

结论：**开服即自动跑**，你不用敲任何额外命令；服务端关了代理一起死（守护线程）。

> ⚠️ 附带行为：它会**强制跳过 Mojang 的 EULA 确认**（自动写 `eula=true`）。这是源码行为，不是配置项。

## 适合谁

- 本来就要开 MC 服务器（Paper 端）的人，顺手跑代理
- 能接受"整个服务端 jar 被换过"的人
- 不想折腾插件、想要开箱即跑的人

## 准备什么

- [ ] 一台能跑 Java 21+ 的游戏面板机/容器（构建用的是 JDK 22）
- [ ] 点仓库 "Use this template" 建一个**私密仓库**（私密原因见下）
- [ ] 生成一个 UUID（必须自己改，默认的是公开值）
- [ ] （可选）哪吒、Argo 固定隧道、TG 推送

## 操作步骤

1. 用模板建私密仓库，在 Actions 页面点启用（`I understand my workflows`）。
2. 打开 `paper-server/src/main/java/io/papermc/paper/sbx/App.java`，找到第 41–64 行，把环境变量的**默认值**改成你自己的（UUID 必须改，不需要的留空）。
3. push 到 main，Actions 自动编译整个 Paper 服务端（约 7–10 分钟）。
4. 去 Release 的 `latest` 下载 `server.jar`，上传覆盖面板机上的服务端主文件。
5. `java -jar server.jar` 启动。**30 秒内**从控制台复制绿色 base64 订阅——之后会清屏。

### 为什么必须改源码、私密仓库？

JVM 环境变量在面板机上一般不可控，所以这个项目把配置直接"烤进" jar：你改的是源码里的默认值，构建后就固化了。UUID、密钥都会进 jar，**公开仓库等于把钥匙贴在墙上**，所以必须用私密仓库。

## 拿订阅的 4 种方式（没有 HTTP 订阅服务！）

和 sbx-native 不同，这个版本**砍掉了 HTTP 订阅服务**（`SUB_PATH` 相关代码是死代码），拿订阅只有 4 条路：

| 方式 | 说明 |
|---|---|
| 控制台复制 | 启动后 30 秒内复制绿色 base64，之后清屏消失 |
| `world/sub.txt` | **唯一持久的本地载体**，45 秒清理后唯一剩下的订阅文件 |
| TG 推送 | `BOT_TOKEN` + `CHAT_ID` 都填才推（源码默认都是空，无内置值） |
| `UPLOAD_URL` | 推送到 Merge-sub，启动时还会先删旧节点防重复 |

> ⚠️ 45 秒后运行目录（`world/`）里除 `keypair.properties` 和 `sub.txt` 外的一切都会被删（含明文的 `list.txt`）。**`sub.txt` 务必及时备份**，丢了就只能重开服再复制。

## 成功标准（对照打勾）

- [ ] Actions 构建成功，Release 里有 `server.jar`
- [ ] 启动后 30 秒内在控制台看到绿色订阅（或 `world/sub.txt` 生成）
- [ ] MC 服务端正常开服（代理不影响开服）
- [ ] 客户端导入订阅后节点可用

## 环境变量（源码默认值）

| 变量 | 源码默认值 | 说明 |
|---|---|---|
| `UUID` | `0a6568ff-ea3c-4271-9020-450560e10d61` | 公开值，必须改 |
| `CFIP` / `CFPORT` | `cf.877774.xyz` / `443` | vmess 节点优选 |
| `FILE_PATH` | `world` | 和 MC 存档同名，文件混在里面（45 秒后被清理，不影响存档本身） |
| `ARGO_PORT` | `8001` | vmess-ws 固定监听 |
| `ARGO_DOMAIN` / `ARGO_AUTH` | 空 | 都空→临时隧道；token（120–250 字符）或含 `TunnelSecret` 的 JSON→固定隧道 |
| `DISABLE_ARGO` | `false` | `true` 则无 vmess 节点 |
| `S5_PORT` / `HY2_PORT` / `TUIC_PORT` / `ANYTLS_PORT` / `REALITY_PORT` | 空 | 填 1–65535 才启用对应协议 |
| `NEZHA_SERVER` / `NEZHA_PORT` / `NEZHA_KEY` | 空 | 三者全有→v1；SERVER+KEY 有、PORT 空→v0；否则跳过 |
| `BOT_TOKEN` / `CHAT_ID` | 空 | **无内置默认值**，都填才推送 |
| `UPLOAD_URL` / `PROJECT_URL` | 空 | 填了才上传订阅/节点 |
| `AUTO_ACCESS` | `false` | `true` 且 `PROJECT_URL` 非空→向 `oooo.serv00.net/add-url` 注册保活 |
| `SHOW_LOG` | 显示 | `false`/`disable`/`no` 才屏蔽 |

Reality 固定 SNI `www.iij.ad.jp`；hy2/tuic 自签证书 CN=bing.com（客户端开"跳过证书验证"）。

## 出问题怎么办

| 症状 | 先查 |
|---|---|
| Actions 构建失败 | 是否 JDK 版本不对（要 21+）；是否改源码时改坏了括号 |
| 启动后没看到订阅 | 30 秒清屏了——直接看 `world/sub.txt`；或配 TG/UPLOAD_URL |
| `sub.txt` 是空的 | `.so` 是否下载成功（`oooen.com` / `00666.xyz` 是否可达） |
| 代理和服务端一起没了 | 守护线程随主进程生死，服务端崩了代理也没了，查服务端日志 |
| 哪吒不亮 | 对照 [排错手册](08-排错手册.md) |

## 卸载 / 清理

换回官方 Paper 的 `server.jar` 即可。删掉 `world/` 下的 `sub.txt`、`keypair.properties`（Reality 密钥，换服建议删）。

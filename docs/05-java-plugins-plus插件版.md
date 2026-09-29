# 05 · java-plugins-plus 插件版

> 仓库：https://github.com/eooce/java-plugins-plus（已验证存在）
> 一句话：魔改版 EssentialsX 插件，内置 sbx-native 的 6 种协议。
> 扔进 `plugins/`（或 `mods/`）目录就行，**不用替换 MC 主文件**，原有玩法不受影响。

## 适合谁

- 已经有 MC 服务器（Paper / Spigot / Purpur / BungeeCord / Velocity / Fabric）的人
- 不想动服务端主文件的人
- 想和假人插件共存的人（都在 `plugins/` 里，不打架）

## 准备什么

- [ ] 一个 GitHub 账号
- [ ] 一台能跑 MC 的服务器/游戏机
- [ ] 生成一个 UUID

## 操作步骤

### 步骤 1：Fork 仓库

1. 打开 https://github.com/eooce/java-plugins-plus
2. 点右上角 **Use this template**（或 Fork）
3. 建一个新仓库，**建议设为私有**
4. 名字随意

### 步骤 2：改环境变量

1. 打开 Actions，点 **I understand my workflows, go ahead and enable them**
2. 打开文件 `common/src/main/java/com/example/essentialsx/common/AppService.java`
3. 改第 46~69 行的环境变量，不用的留空
4. 保存，Actions 自动构建（约 2 分钟）

### 步骤 3：下载插件

1. 等约 2 分钟构建完成
2. 打开仓库右侧 **Releases** → **Latest Build**，下载 jar 文件

### 步骤 4：上传到 MC 服务器

不同平台放不同目录，上传后**重启服务器**：

| 平台 | 放哪里 |
|---|---|
| Paper / Spigot / Purpur | `plugins/` |
| BungeeCord | `plugins/` |
| Velocity | `plugins/` |
| Fabric | `mods/` |

### （可选）步骤 5：加假人插件

假人插件也是 jar，同样放 `plugins/`，和本插件共存，配置参考 [docs/04](04-paper-pro游戏机主文件版.md) 步骤 5。

## 成功标准

- [ ] Actions 构建成功，下载到插件 jar
- [ ] 服务器重启后插件正常加载（看日志/插件列表）
- [ ] 原有 MC 功能正常（进服走两步确认）
- [ ] 订阅链接可访问，客户端导入后出现节点
- [ ] 按 [docs/07](07-客户端使用-订阅导入.md) 最后一节验证可用

## 环境变量

| 变量 | 说明 |
|---|---|
| `UUID` | ★ 节点身份证 |
| `NEZHA_SERVER` / `NEZHA_KEY` | 哪吒监控 🔑 |
| `ARGO_DOMAIN` / `ARGO_AUTH` | 固定隧道 🔑 |
| `CFIP` / `CFPORT` | 优选域名/IP |
| `REALITY_PORT` / `HY2_PORT` / `TUIC_PORT` / `S5_PORT` | 填了才启用对应协议 |

## 出问题怎么办

| 症状 | 先查 |
|---|---|
| 插件没加载 | 确认放对了目录（Fabric 是 `mods/`）；看启动日志报错 |
| 和其他插件冲突 | 先只留本插件启动，逐个加回去定位 |
| 节点不通 | 对照 [排错手册](08-排错手册.md) |
| 构建失败 | 看 Actions 红字报错，多为变量格式问题 |

## 卸载 / 清理

删掉插件 jar，重启服务器即可。不影响原有存档和主文件。

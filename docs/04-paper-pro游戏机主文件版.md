# 04 · paper-pro 游戏机主文件版

> 仓库：https://github.com/eooce/paper-pro（已验证存在）
> 一句话：魔改版 PaperMC 服务端，主文件里内置了 sbx-native 的 6 种协议。
> 上传替换原来的 `server.jar`，MC 服务器照常开服，代理悄悄跑在里面。

## 适合谁

- 有游戏机（Serv00 / CT8 / Hostuno）的人
- 想"看起来像正常 MC 服务器"，顺带防回收的人
- 能接受替换服务端主文件的人

> 防回收原理：MC 玩家连接 + 假人插件让服务器保持活跃，平台不容易判定闲置回收。
> 这是"相对自然"，不是"平台不检测"——原版说法太绝对。

## 准备什么

- [ ] 一个 GitHub 账号
- [ ] 游戏机（Serv00 / CT8 / Hostuno）账号
- [ ] 生成一个 UUID
- [ ] （可选）假人插件：Citizens / Dummy Players / FakePlayer，三选一

## 操作步骤

### 步骤 1：Fork 仓库

1. 打开 https://github.com/eooce/paper-pro
2. 点右上角 **Use this template**（或 Fork）
3. 建一个新仓库，**建议设为私有**（里面要填你的密钥）
4. 名字随意

### 步骤 2：改环境变量

1. 打开你 Fork 后的仓库 → **Actions** 选项卡
2. 点 **I understand my workflows, go ahead and enable them**（启用工作流）
3. 打开文件 `paper-server/src/main/java/io/papermc/paper/sbx/App.java`
4. 改第 41~64 行的环境变量（UUID、NEZHA、ARGO、CFIP 等，不用的留空）
5. 保存，Actions 会自动开始构建

> ⚠️ 这一步填的是密钥，仓库设私有就是为了这个。别 Fork 成公开还填真实密钥。

### 步骤 3：等构建、下载 JAR

1. 等 7~10 分钟，Actions 构建完成
2. 打开仓库右侧 **Releases**，下载 `server.jar`

### 步骤 4：上传到游戏机

1. 登录游戏机面板（Serv00 / CT8 / Hostuno）
2. 把 `server.jar` 上传到文件管理根目录，替换原来的主文件
3. 启动，搞定

### （可选）步骤 5：加假人插件防回收

1. 把假人插件 jar 放到 `plugins/` 目录
2. 配置假人数量和上下线时间（比如 3 个假人、模拟真实行为）
3. 保持服务器活跃

## 成功标准

- [ ] Actions 构建成功，Releases 里能下载到 `server.jar`
- [ ] 游戏机上 MC 服务器正常启动，玩家能连上
- [ ] 订阅链接可访问，客户端导入后出现节点
- [ ] 按 [docs/07](07-客户端使用-订阅导入.md) 最后一节验证可用

## 环境变量

同 sbx-native（见 [docs/03](03-sbx-native原生启动器.md) 的变量表），常用：

| 变量 | 说明 |
|---|---|
| `UUID` | ★ 节点身份证 |
| `NEZHA_SERVER` / `NEZHA_KEY` | 哪吒监控 🔑 |
| `ARGO_DOMAIN` / `ARGO_AUTH` | 固定隧道 🔑 |
| `CFIP` / `CFPORT` | 优选域名/IP |
| `REALITY_PORT` / `HY2_PORT` / `TUIC_PORT` | 填了才启用对应协议 |

## 出问题怎么办

| 症状 | 先查 |
|---|---|
| Actions 构建失败 | 点进失败的 workflow 看红字报错；常见是变量格式填错 |
| 等了很久没构建完 | 正常要 7~10 分钟；超过 30 分钟再看 |
| MC 服务器起不来 | 检查 jar 是否下载完整、游戏机 Java 版本 |
| 节点不通 | 对照 [排错手册](08-排错手册.md) |

## 卸载 / 清理

把原来的 `server.jar` 换回来、删掉插件即可。记得把 Fork 的私有仓库删掉或清空密钥。

# 03 · sbx-native 原生启动器

> 仓库：https://github.com/xfwwl668/sbx-native（已验证存在）
> 一句话：通过 FFI 直接调用 sing-box，不起子进程，隐蔽性相对好一点，支持 6 种协议。

## 适合谁

- 有免费 PaaS（Railway / Koyeb / Fly.io）或游戏机的人
- 想要"只有一个主进程、没有子进程"这种相对隐蔽的运行方式
- 想一次要 6 种协议：VMESS WS+Argo、VLESS Reality、HY2、TUIC、AnyTLS、SOCKS5

> 说明：原版说"无子进程=不易被检测"，实际情况是**相对**隐蔽，不是免死金牌。

## 准备什么

- [ ] 一个 PaaS / 游戏机账号
- [ ] 生成一个 UUID
- [ ] 决定用哪个语言版本：**Node.js（推荐）**、Python、Java，三选一就行
- [ ] （可选）哪吒、Argo 固定隧道、TG 推送的凭据

## 操作步骤

### Node.js 版（推荐）

```bash
# 克隆仓库
git clone https://github.com/xfwwl668/sbx-native.git
cd sbx-native/nodejs

# 安装依赖
npm install

# 设置环境变量（在平台的环境变量面板里填，或写 .env 文件）
# 变量含义见下面的表

# 运行
npm start
```

### Python 版

```bash
cd sbx-native/python
pip install -r requirements.txt
python3 app.py
```

### Java 版

```bash
cd sbx-native/java
mvn -DskipTests package
java -jar target/server-1.0.jar
```

> PaaS 平台一般不用你手动跑命令：把代码推上去，在平台的环境变量面板填好变量，设好启动命令就行。

## 成功标准

- [ ] 服务启动后日志没报错
- [ ] 浏览器打开 `http://你的域名/端口/sub` 能看到订阅内容
- [ ] 客户端导入后出现 6 种协议的节点（启用的才有）
- [ ] 测延迟正常，按 [docs/07](07-客户端使用-订阅导入.md) 最后一节验证可用

## 环境变量

| 变量 | 默认值 | 必填 | 说明 |
|---|---|---|---|
| `UUID` | 随机 | ★ | 节点身份证 |
| `PORT` | `3000` | | 订阅服务监听端口 |
| `SUB_PATH` | `sub` | | 订阅路径（`/sub`） |
| `NAME` | 空 | | 订阅里显示的节点名称 |
| `CFIP` | `cf.877774.xyz` | | 优选域名，流量转发目标 |
| `CFPORT` | `443` | | 优选端口 |
| `REALITY_PORT` | 空 | | 填了才启用 VLESS Reality |
| `HY2_PORT` | 空 | | 填了才启用 HY2 |
| `TUIC_PORT` | 空 | | 填了才启用 TUIC |
| `ANYTLS_PORT` | 空 | | 填了才启用 AnyTLS |
| `S5_PORT` | 空 | | 填了才启用 SOCKS5 |
| `ARGO_DOMAIN` / `ARGO_AUTH` | 空 | | 固定隧道；空=临时隧道 🔑 |
| `ARGO_PORT` | `8001` | | cloudflared 反代端口 |
| `DISABLE_ARGO` | false | | `true`=禁用 Argo |
| `NEZHA_SERVER` / `NEZHA_PORT` / `NEZHA_KEY` | 空 | | 哪吒监控；空=不监控 🔑 |
| `UPLOAD_URL` | 空 | | Merge-sub 上传地址；空=不上传 |
| `PROJECT_URL` | 空 | | 项目公网 URL，用于自动保活 |
| `AUTO_ACCESS` | false | | `true`=自动访问保活 |
| `CHAT_ID` / `BOT_TOKEN` | 空 | | TG 推送 🔑 |
| `FILE_PATH` | `.npm` | | 存放 .so 和配置的目录 |
| `SHOW_LOG` | false | | `true`=显示日志（排错时开） |

## 出问题怎么办

| 症状 | 先查 |
|---|---|
| 启动报错 | 开 `SHOW_LOG=true` 看日志；检查 Node/Python/Java 版本 |
| 订阅空白 | 检查 `PORT`、`SUB_PATH`，确认端口对外可访问 |
| 某协议没节点 | 对应 `*_PORT` 没填就是没启用，填上重启 |
| 哪吒不显示 | 对照 [排错手册](08-排错手册.md) |

## 卸载 / 清理

PaaS 上直接删项目；VPS 上停掉进程、删掉目录即可。记得把环境变量里的密钥从平台面板删掉。

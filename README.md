<div align="center">

# 🌐 代理项目详细对比指南

**代理项目全面分析 · 部署教程 · 选择建议**

[![GitHub stars](https://img.shields.io/github/stars/xfwwl668/proxy-guide)](https://github.com/xfwwl668/proxy-guide/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/xfwwl668/proxy-guide)](https://github.com/xfwwl668/proxy-guide/network)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/xfwwl668/proxy-guide/blob/main/LICENSE)
[![Telegram](https://img.shields.io/badge/Telegram-Group-blue?logo=telegram)](https://t.me/eooceu)

---

**本指南分析 10 个核心代理项目，涵盖协议对比、平台适配、部署教程和选择建议**

</div>

---

## 📋 目录

- [快速选择指南](#-快速选择指南)
- [项目总览](#-项目总览)
- [协议对比分析](#-协议对比分析)
- [项目详细分析](#-项目详细分析)
  - [1. sbx-native](#1-sbx-native)
  - [2. Sing-box](#2-sing-box)
  - [3. nodejs-railway](#3-nodejs-railway)
  - [4. python-xray-argo](#4-python-xray-argo)
  - [5. java-ws](#5-java-ws)
  - [6. edgetunnel](#6-edgetunnel)
  - [7. cnet](#7-cnet)
  - [8. java-xah](#8-java-xah)
  - [9. aimili-vpngate](#9-aimili-vpngate)
  - [10. node-ws-hug](#10-node-ws-hug)
- [部署平台对比](#-部署平台对比)
- [哪吒探针集成指南](#-哪吒探针集成指南)
- [常见问题解答](#-常见问题解答)

---

## 🎯 快速选择指南

### 按部署平台选择

| 平台 | 推荐项目 | 理由 |
|---|---|---|
| **VPS (Ubuntu/CentOS/Debian)** | [Sing-box](#2-sing-box) | 一键脚本，四协议组合，最稳定 |
| **Serv00 / CT8** | [Sing-box](#2-sing-box) | 专用脚本，全自动安装+保活 |
| **PaaS (Railway/Koyeb/Fly)** | [nodejs-railway](#3-nodejs-railway) / [python-xray-argo](#4-python-xray-argo) | 支持临时/固定隧道 |
| **Node.js 平台** | [sbx-native](#1-sbx-native) | 原生启动器，无子进程 |
| **Java 平台** | [sbx-native](#1-sbx-native) / [java-ws](#5-java-ws) | 原生支持，无需内核 |
| **Python 平台** | [sbx-native](#1-sbx-native) / [python-xray-argo](#4-python-xray-argo) | 原生支持 |
| **CF Workers / Pages** | [edgetunnel](#6-edgetunnel) | 边缘计算，无需服务器 |
| **任意平台** | [cnet](#7-cnet) | ECH 代理 + 哪吒 + 隧道三合一 |

### 按协议选择

| 协议 | 推荐项目 | 说明 |
|---|---|---|
| **VLESS Reality** | [sbx-native](#1-sbx-native) / [Sing-box](#2-sing-box) | 最隐蔽，推荐首选 |
| **VMESS WS + Argo** | 所有项目 | 经典组合，稳定 |
| **Hysteria2** | [sbx-native](#1-sbx-native) / [Sing-box](#2-sing-box) | UDP 协议，速度最快 |
| **TUIC 5** | [sbx-native](#1-sbx-native) / [Sing-box](#2-sing-box) | QUIC 协议，低延迟 |
| **ECH** | [cnet](#7-cnet) | 端到端加密，最安全 |
| **Trojan** | [java-ws](#5-java-ws) / [node-ws-hug](#10-node-ws-hug) | 简单稳定 |
| **Shadowsocks** | [java-ws](#5-java-ws) | 兼容性好 |

### 按需求选择

| 需求 | 推荐项目 | 说明 |
|---|---|---|
| **最简单部署** | [Sing-box](#2-sing-box) | 一键脚本，全自动 |
| **最多协议** | [sbx-native](#1-sbx-native) | 6 种协议，原生启动 |
| **最轻量** | [cnet](#7-cnet) | 单二进制文件 |
| **无子进程** | [sbx-native](#1-sbx-native) | 原生 FFI 调用 |
| **最隐蔽** | [cnet](#7-cnet) | ECH 加密 |
| **最快速度** | [Sing-box](#2-sing-box) | HY2 + TUIC |
| **免费平台** | [edgetunnel](#6-edgetunnel) | CF Workers/Pages |

---

## 📊 项目总览

### 项目分类

| 类别 | 项目 | 说明 |
|---|---|---|
| **原生启动器** | sbx-native | sing-box 原生 FFI 启动，无子进程 |
| **一键脚本** | Sing-box | VPS/Serv00/CT8 一键安装 |
| **Argo 隧道** | nodejs-railway, python-xray-argo | Cloudflare Argo 部署 |
| **Java 实现** | java-ws, java-xah | Java 原生代理 |
| **边缘计算** | edgetunnel | CF Workers/Pages |
| **三合一** | cnet | ECH + Nezha + Tunnel |
| **双协议** | node-ws-hug | VLESS + Trojan |
| **出站工具** | aimili-vpngate | vpngate 干净 IP 出站 |

### 项目对比矩阵

| 项目 | 语言 | 协议数 | 哪吒 | Argo | 订阅 | TG推送 | 大小 | 推荐度 |
|---|---|---|---|---|---|---|---|---|
| **sbx-native** | Java/Node/Python | 6 | ✅ | ✅ | ✅ | ✅ | ~50KB | ⭐⭐⭐⭐⭐ |
| **Sing-box** | Shell | 4 | ✅ | ✅ | ✅ | ✅ | ~50KB | ⭐⭐⭐⭐⭐ |
| **nodejs-railway** | JavaScript | 3 | ✅ | ✅ | ✅ | ❌ | ~220KB | ⭐⭐⭐⭐ |
| **python-xray-argo** | Python | 3 | ✅ | ✅ | ✅ | ❌ | ~22KB | ⭐⭐⭐⭐ |
| **java-ws** | Java | 3 | ✅ | ❌ | ✅ | ❌ | ~37KB | ⭐⭐⭐⭐ |
| **edgetunnel** | JavaScript | 2 | ❌ | ❌ | ✅ | ❌ | ~150KB | ⭐⭐⭐⭐ |
| **cnet** | Node/Python/Shell | 1 | ✅ | ✅ | ✅ | ❌ | ~5KB | ⭐⭐⭐⭐ |
| **java-xah** | Java | 2 | ❌ | ✅ | ❌ | ❌ | ~33KB | ⭐⭐⭐ |
| **aimili-vpngate** | - | - | ❌ | ❌ | ❌ | ❌ | ~130KB | ⭐⭐⭐ |
| **node-ws-hug** | JavaScript | 2 | ❌ | ❌ | ❌ | ❌ | ~6MB | ⭐⭐⭐ |

---

## 🔐 协议对比分析

### 协议特性对比

| 协议 | 加密 | 速度 | 隐蔽性 | 穿透力 | 客户端支持 | 推荐度 |
|---|---|---|---|---|---|---|
| **VLESS Reality** | TLS 1.3 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **VMESS WS + TLS** | TLS 1.2 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Hysteria2** | TLS 1.3 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **TUIC 5** | QUIC | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **ECH** | 端到端 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Trojan WS** | TLS 1.2 | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Shadowsocks** | 多种 | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |

### 协议组合推荐

| 场景 | 推荐组合 | 理由 |
|---|---|---|
| **日常使用** | VLESS Reality + VMESS WS | 隐蔽性强，稳定 |
| **追求速度** | Hysteria2 + TUIC 5 | UDP 协议，速度最快 |
| **严格审查** | ECH + VLESS Reality | 端到端加密，最安全 |
| **低延迟** | TUIC 5 + VMESS WS | QUIC 低延迟 |
| **GPT 解锁** | VLESS Reality + VMESS WS + HY2 | 多协议备份 |
| **Netflix** | VMESS WS + TLS | 兼容性最好 |

---

## 📖 项目详细分析

---

### 1. sbx-native

#### 📌 基本信息

| 项目 | 说明 |
|---|---|
| **GitHub** | [xfwwl668/sbx-native](https://github.com/xfwwl668/sbx-native) |
| **语言** | Java / Node.js / Python |
| **协议** | VMESS WS+Argo, VLESS Reality, HY2, TUIC, AnyTLS, SOCKS5 |
| **特点** | 原生 FFI 调用，无子进程 |
| **大小** | ~50KB (不含动态库) |

#### 🚀 核心特性

- ✅ **原生启动**：通过 JNA/koffi 直接调用 sing-box 动态库，无子进程
- ✅ **多协议支持**：6 种协议可选启用
- ✅ **自动生成证书**：Reality X25519 keypair，HY2/TUIC/AnyTLS TLS 证书
- ✅ **自动订阅**：HTTP 暴露订阅链接
- ✅ **哪吒集成**：支持 v0 和 v1
- ✅ **Telegram 推送**：节点上下线通知
- ✅ **自动保活**：Merge-sub 节点上传
- ✅ **YouTube WARP**：可选强制 YouTube 走 WARP 出站

#### 🛠️ 部署教程

##### Java 版本

```bash
# 克隆仓库
git clone https://github.com/xfwwl668/sbx-native.git
cd sbx-native/java

# 构建
mvn -DskipTests package

# 运行
java -jar target/server-1.0.jar
```

##### Node.js 版本

```bash
cd sbx-native/nodejs
npm install
npm start
```

##### Python 版本

```bash
cd sbx-native/python
pip install -r requirements.txt
python3 app.py
```

#### ⚙️ 环境变量配置

| 变量 | 默认值 | 说明 |
|---|---|---|
| `UPLOAD_URL` | 空 | Merge-sub 上传地址 |
| `PROJECT_URL` | 空 | 项目公网 URL |
| `AUTO_ACCESS` | false | 自动保活 |
| `FILE_PATH` | `.npm`/`.cache` | 运行目录 |
| `SUB_PATH` | `sub` | 订阅路径 |
| `UUID` | 随机 | 节点 UUID |
| `NEZHA_SERVER` | 空 | 哪吒面板地址 |
| `NEZHA_PORT` | 空 | 哪吒 v0 agent 端口 |
| `NEZHA_KEY` | 空 | 哪吒密钥 |
| `ARGO_DOMAIN` | 空 | Argo 固定隧道域名 |
| `ARGO_AUTH` | 空 | Argo 隧道 token/JSON |
| `ARGO_PORT` | `8001` | Argo 隧道端口 |
| `S5_PORT` | 空 | SOCKS5 端口 |
| `TUIC_PORT` | 空 | TUIC 端口 |
| `HY2_PORT` | 空 | HY2 端口 |
| `ANYTLS_PORT` | 空 | AnyTLS 端口 |
| `REALITY_PORT` | 空 | VLESS Reality 端口 |
| `CFIP` | `saas.sin.fan` | 优选域名/IP |
| `CFPORT` | `443` | 优选端口 |
| `PORT` | `3000` | HTTP 订阅端口 |
| `NAME` | 空 | 节点名称前缀 |
| `CHAT_ID` | 空 | Telegram chat id |
| `BOT_TOKEN` | 空 | Telegram bot token |
| `DISABLE_ARGO` | false | 禁用 Argo |

#### 💡 使用示例

```bash
# 启用所有协议
export REALITY_PORT=443
export HY2_PORT=8443
export TUIC_PORT=9443
export S5_PORT=1080

# 使用固定隧道
export ARGO_DOMAIN=example.2go.com
export ARGO_AUTH='your-token-or-json'

# 哪吒 v1
export NEZHA_SERVER=nz.example.com:8008
export NEZHA_KEY=your-client-secret

# 运行
node index.js
```

#### 🎯 适用场景

- ✅ Node.js / Java / Python 平台
- ✅ 需要多协议组合
- ✅ 要求无子进程
- ✅ 需要原生性能

#### ⚠️ 注意事项

- 需要 Linux amd64 或 arm64 环境
- 需要访问动态库下载域名
- Reality 首次运行会生成 keypair，后续复用

---

### 2. Sing-box

#### 📌 基本信息

| 项目 | 说明 |
|---|---|
| **GitHub** | [xfwwl668/Sing-box](https://github.com/xfwwl668/Sing-box) |
| **语言** | Shell |
| **协议** | VLESS Reality, VMESS WS+Argo, HY2, TUIC |
| **特点** | 一键安装脚本，全自动 |
| **大小** | ~50KB |

#### 🚀 核心特性

- ✅ **一键安装**：复制粘贴脚本即可部署
- ✅ **四协议组合**：VLESS Reality + VMESS WS+Argo + HY2 + TUIC
- ✅ **多平台支持**：VPS, Serv00, CT8
- ✅ **自动端口**：智能端口分配
- ✅ **哪吒集成**：可选集成
- ✅ **Telegram 通知**：可选
- ✅ **自动保活**：内置保活服务
- ✅ **GPT/Netflix 解锁**：默认配置

#### 🛠️ 部署教程

##### VPS 一键安装

```bash
# 一键四协议安装
bash <(curl -Ls https://raw.githubusercontent.com/xfwwl668/Sing-box/main/sing-box.sh)

# 带端口变量
PORT=443 CFIP=www.visa.com.tw CFPORT=443 bash <(curl -Ls https://raw.githubusercontent.com/xfwwl668/Sing-box/main/sing-box.sh)
```

##### Serv00/CT8 一键安装

```bash
# 交互式安装
bash <(curl -Ls https://raw.githubusercontent.com/xfwwl668/Sing-box/main/sb_serv00.sh)

# 无交互全自动安装
bash <(curl -Ls https://raw.githubusercontent.com/xfwwl668/Sing-box/main/sb4.sh)

# 带参数全自动安装
CHAT_ID=12345 \
BOT_TOKEN=5678:AA812jqIA \
NEZHA_SERVER=nezha.abc.com \
NEZHA_PORT=5555 \
NEZHA_KEY=abc123 \
ARGO_DOMAIN=abc.2go.com \
ARGO_AUTH='{"AccountTag":"123","TunnelSecret":"123","TunnelID":"123"}' \
bash <(curl -Ls https://github.com/xfwwl668/Sing-box/releases/download/00/sb4.sh)
```

##### 单协议安装

```bash
# HY2 单协议
bash <(curl -Ls https://github.com/xfwwl668/Sing-box/releases/download/00/2.sh)

# TUIC 单协议
bash <(curl -Ls https://github.com/xfwwl668/Sing-box/releases/download/00/tu.sh)

# VMESS WS+Argo 单协议
bash <(curl -Ls https://github.com/xfwwl668/Sing-box/releases/download/00/vm.sh)
```

#### ⚙️ 环境变量

| 变量 | 默认值 | 说明 |
|---|---|---|
| `PORT` | 随机 | 订阅端口 |
| `CFIP` | `www.visa.com.tw` | 优选域名/IP |
| `CFPORT` | `443` | 优选端口 |
| `UUID` | 自动 | 节点 UUID |
| `NEZHA_SERVER` | 空 | 哪吒面板地址 |
| `NEZHA_PORT` | `5555` | 哪吒端口 |
| `NEZHA_KEY` | 空 | 哪吒密钥 |
| `ARGO_DOMAIN` | 空 | Argo 固定隧道域名 |
| `ARGO_AUTH` | 空 | Argo 隧道密钥 |
| `SUB_TOKEN` | 自动生成 | 订阅 token |
| `CHAT_ID` | 空 | Telegram chat id |
| `BOT_TOKEN` | 空 | Telegram bot token |

#### 🎯 适用场景

- ✅ VPS 服务器（Ubuntu/Debian/CentOS/Alpine）
- ✅ Serv00/CT8 免费平台
- ✅ 需要最简单部署
- ✅ 追求多协议组合

#### ⚠️ 注意事项

- Serv00/CT8 需要符合端口要求
- 客户端需要开启 `allow_insecure`（HY2/TUIC）
- NAT 小鸡需要手动修改端口

---

### 3. nodejs-railway

#### 📌 基本信息

| 项目 | 说明 |
|---|---|
| **GitHub** | [xfwwl668/nodejs-railway](https://github.com/xfwwl668/nodejs-railway) |
| **语言** | JavaScript |
| **协议** | VLESS, VMESS, Trojan (WS+TLS) |
| **特点** | Argo 隧道部署工具 |
| **大小** | ~220KB |

#### 🚀 核心特性

- ✅ **Argo 隧道**：临时/固定隧道自动切换
- ✅ **多协议**：VLESS + VMESS + Trojan
- ✅ **哪吒集成**：v0/v1 自动检测 TLS
- ✅ **自动端口**：智能端口检测
- ✅ **DNS 缓存**：减少 DNS 查询
- ✅ **域名屏蔽**：自动屏蔽测速网站
- ✅ **Docker 支持**：提供 Dockerfile

#### 🛠️ 部署教程

##### PaaS 平台部署

```bash
# 上传文件
# 只需上传 index.js 和 package.json
# PaaS 平台自动设置环境变量
```

##### Docker 部署

```bash
docker build -t nodejs-railway .
docker run -d -p 3000:3000 \
  -e UUID=your-uuid \
  -e NEZHA_SERVER=nz.example.com:8008 \
  -e NEZHA_KEY=your-key \
  nodejs-railway
```

##### npm 全局安装

```bash
npm install -g nodejs-argo
nodejs-argo
```

#### ⚙️ 环境变量

| 变量 | 默认值 | 说明 |
|---|---|---|
| `UPLOAD_URL` | - | 订阅上传地址 |
| `PROJECT_URL` | `https://www.google.com` | 项目域名 |
| `AUTO_ACCESS` | false | 自动保活 |
| `PORT` | `3000` | HTTP 服务端口 |
| `ARGO_PORT` | `8001` | Argo 隧道端口 |
| `UUID` | 随机 | 用户 UUID |
| `NEZHA_SERVER` | - | 哪吒面板域名 |
| `NEZHA_PORT` | - | 哪吒端口 |
| `NEZHA_KEY` | - | 哪吒密钥 |
| `ARGO_DOMAIN` | - | Argo 固定隧道域名 |
| `ARGO_AUTH` | - | Argo 固定隧道密钥 |
| `CFIP` | `www.visa.com.tw` | 优选域名/IP |
| `CFPORT` | `443` | 优选端口 |
| `NAME` | `Vls` | 节点名称前缀 |
| `FILE_PATH` | `./tmp` | 运行目录 |
| `SUB_PATH` | `sub` | 订阅路径 |

#### 🎯 适用场景

- ✅ Railway / Koyeb / Fly.io
- ✅ 游戏平台玩具
- ✅ 需要 Argo 隧道
- ✅ Node.js 环境

#### ⚠️ 注意事项

- 仅限个人使用，禁止商业用途
- 不填写 ARGO_DOMAIN 和 ARGO_AUTH 使用临时隧道
- 哪吒端口为特定值时自动开启 TLS

---

### 4. python-xray-argo

#### 📌 基本信息

| 项目 | 说明 |
|---|---|
| **GitHub** | [xfwwl668/python-xray-argo](https://github.com/xfwwl668/python-xray-argo) |
| **语言** | Python |
| **协议** | VLESS WS+TLS, VMESS WS+TLS, Trojan WS+TLS |
| **特点** | Argo-Xray 节点，三协议组合 |
| **大小** | ~22KB |

#### 🚀 核心特性

- ✅ **三协议组合**：VLESS + VMESS + Trojan
- ✅ **Argo 隧道**：临时/固定隧道
- ✅ **哪吒集成**：v0/v1 自由选择
- ✅ **自动 TLS**：哪吒端口特定值时自动开启
- ✅ **Docker 镜像**：`ghcr.io/xfwwl668/python:latest`

#### 🛠️ 部署教程

##### Python 环境部署

```bash
# 上传文件
# 只需上传 app.py 和 requirements.txt

# 赋权并运行
chmod +x app.py
pip install -r requirements.txt
screen python app.py
```

##### Docker 部署

```bash
docker run -d -p 3000:3000 \
  -e UUID=your-uuid \
  -e NEZHA_SERVER=nz.example.com:8008 \
  -e NEZHA_KEY=your-key \
  ghcr.io/xfwwl668/python:latest
```

#### ⚙️ 环境变量

与 nodejs-railway 类似，详见 [nodejs-railway](#3-nodejs-railway)

#### 🎯 适用场景

- ✅ Python 平台玩具
- ✅ 游戏平台
- ✅ 需要 Argo 隧道
- ✅ Docker 部署

#### ⚠️ 注意事项

- 仅限学习了解，非盈利目的
- 下载后 24 小时内删除
- 不得用于商业用途

---

### 5. java-ws

#### 📌 基本信息

| 项目 | 说明 |
|---|---|
| **GitHub** | [xfwwl668/java-ws](https://github.com/xfwwl668/java-ws) |
| **语言** | Java |
| **协议** | VLESS, Trojan, Shadowsocks (WS) |
| **特点** | Java 原生实现，无需三方内核 |
| **大小** | ~37KB |

#### 🚀 核心特性

- ✅ **多协议**：VLESS + Trojan + Shadowsocks
- ✅ **自动检测**：自动识别客户端协议
- ✅ **哪吒集成**：v0/v1 支持
- ✅ **自动端口**：端口占用时自动寻找
- ✅ **DNS 缓存**：减少 DNS 查询
- ✅ **域名屏蔽**：屏蔽测速网站
- ✅ **静默模式**：非 DEBUG 模式只显示关键日志
- ✅ **.env 支持**：支持系统环境变量和 .env 文件

#### 🛠️ 部署教程

##### 下载 JAR

```bash
# 从 Release 下载 server.jar
# 上传到 Java 服务器运行

java -jar server.jar
```

##### Maven 构建

```bash
cd java-ws
mvn -DskipTests package
java -jar target/server-1.0.jar
```

#### ⚙️ 环境变量

| 变量 | 是否必须 | 默认值 | 说明 |
|---|---|---|---|
| `UUID` | 否 | 随机 | 节点 UUID |
| `PORT` | 否 | `3000` | 节点监听端口 |
| `DOMAIN` | **是** | - | 项目分配的域名 |
| `NEZHA_SERVER` | 否 | - | 哪吒面板地址 |
| `NEZHA_PORT` | 否 | - | 哪吒 v0 agent 端口 |
| `NEZHA_KEY` | 否 | - | 哪吒密钥 |
| `NAME` | 否 | - | 节点名称前缀 |
| `SUB_PATH` | 否 | `sub` | 订阅 token |
| `AUTO_ACCESS` | 否 | false | 自动保活 |
| `DEBUG` | 否 | false | 调试模式 |

#### 🎯 适用场景

- ✅ Java 平台
- ✅ 需要多协议
- ✅ 要求无需内核
- ✅ 需要 DNS 缓存

#### ⚠️ 注意事项

- DOMAIN 变量必须设置
- 可使用 CF Workers 反代域名套 CDN 加速

---

### 6. edgetunnel

#### 📌 基本信息

| 项目 | 说明 |
|---|---|
| **GitHub** | [cmliu/edgetunnel](https://github.com/cmliu/edgetunnel) |
| **语言** | JavaScript |
| **协议** | VLESS, Trojan |
| **特点** | CF Workers/Pages 边缘隧道解密 |
| **大小** | ~150KB |

#### 🚀 核心特性

- ✅ **边缘计算**：CF Workers/Pages 部署
- ✅ **管理面板**：可视化后台管理
- ✅ **订阅系统**：自动订阅生成
- ✅ **SOCKS5 代理**：链式代理支持
- ✅ **优选 API**：优化网络延迟
- ✅ **多台适配**：Windows, Android, iOS, macOS

#### 🛠️ 部署教程

##### Workers 部署

1. 在 CF Worker 控制台创建新 Worker
2. 粘贴 `_worker.js` 内容
3. 设置变量 `ADMIN` 为管理员密码
4. 绑定 KV 命名空间，变量名 `KV`
5. 绑定自定义域，如 `vless.google.com`
6. 访问 `https://vless.google.com/admin` 登录

##### Pages 上传部署（推荐）

1. 下载 `main.zip`
2. 在 CF Pages 控制台上传资产
3. 设置环境变量 `ADMIN`
4. 绑定 KV 命名空间
5. 绑定自定义域

#### ⚙️ 环境变量

| 变量 | 说明 |
|---|---|
| `ADMIN` | 管理员密码 |
| `KEY` | 加密密钥（默认勿动） |
| `HOST` | 主机名 |
| `PROXYIP` | 反代 IP |
| `GO2SOCKS5` | SOCKS5 白名单 |

#### 🎯 适用场景

- ✅ CF Workers/Pages 免费平台
- ✅ 无需服务器
- ✅ 需要管理面板
- ✅ 需要边缘加速

#### ⚠️ 注意事项

- Error 1101 问题参考视频解析
- 绑定自定义域需使用次级域名
- 需绑定 KV 命名空间

---

### 7. cnet

#### 📌 基本信息

| 项目 | 说明 |
|---|---|
| **GitHub** | [xfwwl668/cnet](https://github.com/xfwwl668/cnet) |
| **语言** | Node.js / Python / Shell / Java / PHP |
| **协议** | ECH (WebSocket) |
| **特点** | ECH 代理 + Nezha + Cloudflare Tunnel 三合一 |
| **大小** | ~5KB |

#### 🚀 核心特性

- ✅ **ECH 代理**：端到端加密，最隐蔽
- ✅ **哪吒集成**：Agent 监控
- ✅ **Cloudflare Tunnel**：自动隧道
- ✅ **多语言**：5 种语言实现
- ✅ **自动守护**：60 秒检查进程状态
- ✅ **多架构**：Linux amd64/arm64, FreeBSD amd64/arm64

#### 🛠️ 部署教程

##### Node.js 部署

```bash
node index.js
```

##### Python 部署

```bash
python3 index.py
```

##### Shell 部署

```bash
chmod +x start.sh
./start.sh
```

##### Docker 部署

```bash
docker run -d \
  -e SERVER_PORT=7860 \
  -e TOKEN=mysecret \
  -e SUB_NAME=mynode \
  -e SUB_URL=https://example.com/upload \
  -e NSERVER=nezha.example.com:5555 \
  -e NKEY=your-agent-key \
  -e APP_TLS=true \
  -e TOK=eyJhIjoixxxx... \
  -e SHOW_LOG=true \
  -v cnet-data:/app \
  -p 7860:7860 \
  cnet
```

#### ⚙️ 环境变量

| 变量 | 默认值 | 说明 |
|---|---|---|
| `FILE_PATH` | `.` | 二进制下载路径 |
| `SHOW_LOG` | false | 显示日志 |
| `SERVER_PORT` | `7860` | 监听端口 |
| `PORT` | `7860` | 监听端口（备用） |
| `TOKEN` | `123` | ECH 密钥 |
| `SUB_NAME` | - | 订阅节点名称 |
| `SUB_URL` | - | 订阅上传地址 |
| `DOM` | - | 隧道域名 |
| `NSERVER` | - | 哪吒服务端地址 |
| `NKEY` | - | 哪吒 Agent 密钥 |
| `APP_UUID` | 自动 | Agent UUID |
| `APP_TLS` | true | 哪吒 TLS 连接 |
| `TOK` | - | Cloudflare Tunnel Token |

#### 🎯 适用场景

- ✅ 任意平台
- ✅ 需要 ECH 加密
- ✅ 需要三合一功能
- ✅ 要求最轻量

#### ⚠️ 注意事项

- 自用备份，非开源项目
- 下载后 24 小时内删除
- 不得用于商业用途

---

### 8. java-xah

#### 📌 基本信息

| 项目 | 说明 |
|---|---|
| **GitHub** | [xfwwl668/java-xah](https://github.com/xfwwl668/java-xah) |
| **语言** | Java |
| **协议** | Xray, Hysteria2, Cloudflared |
| **特点** | Java 版多协议部署 |
| **大小** | ~33KB |

#### 🎯 适用场景

- ✅ Java 平台
- ✅ 需要 Xray/HY2
- ✅ 需要 Cloudflared

---

### 9. aimili-vpngate

#### 📌 基本信息

| 项目 | 说明 |
|---|---|
| **GitHub** | [xfwwl668/aimili-vpngate](https://github.com/xfwwl668/aimili-vpngate) |
| **语言** | - |
| **协议** | vpngate |
| **特点** | 借助 vpngate.net 让 Linux 用干净 IP 出站 |
| **大小** | ~130KB |

#### 🎯 适用场景

- ✅ Linux 环境
- ✅ 需要干净 IP 出站
- ✅ 配合其他代理使用

---

### 10. node-ws-hug

#### 📌 基本信息

| 项目 | 说明 |
|---|---|
| **GitHub** | [xfwwl668/node-ws-hug](https://github.com/xfwwl668/node-ws-hug) |
| **语言** | JavaScript |
| **协议** | VLESS + Trojan (WS) |
| **特点** | Serverless 实现，双协议 |
| **大小** | ~6MB |

#### 🎯 适用场景

- ✅ Serverless 平台
- ✅ 需要双协议
- ✅ Node.js 环境

---

## 🖥️ 部署平台对比

### 平台适配矩阵

| 平台 | sbx-native | Sing-box | nodejs-railway | python-xray-argo | java-ws | edgetunnel | cnet |
|---|---|---|---|---|---|---|---|
| **VPS (Ubuntu/Debian)** | ✅ | ✅ | ✅ | ✅ | ✅ | - | ✅ |
| **VPS (CentOS/Rocky)** | ✅ | ✅ | ✅ | ✅ | ✅ | - | ✅ |
| **VPS (Alpine)** | - | ✅ | ✅ | ✅ | ✅ | - | ✅ |
| **Serv00** | ✅ | ✅ | ✅ | ✅ | ✅ | - | ✅ |
| **CT8** | ✅ | ✅ | ✅ | ✅ | ✅ | - | ✅ |
| **Railway** | ✅ | - | ✅ | ✅ | ✅ | - | ✅ |
| **Koyeb** | ✅ | - | ✅ | ✅ | ✅ | - | ✅ |
| **Fly.io** | ✅ | - | ✅ | ✅ | ✅ | - | ✅ |
| **CF Workers** | - | - | - | - | - | ✅ | - |
| **CF Pages** | - | - | - | - | - | ✅ | - |
| **游戏平台** | ✅ | - | ✅ | ✅ | ✅ | - | ✅ |
| **Docker** | ✅ | - | ✅ | ✅ | ✅ | - | ✅ |

---

## 📊 哪吒探针集成指南

### 哪吒 v0 配置

```bash
# 环境变量
export NEZHA_SERVER=nz.example.com
export NEZHA_PORT=5555
export NEZHA_KEY=your-agent-key
```

### 哪吒 v1 配置

```bash
# 环境变量
export NEZHA_SERVER=nz.example.com:8008
export NEZHA_KEY=your-client-secret
# NEZHA_PORT 留空
```

### 哪吒 TLS 自动检测

当哪吒端口为以下值之一时，自动开启 TLS：
- `443`, `8443`, `2096`, `2087`, `2083`, `2053`

---

## ❓ 常见问题解答

### Q1: 哪个项目最适合新手？

**A:** [Sing-box](#2-sing-box) 最适合新手，一键脚本，复制粘贴即可部署，全自动安装+保活。

### Q2: 哪个项目速度最快？

**A:** [Sing-box](#2-sing-box) 和 [sbx-native](#1-sbx-native) 都支持 HY2 和 TUIC，速度最快。

### Q3: 哪个项目最隐蔽？

**A:** [cnet](#7-cnet) 使用 ECH 端到端加密，最隐蔽。其次是 [sbx-native](#1-sbx-native) 和 [Sing-box](#2-sing-box) 的 VLESS Reality。

### Q4: 哪个项目最稳定？

**A:** [Sing-box](#2-sing-box) 最稳定，成熟的一键脚本，多平台支持。

### Q5: 哪个项目最适合免费平台？

**A:** [edgetunnel](#6-edgetunnel) 使用 CF Workers/Pages，完全免费。

### Q6: 哪个项目支持最多协议？

**A:** [sbx-native](#1-sbx-native) 支持 6 种协议：VMESS WS+Argo, VLESS Reality, HY2, TUIC, AnyTLS, SOCKS5。

### Q7: 无子进程是什么意思？

**A:** 传统方式启动 sing-box 会生成子进程，容易被检测。[sbx-native](#1-sbx-native) 通过原生 FFI 直接调用动态库，只有一个主进程，更隐蔽。

### Q8: Argo 隧道和固定隧道有什么区别？

**A:** 
- **临时隧道**：每次重启生成新域名，适合快速测试
- **固定隧道**：使用固定域名，适合长期使用

### Q9: 哪吒 v0 和 v1 有什么区别？

**A:**
- **v0**：使用 `NEZHA_PORT`，agent 端口
- **v1**：使用 `NZ_CLIENT_SECRET`，不需要端口，地址格式 `host:port`

### Q10: 如何解锁 GPT 和 Netflix？

**A:** 大多数项目默认配置已解锁，建议使用 VLESS Reality + VMESS WS+Argo 组合。

---

## 📝 许可证

本项目为个人使用指南，仅用于学习和交流目的。

各代理项目版权归原作者所有，请遵守各自项目的许可证。

---

<div align="center">

**[⬆️ 返回顶部](#🌐-代理项目详细对比指南)**

---

**[GitHub](https://github.com/xfwwl668/proxy-guide) | [Telegram](https://t.me/eooceu) | [GitHub Stars](https://github.com/xfwwl668/proxy-guide/stargazers)**

</div>
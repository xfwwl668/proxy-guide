<div align="center">

# 🌐 代理项目详细对比指南

**代理项目全面分析 · 部署教程 · 信号流程 · 选择建议**

[![GitHub stars](https://img.shields.io/github/stars/xfwwl668/proxy-guide)](https://github.com/xfwwl668/proxy-guide/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/xfwwl668/proxy-guide)](https://github.com/xfwwl668/proxy-guide/network)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/xfwwl668/proxy-guide/blob/main/LICENSE)
[![Telegram](https://img.shields.io/badge/Telegram-Group-blue?logo=telegram)](https://t.me/eooceu)

---

**本指南分析 5 个核心代理项目，涵盖协议对比、平台适配、信号流程、部署教程和选择建议**

</div>

---

## 📋 目录

- [快速选择指南](#-快速选择指南)
- [项目总览](#-项目总览)
- [信号流程详解](#-信号流程详解)
- [项目详细分析](#-项目详细分析)
  - [1. sbx-native](#1-sbx-native)
  - [2. paper-pro](#2-paper-pro)
  - [3. java-plugins-plus](#3-java-plugins-plus)
  - [4. Sing-box](#4-sing-box)
  - [5. deploy-vercel](#5-deploy-vercel)
- [项目对比矩阵](#-项目对比矩阵)
- [假人保活方案](#-假人保活方案)
- [常见设置详解](#-常见设置详解)
- [常见问题解答](#-常见问题解答)

---

## 🎯 快速选择指南

### 按平台选择

| 平台 | 推荐项目 | 为什么 |
|---|---|---|
| **PaaS (Railway/Koyeb/Fly)** | [sbx-native](#1-sbx-native) | 原生 FFI，无子进程，不易被检测 |
| **游戏机 (Serv00/CT8/Hostuno)** | [paper-pro](#2-paper-pro) | 替换主文件，MC 最自然，防回收 |
| **游戏机（已有 MC）** | [java-plugins-plus](#3-java-plugins-plus) | 插件版，加个插件就行，不影响原 MC |
| **VPS (Ubuntu/CentOS/Debian)** | [Sing-box](#4-sing-box) | 一键脚本，四协议组合，最稳定 |
| **Vercel** | [deploy-vercel](#5-deploy-vercel) | 免费部署，低延迟，需反代套 CDN |

### 按语言选择

| 语言 | 推荐项目 |
|---|---|
| **Node.js** | [sbx-native](#1-sbx-native) / [deploy-vercel](#5-deploy-vercel) |
| **Python** | [sbx-native](#1-sbx-native) |
| **Java** | [sbx-native](#1-sbx-native) / [paper-pro](#2-paper-pro) / [java-plugins-plus](#3-java-plugins-plus) |
| **Shell** | [Sing-box](#4-sing-box) |

---

## 📊 项目总览

### 五个项目定位

| 项目 | 定位 | 部署方式 | 平台 |
|---|---|---|---|
| **sbx-native** | 原生启动器 | FFI 调用 .so | PaaS / 游戏机 |
| **paper-pro** | MC 主文件 | 替换 server.jar | 游戏机 |
| **java-plugins-plus** | MC 插件 | 放 plugins/ 目录 | 游戏机 |
| **Sing-box** | VPS 脚本 | 一键安装 | VPS |
| **deploy-vercel** | Vercel 部署 | npm 部署 | Vercel |

### 核心区别

```
sbx-native:      独立运行，无依赖，原生 FFI
paper-pro:       MC 服务端内置，替换主文件
java-plugins-plus: MC 插件，不影响原 MC 功能
Sing-box:        VPS 一键脚本，全自动安装
deploy-vercel:   Vercel 免费部署，需反代套 CDN
```

---

## 🔄 信号流程详解

### 完整信号流程

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          完整信号流程图                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌──────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────┐  │
│  │  客户端   │────▶│   代理节点   │────▶│  优选域名/IP  │────▶│  目标网站 │  │
│  │          │     │              │     │              │     │          │  │
│  │ Siri     │     │ sbx-native   │     │ www.google   │     │ Google   │  │
│  │ Mihomo   │     │ paper-pro    │     │ .com         │     │          │  │
│  │ Clash    │     │ java-plugins │     │              │     │          │  │
│  │          │     │ Sing-box     │     │              │     │          │  │
│  └──────────┘     │              │     │              │     └──────────┘  │
│                   │ deploy-vercel│     └──────────────┘                   │
│                   └──────────────┘                                        │
│                        │                                                  │
│                        ▼                                                  │
│                   ┌──────────┐                                           │
│                   │  哪吒面板  │                                           │
│                   │  (监控)   │                                           │
│                   └──────────┘                                           │
│                        │                                                  │
│                        ▼                                                  │
│                   ┌──────────┐                                           │
│                   │  CF CDN   │                                           │
│                   │ (反代加速) │                                           │
│                   └──────────┘                                           │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 每个环节详解

#### 1️⃣ 客户端（你的设备）

```
常用客户端：
- Siri (iOS/Android) - 免费，简洁
- Mihomo (全平台) - 功能强大，支持策略
- Clash (全平台) - 经典，兼容性好
- Nekoray (Windows) - 付费，功能多

客户端做的事：
1. 读取订阅链接
2. 解析节点信息
3. 选择最佳节点
4. 建立加密连接
```

#### 2️⃣ 代理节点（服务器端）

```
节点在哪里运行：
- PaaS: Railway / Koyeb / Fly.io → sbx-native
- 游戏机: Serv00 / CT8 / Hostuno → paper-pro / java-plugins-plus
- VPS: 自建服务器 → Sing-box
- Vercel: 免费平台 → deploy-vercel

节点做的事：
1. 接收客户端加密连接
2. 解密流量
3. 通过优选域名/IP 转发
4. 获取目标网站内容
5. 加密返回客户端
```

#### 3️⃣ 优选域名/IP

```
什么是优选域名/IP：
- 优选域名：解析到 CDN 边缘节点的域名，延迟低
- 优选IP：直连 CDN 边缘节点 IP，跳过 DNS

为什么要优选：
1. 降低延迟 - 直连边缘节点
2. 提高稳定性 - 避免 DNS 污染
3. 隐藏真实节点 - 流量经过 CDN

常用优选域名：
- www.google.com
- api.github.com
- gitee.com
- www.visa.com.tw

怎么用：
1. 访问 https://sub.eooce.xx.kg 获取优选域名
2. 选择延迟最低的
3. 填入 CFIP 变量
```

#### 4️⃣ 反代 CDN

```
什么是反代：
- 用 CF Workers 把你的节点域名映射到另一个域名
- 流量先经过 CDN，再转发到真实节点

为什么要反代：
1. 套 CDN 加速 - 降低延迟
2. 隐藏真实 IP - 防止节点被封
3. 防检测 - 流量看起来像正常网站

怎么反代：
1. 创建 CF Worker
2. 粘贴反代代码
3. 绑定自定义域名
4. 客户端用新域名连接
```

#### 5️⃣ 哪吒面板

```
什么是哪吒：
- 服务器监控面板
- 显示节点连接数、流量、CPU/内存

为什么要用：
1. 监控节点状态
2. 统计流量
3. 管理多个节点

哪吒 v0 vs v1：
- v0: 需要 NEZHA_PORT，agent 端口
- v1: 不需要端口，地址格式 host:port
```

---

## 📖 项目详细分析

---

### 1. sbx-native

#### 📌 基本信息

| 项目 | 说明 |
|---|---|
| **GitHub** | [xfwwl668/sbx-native](https://github.com/xfwwl668/sbx-native) |
| **定位** | 原生启动器，无子进程 |
| **语言** | Java / Node.js / Python |
| **协议** | VMESS WS+Argo, VLESS Reality, HY2, TUIC, AnyTLS, SOCKS5 |
| **平台** | PaaS / 游戏机 / VPS |

#### 🚀 核心特性

- ✅ **原生 FFI**：通过 JNA/koffi 直接调用 sing-box .so，无子进程
- ✅ **6 种协议**：VMESS WS+Argo, VLESS Reality, HY2, TUIC, AnyTLS, SOCKS5
- ✅ **自动证书**：Reality X25519 keypair，HY2/TUIC/AnyTLS TLS 证书
- ✅ **自动订阅**：HTTP 暴露订阅链接
- ✅ **哪吒集成**：支持 v0 和 v1
- ✅ **TG 推送**：节点上下线通知
- ✅ **自动保活**：Merge-sub 节点上传

#### 🔄 信号流程

```
客户端 → 节点(PaaS/游戏机) → 优选域名/IP → 目标网站

具体：
1. 客户端连接节点（WS/TLS）
2. 节点解密流量
3. 节点通过优选域名/IP 转发
4. 获取目标内容
5. 加密返回客户端
```

#### 🛠️ 部署教程

##### Node.js 版本（推荐）

```bash
# 克隆仓库
git clone https://github.com/xfwwl668/sbx-native.git
cd sbx-native/nodejs

# 安装依赖
npm install

# 设置环境变量（编辑 .env 或在平台设置）
# 详见环境变量说明

# 运行
npm start
```

##### Python 版本

```bash
cd sbx-native/python
pip install -r requirements.txt
python3 app.py
```

##### Java 版本

```bash
cd sbx-native/java
mvn -DskipTests package
java -jar target/server-1.0.jar
```

#### ⚙️ 环境变量详解

| 变量 | 默认值 | 为什么这么设置 | 有什么用 |
|---|---|---|---|
| `UPLOAD_URL` | 空 | 不填不上传 | Merge-sub 订阅上传地址 |
| `PROJECT_URL` | 空 | 不填不保活 | 项目公网 URL，用于自动保活 |
| `AUTO_ACCESS` | false | 默认关闭 | 自动访问保活，true 开启 |
| `FILE_PATH` | `.npm` | 运行目录 | 存放 .so 动态库和配置 |
| `SUB_PATH` | `sub` | 订阅路径 | HTTP 订阅地址 `/sub` |
| `UUID` | 随机 | 每个节点唯一 | 客户端识别节点 |
| `NEZHA_SERVER` | 空 | 不填不监控 | 哪吒面板地址 |
| `NEZHA_PORT` | 空 | v1 留空 | 哪吒 v0 agent 端口 |
| `NEZHA_KEY` | 空 | 不填不监控 | 哪吒密钥 |
| `ARGO_DOMAIN` | 空 | 空用临时隧道 | Argo 固定隧道域名 |
| `ARGO_AUTH` | 空 | 空用临时隧道 | Argo 隧道 token/JSON |
| `ARGO_PORT` | `8001` | 固定隧道端口 | cloudflared 反代端口 |
| `S5_PORT` | 空 | 空不启用 | SOCKS5 端口 |
| `TUIC_PORT` | 空 | 空不启用 | TUIC 端口 |
| `HY2_PORT` | 空 | 空不启用 | HY2 端口 |
| `ANYTLS_PORT` | 空 | 空不启用 | AnyTLS 端口 |
| `REALITY_PORT` | 空 | 空不启用 | VLESS Reality 端口 |
| `CFIP` | `cf.877774.xyz` | 优选域名 | 流量转发目标 |
| `CFPORT` | `443` | 优选端口 | 转发目标端口 |
| `PORT` | `3000` | HTTP 端口 | 订阅服务监听端口 |
| `NAME` | 空 | 节点名称 | 订阅里显示的名称 |
| `CHAT_ID` | 空 | 不填不推送 | Telegram chat id |
| `BOT_TOKEN` | 空 | 不填不推送 | Telegram bot token |
| `DISABLE_ARGO` | false | 默认开启 | 禁用 Argo，true 禁用 |
| `SHOW_LOG` | false | 默认关闭 | 显示日志 |

#### 💡 为什么用 FFI？

```
传统方式：
- 启动 sing-box 二进制文件
- 生成子进程
- 容易被检测（子进程特征）

FFI 方式：
- 直接调用 sing-box .so 动态库
- 只有一个主进程
- 不易被检测（无子进程）
- 性能更好（无进程间通信）
```

#### 🎯 适用场景

- ✅ PaaS 平台（Railway / Koyeb / Fly.io）
- ✅ 游戏平台玩具
- ✅ 需要无子进程
- ✅ 需要多协议组合

---

### 2. paper-pro

#### 📌 基本信息

| 项目 | 说明 |
|---|---|
| **GitHub** | [eooce/paper-pro](https://github.com/eooce/paper-pro) |
| **定位** | MC 主文件，内置代理 |
| **语言** | Java |
| **协议** | 同 sbx-native（6 种） |
| **平台** | 游戏机（Serv00/CT8/Hostuno） |

#### 🚀 核心特性

- ✅ **MC 内置**：PaperMC 修改版，内置 sbx-native
- ✅ **替换主文件**：上传 server.jar 替换原来的
- ✅ **自然真实**：看起来像正常 MC 服务器
- ✅ **防回收**：MC 连接最自然，平台不检测
- ✅ **假人支持**：可加假人插件保持活跃

#### 🔄 信号流程

```
客户端 → MC 服务器(游戏机) → 优选域名/IP → 目标网站

同时：
MC 玩家连接 → 保持服务器活跃 → 防止回收

具体：
1. MC 客户端连接节点（WS/TLS）
2. 节点解密流量
3. 节点通过优选域名/IP 转发
4. 获取目标内容
5. 加密返回客户端

同时 MC 玩家连接保持服务器活跃
```

#### 🛠️ 部署教程

##### 步骤 1：Fork 仓库

```
1. 打开 https://github.com/eooce/paper-pro
2. 点击右上角 "Use this template"
3. 创建一个新仓库（建议私有）
4. 名称随意
```

##### 步骤 2：修改环境变量

```
1. 打开 Actions 菜单
2. 点击 "I understand my workflows, go ahead and enable them"
3. 打开文件：
   paper-server/src/main/java/io/papermc/paper/sbx/App.java
4. 修改第 41-64 行的环境变量
5. 不需要的留空
6. 保存后 Actions 自动构建
```

##### 步骤 3：下载 JAR

```
1. 等待 7-10 分钟构建完成
2. 打开仓库右侧 "Releases"
3. 下载 server.jar
```

##### 步骤 4：上传到游戏机

```
1. 登录游戏机面板（Serv00/CT8/Hostuno）
2. 上传 server.jar 到文件管理根目录
3. 运行即可
```

#### ⚙️ 环境变量（同 sbx-native）

| 变量 | 说明 |
|---|---|
| `UUID` | 节点 UUID，每个节点唯一 |
| `NEZHA_SERVER` | 哪吒面板地址 |
| `NEZHA_KEY` | 哪吒密钥 |
| `ARGO_DOMAIN` | Argo 固定隧道域名 |
| `ARGO_AUTH` | Argo 隧道密钥 |
| `CFIP` | 优选域名/IP |
| `CFPORT` | 优选端口 |
| `REALITY_PORT` | VLESS Reality 端口 |
| `HY2_PORT` | HY2 端口 |
| `TUIC_PORT` | TUIC 端口 |

#### 🎯 适用场景

- ✅ 游戏机平台（Serv00/CT8/Hostuno）
- ✅ 需要防回收
- ✅ 需要自然真实
- ✅ 需要 MC 环境

---

### 3. java-plugins-plus

#### 📌 基本信息

| 项目 | 说明 |
|---|---|
| **GitHub** | [eooce/java-plugins-plus](https://github.com/eooce/java-plugins-plus) |
| **定位** | MC 插件，内置代理 |
| **语言** | Java |
| **协议** | 同 sbx-native（6 种） |
| **平台** | Paper/Spigot/Purpur/BungeeCord/Fabric/Velocity |

#### 🚀 核心特性

- ✅ **MC 插件**：EssentialsX 修改版，内置代理
- ✅ **放插件目录**：不影响原 MC 功能
- ✅ **多平台支持**：Paper/Spigot/Purpur/BungeeCord/Fabric/Velocity
- ✅ **假人支持**：可配合假人插件使用
- ✅ **自动构建**：GitHub Actions 自动打包

#### 🔄 信号流程

```
客户端 → MC 插件(游戏机) → 优选域名/IP → 目标网站

同时：
MC 玩家连接 → 保持服务器活跃 → 防止回收

具体：
1. MC 客户端连接节点（WS/TLS）
2. 插件解密流量
3. 插件通过优选域名/IP 转发
4. 获取目标内容
5. 加密返回客户端
```

#### 🛠️ 部署教程

##### 步骤 1：Fork 仓库

```
1. 打开 https://github.com/eooce/java-plugins-plus
2. 点击右上角 "Use this template"
3. 创建一个新仓库（建议私有）
4. 名称随意
```

##### 步骤 2：修改环境变量

```
1. 打开 Actions 菜单
2. 点击 "I understand my workflows, go ahead and enable them"
3. 打开文件：
   common/src/main/java/com/example/essentialsx/common/AppService.java
4. 修改第 46-69 行的环境变量
5. 不需要的留空
6. 保存后 Actions 自动构建
```

##### 步骤 3：下载插件

```
1. 等待 2 分钟构建完成
2. 打开仓库右侧 "Releases"
3. 在 "Latest Build" 里下载 jar 文件
```

##### 步骤 4：上传到 MC 服务器

```
不同平台放不同目录：

- Paper/Spigot/Purpur：放到 plugins/ 文件夹
- BungeeCord：放到 plugins/ 文件夹
- Velocity：放到 plugins/ 文件夹
- Fabric：放到 mods/ 文件夹

上传后重启服务器即可
```

#### ⚙️ 环境变量

| 变量 | 说明 |
|---|---|
| `UUID` | 节点 UUID，每个节点唯一 |
| `NEZHA_SERVER` | 哪吒面板地址 |
| `NEZHA_KEY` | 哪吒密钥 |
| `ARGO_DOMAIN` | Argo 固定隧道域名 |
| `ARGO_AUTH` | Argo 隧道密钥 |
| `CFIP` | 优选域名/IP |
| `CFPORT` | 优选端口 |
| `REALITY_PORT` | VLESS Reality 端口 |
| `HY2_PORT` | HY2 端口 |
| `TUIC_PORT` | TUIC 端口 |
| `S5_PORT` | SOCKS5 端口 |

#### 🎯 适用场景

- ✅ 已有 MC 环境
- ✅ 不想替换主文件
- ✅ 需要保留原 MC 功能
- ✅ 多平台支持

---

### 4. Sing-box

#### 📌 基本信息

| 项目 | 说明 |
|---|---|
| **GitHub** | [xfwwl668/Sing-box](https://github.com/xfwwl668/Sing-box) |
| **定位** | VPS 一键脚本 |
| **语言** | Shell |
| **协议** | VLESS Reality, VMESS WS+Argo, HY2, TUIC |
| **平台** | VPS (Ubuntu/CentOS/Debian/Alpine) |

#### 🚀 核心特性

- ✅ **一键安装**：复制粘贴脚本即可
- ✅ **四协议组合**：VLESS Reality + VMESS WS+Argo + HY2 + TUIC
- ✅ **多平台**：VPS / Serv00 / CT8
- ✅ **自动端口**：智能端口分配
- ✅ **哪吒集成**：可选
- ✅ **TG 通知**：可选
- ✅ **自动保活**：内置

#### 🔄 信号流程

```
客户端 → VPS 节点 → 优选域名/IP → 目标网站

具体：
1. 客户端连接 VPS 节点（Reality/WS+Argo/HY2/TUIC）
2. VPS 解密流量
3. VPS 通过优选域名/IP 转发
4. 获取目标内容
5. 加密返回客户端
```

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

#### ⚙️ 环境变量

| 变量 | 说明 |
|---|---|
| `PORT` | 订阅端口 |
| `CFIP` | 优选域名/IP |
| `CFPORT` | 优选端口 |
| `UUID` | 节点 UUID |
| `NEZHA_SERVER` | 哪吒面板地址 |
| `NEZHA_PORT` | 哪吒端口 |
| `NEZHA_KEY` | 哪吒密钥 |
| `ARGO_DOMAIN` | Argo 固定隧道域名 |
| `ARGO_AUTH` | Argo 隧道密钥 |
| `SUB_TOKEN` | 订阅 token |
| `CHAT_ID` | Telegram chat id |
| `BOT_TOKEN` | Telegram bot token |

#### 🎯 适用场景

- ✅ VPS 服务器
- ✅ 需要最简单部署
- ✅ 追求多协议组合
- ✅ 需要最稳定

---

### 5. deploy-vercel

#### 📌 基本信息

| 项目 | 说明 |
|---|---|
| **GitHub** | [vvqx/deploy-vercel](https://github.com/vvxw/deploy-vercel) |
| **定位** | Vercel 部署工具 |
| **语言** | JavaScript |
| **协议** | VLESS WS+TLS, Trojan WS+TLS, Shadowsocks WS |
| **平台** | Vercel（免费） |

#### 🚀 核心特性

- ✅ **Vercel 免费**：完全免费部署
- ✅ **低延迟**：全球 CDN 加速
- ✅ **自动构建**：GitHub Actions 自动打包
- ✅ **哪吒集成**：支持 v0 和 v1
- ✅ **自动保活**：IP 上报保活

#### 🔄 信号流程

```
客户端 → CF Worker(反代) → Vercel 节点 → 优选域名/IP → 目标网站

具体：
1. 客户端连接 CF Worker（自定义域名）
2. CF Worker 转发到 Vercel
3. Vercel 解密流量
4. Vercel 通过优选域名/IP 转发
5. 获取目标内容
6. 加密返回客户端
```

#### ⚠️ 重要：为什么需要反代？

```
问题：
- Vercel 分配的域名已被墙
- 无法直接连接 Vercel 域名

解决：
1. 部署到 Vercel
2. 创建 CF Worker 反代
3. 绑定自定义域名
4. 客户端用新域名连接
```

#### 🛠️ 部署教程

##### 步骤 1：Fork 仓库

```
1. 打开 https://github.com/vvxw/deploy-vercel
2. 点击右上角 "Use this template"
3. 创建一个新仓库（建议私有）
4. 名称随意
```

##### 步骤 2：修改环境变量

```
1. 打开 index.js
2. 修改第 1-30 行的环境变量
3. 不需要的留空
4. 保存
```

##### 步骤 3：替换伪装网页

```
1. 用 AI 生成一个纯 HTML 网页
2. 替换 index.html
3. 保存
```

##### 步骤 4：部署到 Vercel

```
1. 打开 Vercel 控制台
2. 点击 "New Project"
3. Import 你的仓库
4. 选择默认配置
5. Install Command 设置为 "npm install"
6. 点击 "Deploy"
7. 等待部署完成
```

##### 步骤 5：反代套 CDN

```
1. 创建 CF Worker
2. 粘贴以下代码：

export default {
    async fetch(request, env) {
        let url = new URL(request.url);
        if (url.pathname.startsWith('/')) {
            var arrStr = [
                'xxx-xxx.vercel.app',   // 填写你的 Vercel 域名
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

3. 绑定自定义域名
4. 将反代后的域名填入 index.js 的 DOMAIN 变量
5. 用 https://www.jshaman.com/index.html 混淆后保存
```

#### ⚙️ 环境变量

| 变量 | 说明 |
|---|---|
| `UUID` | 节点 UUID |
| `NEZHA_SERVER` | 哪吒面板地址 |
| `NEZHA_KEY` | 哪吒密钥 |
| `DOMAIN` | 反代后的域名 |
| `AUTO_ACCESS` | 自动保活 |
| `SUB_PATH` | 订阅路径 |
| `NAME` | 节点名称 |
| `PORT` | 端口 |
| `SHOW_LOG` | 显示日志 |
| `WSPATH` | WS 路径 |

#### 🎯 适用场景

- ✅ Vercel 免费平台
- ✅ 需要低延迟
- ✅ 已有 CF Worker
- ✅ 愿意反代套 CDN

---

## 📊 项目对比矩阵

### 功能对比

| 功能 | sbx-native | paper-pro | java-plugins-plus | Sing-box | deploy-vercel |
|---|---|---|---|---|---|
| **无子进程** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **VLESS Reality** | ✅ | ✅ | ✅ | ✅ | ❌ |
| **VMESS WS+Argo** | ✅ | ✅ | ✅ | ✅ | ❌ |
| **HY2** | ✅ | ✅ | ✅ | ✅ | ❌ |
| **TUIC** | ✅ | ✅ | ✅ | ✅ | ❌ |
| **Trojan** | ✅ | ✅ | ✅ | ❌ | ✅ |
| **Shadowsocks** | ✅ | ✅ | ✅ | ❌ | ✅ |
| **哪吒 v0** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **哪吒 v1** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **TG 推送** | ✅ | ✅ | ✅ | ✅ | ❌ |
| **自动保活** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Argo 隧道** | ✅ | ✅ | ✅ | ✅ | ❌ |
| **CF 反代** | ❌ | ❌ | ❌ | ❌ | ✅ |

### 平台对比

| 平台 | sbx-native | paper-pro | java-plugins-plus | Sing-box | deploy-vercel |
|---|---|---|---|---|---|
| **Railway** | ✅ | ❌ | ❌ | ❌ | ❌ |
| **Koyeb** | ✅ | ❌ | ❌ | ❌ | ❌ |
| **Fly.io** | ✅ | ❌ | ❌ | ❌ | ❌ |
| **Serv00** | ✅ | ✅ | ✅ | ✅ | ❌ |
| **CT8** | ✅ | ✅ | ✅ | ✅ | ❌ |
| **Hostuno** | ✅ | ✅ | ✅ | ❌ | ❌ |
| **VPS** | ✅ | ❌ | ❌ | ✅ | ❌ |
| **Vercel** | ❌ | ❌ | ❌ | ❌ | ✅ |
| **游戏机 MC** | ✅ | ✅ | ✅ | ❌ | ❌ |

### 难度对比

| 项目 | 难度 | 构建时间 | 部署方式 |
|---|---|---|---|
| **sbx-native** | ⭐⭐ | 即时 | 上传文件 |
| **paper-pro** | ⭐⭐⭐ | 7-10 分钟 | 替换主文件 |
| **java-plugins-plus** | ⭐⭐ | 2 分钟 | 放插件目录 |
| **Sing-box** | ⭐ | 即时 | 一键脚本 |
| **deploy-vercel** | ⭐⭐⭐ | 即时 | Vercel 部署 + 反代 |

---

## 👥 假人保活方案

### 为什么需要假人？

玩具平台（Serv00/CT8/Hostuno）回收服务器的条件：

| 回收条件 | 说明 | 风险等级 |
|---|---|---|
| **长时间无连接** | 超过 24-48 小时无人连接 | 🔴 高 |
| **连接数过低** | 长期 0 连接 | 🔴 高 |
| **CPU 使用率过低** | 长期闲置 | 🟡 中 |
| **内存使用率过低** | 长期闲置 | 🟡 中 |

### 方案对比

| 方案 | 检测风险 | 稳定性 | 隐蔽性 | 推荐度 |
|---|---|---|---|---|
| **MC 假人插件** | 🟢 极低 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **sbx-native 保活** | 🟢 低 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **代理流量保活** | 🟢 低 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **脚本模拟连接** | 🔴 高 | ⭐⭐⭐ | ⭐⭐ | ⭐⭐ |
| **固定间隔访问** | 🟡 中 | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |

### 方案 1：MC 假人插件（推荐）

```
优势：
- 最自然 - 模拟真实玩家行为
- 平台不检测 - 看起来像正常玩家
- 可控制 - 定时上下线
- 多玩家 - 可模拟多个玩家

劣势：
- 需要 MC 环境
- 需要配置插件

推荐插件：
- Citizens（NPC 管理）
- Dummy Players（假人）
- FakePlayer（假人）
```

#### 配合 paper-pro 使用

```
步骤：
1. 部署 paper-pro（替换 server.jar）
2. 安装假人插件到 plugins/ 目录
3. 配置假人数量和时间表
4. 保持服务器 24/7 活跃

配置示例：
- 3 个假人，每 5 分钟上下线一次
- 模拟真实玩家行为（移动、聊天）
- 保持服务器活跃
```

#### 配合 java-plugins-plus 使用

```
步骤：
1. 部署 java-plugins-plus（放 plugins/ 目录）
2. 安装假人插件到 plugins/ 目录
3. 配置假人数量和时间表
4. 保持服务器活跃

注意：
- java-plugins-plus 本身是 EssentialsX 插件
- 假人插件也是 plugins/ 目录
- 两个插件可以共存
```

### 方案 2：sbx-native 自动保活

```
配置：
- AUTO_ACCESS=true
- PROJECT_URL=https://your-server-url

效果：
- 每 5 分钟自动访问
- 保持服务器活跃
- 防止回收
```

### 方案 3：代理流量保活

```
配置：
# 随机间隔访问订阅链接
curl -s --connect-timeout 10 "https://your-sub-url/sub"

# 随机间隔（300-600 秒）
sleep $((300 + RANDOM % 300))
```

---

## ⚙️ 常见设置详解

### UUID

```
为什么每个节点要唯一：
- 客户端识别节点
- 防止节点冲突
- 哪吒监控区分节点

怎么生成：
- 使用在线 UUID 生成器
- 每个节点随机生成一个
- 格式：xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

### NEZHA_SERVER / NEZHA_KEY

```
哪吒监控什么：
- 连接数
- 流量（上传/下载）
- CPU/内存使用
- 节点状态

哪吒 v0 vs v1：
- v0: 需要 NEZHA_PORT，agent 端口
- v1: 不需要端口，地址格式 host:port

配置示例：
v0: NEZHA_SERVER=nz.example.com, NEZHA_PORT=5555
v1: NEZHA_SERVER=nz.example.com:8008, NEZHA_PORT 留空
```

### ARGO_DOMAIN / ARGO_AUTH

```
Argo 隧道是什么：
- Cloudflare 隧道
- 把流量从 CF 边缘节点转到你的服务器
- 不需要开放端口

临时隧道 vs 固定隧道：
- 临时：每次重启生成新域名
- 固定：使用固定域名，长期使用

配置示例：
ARGO_DOMAIN=abc.2go.com
ARGO_AUTH=your-token-or-json
```

### CFIP / CFPORT

```
优选域名/IP 是什么：
- 解析到 CDN 边缘节点的域名
- 延迟低，稳定性高

为什么要优选：
- 降低延迟
- 避免 DNS 污染
- 隐藏真实节点

怎么选：
1. 访问 https://sub.eooce.xx.kg
2. 选择延迟最低的
3. 填入 CFIP

常用优选：
- www.google.com
- api.github.com
- gitee.com
```

### UPLOAD_URL

```
订阅上传是什么：
- 把节点信息上传到 Merge-sub
- 一个订阅链接包含所有节点

为什么要上传：
- 管理多个节点
- 方便客户端订阅
- 自动更新

配置示例：
UPLOAD_URL=https://merge.serv00.net
```

### CHAT_ID / BOT_TOKEN

```
TG 推送有什么用：
- 节点上线通知
- 节点下线通知
- 节点流量统计

为什么要推送：
- 及时发现节点问题
- 管理多个节点
- 远程监控

配置示例：
CHAT_ID=12345
BOT_TOKEN=5678:AA812jqIA...
```

---

## ❓ 常见问题解答

### Q1: 哪个项目最适合新手？

**A:** [Sing-box](#4-sing-box) 最适合新手，一键脚本，复制粘贴即可部署。

### Q2: 哪个项目最稳定？

**A:** [Sing-box](#4-sing-box) 最稳定，成熟的一键脚本，多平台支持。

### Q3: 哪个项目最隐蔽？

**A:** [sbx-native](#1-sbx-native) 最隐蔽，原生 FFI，无子进程，不易被检测。

### Q4: 哪个项目最适合免费平台？

**A:** [deploy-vercel](#5-deploy-vercel) 使用 Vercel，完全免费。

### Q5: 哪个项目支持最多协议？

**A:** [sbx-native](#1-sbx-native) / [paper-pro](#2-paper-pro) / [java-plugins-plus](#3-java-plugins-plus) 都支持 6 种协议。

### Q6: 无子进程是什么意思？

**A:** 传统方式启动 sing-box 会生成子进程，容易被检测。[sbx-native](#1-sbx-native) 通过原生 FFI 直接调用动态库，只有一个主进程，更隐蔽。

### Q7: Argo 隧道和固定隧道有什么区别？

**A:** 
- **临时隧道**：每次重启生成新域名，适合快速测试
- **固定隧道**：使用固定域名，适合长期使用

### Q8: 哪吒 v0 和 v1 有什么区别？

**A:**
- **v0**：使用 `NEZHA_PORT`，agent 端口
- **v1**：使用 `NZ_CLIENT_SECRET`，不需要端口，地址格式 `host:port`

### Q9: 如何解锁 GPT 和 Netflix？

**A:** 大多数项目默认配置已解锁，建议使用 VLESS Reality + VMESS WS+Argo 组合。

### Q10: 假人怎么加？

**A:** 
- 用 [paper-pro](#2-paper-pro)：替换主文件后，假人插件放 plugins/ 目录
- 用 [java-plugins-plus](#3-java-plugins-plus)：插件放 plugins/ 目录，假人插件也放 plugins/ 目录
- 推荐插件：Citizens / Dummy Players / FakePlayer

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
# 道旅RollingGo酒店MCP | RollingGo— Hotel Search & Booking MCP

[![Version](https://img.shields.io/badge/Version-1.0.0-blue.svg)](https://github.com/DIDA-AI/DIDA-Hotel-MCP-CN/releases)
[![ModelScope](https://img.shields.io/badge/ModelScope-Rank%237-brightgreen.svg)](https://modelscope.cn/)
[![Calls](https://img.shields.io/badge/Calls-847.3k-orange.svg)](https://github.com/DIDA-AI/DIDA-Hotel-MCP-CN)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

🏠 [官网](https://rollinggo.store/)🚀[ 快速开始](#快速开始)📚[ 使用示例](#使用示例)💬[ 技术支持](#技术支持)📚 [接入视频(0基础0代码可实操)](https://www.xiaohongshu.com/discovery/item/6a22affe0000000017029504?app_platform=ios&app_version=9.33.4&share_from_user_hidden=true&xsec_source=app_share&type=video&xsec_token=CBwWFsJ1iLP0QLjYWHV4RatLComUk4vekr3adma28ssMU=&author_share=1&xhsshare=CopyLink&shareRedId=NzxGN0RLSTo-O0pGTEwzOTszTkBGSUlM&apptime=1782376771&share_id=09ec1dc114174939916826fc8471d07a&code=051iMqFa1D1hXL08HNGa1Eq5Jb3iMqF7&state=wx_oauth)
📚 [接入文档](https://rollinggo.store/docs/mcp-docs/quick-start) · 💰[开发者变现](https://rollinggo.store/docs/partnerdoc/partner1) 



## 项目简介
**道旅酒店MCP**为 AI Agent 和 MCP 客户端提供酒店预订能力，它适合希望在 AI 产品中接入酒店交易能力的开发者、Agent 构建者、旅游产品团队和企业差旅场景，企业和个人均可完全免费一键接入，无调用量限制。

🔍 按需求**智能筛选和比价**，省心挑酒店

📋 实时查**房型、报价和退改规则**，明明白白不踩坑

🛏️ 心仪房型提前**锁定**，不用愁晚订没房

💳 说句“下单”就实时确认库存和价格**直接付**

📑 订单状态随时能查，全程都省心

💴 还能设置24 小时自动**盯价**，降价马上**提醒**



| 服务 | 端点 | 已上线 Tool | 认证 |
|------|------|------------|------|
| 酒店 MCP | `https://mcp.rollinggo.cn/mcp` | searchHotels, getHotelDetail, getHotelSearchTags | `Authorization: Bearer <YOUR_API_KEY>` |

- **传输协议**：`streamable-http`
- **价格**：完全免费，无调用量限制
- **接入方式**：参考本文档可自助完成，适合需要短时间完成快速原型验证和工具开发

道旅MCP还提供OAuth 2.0 授权码模式，提供7个工具，包括：getHotelSearchTags, searchHotels, getHotelDetail, hotelPriceConfirm, searchHotelOrders等。该模式适合企业级生产应用深度集成，需商务对接contact@rollinggo.ai。
> 如果你是国际用户，或者你的目标用户为中国以外的国际化国家，请参考 [Dida-Hotel-MCP-Global](https://github.com/DIDA-AI/Dida-Hotel-MCP-Global)。该版本支持信用卡支付，适合非中国大陆地区的业务场景。



## MCP亮点
- ✅ **实时库存价确** - 库存直连+实时价格确认能力，信息零延迟，查询结果均可直接预订
- ✅ **成熟供应链保障** - 全球第三大酒旅B2B官方数据源，14年旅行产品供应链积累，全链路API直连
- ✅ **海量酒店覆盖** - 坐拥200万+酒店资源，覆盖全球主要目的地
- ✅ **直签酒店资源** - 11万+直签酒店直连，价格库存实时响应，确保查询结果准确可订
- ✅ **多元供应体系** - 整合500+全球供应商，涵盖各类酒店品牌，满足不同用户预订需求
- ✅ **差异化价格优势** - 锚定OTA上游供应，海外酒店及上海、香港、日韩等热门目的地价格优势显著
- ✅ **兼容性** - 支持 Cursor、Claude Code、Codex、Windsurf、Copilot 等 40 多种主流大模型代理，针对ClawHub/扣子/Qclaw等Agent 平台，还提供[全能订酒店Skill](https://rollinggo.store/solutions/skills)
- ✅ **开发者返佣** - 接入即可按国家设置加价比例，当用户通过你的工具完成预订，对应金额将作为返佣，订单、收益、提现状态实时可查，灵活提现
  
## 适合用户
- 正在开发 AI Agent 的团队或个人开发者
- 想在 MCP Client 中接入酒店预订能力的开发者
- 正在构建旅行规划、差旅管理、OTA、生活服务类智能体的开发者
- 希望验证 AI Agent 商业交易闭环的产品团队
- 有酒店查询、酒店比价、盯价提醒接入需求的用户

## 应用场景
- **通用Agent**：让Agent 直接拥有原生酒店预订能力，用户在自然对话中即可完成从比价筛选到订单创建的全流程
- **AI旅行助手**：根据用户目的地、日期、预算和个性化偏好精准推荐酒店，支持多维度需求匹配
- **MCP / Agent Demo**：快速验证 "AI Agent 直接完成酒店交易" 的产品能力，打造可演示的完整闭环

## 核心功能
- 支持**城市名称、热门景点、交通枢纽、酒店名称、具体地址**等 6 种目标地点类型精准搜索
- 提供灵活的**星级筛选、入住日期设置、住宿天数配置、价格区间过滤**等专业筛选功能
- 基于用户个人偏好提供**个性化推荐，生成高性价比、好评热门、人气精选**等多维度专业榜单
- 全程自然语言交互，智能完成从**地点解析、筛选比价、个性化推荐到订单生成**的完整闭环



## 快速开始
> 💡 总结来说，你只需要做两件事：申请API Key+ 在AI助手中一键配置，无需编写代码，就能让任何支持MCP的AI助手具备酒店搜索能力，5 分钟内完成第一次 MCP Tool 调用

### 第一步：获取API密钥

1. [点击申请](https://travelportal-partner-center.dida.com/register?lang=zh)
2. 填写基本信息，0等待，申领即得。
3. 为什么需要填写信息申请 KEY？酒店价格、库存和订单能力涉及真实交易链路，因此我们需要为每个开发者开通专属的独立KEY。申请 KEY 时仅需填写少量信息，这样做主要是为了减少无效配置成本，保护接口稳定性，避免恶意调用或异常流量，在测试订单、价格查询、库存校验等问题上能及时联系到你。

### 第二步：接入 Agent 工具

> 推荐 Claude CLI、Codex、Cursor 三个客户端。其他支持 MCP 的客户端（如 Kiro、豆包等）配置方式类似。

### Claude CLI

在项目根目录创建 `.mcp.json`：

```json
{
  "mcpServers": {
    "DIDA-Hotel": {
      "url": "https://mcp.rollinggo.cn/mcp",
      "type": "http",
      "headers": {
        "Authorization": "Bearer YOUR_API_KEY"
      }
    }
  }
}
```

也可以通过命令行直接添加：

```bash
claude mcp add \
  --transport http \
  --header "Authorization: Bearer YOUR_API_KEY" \
  DIDA-Hotel \
  https://mcp.rollinggo.cn/mcp

```

### Codex

配置文件位置：项目根目录 `.codex/config.json` 或全局 `~/.codex/config.json`

```json
{
  "mcpServers": {
    "DIDA-Hotel": {
      "url": "https://mcp.rollinggo.cn/mcp",
      "type": "streamable-http",
      "headers": {
        "Authorization": "Bearer YOUR_API_KEY"
      }
    }
  }
}
```

### Cursor

配置文件位置：项目根目录 `.cursor/mcp.json` 或全局 `~/.cursor/mcp.json`

```json
{
  "mcpServers": {
    "DIDA-Hotel": {
      "url": "https://mcp.rollinggo.cn/mcp",
      "type": "streamable-http",
      "headers": {
        "Authorization": "Bearer YOUR_API_KEY"
      }
    }
  }
}
```

> 将 `YOUR_API_KEY` 替换为你收到的实际 API Key。酒店和机票使用相同的认证方式，区别仅在于 URL（`/mcp` vs `/mcp/flight`）。

### cURL 直接测试

> **注意**：cURL 必须带 `-H "Accept: application/json, text/event-stream"` 头，否则服务端返回 400。

```bash
curl -X POST https://mcp.rollinggo.cn/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "jsonrpc": "2.0",
    "method": "tools/call",
    "params": {
      "name": "searchHotels",
      "arguments": {
        "originQuery": "上海外滩五星酒店",
        "place": "上海外滩",
        "placeType": "景点",
        "checkInParam": {
          "checkInDate": "2026-06-01",
          "stayNights": 2
        },
        "filterOptions": {
          "starRatings": [5.0]
        },
        "size": 3
      }
    },
    "id": 1
  }'
```

---

## 第三步：第一次 MCP 调用

配置完成后，对你的 AI 助手说：

> "帮我搜一下上海外滩附近后天入住的五星酒店"

AI 会自动调用 `searchHotels` Tool，返回酒店列表。

### 酒店搜索示例

```json
{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "params": {
    "name": "searchHotels",
    "arguments": {
      "originQuery": "上海外滩五星酒店",
      "place": "上海外滩",
      "placeType": "景点",
      "checkInParam": {
        "checkInDate": "2026-06-01",
        "stayNights": 2
      },
      "filterOptions": {
        "starRatings": [5.0]
      },
      "size": 3
    }
  },
  "id": 1
}
```


## 使用示例
### 示例1：酒店盯价提醒
> "帮我监控杭州西溪湿地附近这家酒店"

### 示例2：城市酒店搜索
> "帮我看看未来三天内，杭州有哪些4星以上的酒店推荐？"

![showcase1](https://raw.githubusercontent.com/young63/dida-picbed/main/showcase1.png)
![showcase2](https://raw.githubusercontent.com/young63/dida-picbed/main/showcase2.png)



### 示例2：景点周边搜索
> "2026年七夕节，想在香港迪士尼附近找个性价比高的酒店"

![showcase3](https://raw.githubusercontent.com/young63/dida-picbed/main/showcase3.png )
![showcase5](https://raw.githubusercontent.com/young63/dida-picbed/main/showcase5.png)
---


## ✨ 功能特性

| 功能 | 说明 |
|------|------|
| 🏙️ **多地点搜索** | 支持城市、景点、机场、火车站、地铁站等 |
| 📅 **日期筛选** | 指定入住日期和住宿天数 |
| ⭐ **星级过滤** | 支持0-5星筛选，精确到0.5星梯度 |
| 📍 **距离搜索** | 以景点为中心，限定半径范围（米） |
| 🛏️ **设施详情** | 可选返回酒店设施、房间设施信息 |
| 🌐 **多语言** | 支持中文、英文等语言环境 |


### 配置参数说明

#### 常用核心参数

| 参数 | 必填 | 说明 | 示例 |
|------|------|------|------|
| place | ✅ | 搜索地点 | 杭州、迪士尼 |
| placeType | ✅ | 地点类型 | 城市、景点、机场、地铁站、区/县... |
| originQuery | ✅ | 你的原始需求描述 | 帮我找酒店 |
| checkIn | ❌ | 入住日期(yyyy-MM-dd) | 2026-05-01 |
| stayNights | ❌ | 住宿天数 | 2 |
| starRatings | ❌ | 星级范围 | [4, 5] 表示4-5星 |
| size | ❌ | 返回数量(默认10)，最大20 | 5 |

> 注意：
> - 实际字段以接口数据返回为准，上述示例仅展示部分字段。
> -   随着后端能力演进，字段可能会新增或调整，MCP 客户端侧建议按"有则使用、无则忽略"的方式做兼容。


## ❓ 常见问题
### Q: 支持哪些AI助手/IDE？

**A:** 目前支持以下平台：
- Cursor
- Windsurf
- Antigravity
- Claude Desktop
- Cherry studio等其他支持MCP协议的客户端

### Q: 搜索结果包含哪些信息？

**A:** 默认返回酒店名称、星级、价格、地址、预订链接，酒店图片、酒店设施等。(具体可参考实际返回数据)
### Q: 有调用次数限制吗？

**A:** 目前阶段免费使用。


## 🔒 安全与鉴权

### 认证方式

| 环境 | 认证方式 | Header |
|------|----------|--------|
| 远程(云端) | Bearer Token | \Authorization: Bearer YOUR_API_KEY\ |
| 本地服务 | Secret Key | \X-Secret-Key: YOUR_API_KEY\ |

### 安全建议

- API Key请妥善保管，不要硬编码在代码中
- 生产环境建议使用环境变量管理
- 公网访问请使用HTTPS协议



## 🤝技术支持
感谢每一位开发者的交流、分享与反馈，让DIDA的迭代更高效。

加入微信群，核心开发团队会全程在线，协助搞定环境配置、接口调试，一起跑通第一个成功的酒店预订调用，零障碍快速上线。

![Support WeChat](support-wehcat%20group.png)

你可以在群内获得：
- ✅ 接入配置指导
- ✅ API / MCP 调用问题排查
- ✅ 酒店搜索、价格、预订流程说明
- ✅ 适合你业务场景的集成建议

邮箱：[york.lu@dida.com](mailto:york.lu@dida.com)

## ⚠ 附录：道旅Hotel MCP (OAuth) v2.3 更新说明

v2.3 优化了订单查询结构，新增多个订单详情字段，帮助 Agent 更好地处理入住、支付和取消场景。注：此更新仅适用于 OAuth 接入版本，非本文档所述的 API Key 版本。OAuth 版本需商务对接。

### What changed

#### Unchanged tools (4)

- `getHotelSearchTags` — 获取所有可用酒店筛选标签
- `searchHotels` — 按条件搜索全球酒店列表
- `getHotelDetail` — 获取指定酒店的可用房型及价格
- `hotelPriceConfirm` — 锁定选中房型的实时最终零售价

#### Modified tools (2)

- `createHotelBookingWithPaymentURL` — 移除 `alipayUrlScene` 参数；`bookingResult.paymentUrl` 统一为通用收银台
- `searchHotelOrders` — 输出精简为 9 个核心字段（`orderNo`、`hotelName`、`roomName`、`orderStatus`、`totalPrice` 等），仅用于列表展示；完整详情移至独立接口查询

#### New tools (1)

- `getHotelOrderDetail` — 按 `orderNo` 查询完整订单详情，包含 `hotelConfirmationNo`、入住人名单、床型、联系电话、经纬度、支付/取消截止时间、政策标识等

#### New fields

- `hotelConfirmationNo` — 酒店侧真实确认号，供前台查询入住
- `stayInfo.bedTypeStr` — 床型中文描述（如 `"1张特大床 (1.8m)"`）
- `stayInfo.guestNames` — 入住人拼音/英文姓名列表，用于入住核验
- `priceInfo.paymentDeadline` — 支付截止时间（`YYYY-MM-DD HH:mm:ss`），用于倒计时提醒
- `policyInfo.freeCancelDeadline` — 免费取消截止时间，用于判断退款窗口
- `policyInfo.isCancelable` — 当前时刻是否仍可免费取消


#### **工具总数**： 7 个（V2.2 为 6 个）—— 新增 1 个，变更 2 个，未变更 4 个。
---
**Made with ❤️ by DIDA Team**
</div>

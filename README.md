# AI Finance Daily

[![Daily update](https://github.com/theneao/ai-finance-daily/actions/workflows/daily.yml/badge.svg)](https://github.com/theneao/ai-finance-daily/actions/workflows/daily.yml)

每天自动搜集 AI 投资研究、金融 Agent、交易框架、金融工具和交易游戏。论文源结合 arXiv 与 [Hugging Face Trending Papers](https://huggingface.co/papers/trending)，仅筛选 AI 投资交易研究，按 arXiv ID 去重；Trending 中重新走热的旧论文也可收录，保留原发表日期与 HF 社区热度。

**[📚 完整热门项目总榜（全部历史项目 · Star 排名 · 分类导航）](HOT_PROJECTS.md)** · **[月度总结](archive/index.md)**

热门总榜每天随日报刷新，按 Star 降序排列。**500–999 Star** 须近一年有代码更新且 Star 增长 **≥ 30%**。**1,000 Star 及以上**须近三年有代码更新。分类包括 Agent、交易框架（回测/语言）、工具（看板/数据源/创意）、游戏、论文研究，市场标签区分美股、A股、虚拟货币、期货、因子。

每天北京时间 **08:30** 运行，也可在 Actions 页面手动运行。首页保留当日日报；历史内容每月仅一份 Markdown，月内累计去重更新，不再保存逐日日报文件。`data/` 中 JSON 用于累计和去重，不是逐日归档。日报项目须 **Star ≥ 200**，且近半年有代码更新或 Star 增长 **≥ 30%**。涨幅按窗口内最早一条有效 Star 快照与当前值比较，缺少历史快照时无法验证增长。项目名称、简介、topics、README 和论文标题、摘要会进行政治敏感主题筛选，检查不可用的仓库暂缓展示。同时排除 `.github`/个人主页仓库、资源导航合集及超过 400 字符的冗长简介仓库，优先展示可使用的项目。检索范围和阈值见 [`config.yaml`](config.yaml)。

---

## 热门项目 · Star ≥ 500

按 Star 降序，按分类直接展示各类前 10 个项目；[查看全部热门项目](HOT_PROJECTS.md)。

### Agent

| 项目 | 简介 | ⭐ | 半年内已观测涨幅 | 语言 | 分类 | 市场/因子 | 能力/用途 |
|---|---|---:|---:|---|---|---|---|
| [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | TradingAgents: Multi-Agents LLM Financial Trading Framework | 121964 | — | Python | Agent | 未明确（需查文档） | Agent |
| [openbq-org/OpenBB](https://github.com/openbq-org/OpenBB) | Open Data Platform for analysts, quants and AI agents. | 75326 | — | Python | Agent | 虚拟货币、期货 | Agent |
| [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | LLM 驱动的多市场股票智能分析系统：多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。  LLM-powered multi-market stock analysis system with multi-source market data, real-time news, decision dashboard, automated notifications, and cost-free scheduled runs. | 69704 | — | Python | Agent | 未明确（需查文档） | Agent |
| [microsoft/qlib](https://github.com/microsoft/qlib) | Qlib is an AI-oriented Quant investment platform that aims to use AI tech to empower Quant Research, from exploring ideas to implementing productions. Qlib supports diverse ML modeling paradigms, including supervised learning, market dynamics modeling, and RL, and is now equipped with https://github.com/microsoft/RD-Agent to automate R&D process. | 50213 | — | Python | Agent | 未明确（需查文档） | Agent |
| [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | "Vibe-Trading: Your Personal Trading Agent" | 38030 | +3.4%（自 2026-10-27） | Python | Agent | 未明确（需查文档） | Agent |
| [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | 410 Claude Code skills & agent skills & plugins (120+ Agents, custom commands, 410+ skills, customizable references, scripts)for Claude Code, Codex, Gemini CLI, Cursor, and 8 more coding agents — engineering, marketing, product, compliance, C-level advisory, research, business operations, commercial & finance, and your daily productivity skills. | 29625 | — | Python | Agent | 未明确（需查文档） | Agent |
| [virattt/dexter](https://github.com/virattt/dexter) | An autonomous agent for deep financial research | 27816 | — | TypeScript | Agent | 未明确（需查文档） | Agent |
| [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | "AI-Trader: 100% Fully-Automated Agent-Native Trading"   | 23226 | — | Python | Agent | 未明确（需查文档） | Agent |
| [stefan-jansen/machine-learning-for-trading](https://github.com/stefan-jansen/machine-learning-for-trading) | Code for Machine Learning for Trading, 3rd edition — from data sourcing to live execution. | 21781 | +1.0%（自 2026-10-27） | Jupyter Notebook | Agent | 未明确（需查文档） | Agent |
| [hummingbot/hummingbot](https://github.com/hummingbot/hummingbot) | Open source software that helps you create and deploy high-frequency crypto trading bots | 21161 | — | Python | Agent | 虚拟货币 | Agent |

### 交易框架

| 项目 | 简介 | ⭐ | 半年内已观测涨幅 | 语言 | 分类 | 市场/因子 | 能力/用途 |
|---|---|---:|---:|---|---|---|---|
| [vnpy/vnpy](https://github.com/vnpy/vnpy) | 基于Python的开源量化交易平台开发框架 | 46333 | — | Python | 交易框架 | 未明确（需查文档） | 回测：需查文档 |
| [mementum/backtrader](https://github.com/mementum/backtrader) | Python Backtesting library for trading strategies | 23715 | — | Python | 交易框架 | 未明确（需查文档） | 回测：明确提及 |
| [QuantConnect/Lean](https://github.com/QuantConnect/Lean) | Lean Algorithmic Trading Engine by QuantConnect (Python, C#) | 22481 | — | C# | 交易框架 | 未明确（需查文档） | 回测：需查文档 |
| [myhhub/stock](https://github.com/myhhub/stock) | stock股票.获取股票数据,计算股票指标,筹码分布,识别股票形态,综合选股,选股策略,股票验证回测,股票自动交易,支持PC及移动设备。 | 15102 | — | Python | 交易框架 | 未明确（需查文档） | 回测：明确提及 |
| [yutiansut/QUANTAXIS](https://github.com/yutiansut/QUANTAXIS) | QUANTAXIS 支持任务调度 分布式部署的 股票/期货/期权  数据/回测/模拟/交易/可视化/多账户 纯本地量化解决方案 | 11359 | — | Python | 交易框架 | 期货 | 回测：明确提及 |
| [StockSharp/StockSharp](https://github.com/StockSharp/StockSharp) | Algorithmic trading and quantitative trading open source platform to develop trading robots (stock markets, forex, crypto, bitcoins, and options). | 11090 | — | C# | 交易框架 | 虚拟货币 | 回测：明确提及 |
| [kernc/backtesting.py](https://github.com/kernc/backtesting.py) | 🔎 📈 🐍 💰  Backtest trading strategies in Python. | 9225 | — | Python | 交易框架 | 未明确（需查文档） | 回测：明确提及 |
| [ricequant/rqalpha](https://github.com/ricequant/rqalpha) | A extendable, replaceable Python algorithmic backtest && trading framework supporting multiple securities | 6870 | +0.4%（自 2026-10-27） | Python | 交易框架 | 期货 | 回测：明确提及 |
| [Jakeschincariol/day-trader-skill](https://github.com/Jakeschincariol/day-trader-skill) | 11 Claude skills for day trading: scan thousands of charts, track breaking news, time every entry and exit, and replay every outcome before you risk a dollar. | 6820 | — | Python | 交易框架 | 未明确（需查文档） | 回测：明确提及 |
| [Mathieu2301/TradingView-API](https://github.com/Mathieu2301/TradingView-API) | 📈 Get real-time stocks from TradingView | 5866 | +1.8%（自 2026-10-27） | TypeScript | 交易框架 | 虚拟货币 | 回测：明确提及 |

### 工具

| 项目 | 简介 | ⭐ | 半年内已观测涨幅 | 语言 | 分类 | 市场/因子 | 能力/用途 |
|---|---|---:|---:|---|---|---|---|
| [freqtrade/freqtrade](https://github.com/freqtrade/freqtrade) | Free, open source crypto trading bot | 56762 | — | Python | 工具 | 虚拟货币 | 分析/策略工具 |
| [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | Kronos: A Foundation Model for the Language of Financial Markets | 47604 | — | Python | 工具 | 未明确（需查文档） | 分析/策略工具 |
| [ccxt/ccxt](https://github.com/ccxt/ccxt) | A unified trading API with more than 100 crypto exchanges and prediction markets in JavaScript / TypeScript / Python / C# / PHP / Go / Java / Rust | 44857 | — | Python | 工具 | 虚拟货币 | 数据源 |
| [akfamily/akshare](https://github.com/akfamily/akshare) | AKShare is an elegant and simple financial data interface library for Python, built for human beings! 开源财经数据接口库 | 23292 | — | Python | 工具 | A股、期货 | 数据源 |
| [quantopian/zipline](https://github.com/quantopian/zipline) | Zipline, a Pythonic Algorithmic Trading Library | 20230 | — | Python | 工具 | 未明确（需查文档） | 分析/策略工具 |
| [bbfamily/abu](https://github.com/bbfamily/abu) | 阿布量化交易系统(股票，期权，期货，比特币，机器学习) 基于python的开源量化交易，量化投资架构 | 19164 | — | Python | 工具 | 虚拟货币、期货 | 分析/策略工具 |
| [xcanwin/KeepChatGPT](https://github.com/xcanwin/KeepChatGPT) | 这是一款提高ChatGPT的数据安全能力和效率的插件。并且免费共享大量创新功能，如：自动刷新、保持活跃、数据安全、取消审计、克隆对话、言无不尽、净化页面、展示大屏、拦截跟踪、日新月异、明察秋毫等。让我们的AI体验无比安全、顺畅、丝滑、高效、简洁。 | 14890 | — | JavaScript | 工具 | 未明确（需查文档） | 数据源 |
| [wechat-article/wechat-article-exporter](https://github.com/wechat-article/wechat-article-exporter) | 一款在线的 微信公众号文章批量下载 工具，支持导出阅读量与评论数据，无需搭建任何环境，可通过 在线网站 使用，支持 docker 私有化部署和 Cloudflare 部署。  支持下载各种文件格式，其中 HTML 格式可100%还原文章排版与样式。 | 13147 | — | TypeScript | 工具 | 未明确（需查文档） | 数据源 |
| [daniulive/SmarterStreaming](https://github.com/daniulive/SmarterStreaming) | 业内为数不多致力于极致体验的超强全自研跨平台(windows/linux/android/iOS)流媒体内核，通过模块化自由组合，支持实时RTMP推流、RTSP推流、RTMP播放器、RTSP播放器、录像、多路流媒体转发、音视频导播、动态视频合成、音频混音、直播互动、内置轻量级RTSP服务等，比快更快，业界真正靠谱的超低延迟直播SDK(延迟低至100~200ms)。 | 11172 | — | Java | 工具 | 未明确（需查文档） | 分析/策略工具 |
| [chaitin/PandaWiki](https://github.com/chaitin/PandaWiki) | PandaWiki 是一款 AI 大模型驱动的开源知识库搭建系统，帮助你快速构建智能化的 产品文档、技术文档、FAQ、博客系统，借助大模型的力量为你提供 AI 创作、AI 问答、AI 搜索等能力。 | 10496 | — | TypeScript | 工具 | 未明确（需查文档） | 分析/策略工具 |

### 游戏

| 项目 | 简介 | ⭐ | 半年内已观测涨幅 | 语言 | 分类 | 市场/因子 | 能力/用途 |
|---|---|---:|---:|---|---|---|---|
| [kingston-csj/jforgame](https://github.com/kingston-csj/jforgame) | jforgame是一个一站式游戏服务器开发框架。包含游戏服务器开发所需要的各种组件，比如socket服务端与客户端，高性能线程模型，自定义二进制消息编解码，自定义orm工具，异步持久化方案，游戏热更新，配置表自动化仓库，游戏通用工具等等，同时提供大量业务案例以供学习。亦可用于其他socket应用，例如及时聊天等。 | 1102 | — | Java | 游戏 | 未明确（需查文档） | 游戏 |

### 论文研究

| 项目 | 简介 | ⭐ | 半年内已观测涨幅 | 语言 | 分类 | 市场/因子 | 能力/用途 |
|---|---|---:|---:|---|---|---|---|
| [UFund-Me/Qbot](https://github.com/UFund-Me/Qbot) | [🔥updating ...] AI 自动量化交易机器人(完全本地部署) AI-powered Quantitative Investment Research Platform. 📃 online docs: https://ufund-me.github.io/Qbot   ✨ :news: qbot-mini: https://github.com/Charmve/iQuant | 18799 | — | Jupyter Notebook | 论文研究 | 虚拟货币 | 论文研究 |
| [polakowo/vectorbt](https://github.com/polakowo/vectorbt) | The research engine that gives you an unfair advantage. Run thousands of trading ideas before others finish one. | 9811 | +2.7%（自 2026-10-27） | Python | 论文研究 | 虚拟货币 | 论文研究 |
| [Drakkar-Software/OctoBot](https://github.com/Drakkar-Software/OctoBot) | Free open source crypto trading bot to automate AI, Grid, DCA and TradingView strategies on Binance, Hyperliquid and 15+ exchanges, with a simple interface. | 6925 | +0.9%（自 2026-10-27） | Python | 论文研究 | 虚拟货币 | 论文研究 |
| [hugo2046/QuantsPlaybook](https://github.com/hugo2046/QuantsPlaybook) | 量化研究-券商金工研报复现 | 6873 | — | Jupyter Notebook | 论文研究 | 未明确（需查文档） | 论文研究 |
| [Superalgos/Superalgos](https://github.com/Superalgos/Superalgos) | Free, open-source crypto trading bot, automated bitcoin / cryptocurrency trading software, algorithmic trading bots. Visually design your crypto trading bot, leveraging an integrated charting system, data-mining, backtesting, paper trading, and multi-server crypto bot deployments. | 5786 | — | JavaScript | 论文研究 | 虚拟货币 | 论文研究 |
| [cybergeekgyan/Quant-Developers-Resources](https://github.com/cybergeekgyan/Quant-Developers-Resources) | Resources to Prepare for Quant Developers/ Quantitative Researcher/ Quantitative Trader/ Quant Analyst/ Software Engineers in Quant Trading Firms, HFTs and Hedge Funds | 4140 | +5.0%（自 2026-09-19） | Python | 论文研究 | 未明确（需查文档） | 论文研究 |
| [mpquant/Ashare](https://github.com/mpquant/Ashare) | 股票行情实时数据接口-A股,完全免费的沪深证券股票数据-中国股市,python最简封装的API接口,包含日线,历史K线,分时线,分钟线,全部实时采集，系统包括新浪腾讯双数据核心采集获取，自动故障切换，STOCK数据格式成DataFrame格式,可用来查询研究量化分析，股票程序自动化交易系统.为量化研究者在数据获取方面极大地减轻工作量，更加专注于策略和模型的研究与实现。 | 3939 | — | Python | 论文研究 | A股 | 论文研究 |
| [AI4Finance-Foundation/FinRL-Trading](https://github.com/AI4Finance-Foundation/FinRL-Trading) | FinRL-X: An AI-Native Modular Infrastructure for Quantitative Trading | 3930 | +5.9%（自 2026-09-18） | Python | 论文研究 | 未明确（需查文档） | 论文研究 |
| [hello245m/free-stockdb](https://github.com/hello245m/free-stockdb) | 面向 A 股日K、分钟K与ETF分钟数据的本地量化引擎，集成增量同步、本地缓存、复权、批量查询、回测与指标计算。 | 3160 | — | HTML | 论文研究 | A股 | 论文研究 |
| [weslynn/AlphaTree-graphic-deep-neural-network](https://github.com/weslynn/AlphaTree-graphic-deep-neural-network) | AI Roadmap:机器学习(Machine Learning)、深度学习(Deep Learning)、对抗神经网络(GAN），图神经网络（GNN），NLP，大数据相关的发展路书(roadmap), 并附海量源码（python，pytorch）带大家消化基本知识点，突破面试，完成从新手到合格工程师的跨越，其中深度学习相关论文附有tensorflow caffe官方源码，应用部分含推荐算法和知识图谱 | 3027 | — |  | 论文研究 | 未明确（需查文档） | 论文研究 |


---

# AI 应用研究日报 · 2026-11-11

本期新增：**1 篇论文**（其中 0 篇找到可能的代码）和 **22 个 GitHub 项目**。

## AI 投资与交易论文

| 日期 | 论文 | 作者 | 代码 | 市场/因子 | 来源/热度 |
|---|---|---|---|---|---|
| 2026-11-10 | [Online-Adaptive Fuzzy Cognitive Maps for Neuro-symbolic Financial Forecasting](https://arxiv.org/abs/2611.13388) | Brandon Rodriguez, Abel Deulofeu, Olaoluwa Adigun | — | 美股、因子 | arXiv |


## GitHub 金融与交易工具

| 项目 | 简介 | ⭐ | 半年内已观测涨幅 | 语言 | 分类 | 市场/因子 | 能力/用途 |
|---|---|---:|---:|---|---|---|---|
| [51bitquant/binance_grid_trader](https://github.com/51bitquant/binance_grid_trader) | Binance_grid_trader is a grid strategy bot trading with Binance Spot and Binance Futures Exchange. you can use it to trade any pair in Binance Exchange. Binance_grid_trader是一个币安网格策略软件, 目前支持币安现货，USDT合约和币币合约。 | 991 | — | Python | 工具 | 虚拟货币、期货 | 数据源 |
| [51bitquant/howtrader](https://github.com/51bitquant/howtrader) | Howtrader: A crypto quant framework for developing, backtesting, and executing your own trading strategies. Seamlessly integrates with TradingView and other third-party signals. Simply send a post request to automate trading and order placement. Supports Binance and Okex exchanges. | 972 | — | Python | 交易框架 | 虚拟货币 | 回测：明确提及 |
| [ailabx/agilab](https://github.com/ailabx/agilab) | AgiLab(Agi实验室)，专注于将前沿AI技术落地：量化投资，多智能体落地，科研自动化。 | 971 | — | Python | Agent | 未明确（需查文档） | Agent |
| [dromara/dante-cloud](https://github.com/dromara/dante-cloud) | 🐉 Dante Cloud 是支持阻塞式与响应式服务并行的微服务云原生基座和面向AI Agent开发的智能基座，基于领域驱动模型（DDD）设计，以高质量代码与低安全漏洞为核心，高度模块化、组件化，覆盖IoT设备认证、国家等保三级、接口国密数字信封加密等多层次安全体系，并提供多租户解决方案。独创“一套代码实现微服务和单体架构灵活切换”，赋能企业级智能应用构建。🔝🔝点个star 持续关注更新！ | 969 | — | Java | Agent | 未明确（需查文档） | Agent |
| [Leo4815162342/dukascopy-node](https://github.com/Leo4815162342/dukascopy-node) | ✨ Download historical and real-time price tick data for Crypto, Stocks, ETFs, CFDs, Forex via CLI and Node.js ✨ | 963 | — | TypeScript | 交易框架 | 虚拟货币 | 回测：明确提及 |
| [sensorsdata/sa-sdk-javascript](https://github.com/sensorsdata/sa-sdk-javascript) | 神策数据官方 Web JavaScript 埋点 SDK，是一款轻量级用于 Web 端和 H5 端的数据采集埋点 SDK。使用原生 JavaScript 技术实现代码埋点、全埋点、可视化全埋点、网页热力图和触达图等功能。 | 958 | — | JavaScript | 工具 | 未明确（需查文档） | 看板、数据源 |
| [jianweiweng05/qsx-strategy-score](https://github.com/jianweiweng05/qsx-strategy-score) | Free strategy scorecard for trading backtests. Detect overfitting, weak edge, drawdown risk, and random-timing luck from returns, equity curves, or trade logs. | 928 | — | Python | 交易框架 | 未明确（需查文档） | 回测：明确提及 |
| [rush86999/atom](https://github.com/rush86999/atom) | Atom Agent, Open-Source Governed AI Agent Platform for Self-Hosted Automation | 915 | — | Python | Agent | 未明确（需查文档） | Agent |
| [sdcoffey/techan](https://github.com/sdcoffey/techan) | Technical Analysis Library for Golang | 905 | — | Go | 工具 | 虚拟货币 | 分析/策略工具 |
| [KylinMountain/TradingAgents-AShare](https://github.com/KylinMountain/TradingAgents-AShare) | A 股多智能体智能投研系统 — 基于 TradingAgents 架构，15 名 AI Agent 模拟机构协作与实时辩论对抗，全流程可视化，支持 OpenClaw / Claude Code 集成，Docker 一键部署。 | 899 | — | Python | Agent | A股 | Agent |
| [hananedupouy/LLMs-in-Finance](https://github.com/hananedupouy/LLMs-in-Finance) | LLMs in Finance - Generative AI - AI Agents  | 896 | — | Jupyter Notebook | Agent | 未明确（需查文档） | Agent |
| [jwangkun/claude-for-financial-services-cn](https://github.com/jwangkun/claude-for-financial-services-cn) |  63 个 Claude Skills，为 A 股金融从业者而生  基于 Anthropic 官方 claude-for-financial-services 深度适配国内市场，现已开源。 | 889 | — | Python | 工具 | 未明确（需查文档） | 分析/策略工具 |
| [xingwudao/xquant-beginner](https://github.com/xingwudao/xquant-beginner) | 《XQuant：人人都是量化交易员》量化交易入门与自学开源书：用 AI 和 Python 从零跑通策略回测、风险评估、交易执行和因子研究。 | 888 | — | TypeScript | 论文研究 | 因子 | 论文研究 |
| [NewLifeX/NewLife.Redis](https://github.com/NewLifeX/NewLife.Redis) | High performance redis client, support NETCore/. NET4. 0/. NET4. 5. It is specially optimized for big data and message queue. The average daily consumption of online single application is 10 billion. 高性能Redis客户端，支持.NETCore/.NET4.0/.NET4.5，为大数据与消息队列而特别优化，线上单应用日均100亿调用量 | 879 | — | C# | 工具 | 未明确（需查文档） | 数据源 |
| [TencentBlueKing/bk-job](https://github.com/TencentBlueKing/bk-job) | 蓝鲸作业平台（Job）是一套运维基础操作管理系统，具备海量任务并发处理能力。除了支持脚本执行、文件分发、定时任务等一系列基础运维场景以外，还支持通过流程调度能力将零碎的单个任务组装成一个自动化作业流程；而每个作业都可做为一个原子节点，提供给上层或周边系统/平台使用，实现调度自动化。 | 875 | — | Java | 工具 | 未明确（需查文档） | 分析/策略工具 |
| [zgsfsec/Full-Chain-Sentinel-System](https://github.com/zgsfsec/Full-Chain-Sentinel-System) | 全链哨兵，是集Web 渗透、安卓 App 安全测试、iOS APP安全测试、攻防批量打点、自动化应急响应、开源漏洞监测为一体的网络安全 Agent，用于安全服务交付自动化辅助，禁止用于非法用途。 | 869 | — | TypeScript | Agent | 未明确（需查文档） | Agent |
| [Adamant-im/adamant-tradebot](https://github.com/Adamant-im/adamant-tradebot) | Free self-hosted liquidity bot for token issuers who want to improve CEX market quality without sending tokens, funds, or API keys to a third-party market maker. | 863 | — | JavaScript | 工具 | 虚拟货币 | 数据源 |
| [gazbert/bxbot](https://github.com/gazbert/bxbot) | A simple Bitcoin trading bot written in Java. | 863 | — | Java | 工具 | 虚拟货币 | 数据源 |
| [KunMoe/kun-touchgal-next](https://github.com/KunMoe/kun-touchgal-next) | TouchGal 是一个一站式 Galgame 文化社区。提供Galgame 论坛、Galgame 下载等服务。承诺永久免费, 高质量。为Galgame 爱好者提供一片净土！ | 849 | — | TypeScript | 工具 | 未明确（需查文档） | 分析/策略工具 |
| [huanyuejue/Fluent-Steam-Lua](https://github.com/huanyuejue/Fluent-Steam-Lua) | 基于 WPF + Fluent Design 开发的现代化轻量级 Steam Lua 入库管理工具，目前仅适配OpenSteamTool | 844 | — | C# | 工具 | 未明确（需查文档） | 分析/策略工具 |
| [liudf0716/xfrpc](https://github.com/liudf0716/xfrpc) | xfrpc 是一个轻量级的 FRP 客户端，完美兼容 frps，采用 C 语言实现，专为 OpenWRT 和物联网等资源受限系统优化设计。它针对 ROM 和 RAM 空间有限的设备，提供高效的内网穿透解决方案。xfrpc 集成了xDPI（深度包检测）功能，增强了安全性，有效防止内网穿透中因恶意嗅探导致的安全威胁，确保数据传输和网络访问的可靠保护。购买下面的链接中的服务支持我的开源 | 844 | — | C | 工具 | 未明确（需查文档） | 数据源 |
| [AsyncAlgoTrading/aat](https://github.com/AsyncAlgoTrading/aat) | Asynchronous, event-driven algorithmic trading in Python and C++ | 843 | — | C++ | 交易框架 | 虚拟货币 | 回测：明确提及 |


> 论文代码按“论文自带链接 → Papers with Code → ResearchCode → arXiv 页面 → GitHub”依次匹配；低可信标题匹配仍需人工复核。本仓库只做研究信息整理，不构成投资建议。


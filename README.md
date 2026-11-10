# AI Finance Daily

[![Daily update](https://github.com/theneao/ai-finance-daily/actions/workflows/daily.yml/badge.svg)](https://github.com/theneao/ai-finance-daily/actions/workflows/daily.yml)

每天自动搜集 AI 投资研究、金融 Agent、交易框架、金融工具和交易游戏。论文源结合 arXiv 与 [Hugging Face Trending Papers](https://huggingface.co/papers/trending)，仅筛选 AI 投资交易研究，按 arXiv ID 去重；Trending 中重新走热的旧论文也可收录，保留原发表日期与 HF 社区热度。

**[📚 完整热门项目总榜（全部历史项目 · Star 排名 · 分类导航）](HOT_PROJECTS.md)** · **[月度总结](archive/index.md)**

热门总榜不限制项目创建时间，收录 **Star ≥ 1,000** 且**近三年有代码更新**的非归档项目，包括历史成熟项目；每天随日报刷新，按 Star 降序排列。分类包括 Agent、交易框架（回测/语言）、工具（看板/数据源/创意）、游戏、论文研究，市场标签区分美股、A股、虚拟货币、期货、因子。

每天北京时间 **08:30** 运行，也可在 Actions 页面手动运行。首页保留当日日报；历史内容每月仅一份 Markdown，月内累计去重更新，不再保存逐日日报文件。`data/` 中 JSON 用于累计和去重，不是逐日归档。日报仍允许近 7 天增长 ≥ 20 Star 的新项目，总榜采用Star ≥ 1,000 门槛。项目名称、简介、topics、README 和论文标题、摘要会进行政治敏感主题筛选，检查不可用的仓库暂缓展示。同时排除 `.github`/个人主页仓库、资源导航合集及超过 400 字符的冗长简介仓库，优先展示可使用的项目。检索范围和阈值见 [`config.yaml`](config.yaml)。

---

## 热门项目 · Star ≥ 1,000

按 Star 降序，按分类直接展示各类前 10 个项目；[查看全部热门项目](HOT_PROJECTS.md)。

### Agent

| 项目 | 简介 | ⭐ | 近7天 | 语言 | 分类 | 市场/因子 | 能力/用途 |
|---|---|---:|---:|---|---|---|---|
| [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | TradingAgents: Multi-Agents LLM Financial Trading Framework | 121814 | — | Python | Agent | 未明确（需查文档） | Agent |
| [openbq-org/OpenBB](https://github.com/openbq-org/OpenBB) | Open Data Platform for analysts, quants and AI agents. | 75301 | — | Python | Agent | 虚拟货币、期货 | Agent |
| [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | LLM 驱动的多市场股票智能分析系统：多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。  LLM-powered multi-market stock analysis system with multi-source market data, real-time news, decision dashboard, automated notifications, and cost-free scheduled runs. | 69502 | — | Python | Agent | 未明确（需查文档） | Agent |
| [microsoft/qlib](https://github.com/microsoft/qlib) | Qlib is an AI-oriented Quant investment platform that aims to use AI tech to empower Quant Research, from exploring ideas to implementing productions. Qlib supports diverse ML modeling paradigms, including supervised learning, market dynamics modeling, and RL, and is now equipped with https://github.com/microsoft/RD-Agent to automate R&D process. | 50193 | — | Python | Agent | 未明确（需查文档） | Agent |
| [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | "Vibe-Trading: Your Personal Trading Agent" | 37995 | — | Python | Agent | 未明确（需查文档） | Agent |
| [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | 410 Claude Code skills & agent skills & plugins (120+ Agents, custom commands, 410+ skills, customizable references, scripts)for Claude Code, Codex, Gemini CLI, Cursor, and 8 more coding agents — engineering, marketing, product, compliance, C-level advisory, research, business operations, commercial & finance, and your daily productivity skills. | 29582 | — | Python | Agent | 未明确（需查文档） | Agent |
| [virattt/dexter](https://github.com/virattt/dexter) | An autonomous agent for deep financial research | 27809 | — | TypeScript | Agent | 未明确（需查文档） | Agent |
| [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | "AI-Trader: 100% Fully-Automated Agent-Native Trading"   | 23223 | — | Python | Agent | 未明确（需查文档） | Agent |
| [stefan-jansen/machine-learning-for-trading](https://github.com/stefan-jansen/machine-learning-for-trading) | Code for Machine Learning for Trading, 3rd edition — from data sourcing to live execution. | 21775 | — | Jupyter Notebook | Agent | 未明确（需查文档） | Agent |
| [OpenByteInc/QuantDinger](https://github.com/OpenByteInc/QuantDinger) | The most complete open-source, self-hosted Agentic Trading OS—AI research, Python strategies, factor discovery, backtesting, optimization, paper/live multi-asset execution, risk controls, monitoring, MCP, and multi-tenant SaaS in one auditable stack. | 13674 | — | Python | Agent | 虚拟货币、因子 | Agent |

### 交易框架

| 项目 | 简介 | ⭐ | 近7天 | 语言 | 分类 | 市场/因子 | 能力/用途 |
|---|---|---:|---:|---|---|---|---|
| [mementum/backtrader](https://github.com/mementum/backtrader) | Python Backtesting library for trading strategies | 23710 | — | Python | 交易框架 | 未明确（需查文档） | 回测：明确提及 |
| [QuantConnect/Lean](https://github.com/QuantConnect/Lean) | Lean Algorithmic Trading Engine by QuantConnect (Python, C#) | 22476 | — | C# | 交易框架 | 未明确（需查文档） | 回测：需查文档 |
| [myhhub/stock](https://github.com/myhhub/stock) | stock股票.获取股票数据,计算股票指标,筹码分布,识别股票形态,综合选股,选股策略,股票验证回测,股票自动交易,支持PC及移动设备。 | 15088 | — | Python | 交易框架 | 未明确（需查文档） | 回测：明确提及 |
| [yutiansut/QUANTAXIS](https://github.com/yutiansut/QUANTAXIS) | QUANTAXIS 支持任务调度 分布式部署的 股票/期货/期权  数据/回测/模拟/交易/可视化/多账户 纯本地量化解决方案 | 11355 | — | Python | 交易框架 | 期货 | 回测：明确提及 |
| [kernc/backtesting.py](https://github.com/kernc/backtesting.py) | 🔎 📈 🐍 💰  Backtest trading strategies in Python. | 9222 | — | Python | 交易框架 | 未明确（需查文档） | 回测：明确提及 |
| [ricequant/rqalpha](https://github.com/ricequant/rqalpha) | A extendable, replaceable Python algorithmic backtest && trading framework supporting multiple securities | 6866 | — | Python | 交易框架 | 期货 | 回测：明确提及 |
| [Jakeschincariol/day-trader-skill](https://github.com/Jakeschincariol/day-trader-skill) | 11 Claude skills for day trading: scan thousands of charts, track breaking news, time every entry and exit, and replay every outcome before you risk a dollar. | 6554 | — | Python | 交易框架 | 未明确（需查文档） | 回测：明确提及 |
| [Mathieu2301/TradingView-API](https://github.com/Mathieu2301/TradingView-API) | 📈 Get real-time stocks from TradingView | 5860 | — | TypeScript | 交易框架 | 虚拟货币 | 回测：明确提及 |
| [atilaahmettaner/tradingview-mcp](https://github.com/atilaahmettaner/tradingview-mcp) | MCP server for market analysis in AI assistants: screeners, multi-timeframe technical analysis, backtests and sentiment for crypto, stocks, forex and futures. 39 tools. Self-host free, or use the hosted version, TradingMCP. | 5261 | — | Python | 交易框架 | 虚拟货币、期货 | 回测：明确提及 |
| [nkaz001/hftbacktest](https://github.com/nkaz001/hftbacktest) | Free, open source, a high frequency trading and market making backtesting and trading bot, which accounts for limit orders, queue positions, and latencies, utilizing full tick data for trades and order books(Level-2 and Level-3), with real-world crypto trading examples for Binance and Bybit | 5067 | — | Rust | 交易框架 | 虚拟货币 | 回测：明确提及 |

### 工具

| 项目 | 简介 | ⭐ | 近7天 | 语言 | 分类 | 市场/因子 | 能力/用途 |
|---|---|---:|---:|---|---|---|---|
| [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | Kronos: A Foundation Model for the Language of Financial Markets | 47522 | — | Python | 工具 | 未明确（需查文档） | 分析/策略工具 |
| [akfamily/akshare](https://github.com/akfamily/akshare) | AKShare is an elegant and simple financial data interface library for Python, built for human beings! 开源财经数据接口库 | 23282 | — | Python | 工具 | A股、期货 | 数据源 |
| [quantopian/zipline](https://github.com/quantopian/zipline) | Zipline, a Pythonic Algorithmic Trading Library | 20227 | — | Python | 工具 | 未明确（需查文档） | 分析/策略工具 |
| [bbfamily/abu](https://github.com/bbfamily/abu) | 阿布量化交易系统(股票，期权，期货，比特币，机器学习) 基于python的开源量化交易，量化投资架构 | 19158 | — | Python | 工具 | 虚拟货币、期货 | 分析/策略工具 |
| [xcanwin/KeepChatGPT](https://github.com/xcanwin/KeepChatGPT) | 这是一款提高ChatGPT的数据安全能力和效率的插件。并且免费共享大量创新功能，如：自动刷新、保持活跃、数据安全、取消审计、克隆对话、言无不尽、净化页面、展示大屏、拦截跟踪、日新月异、明察秋毫等。让我们的AI体验无比安全、顺畅、丝滑、高效、简洁。 | 14888 | — | JavaScript | 工具 | 未明确（需查文档） | 数据源 |
| [wechat-article/wechat-article-exporter](https://github.com/wechat-article/wechat-article-exporter) | 一款在线的 微信公众号文章批量下载 工具，支持导出阅读量与评论数据，无需搭建任何环境，可通过 在线网站 使用，支持 docker 私有化部署和 Cloudflare 部署。  支持下载各种文件格式，其中 HTML 格式可100%还原文章排版与样式。 | 13145 | — | TypeScript | 工具 | 未明确（需查文档） | 数据源 |
| [daniulive/SmarterStreaming](https://github.com/daniulive/SmarterStreaming) | 业内为数不多致力于极致体验的超强全自研跨平台(windows/linux/android/iOS)流媒体内核，通过模块化自由组合，支持实时RTMP推流、RTSP推流、RTMP播放器、RTSP播放器、录像、多路流媒体转发、音视频导播、动态视频合成、音频混音、直播互动、内置轻量级RTSP服务等，比快更快，业界真正靠谱的超低延迟直播SDK(延迟低至100~200ms)。 | 11172 | — | Java | 工具 | 未明确（需查文档） | 分析/策略工具 |
| [chaitin/PandaWiki](https://github.com/chaitin/PandaWiki) | PandaWiki 是一款 AI 大模型驱动的开源知识库搭建系统，帮助你快速构建智能化的 产品文档、技术文档、FAQ、博客系统，借助大模型的力量为你提供 AI 创作、AI 问答、AI 搜索等能力。 | 10490 | — | TypeScript | 工具 | 未明确（需查文档） | 分析/策略工具 |
| [shidenggui/easytrader](https://github.com/shidenggui/easytrader) | 提供同花顺客户端/miniqmt/雪球的股票量化交易，支持跟踪 joinquant /ricequant 模拟交易 和 实盘雪球组合 | 10276 | — | Python | 工具 | 未明确（需查文档） | 分析/策略工具 |
| [JessYanCoding/MVPArms](https://github.com/JessYanCoding/MVPArms) | ⚔️ A common architecture for Android applications developing based on MVP, integrates many open source projects, to make your developing quicker and easier (一个整合了大量主流开源项目高度可配置化的 Android MVP 快速集成框架).  | 10222 | — | Java | 工具 | 未明确（需查文档） | 分析/策略工具 |

### 游戏

| 项目 | 简介 | ⭐ | 近7天 | 语言 | 分类 | 市场/因子 | 能力/用途 |
|---|---|---:|---:|---|---|---|---|
| [kingston-csj/jforgame](https://github.com/kingston-csj/jforgame) | jforgame是一个一站式游戏服务器开发框架。包含游戏服务器开发所需要的各种组件，比如socket服务端与客户端，高性能线程模型，自定义二进制消息编解码，自定义orm工具，异步持久化方案，游戏热更新，配置表自动化仓库，游戏通用工具等等，同时提供大量业务案例以供学习。亦可用于其他socket应用，例如及时聊天等。 | 1102 | — | Java | 游戏 | 未明确（需查文档） | 游戏 |

### 论文研究

| 项目 | 简介 | ⭐ | 近7天 | 语言 | 分类 | 市场/因子 | 能力/用途 |
|---|---|---:|---:|---|---|---|---|
| [UFund-Me/Qbot](https://github.com/UFund-Me/Qbot) | [🔥updating ...] AI 自动量化交易机器人(完全本地部署) AI-powered Quantitative Investment Research Platform. 📃 online docs: https://ufund-me.github.io/Qbot   ✨ :news: qbot-mini: https://github.com/Charmve/iQuant | 18796 | — | Jupyter Notebook | 论文研究 | 虚拟货币 | 论文研究 |
| [polakowo/vectorbt](https://github.com/polakowo/vectorbt) | The research engine that gives you an unfair advantage. Run thousands of trading ideas before others finish one. | 9798 | — | Python | 论文研究 | 虚拟货币 | 论文研究 |
| [Drakkar-Software/OctoBot](https://github.com/Drakkar-Software/OctoBot) | Free open source crypto trading bot to automate AI, Grid, DCA and TradingView strategies on Binance, Hyperliquid and 15+ exchanges, with a simple interface. | 6919 | — | Python | 论文研究 | 虚拟货币 | 论文研究 |
| [hugo2046/QuantsPlaybook](https://github.com/hugo2046/QuantsPlaybook) | 量化研究-券商金工研报复现 | 6872 | — | Jupyter Notebook | 论文研究 | 未明确（需查文档） | 论文研究 |
| [cybergeekgyan/Quant-Developers-Resources](https://github.com/cybergeekgyan/Quant-Developers-Resources) | Resources to Prepare for Quant Developers/ Quantitative Researcher/ Quantitative Trader/ Quant Analyst/ Software Engineers in Quant Trading Firms, HFTs and Hedge Funds | 4139 | — | Python | 论文研究 | 未明确（需查文档） | 论文研究 |
| [mpquant/Ashare](https://github.com/mpquant/Ashare) | 股票行情实时数据接口-A股,完全免费的沪深证券股票数据-中国股市,python最简封装的API接口,包含日线,历史K线,分时线,分钟线,全部实时采集，系统包括新浪腾讯双数据核心采集获取，自动故障切换，STOCK数据格式成DataFrame格式,可用来查询研究量化分析，股票程序自动化交易系统.为量化研究者在数据获取方面极大地减轻工作量，更加专注于策略和模型的研究与实现。 | 3939 | — | Python | 论文研究 | A股 | 论文研究 |
| [AI4Finance-Foundation/FinRL-Trading](https://github.com/AI4Finance-Foundation/FinRL-Trading) | FinRL-X: An AI-Native Modular Infrastructure for Quantitative Trading | 3926 | — | Python | 论文研究 | 未明确（需查文档） | 论文研究 |
| [hello245m/free-stockdb](https://github.com/hello245m/free-stockdb) | 面向 A 股日K、分钟K与ETF分钟数据的本地量化引擎，集成增量同步、本地缓存、复权、批量查询、回测与指标计算。 | 3155 | — | HTML | 论文研究 | A股 | 论文研究 |
| [weslynn/AlphaTree-graphic-deep-neural-network](https://github.com/weslynn/AlphaTree-graphic-deep-neural-network) | AI Roadmap:机器学习(Machine Learning)、深度学习(Deep Learning)、对抗神经网络(GAN），图神经网络（GNN），NLP，大数据相关的发展路书(roadmap), 并附海量源码（python，pytorch）带大家消化基本知识点，突破面试，完成从新手到合格工程师的跨越，其中深度学习相关论文附有tensorflow caffe官方源码，应用部分含推荐算法和知识图谱 | 3027 | — |  | 论文研究 | 未明确（需查文档） | 论文研究 |
| [akfamily/akquant](https://github.com/akfamily/akquant) | AKQuant is a high-performance quantitative research and trading framework built on Rust and Python! 开源量化回测框架 | 2583 | — | Python | 论文研究 | A股 | 论文研究 |


---

# AI 应用研究日报 · 2026-11-10

本期新增：**7 篇论文**（其中 4 篇找到可能的代码）和 **0 个 GitHub 项目**。

## AI 投资与交易论文

| 日期 | 论文 | 作者 | 代码 | 市场/因子 | 来源/热度 |
|---|---|---|---|---|---|
| 2026-11-09 | [Diversification Across Predictors: Heterogeneous Ensemble Learning for Cross-Sectional Return Prediction](https://arxiv.org/abs/2611.12389) | Danning Li | — | 因子 | arXiv |
| 2026-11-07 | [A Bayesian oriented exploration and reinforcement learning in continuous-time mean-variance portfolio optimization](https://arxiv.org/abs/2611.10759) | Kexin Chen, Xiang Yu, Shanshan Zhao | — | 未明确（需查文档） | arXiv |
| 2026-11-07 | [M3FT: Micro-Macro-Micro Reasoning for Multi-Agent Cryptocurrency Perpetual Futures Trading](https://arxiv.org/abs/2611.10586) | Jiashun Wang, Beile Wang, Guangyan Gan 等 | — | 虚拟货币、期货 | arXiv |
| 2025-12-01 | [AI-Trader: Benchmarking Autonomous Agents in Real-Time Financial Markets](https://arxiv.org/abs/2512.10971) | Tianyu Fan, Yuhao Yang, Yangqin Jiang 等 | [HF 社区代码候选](https://github.com/HKUDS/AI-Trader) | A股、虚拟货币、期货 | [HF Trending](https://huggingface.co/papers/2512.10971) · 👍 13 |
| 2025-09-14 | [Trading-R1: Financial Trading with LLM Reasoning via Reinforcement   Learning](https://arxiv.org/abs/2509.11420) | Yijia Xiao, Edward Sun, Tong Chen 等 | [HF 社区代码候选](https://github.com/TauricResearch/Trading-R1) | 未明确（需查文档） | [HF Trending](https://huggingface.co/papers/2509.11420) · 👍 5 |
| 2025-08-02 | [Kronos: A Foundation Model for the Language of Financial Markets](https://arxiv.org/abs/2508.02739) | Yu Shi, Zongliang Fu, Shuo Chen 等 | [HF 社区代码候选](https://github.com/shiyu-coder/Kronos) | 未明确（需查文档） | [HF Trending](https://huggingface.co/papers/2508.02739) · 👍 65 |
| 2024-12-28 | [TradingAgents: Multi-Agents LLM Financial Trading Framework](https://arxiv.org/abs/2412.20138) | Yijia Xiao, Edward Sun, Di Luo 等 | [HF 社区代码候选](https://github.com/tauricresearch/tradingagents) | 未明确（需查文档） | [HF Trending](https://huggingface.co/papers/2412.20138) · 👍 164 |


## GitHub 金融与交易工具

本期没有发现符合条件的新项目。


> 论文代码按“论文自带链接 → Papers with Code → ResearchCode → arXiv 页面 → GitHub”依次匹配；低可信标题匹配仍需人工复核。本仓库只做研究信息整理，不构成投资建议。


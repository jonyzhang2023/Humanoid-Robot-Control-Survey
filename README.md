# 世界模型（World Model）完整研究报告

> 覆盖 1943–2026 年，~200 篇论文，9 大研究方向的系统性深度调研

🌐 **在线阅读**：[joenhune.github.io/world-model-survey](https://joenhune.github.io/world-model-survey/)

## 内容概览

本项目是对**世界模型（World Model）**领域的系统性深度调研，覆盖从 Kenneth Craik（1943）的"心智模型"假说到 2026 年 2 月的最新进展。

### 报告结构

| 部分 | 内容 |
|------|------|
| **第一部分：认知建立** | 执行摘要、核心定义与数学框架、发展历程时间线 |
| **第二部分：九大研究方向** | ① 强化学习 ② 视频生成 ③ 自动驾驶 ④ 具身 AI ⑤ LLM ⑥ JEPA ⑦ 游戏 ⑧ 3D/4D ⑨ 领域特定 |
| **第三部分：生态与产业** | 全球企业与机构布局、开源生态全景 |
| **第四部分：分析与展望** | 技术路线对比、评估基准、趋势与未来 |
| **附录** | 论文与参考文献总索引（~200 篇） |

### 核心数字

- 📄 **~200 篇** 代表性论文（含 arXiv 链接）
- 🔬 **9 个** 研究方向深度解析
- 🏢 **15+ 家** 全球企业与机构布局分析
- 📊 **11 个** 评估基准对比
- 📦 **15+** 核心开源项目

## 本地开发

```bash
# 安装依赖
npm install

# 启动开发服务器
npm run docs:dev

# 构建
npm run docs:build

# 合并为单文件版本
npm run merge
```

## 项目结构

```
├── docs/                          # VitePress 网站内容
│   ├── index.md                   # 首页
│   ├── overview/                  # 第一部分：认知建立
│   ├── directions/                # 第二部分：9 大研究方向
│   ├── ecosystem/                 # 第三部分：生态与产业
│   ├── analysis/                  # 第四部分：分析与展望
│   ├── appendix.md                # 附录
│   └── .vitepress/                # VitePress 配置与主题
├── .claude/skills/                # Claude 调研 skill 定义
├── scripts/merge.sh               # 多文件合并为单文件的脚本
└── package.json
```

## 更新机制

- 网站多文件为**主版本**（source of truth）
- 每月更新对应方向的内容页面
- 运行 `npm run merge` 自动合并生成单文件完整版
- Push 到 `main` 分支后 GitHub Actions 自动构建并部署

## 许可证

MIT

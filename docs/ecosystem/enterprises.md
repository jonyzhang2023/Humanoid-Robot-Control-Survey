---
outline: deep
---

# 九、全球企业与机构布局

## 9.1 硬件平台厂商

| 企业 | 平台 | DoF | 2025 出货量 | 关键特色 | 国家 |
|------|------|-----|-----------|---------|------|
| **Boston Dynamics** | Atlas（全电动） | 28+ | 全部已预定 | CES 2026 商业版发布，Hyundai Metaplant 部署 | 🇺🇸 |
| **Tesla** | Optimus Gen 3 | 28 | 1,000+ 在 Tesla 工厂 | 端到端神经网络，目标年产百万台 | 🇺🇸 |
| **Figure AI** | Figure 02 / 03 | 25+ | 150 | BMW 20h 连续工作验证，$39B 估值，BotQ 工厂年产 12K | 🇺🇸 |
| **Agility Robotics** | Digit | 16 | — | Amazon 仓库部署 | 🇺🇸 |
| **1X Technologies** | NEO | 20+ | — | 家庭场景，世界模型驱动 | 🇳🇴 |
| **智元 (AgiBot)** | A2 等 | 28+ | **5,100+（全球第一）** | 五大场景全覆盖，39% 全球份额，RaaS 模式 | 🇨🇳 |
| **宇树 (Unitree)** | G1 / H1 / **H2** | 23–19 | **5,500+（全球第二）** | 学术标准平台，H2 展示飞踢/空翻 | 🇨🇳 |
| **小鹏 (XPENG)** | **IRON** | 26+ | — | VLA Gen2，仿人脊椎/肌肉，2026 底量产 | 🇨🇳 |
| **傅利叶 (Fourier)** | GR-2 / GRx | 44 | 300 | 工业解决方案，多机协作 | 🇨🇳 |
| **开普勒** | K2 | 40+ | — | 工业场景高负载 | 🇨🇳 |

> 🌍 **中国力量**：2025 年全球人形机器人出货量前六名**全部是中国企业**（Omdia 数据：智元 5100+ / 宇树 5500+ / 傅利叶 300 等）。2026 年中国国内产量预计达 10–20 万台。

## 9.2 运动控制技术布局

| 机构 | 核心方向 | 代表工作 | 技术路线 |
|------|---------|---------|---------|
| **NVIDIA** | 全栈基础设施 | GR00T N1, Isaac Lab, FLARE | Isaac 仿真 → GR00T 策略 → Jetson 部署 |
| **Google DeepMind** | 基础研究 | MuJoCo, DreamZero | 世界模型 + 物理引擎 |
| **CMU** | 学术引领 | DWL, H2O, OmniH2O, SONIC | Sim-to-Real, 全身控制, 基础模型 |
| **Stanford** | 全栈系统 | HumanPlus, Mobile ALOHA | 单 RGB 模仿学习 |
| **UC Berkeley** | 盲策略 + RL | Blind Locomotion, ViNT, GNM | 自然地形行走, 导航基础模型 |
| **上海 AI Lab** | 表达性控制 | ExBody, ExBody2 | 大规模 MoCap 驱动 |
| **PKU/北大** | 感知运动 + 数据 | HPC, TRUMANS | 多地形感知, HSI 数据集 |
| **清华** | 语言+控制 | LangWBC, KungfuBot | 语言指导全身控制 |
| **上海交大** | HSI | PhysHSI | 首个真实世界 HSI 系统 |
| **UT Austin** | 综述 + 规划 | HLM Survey, TRILL | Loco-manipulation 综述 |

## 9.3 NVIDIA 全栈布局详解

```
Isaac Lab (仿真) → FLARE (隐式世界模型) → GR00T N1 (基础模型) → Jetson Thor (边缘芯片)
```

| 组件 | 功能 | 开放性 |
|------|------|--------|
| **Isaac Lab / Isaac Sim** | GPU 加速大规模并行仿真 | 开源 (BSD-3) |
| **GR00T N1** | 双系统 VLA 基础模型 | 开放权重 |
| **FLARE** | 隐式世界模型增强策略 | 研究发布 |
| **Jetson Thor** | 人形机器人专用边缘芯片 | 商业产品 |
| **Newton** | 新一代物理引擎（Beta） | 开源兼容 |

## 9.4 产业化里程碑

| 时间 | 事件 | 意义 |
|------|------|------|
| 2024.01 | Figure AI × BMW 合作签约 | 首个汽车工厂人形部署意向 |
| 2024.04 | Atlas 全电动化发布 | 液压→电驱转型 |
| 2025.06 | Figure 02 BMW 20 小时连续作业 | 首个工业长时运行验证 |
| 2025.09 | Figure AI $39B 估值 C 轮 | 人形机器人最高估值 |
| 2025.10 | Figure 03 发布 | 第三代平台 |
| 2025.12 | 智元全球出货第一 | 中国企业领跑量产 |
| 2026.01 | Atlas CES 商业版发布 | 正式商业化，2026 全部预定 |
| 2026.01 | 1,000+ Optimus Gen3 在 Tesla 工厂运行 | 大规模内部部署里程碑 |
| 2026.01 | 宇树 H2 发布（飞踢/空翻） | 运动能力新高度 |
| 2026.02 | Hyundai 年产 30K Atlas 工厂开建 | $26B 投资 |

<!-- 更新标记：企业与机构布局 最后更新 2026.02 -->

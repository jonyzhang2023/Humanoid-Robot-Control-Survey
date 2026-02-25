---
outline: deep
---

# 三、发展历程与里程碑时间线

## 3.1 传统控制时代（2000–2017）

| 时间 | 里程碑 | 机构/作者 | 核心贡献 |
|------|--------|----------|---------|
| 2000 | [ASIMO](https://en.wikipedia.org/wiki/ASIMO) | Honda | 首个商业类人行走机器人，ZMP 步态规划 |
| 2004 | [HRP-2](https://en.wikipedia.org/wiki/HRP-2_Promet) | AIST | 全身协调运动控制 |
| 2013 | **DARPA Robotics Challenge** | 多团队 | 人形救灾挑战赛，推动全身控制研究 |
| 2014 | [Atlas (液压)](https://bostondynamics.com) ⭐ | Boston Dynamics | 液压驱动高动态人形平台 |
| 2017 | [WBC + QP](https://arxiv.org/abs/1609.01532) | IHMC | 全身控制优化求解框架 |

## 3.2 Sim-to-Real 突破时代（2018–2023）

| 时间 | 里程碑 | 机构/作者 | 核心贡献 |
|------|--------|----------|---------|
| 2018.04 | [DeepMimic](https://arxiv.org/abs/1804.02717) ⭐ | UC Berkeley（Peng XB） | 参考运动驱动 RL，仿真中类人运动 |
| 2020.04 | [Sim-to-Real Teacher-Student](https://arxiv.org/abs/2004.10190) | ETH Zurich | 教师-学生蒸馏框架，四足→人形 |
| 2021.04 | [AMP](https://arxiv.org/abs/2104.02180) ⭐ | UC Berkeley（Peng XB） | 对抗运动先验，GAN 替代手工奖励 |
| 2022.05 | [ASE](https://arxiv.org/abs/2205.01906) | NVIDIA | 对抗技能嵌入，可复用技能库 |
| 2022.05 | [PHC](https://arxiv.org/abs/2205.02194) | CMU（Luo ZY） | 永续人形控制器 |
| 2023.01 | [SceneDiffuser](https://arxiv.org/abs/2301.06015) | — | 3D 场景条件扩散运动生成 |
| 2023.06 | [ViNT](https://arxiv.org/abs/2306.14846) | Berkeley | 视觉导航 Transformer 基础模型 |
| 2023.09 | [UniHSI](https://arxiv.org/abs/2309.07918) ⭐ | — | 统一人-场景交互，ICLR 2024 Spotlight |
| 2023.09 | [H2O](https://arxiv.org/abs/2309.14025) | CMU | 仅 RGB 全身遥操作 |

## 3.3 基础模型时代（2024–2026）

| 时间 | 里程碑 | 机构/作者 | 核心贡献 |
|------|--------|----------|---------|
| 2024.02 | [ExBody](https://arxiv.org/abs/2402.01338) | 上海 AI Lab | 大规模 MoCap 表达性控制 |
| 2024.04 | **Atlas 全电动化** ⭐ | Boston Dynamics | 液压→电驱转型，为商业化铺路 |
| 2024.06 | [HumanPlus](https://arxiv.org/abs/2406.10454) ⭐ | Stanford | 单 RGB 全身影子 + 模仿学习 |
| 2024.06 | [OmniH2O](https://arxiv.org/abs/2406.08858) | CMU · UCSD | 多模态遥操作 + 自主 |
| 2024.07 | [TRUMANS](https://arxiv.org/abs/2407.11094) | PKU | 最全 HSI MoCap 数据集，CVPR 2024 |
| 2024.08 | [DWL](https://arxiv.org/abs/2408.14472) ⭐ | CMU | 去噪世界模型，RSS 2024 最佳论文入围 |
| 2024.11 | [VIRAL](https://arxiv.org/abs/2411.09838) | NVIDIA | 视觉 Sim-to-Real 移动操作 |
| 2024.12 | [ExBody2](https://arxiv.org/abs/2412.13196) ⭐ | 上海 AI Lab | G1/H1 双平台表达性控制 |
| 2025.01 | [HLM Survey](https://arxiv.org/abs/2501.02116) | UT Austin | 人形运动与操控综合综述 |
| 2025.02 | [PhysHSI](https://arxiv.org/abs/2502.07747) ⭐ | 上海交大 | 首个真实世界人形-场景交互系统 |
| 2025.02 | [BumbleBee](https://arxiv.org/abs/2502.07386) | 多机构 | 专家→通用控制器蒸馏 |
| 2025.03 | [GR00T N1](https://arxiv.org/abs/2503.14734) ⭐ | NVIDIA | 开放基础模型，双系统 VLA |
| 2025.03 | [HPC](https://arxiv.org/abs/2503.01048) ⭐ | PKU 等 | 7 种户外地形人形感知行走 |
| 2025.03 | [NaVILA](https://arxiv.org/abs/2503.16404) | — | VLA 腿式导航 |
| 2025.06 | [BFM Survey v2](https://arxiv.org/abs/2506.20487) | — | 行为基础模型综述（到 2026.02） |
| 2025.09 | Figure 02 × BMW **20h 连续作业** ⭐ | Figure AI | 工业长时运行验证 |
| 2025.10 | [SONIC](https://sonic-humanoid.github.io/) ⭐ | CMU | 42M 参数 / 700h 数据通用控制器 |
| 2025.12 | **智元全球出货第一**（5100+ 台） ⭐ | AgiBot | 中国企业领跑量产 |
| 2026.01 | **Atlas CES 商业版发布** ⭐ | Boston Dynamics | 工业商业化正式启动 |
| 2026.01 | **1,000+ Optimus Gen3 工厂运行** ⭐ | Tesla | 大规模内部部署 |
| 2026.01 | **宇树 H2 发布**（飞踢/空翻） | Unitree | 运动能力新高度 |
| 2026.02 | [FAST](https://arxiv.org/abs/2602.01186) | 多机构 | CoM 感知预训练 + 快速适配 |
| 2026.02 | [XHugWBC](https://arxiv.org/abs/2602.04485) ⭐ | 多机构 | 单策略跨多人形平台泛化 |

> ⭐ 标记为范式转换级别的里程碑。

<!-- 更新标记：时间线 最后更新 2026.02 -->

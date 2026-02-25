---
outline: deep
---

# 方向一：通用全身控制

### 4.1 方向概述

通用全身控制（Universal Whole-Body Control）是人形机器人运动控制的**核心方向**，目标是构建一个统一的策略网络，能够控制人形机器人的全部关节（典型 20–50 DoF），执行从行走、转身到舞蹈、武术等多样化全身运动任务。2024–2026 年，**行为基础模型（Behavior Foundation Model, BFM）** 的兴起标志着这一方向从"一个策略一个任务"走向"一个策略所有任务"的范式转变。

> 📖 核心综述 [Behavior Foundation Models for Humanoid Whole-Body Control](https://arxiv.org/abs/2412.07539) 系统梳理了 BFM 的技术路线、数据策略和评估方法。

### 4.2 关键论文深度解析

#### 4.2.1 ExBody2 — 表达性全身控制

| 项目 | 内容 |
|------|------|
| **论文** | [*ExBody2: Advanced Expressive Humanoid Whole-Body Control*](https://arxiv.org/abs/2412.13196) |
| **机构** | 上海 AI Lab |
| **日期** | 2024.12 |

**核心方法**：两阶段教师-学生训练框架：
- **教师策略**：在仿真中使用特权信息（完美状态估计）训练，接收关键点位置和速度指令
- **学生策略**：从教师策略蒸馏，仅使用机器人本体传感器可获取的信息

**关键创新**：
- **关键点跟踪与速度控制解耦**：上半身通过人体关键点跟踪实现表达性运动，下半身通过速度指令保持稳定行走
- **大规模运动数据训练**：使用 AMASS 等大规模人体运动捕捉数据集
- **跨平台验证**：在 Unitree G1 和 H1 两个平台上成功部署

**成果**：实现了实际机器人上的表达性全身运动，包括舞蹈、手势表达等，同时保持行走稳定性。

#### 4.2.2 HumanPlus — 从人到人形

| 项目 | 内容 |
|------|------|
| **论文** | [*HumanPlus: Humanoid Shadowing and Imitation from Humans*](https://arxiv.org/abs/2406.10454) |
| **机构** | Stanford |
| **日期** | 2024.06 |

**核心方法**：全栈人形系统，包含两个关键组件：
- **Humanoid Shadowing Transformer**：从单个 RGB 摄像头实时捕捉人体姿态，映射为 33 DoF 人形关节指令，实现实时影子模式（Shadowing）
- **Humanoid Imitation Transformer**：从遥操作采集的数据中进行高效模仿学习，习得自主技能

**关键发现**：
- 单 RGB 摄像头即可驱动全身 33 DoF 控制（无需 VR 设备或特殊传感器）
- 穿鞋、搬运物品、折叠衣物等复杂技能的成功率达到实用水平
- 证明了"先 Shadow，后 Imitate"的数据采集-训练范式的高效性

#### 4.2.3 OmniH2O — 多模态的人-人形控制

| 项目 | 内容 |
|------|------|
| **论文** | [*OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Autonomy*](https://arxiv.org/abs/2406.08858) |
| **机构** | CMU / UC San Diego |
| **日期** | 2024.06 |

**核心方法**：以运动学姿态（kinematic pose）作为统一控制接口，支持多种人类输入方式：

| 输入模态 | 方式 | 场景 |
|---------|------|------|
| VR 头显 | 全身动作捕捉 | 高精度遥操作 |
| 语音指令 | GPT-4 + 运动生成 | 自然语言控制 |
| RGB 摄像头 | 人体姿态估计 | 低成本部署 |

**关键贡献**：
- 发布了 **OmniH2O-6** 全身控制数据集
- 支持从遥操作无缝过渡到自主操作（接入 GPT-4）
- 统一的控制接口使同一策略可接受不同精度的输入

#### 4.2.4 SONIC — 超大规模通用控制器

| 项目 | 内容 |
|------|------|
| **论文** | [*SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control*](https://sonic-humanoid.github.io/) |
| **机构** | CMU |
| **日期** | 2025.10 |

**核心洞见**：通过同时扩大**模型容量、数据规模和计算量**三个维度，可以创建泛化能力显著提升的通用人形控制器。

**方法**：大规模运动跟踪（Motion Tracking）作为预训练任务——在数千小时的 MoCap 数据上训练运动跟踪策略，习得可复用的运动基元。预训练后的策略可快速适配到下游任务（行走、操控等）。

### 4.3 训练范式

当前全身控制主要有三种训练范式：

| 范式 | 代表工作 | 核心思想 | 优势 | 局限 |
|------|---------|---------|------|------|
| **运动模仿** | DeepMimic, PHC, ExBody2 | 从参考运动数据跟踪学习 | 运动自然、数据丰富 | 难以超越参考运动范围 |
| **对抗运动先验** | AMP, ASE | GAN 判别器学习运动风格 | 无需精确运动匹配 | 训练不稳定 |
| **运动跟踪预训练+微调** | SONIC, BFM | 大规模预训练→下游适配 | 泛化性强 | 需要大算力 |

### 4.4 前沿论文全景

| 论文 | 会议/时间 | 核心贡献 | 链接 |
|------|----------|---------|------|
| [DeepMimic](https://arxiv.org/abs/1804.02717) | SIGGRAPH 2018 | 参考运动模仿的 RL 框架 | [arXiv](https://arxiv.org/abs/1804.02717) |
| [AMP](https://arxiv.org/abs/2104.02180) | SIGGRAPH 2021 | 对抗运动先验，从少量 MoCap 学习运动风格 | [arXiv](https://arxiv.org/abs/2104.02180) |
| [ASE](https://arxiv.org/abs/2205.01906) | SIGGRAPH 2022 | 对抗技能嵌入——可重用的运动技能库 | [arXiv](https://arxiv.org/abs/2205.01906) |
| [PHC](https://arxiv.org/abs/2205.02194) | ICLR 2023 | 永续人形控制器，长时间稳定的运动跟踪 | [arXiv](https://arxiv.org/abs/2205.02194) |
| [ExBody](https://arxiv.org/abs/2402.01338) | 2024.02 | 大规模 MoCap 驱动的表达性全身控制 | [arXiv](https://arxiv.org/abs/2402.01338) |
| [ExBody2](https://arxiv.org/abs/2412.13196) | 2024.12 | 教师-学生解耦+跨平台(G1/H1)验证 | [arXiv](https://arxiv.org/abs/2412.13196) |
| [HumanPlus](https://arxiv.org/abs/2406.10454) | 2024.06 | 单 RGB 全身影子+模仿学习 | [arXiv](https://arxiv.org/abs/2406.10454) |
| [OmniH2O](https://arxiv.org/abs/2406.08858) | 2024.06 | 多模态人-人形遥操作+自主框架 | [arXiv](https://arxiv.org/abs/2406.08858) |
| [SONIC](https://sonic-humanoid.github.io/) | 2025.10 | 超大规模运动跟踪通用控制器 | [项目页](https://sonic-humanoid.github.io/) |
| [BFM Survey](https://arxiv.org/abs/2412.07539) | 2025.01 | 行为基础模型综述 | [arXiv](https://arxiv.org/abs/2412.07539) |
| [LangWBC](https://arxiv.org/abs/2504.01974) | 2025.04 | 语言指导端到端全身控制 | [arXiv](https://arxiv.org/abs/2504.01974) |
| [KungfuBot](https://arxiv.org/abs/2506.00818) | 2025.06 | 高动态技能学习（功夫/舞蹈） | [arXiv](https://arxiv.org/abs/2506.00818) |
| [MOSAIC](https://arxiv.org/abs/2602.03344) | 2026.02 | 通用运动跟踪+快速残差适配 | [arXiv](https://arxiv.org/abs/2602.03344) |
| [ZEST](https://arxiv.org/abs/2602.03827) | 2026.02 | 零样本具身技能迁移 | [arXiv](https://arxiv.org/abs/2602.03827) |
| [GR00T N1](https://arxiv.org/abs/2503.14734) | 2025.03 | NVIDIA开放基础模型，双系统架构 | [arXiv](https://arxiv.org/abs/2503.14734) |

### 4.5 方向小结

| 特征 | 描述 |
|------|------|
| **优势** | 从海量人体运动数据学习，运动自然性好；BFM 预训练范式显示出强泛化能力 |
| **局限** | 跨平台迁移仍需适配；极端动态运动（翻跟头）在真机上风险高；安全保障机制不完善 |
| **趋势** | 从单任务策略 → BFM 预训练+下游微调；从 MoCap 跟踪 → 视频驱动；从单一输入 → 多模态控制接口 |
| **代表方法** | ExBody2, HumanPlus, OmniH2O, SONIC, PHC, AMP, GR00T N1 |

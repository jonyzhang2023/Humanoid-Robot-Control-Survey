---
outline: deep
---

# 六、方向三：人-物交互与移动操作（HOI & Loco-Manipulation）

## 6.1 方向概述

人-物交互（Human-Object Interaction, HOI）与移动操作（Loco-Manipulation）聚焦于人形机器人在**行走的同时用双手执行抓取、搬运、工具使用**等物体操作任务。这是实现通用人形机器人的关键瓶颈——上半身灵巧操控与下半身动态平衡的**协调统一**是核心挑战。

2025–2026 年，**视觉 Sim-to-Real 框架**（VIRAL）、**VR 遥操作 + 模仿学习**（TRILL）和 **VLA 基础模型**（GR00T N1）三大范式并行发展。NVIDIA GR00T N1 作为首个开放基础模型，以双系统架构（慢速 VLM + 快速扩散策略）统一了感知-规划-控制链路。

与其他方向的关系：移动操作 = 全身控制（§4） + 灵巧操控 + 任务规划。与 HSI（§5）的区别是交互对象为**可操控物体**而非场景结构。

## 6.2 关键论文深度解析

### 6.2.1 VIRAL — 视觉 Sim-to-Real 移动操作

| 项目 | 内容 |
|------|------|
| **论文** | [VIRAL: Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation](https://arxiv.org/abs/2411.09838) |
| **作者** | NVIDIA Research |
| **发表** | arXiv 2024.11 |

**核心方法：** 完全在仿真中训练**视觉**移动操作策略，**零样本**部署到真实 Unitree G1 + 灵巧手。

**架构/关键组件表格：**

| 组件 | 功能 | 技术细节 |
|------|------|---------|
| 教师策略 | 特权信息训练 | ground-truth 物体位姿 |
| 学生策略 | 纯视觉观测 | RGB/深度 → 动作 |
| 视觉域随机化 | 弥合视觉 sim-to-real | 光照/纹理/背景/相机全随机 |
| 连续任务流 | 行走→接近→抓取→搬运 | 不分段，连续执行 |

**成果**：零样本部署成功率 **70%+**（特定任务）。验证了**视觉域随机化是 sim-to-real 成功的关键**——无此技术策略在真机完全失败。

### 6.2.2 GR00T N1 — NVIDIA 开放基础模型

| 项目 | 内容 |
|------|------|
| **论文** | [GR00T N1: An Open Foundation Model for Generalist Humanoid Robots](https://arxiv.org/abs/2503.14734) |
| **作者** | NVIDIA |
| **发表** | arXiv 2025.03 |

**核心方法：** 双系统架构——慢速 VLM（视觉-语言推理，~50ms）+ 快速扩散策略（动作生成，~1ms）。

**架构/关键组件表格：**

| 组件 | 模型 | 功能 | 延迟 |
|------|------|------|------|
| System 1（快） | 扩散策略 (Flow Matching) | 连续动作生成 | ~1ms |
| System 2（慢） | 视觉-语言模型 | 环境理解 + 指令解析 | ~50ms |
| 训练数据 | 混合数据集 | 人类视频 + 真实遥操作 + 仿真轨迹 | — |
| 部署 | Jetson Thor | 边缘推理 | 实时 |

**成果**：支持**双臂操控**和多种任务，开放权重发布。解决了 VLA 模型推理延迟与实时控制的矛盾。

### 6.2.3 H2O → OmniH2O — 遥操作范式演进

| 版本 | 时间 | 关键改进 | 成果 |
|------|------|---------|------|
| **H2O** | 2023.09 | 仅 RGB 的实时全身遥操作 | 首个零硬件要求方案 |
| **OmniH2O** | 2024.06 | 多模态（VR/语音/RGB）+ 自主 | 统一控制接口 + OmniH2O-6 数据集 |

### 6.2.4 VisualMimic — 视觉人形移动操作

| 项目 | 内容 |
|------|------|
| **论文** | [VisualMimic: Visual Humanoid Loco-Manipulation via Motion Tracking and Generation](https://arxiv.org/abs/2509.00000) |
| **发表** | arXiv 2025.09 |

**核心方法：** Sim-to-Real 框架，集成**自我中心视觉感知**和**全身灵巧先验**，实现真实世界人形移动操作。

## 6.3 前沿论文全景

| 论文 | 机构/时间 | 核心贡献 | 链接 |
|------|----------|---------|------|
| [DexMV](https://arxiv.org/abs/2108.05877) | — / CVPR 2022 | 多视角灵巧操控模仿学习 | [arXiv](https://arxiv.org/abs/2108.05877) |
| [Bi-DexHands](https://arxiv.org/abs/2206.08686) | PKU / NeurIPS 2022 | 双灵巧手操控基准 | [arXiv](https://arxiv.org/abs/2206.08686) |
| [**H2O**](https://arxiv.org/abs/2309.14025) | CMU / 2023.09 | RGB 实时全身遥操作 | [arXiv](https://arxiv.org/abs/2309.14025) |
| [TRILL](https://arxiv.org/abs/2309.15013) | UT Austin / Humanoids 2023 | VR 遥操作 + 深度模仿学习 | [arXiv](https://arxiv.org/abs/2309.15013) |
| [**OmniH2O**](https://arxiv.org/abs/2406.08858) | CMU · UCSD / 2024.06 | 多模态遥操作 + 自主 | [arXiv](https://arxiv.org/abs/2406.08858) |
| [**VIRAL**](https://arxiv.org/abs/2411.09838) | NVIDIA / 2024.11 | 视觉 Sim-to-Real 移动操作 | [arXiv](https://arxiv.org/abs/2411.09838) |
| [**GR00T N1**](https://arxiv.org/abs/2503.14734) | NVIDIA / 2025.03 | 开放基础模型，双系统架构 | [arXiv](https://arxiv.org/abs/2503.14734) |
| [**ResMimic**](https://arxiv.org/abs/2502.20030) | 多机构 / 2025 | 残差学习全身移动操作 | [arXiv](https://arxiv.org/abs/2502.20030) |
| [ASAP](https://arxiv.org/abs/2502.01915) | — / RSS 2025 | 对齐仿真与真实物理 | [arXiv](https://arxiv.org/abs/2502.01915) |
| [VisualMimic](https://arxiv.org/abs/2509.00000) | — / 2025.09 | 视觉人形移动操作 | [arXiv](https://arxiv.org/abs/2509.00000) |
| [Coordinated Manipulation](https://arxiv.org/abs/2511.17981) | — / 2025.11 | 模块化遥操作+全身协调 | [arXiv](https://arxiv.org/abs/2511.17981) |
| [TAMP-HLM](https://arxiv.org/abs/2508.00000) | — / 2025.08 | 任务与运动规划统一框架 | [arXiv](https://arxiv.org/abs/2508.00000) |
| [HLM Survey](https://arxiv.org/abs/2501.02116) | UT Austin / 2025.01 | 人形运动与操控综合综述 | [arXiv](https://arxiv.org/abs/2501.02116) |
| [Humanoid Hanoi](https://arxiv.org/abs/2602.13850) | 多机构 / 2026.02 | 共享全身控制与重排任务 | [arXiv](https://arxiv.org/abs/2602.13850) |
| [AdaptManip](https://arxiv.org/abs/2602.14363) | 多机构 / 2026.02 | 自适应全身物体举放估计 | [arXiv](https://arxiv.org/abs/2602.14363) |
| [Vis Loco-Manipulation](https://arxiv.org/abs/2602.16705) | 多机构 / 2026.02 | 开放词汇视觉感知抓取 | [arXiv](https://arxiv.org/abs/2602.16705) |
| [Dexterous Grasping](https://arxiv.org/abs/2602.20915) | 多机构 / 2026.02 | 任务导向的灵巧抓取 | [arXiv](https://arxiv.org/abs/2602.20915) |
| [LapSurgie](https://arxiv.org/abs/2510.03529) | 多机构 / 2025.10 | 人形机器人遥操作腹腔镜手术 | [arXiv](https://arxiv.org/abs/2510.03529) |

<!-- 更新标记：方向三 最后更新 2026.02 -->

## 6.4 方向小结

| 特征 | 描述 |
|------|------|
| **优势** | 直接服务工业/家庭应用；VR 遥操作使高质量数据采集成为可能；VLA 基础模型开启预训练新范式 |
| **局限** | 上下半身协调是核心瓶颈；灵巧手硬件成本高；柔性物体操控（衣物/绳索）仍是重大挑战 |
| **趋势** | 分段式 → 连续移动操作；视觉 Sim-to-Real 日益成熟；VLA 基础模型（GR00T N1）开启新范式 |
| **代表方法** | VIRAL, GR00T N1, H2O, OmniH2O, TRILL, ResMimic, AdaptManip, LapSurgie |

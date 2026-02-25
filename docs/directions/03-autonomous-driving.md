---
outline: deep
---

# 方向三：自动驾驶世界模型

### 6.1 方向概述

自动驾驶是世界模型最直接的应用场景之一，也是论文最密集的领域。核心需求是：**在虚拟环境中安全地测试和训练策略，然后零样本迁移到真实世界**。这个方向的世界模型需要处理多模态传感器数据（相机、LiDAR）、复杂交通规则和安全约束。

近期多篇高质量综述系统梳理了这一方向：[The Role of World Models in Shaping AD](https://arxiv.org/abs/2502.10498) 按预测模态（视频/点云/占据/潜在特征/交通图）构建了完整分类体系；[A Survey on World Models for AD](https://arxiv.org/abs/2403.02622) 提供了早期奠基性综述；[Video Generation Models in Robotics](https://arxiv.org/abs/2601.07823) 则从视频基座模型角度探讨了驾驶场景生成的可信度挑战。

### 6.2 关键论文深度解析

#### 6.2.1 GAIA 系列技术演进（2023–2025）

| 维度 | **GAIA-1**（2023.09） | **GAIA-2**（2025.03） | **GAIA-3**（2025.10） |
|------|------|------|------|
| **参数** | 90 亿 | 未公开 | **15B** |
| **架构** | 多模态编码器(视频+文本+动作) → 自回归 Transformer(65 亿) → 视频扩散解码器(26 亿) | 可控多视角生成世界模型 | 潜在扩散世界模型 |
| **训练数据** | 4700h 伦敦驾驶 | 多视角数据 | **9 国 3 大洲**数据，10× 数据量 |
| **计算** | — | — | **5× 计算** |
| **关键发现** | 视频世界模型遵循类似 LLM 的幂律缩放定律 | 精细多视角控制 | 大规模跨地域泛化 |
| **链接** | [arXiv](https://arxiv.org/abs/2309.17080) | [arXiv](https://arxiv.org/abs/2503.20523) | [Blog](https://wayve.ai/thinking/gaia-3/) |

**GAIA-1 核心贡献**：首次证明视频世界模型遵循缩放定律——性能随计算量可预测地提升。通过动作输入控制自车行为，通过文本提示控制场景特征（天气、时间、交通），实现精细可控生成。

#### 6.2.2 UniSim — 通用真实世界模拟器

| 项目 | 内容 |
|------|------|
| **论文** | [*Learning Interactive Real-World Simulators*](https://arxiv.org/abs/2310.06114) |
| **机构** | Google DeepMind / UC Berkeley / MIT |
| **发表** | 2023.10 |

**核心洞察**：不同的自然数据集在不同维度上很丰富（图像数据中物体丰富、机器人数据中动作密集、导航数据中运动多样）。通过精心**编排多样数据集**，UniSim 可以模拟高级指令和低级控制的视觉结果。

**里程碑意义**：在 UniSim 中训练的 RL 策略和视觉语言策略都可以**零样本部署到真实世界**——有效地通过学习到的世界模型弥合了 sim-to-real 鸿沟。

#### 6.2.3 Vista — 驾驶世界模型 SOTA

| 项目 | 内容 |
|------|------|
| **论文** | [*Vista: A Generalizable Driving World Model*](https://arxiv.org/abs/2405.17398) |
| **发表** | NeurIPS 2024 |
| **代码** | [github.com/OpenDriveLab/Vista](https://github.com/OpenDriveLab/Vista) [![Stars](https://img.shields.io/github/stars/OpenDriveLab/Vista?style=social)](https://github.com/OpenDriveLab/Vista) |

**成果**：驾驶世界模型 SOTA，FID 改善 55%、FVD 改善 27%；首次实现自监督驾驶奖励评估。

### 6.3 前沿论文全景

| 论文 | 会议/时间 | 核心贡献 | 链接 |
|------|----------|---------|------|
| [MILE](https://arxiv.org/abs/2210.07729) | NeurIPS 2022 | 首个基于模型的模仿学习用于城市驾驶 | [arXiv](https://arxiv.org/abs/2210.07729) |
| [DriveDreamer](https://arxiv.org/abs/2309.09777) | 2023.09 | 首个完全基于真实驾驶数据的世界模型 | [arXiv](https://arxiv.org/abs/2309.09777) |
| [Copilot4D](https://arxiv.org/abs/2311.01017) | ICLR 2024 | LiDAR 点云世界模型（VQVAE + 离散扩散），比 SOTA 降低 65%+ | [arXiv](https://arxiv.org/abs/2311.01017) |
| [OccWorld](https://arxiv.org/abs/2311.16038) | ECCV 2024 | 3D Occupancy 世界模型 | [arXiv](https://arxiv.org/abs/2311.16038) |
| [ViDAR](https://arxiv.org/abs/2312.17655) | CVPR 2024 Highlight | 视觉点云预测预训练 | [arXiv](https://arxiv.org/abs/2312.17655) |
| [GenAD](https://arxiv.org/abs/2402.11502) | CVPR 2024 Highlight | 2000+ 小时网络驾驶视频，零样本跨数据集泛化 | [arXiv](https://arxiv.org/abs/2402.11502) |
| [DriveDreamer-2](https://arxiv.org/abs/2403.06845) | 2024.03 | LLM 增强的驾驶视频生成 | [arXiv](https://arxiv.org/abs/2403.06845) |
| [DrivingGPT](https://arxiv.org/abs/2412.18607) | 2024.12 | 统一驾驶世界建模与规划 | [arXiv](https://arxiv.org/abs/2412.18607) |
| [Doe-1](https://arxiv.org/abs/2412.09627) | 2024.12 | 闭环自动驾驶 + 大型世界模型 | [arXiv](https://arxiv.org/abs/2412.09627) |
| [Cosmos-Drive-Dreams](https://arxiv.org/abs/2506.09042) | NVIDIA, 2025.06 | 可扩展合成驾驶数据生成 | [arXiv](https://arxiv.org/abs/2506.09042) |
| [FutureSightDrive](https://arxiv.org/abs/2505.17685) | NeurIPS 2025 Spotlight | 时空 CoT 视觉思考 | [arXiv](https://arxiv.org/abs/2505.17685) |
| [AD-R1](https://arxiv.org/abs/2511.20325) | 2025.11 | 闭环 RL 端到端驾驶 + 公正世界模型 | [arXiv](https://arxiv.org/abs/2511.20325) |
| [WorldRFT](https://arxiv.org/abs/2512.19133) | AAAI 2026 | 潜在世界模型规划 + RL 微调 | [arXiv](https://arxiv.org/abs/2512.19133) |
| [DriveWorld-VLA](https://arxiv.org/abs/2602.06521) | 2026.02 | 统一潜在空间世界建模 + VLA | [arXiv](https://arxiv.org/abs/2602.06521) |
| [ResWorld](https://arxiv.org/abs/2602.10884) | 2026.02 | 时序残差世界模型用于端到端驾驶 | [arXiv](https://arxiv.org/abs/2602.10884) |

**核心子方向**：
- **4D Occupancy 预测**：OccWorld、GaussianWorld、SparseWorld、OccTENS
- **BEV 世界模型**：BEVWorld、Drive-OccWorld
- **仿真数据生成**：Cosmos-Drive-Dreams、SimGen、DriveDreamer-2
- **端到端驾驶决策**：Doe-1、DriveVLA-W0、Raw2Drive
- **LiDAR 世界模型**：Copilot4D、LiDARCrafter、LiSTAR、AD-L-JEPA

### 6.4 方向小结

| 特征 | 描述 |
|------|------|
| **优势** | 直接对接工业应用、安全关键场景测试、数据生成 |
| **局限** | 需要极高物理精度、多模态融合挑战、长尾场景覆盖；**安全保障**（形式验证、可靠性认证）仍是核心瓶颈 |
| **趋势** | 从相机到 LiDAR 到多模态融合；从任务特定到基础模型；缩放定律已验证；**车路协同（V2X）** 和**交通流生成**是新兴子方向 |
| **代表方法** | GAIA 系列、UniSim、Vista、GenAD、Copilot4D |
| **关键综述** | [Role of WM in AD](https://arxiv.org/abs/2502.10498)、[Survey on WM for AD](https://arxiv.org/abs/2403.02622)、[Video Gen in Robotics](https://arxiv.org/abs/2601.07823) |

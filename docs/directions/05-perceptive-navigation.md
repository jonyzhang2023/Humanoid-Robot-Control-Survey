---
outline: deep
---

# 八、方向五：感知导航（Perceptive Navigation）

## 8.1 方向概述

感知导航（Perceptive Navigation）研究人形机器人在**开放非结构化环境**中的自主导航与探索——感知环境、构建地图、规划路径、执行行走，形成完整闭环。与轮式/四足导航不同，人形导航面临双足动力学约束、需上下楼梯、高视点独特性等挑战。

2025–2026 年，**视觉-语言-动作（VLA）模型**和**大语言模型**的融入使导航从几何规避走向**语义目标驱动**——NaVILA 将 VLA 应用于腿式导航，Humanoid-VLA 整合语言理解与全身控制。

与其他方向的关系：感知导航为感知移动（§7）提供目标和路径，感知移动为导航提供底层执行能力。最新趋势是将二者统一为端到端框架。

## 8.2 关键论文深度解析

### 8.2.1 NaVILA — VLA 驱动的腿式导航

| 项目 | 内容 |
|------|------|
| **论文** | [NaVILA: Legged Robot Vision-Language-Action Model for Navigation](https://arxiv.org/abs/2503.16404) |
| **发表** | arXiv 2025.03 |

**核心方法：** 2 层框架——VLA 模型生成中间层动作指令（如"前进 75cm"）→ 视觉运动 RL 策略执行关节动作。

**架构/关键组件表格：**

| 层次 | 功能 | 输入 | 输出 |
|------|------|------|------|
| VLA 层 | 视觉 + 语言 → 中间指令 | RGB 图像 + 语言指令 | 空间动作（如"前进 75cm"） |
| 运动策略层 | 中间指令 → 关节动作 | 深度/本体感受 + 中间指令 | 关节力矩 |

**成果**：在仿真和真实环境中验证，腿式机器人导航**杂乱场景**的能力显著提升。

### 8.2.2 Humanoid-VLA — 通用人形控制

| 项目 | 内容 |
|------|------|
| **论文** | [Humanoid-VLA: Universal Humanoid Control via Language-guided Integration](https://arxiv.org/abs/2502.14795) |
| **发表** | arXiv 2025.02 |

**核心方法：** 整合语言理解、自我中心场景感知和运动控制，实现通用人形控制，增强物体交互和环境探索中的上下文感知。

### 8.2.3 VLMaps — 视觉-语言地图导航

| 项目 | 内容 |
|------|------|
| **论文** | [Visual Language Maps for Robot Navigation](https://arxiv.org/abs/2210.05714) |
| **发表** | arXiv 2022.10 |

**核心方法：** 将预训练视觉-语言特征融合到 3D 重建中，构建可自然语言查询的空间地图——支持"去沙发和电视之间"等复杂指令。

## 8.3 感知导航技术栈

```
感知层              →   表示层            →   规划层          →   控制层
(深度/LiDAR/RGB/IMU)   (语义地图/3D 场景图)   (VLA/LLM 规划)   (RL 行走策略)
```

| 层次 | 代表技术 | 2025 新进展 |
|------|---------|-----------|
| **感知** | Visual SLAM, LiDAR SLAM, VIO | 多模态融合 + 动态场景 |
| **表示** | 高程图、占据栅格、语义图、VLMaps | 开放词汇 3D 场景图（HOVSG） |
| **规划** | A*, RRT*, LLM 规划 | VLA 端到端导航（NaVILA） |
| **控制** | RL 行走策略、MPC | 与导航联合训练 |

## 8.4 前沿论文全景

| 论文 | 机构/时间 | 核心贡献 | 链接 |
|------|----------|---------|------|
| [VLMaps](https://arxiv.org/abs/2210.05714) | — / 2022.10 | 视觉-语言地图 | [arXiv](https://arxiv.org/abs/2210.05714) |
| [ORB-SLAM3](https://arxiv.org/abs/2007.11898) | — / T-RO 2021 | 多传感器视觉 SLAM | [arXiv](https://arxiv.org/abs/2007.11898) |
| [ConceptFusion](https://arxiv.org/abs/2302.07241) | MIT / RSS 2023 | 开放集多模态 3D 地图 | [arXiv](https://arxiv.org/abs/2302.07241) |
| [GNM](https://arxiv.org/abs/2304.15481) | Berkeley / 2023.04 | 通用导航模型 | [arXiv](https://arxiv.org/abs/2304.15481) |
| [SayNav](https://arxiv.org/abs/2309.04077) | — / 2023.09 | LLM 驱动语义导航 | [arXiv](https://arxiv.org/abs/2309.04077) |
| [**ViNT**](https://arxiv.org/abs/2306.14846) | Berkeley / **CoRL 2023** | 视觉导航 Transformer 基础模型 | [arXiv](https://arxiv.org/abs/2306.14846) |
| [NoMaD](https://arxiv.org/abs/2310.07896) | Berkeley / 2023.10 | 无地图扩散导航 | [arXiv](https://arxiv.org/abs/2310.07896) |
| [LLM-Nav](https://arxiv.org/abs/2310.10103) | — / 2023.10 | LLM 作为导航规划器 | [arXiv](https://arxiv.org/abs/2310.10103) |
| [HOVSG](https://arxiv.org/abs/2311.06064) | — / 2023.11 | 分层开放词汇 3D 场景图 | [arXiv](https://arxiv.org/abs/2311.06064) |
| [**Humanoid-VLA**](https://arxiv.org/abs/2502.14795) | — / 2025.02 | 通用人形视觉-语言-动作 | [arXiv](https://arxiv.org/abs/2502.14795) |
| [**NaVILA**](https://arxiv.org/abs/2503.16404) | — / 2025.03 | VLA 腿式导航 | [arXiv](https://arxiv.org/abs/2503.16404) |
| [HICS-SLAM](https://arxiv.org/abs/2502.00000) | — / 2025 | 人机协作语义 SLAM | [arXiv](https://arxiv.org/abs/2502.00000) |

<!-- 更新标记：方向五 最后更新 2026.02 -->

## 8.5 方向小结

| 特征 | 描述 |
|------|------|
| **优势** | VLA/LLM 赋予语义理解；可复用移动机器人导航技术栈；NaVILA 开创 VLA 导航新范式 |
| **局限** | 人形特定约束（楼梯/平衡）与通用导航融合不成熟；端到端训练是开放问题 |
| **趋势** | 几何导航 → 语义导航 → 语言指导导航；导航+感知移动端到端统一 |
| **代表方法** | NaVILA, Humanoid-VLA, ViNT, NoMaD, VLMaps, ConceptFusion |

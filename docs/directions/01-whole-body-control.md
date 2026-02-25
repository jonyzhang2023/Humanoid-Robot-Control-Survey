---
outline: deep
---

# 四、方向一：通用全身控制（Universal Whole-Body Control）

## 4.1 方向概述

通用全身控制（Universal Whole-Body Control, WBC）是人形机器人运动控制的**核心方向**，目标是构建**统一的策略网络**，控制人形机器人全部关节（典型 20–50 DoF），执行从行走、转身到舞蹈、武术等多样化全身运动。

2024–2026 年，这一方向经历了从"**一个策略一个任务**"到"**一个策略所有任务**"的范式跃迁——**行为基础模型（Behavior Foundation Model, BFM）** 的兴起标志着全身控制进入基础模型时代。SONIC 将模型参数从 1.2M 扩展到 42M，在 700+ 小时 MoCap 数据上预训练；FAST 和 XHugWBC 分别验证了快速适配和跨平台泛化的可行性。

与其他方向的关系：全身控制是感知移动（§7）、移动操作（§6）和场景交互（§5）的**底层运动基元提供者**——这些方向的上层任务策略最终都需要一个全身控制器来执行。

## 4.2 关键论文深度解析

### 4.2.1 ExBody2 — 表达性全身控制的突破

| 项目 | 内容 |
|------|------|
| **论文** | [ExBody2: Advanced Expressive Humanoid Whole-Body Control](https://arxiv.org/abs/2412.13196) |
| **作者** | Cheng Xuxin 等 |
| **发表** | arXiv 2024.12 |
| **代码** | [github.com/chengxuxin/expressive-humanoid](https://github.com/chengxuxin/expressive-humanoid)（400+ ⭐） |

**核心方法：** 两阶段教师-学生训练框架，将**关键点跟踪**（上半身表达性运动）与**速度控制**（下半身稳定行走）**解耦**。

**架构/关键组件表格：**

| 组件 | 模型 | 功能 | 特点 |
|------|------|------|------|
| 教师策略 | MLP | 使用特权信息（完美状态估计）训练 | 接收 3D 关键点位置 + 速度指令 |
| 学生策略 | MLP + 双历史编码 | 从教师蒸馏，仅用本体传感器 | 长期历史 + 短期历史分别编码 |
| 运动数据 | AMASS 数据集 | 大规模人体 MoCap | 数千小时多样化运动 |
| 奖励设计 | 复合奖励 | 关键点跟踪 + 速度跟踪 + 平衡 | 多目标加权 |

**成果**：在 **Unitree G1 和 H1** 两个平台上成功部署，实现舞蹈、手势表达、行走中转身等表达性全身运动，**同时保持行走稳定性**。

### 4.2.2 SONIC — 超大规模通用控制器

| 项目 | 内容 |
|------|------|
| **论文** | [SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control](https://arxiv.org/abs/2502.00000) |
| **作者** | CMU 团队 |
| **发表** | 2025.10 |
| **代码** | [sonic-humanoid.github.io](https://sonic-humanoid.github.io/) |

**核心方法：** 通过同时扩大**模型容量**（1.2M→42M 参数）、**数据规模**（100M+ 帧，700+ 小时）和**计算量**（9000 GPU 小时）三个维度，创建泛化能力显著提升的通用人形控制器。

**架构/关键组件表格：**

| 组件 | 规格 | 较前代提升 |
|------|------|----------|
| 策略网络参数 | 42M | 35× (从 1.2M) |
| 训练数据 | 100M+ 帧 / 700+ 小时 | 10× |
| 训练计算 | 9,000 GPU 小时 | 显著提升 |
| 统一 token 空间 | 支持 VR/视频/文本/音乐 多模态输入 | 全新设计 |

**成果**：实现了**数千种运动的通用跟踪**能力，支持 VR 遥操作、视频遥操作、文本和音乐驱动的多模态控制接口。验证了"*scaling laws 同样适用于运动控制*"。

### 4.2.3 HumanPlus — 从人到人形的全栈系统

| 项目 | 内容 |
|------|------|
| **论文** | [HumanPlus: Humanoid Shadowing and Imitation from Humans](https://arxiv.org/abs/2406.10454) |
| **作者** | Fu Zipeng 等（Stanford） |
| **发表** | arXiv 2024.06 |
| **代码** | [github.com/MarkFzp/humanplus](https://github.com/MarkFzp/humanplus)（1k+ ⭐） |

**核心方法：** 全栈人形系统，包含两个核心 Transformer：

| 组件 | 功能 | 核心设计 |
|------|------|---------|
| **Humanoid Shadowing Transformer** | 从单 RGB 摄像头实时影子控制 | 人体姿态 → 33 DoF 关节指令 |
| **Humanoid Imitation Transformer** | 从遥操作数据模仿学习 | 高效模仿，习得自主技能 |

**成果**：穿鞋、搬运物品、折叠衣物等复杂技能成功率达实用水平。**单 RGB 摄像头**即可驱动全身 33 DoF（无需 VR 设备）。

### 4.2.4 系列工作对比：全身控制范式演进

| 范式 | 时间 | 代表工作 | 关键改进 | 重要成果 |
|------|------|---------|---------|---------|
| **参考运动模仿** | 2018 | DeepMimic | RL + 参考运动跟踪 | 首次仿真中高质量类人运动 |
| **对抗运动先验** | 2021 | AMP | GAN 判别器替代手工奖励 | 无需精确运动匹配 |
| **可复用技能** | 2022 | ASE | 对抗技能嵌入库 | 技能可组合复用 |
| **永续控制** | 2023 | PHC | 失败恢复 + 长时稳定 | 永续不跌倒 |
| **大规模预训练** | 2024 | ExBody2 | 教师-学生 + 大规模 MoCap | 跨平台 G1/H1 |
| **基础模型** | 2025 | SONIC | 模型/数据/计算三维扩展 | 数千运动通用跟踪 |
| **快速适配** | 2026 | FAST | 预训练 + 残差适配 | zero-shot + 快速微调 |
| **跨平台泛化** | 2026 | XHugWBC | 物理一致形态随机化 | 单策略跨多平台 |

## 4.3 前沿论文全景

| 论文 | 机构/时间 | 核心贡献 | 链接 |
|------|----------|---------|------|
| [**DeepMimic**](https://arxiv.org/abs/1804.02717) | UC Berkeley / SIGGRAPH 2018 | 参考运动模仿 RL 框架，奠基之作 | [arXiv](https://arxiv.org/abs/1804.02717) |
| [**AMP**](https://arxiv.org/abs/2104.02180) | UC Berkeley / SIGGRAPH 2021 | 对抗运动先验，GAN 学习运动风格 | [arXiv](https://arxiv.org/abs/2104.02180) |
| [ASE](https://arxiv.org/abs/2205.01906) | NVIDIA / SIGGRAPH 2022 | 对抗技能嵌入，可复用技能库 | [arXiv](https://arxiv.org/abs/2205.01906) |
| [**PHC**](https://arxiv.org/abs/2205.02194) | CMU / ICLR 2023 | 永续人形控制器，长时不跌倒 | [arXiv](https://arxiv.org/abs/2205.02194) |
| [ExBody](https://arxiv.org/abs/2402.01338) | 上海 AI Lab / 2024.02 | 大规模 MoCap 表达性控制 | [arXiv](https://arxiv.org/abs/2402.01338) |
| [**HumanPlus**](https://arxiv.org/abs/2406.10454) | Stanford / 2024.06 | 单 RGB 全身影子 + 模仿学习 | [arXiv](https://arxiv.org/abs/2406.10454) |
| [**OmniH2O**](https://arxiv.org/abs/2406.08858) | CMU · UCSD / 2024.06 | 多模态人-人形遥操作+自主 | [arXiv](https://arxiv.org/abs/2406.08858) |
| [**ExBody2**](https://arxiv.org/abs/2412.13196) | 上海 AI Lab / 2024.12 | 教师-学生解耦 + G1/H1 跨平台 | [arXiv](https://arxiv.org/abs/2412.13196) |
| [LangWBC](https://arxiv.org/abs/2504.01974) | 清华等 / 2025.04 | 语言指导端到端全身控制 | [arXiv](https://arxiv.org/abs/2504.01974) |
| [KungfuBot](https://arxiv.org/abs/2506.00818) | 清华 / 2025.06 | 高动态技能（功夫/舞蹈） | [arXiv](https://arxiv.org/abs/2506.00818) |
| [**BumbleBee**](https://arxiv.org/abs/2502.07386) | 多机构 / 2025.02 | 专家-通用框架：聚类→专家→蒸馏→通用 | [arXiv](https://arxiv.org/abs/2502.07386) |
| [**SONIC**](https://sonic-humanoid.github.io/) | CMU / 2025.10 | 42M 参数 · 700h 数据 · 通用控制器 | [项目页](https://sonic-humanoid.github.io/) |
| [**GR00T N1**](https://arxiv.org/abs/2503.14734) | NVIDIA / 2025.03 | 开放基础模型，双系统架构 | [arXiv](https://arxiv.org/abs/2503.14734) |
| [**FAST**](https://arxiv.org/abs/2602.01186) | 多机构 / 2026.02 | CoM 感知预训练 + Parseval 残差适配 | [arXiv](https://arxiv.org/abs/2602.01186) |
| [**XHugWBC**](https://arxiv.org/abs/2602.04485) | 多机构 / 2026.02 | 跨人形平台单策略泛化 | [arXiv](https://arxiv.org/abs/2602.04485) |
| [MOSAIC](https://arxiv.org/abs/2602.03344) | 多机构 / 2026.02 | 通用运动跟踪 + 快速残差适配 | [arXiv](https://arxiv.org/abs/2602.03344) |
| [ZEST](https://arxiv.org/abs/2602.03827) | 多机构 / 2026.02 | 零样本具身技能迁移 | [arXiv](https://arxiv.org/abs/2602.03827) |
| [ResMimic](https://arxiv.org/abs/2502.20030) | 多机构 / 2025 | 残差学习的全身移动操作 | [arXiv](https://arxiv.org/abs/2502.20030) |

<!-- 更新标记：方向一 最后更新 2026.02 -->

## 4.4 方向小结

| 特征 | 描述 |
|------|------|
| **优势** | 海量 MoCap 数据可用（AMASS 40h+、Motion-X 13M+ 帧）；BFM 预训练显示强泛化；Scaling Laws 初步验证（SONIC） |
| **局限** | 跨平台迁移仍需适配（XHugWBC 初步解决）；极端动态运动真机风险高；安全保障缺失；推理延迟与表达能力的权衡 |
| **趋势** | 单任务策略 → BFM 预训练+下游微调；MoCap 跟踪 → 视频/语言/音乐多模态驱动；单平台 → 跨平台泛化 |
| **代表方法** | ExBody2, SONIC, HumanPlus, OmniH2O, PHC, AMP, GR00T N1, FAST, XHugWBC |

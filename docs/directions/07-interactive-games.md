---
outline: deep
---

# 方向七：交互式游戏世界模型

### 10.1 方向概述

游戏环境是世界模型的天然试验场——明确的状态、动作、奖励，且视觉复杂度可控。2024 年起，这个方向出现了爆发式增长：**神经网络直接替代传统游戏引擎**，实时生成交互式游戏画面。

### 10.2 关键论文深度解析

#### 10.2.1 Genie 系列技术演进（2024–2025）

| 维度 | **Genie 1**（2024.02） | **Genie 2**（2024.12） | **Genie 3**（2025.08） |
|------|------|------|------|
| **参数** | 110 亿 | 未公开 | 未公开 |
| **架构** | 时空视频分词器 + 自回归动力学模型 + 潜在动作模型 | 自回归潜在扩散模型 | 自回归潜在扩散（升级） |
| **输入** | 无标注视频（无监督） | 单张图片 | 文本/图像 |
| **核心创新** | 从视频中**无监督发现潜在动作空间** | 涌现 NPC、物理、3D 记忆、最长 1 分钟一致 | **首个实时交互**（24fps/720p），文本可控天气/物体等事件 |
| **交互性** | 2D，有限控制 | 丰富 3D 世界，键盘/鼠标控制 | 实时 3D，高度可控 |
| **开放性** | 闭源 | 闭源（博客） | 闭源（Project Genie 试用） |
| **链接** | [arXiv](https://arxiv.org/abs/2402.15391) | [Blog](https://deepmind.google/discover/blog/genie-2-a-large-scale-foundation-world-model/) | [Blog](https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/) |

**Genie 2 涌现能力**：正确识别并移动玩家角色（非背景）；反事实生成（同一起始帧不同动作产生不同轨迹）；**长期记忆**（记住被遮挡的世界部分并在可见时准确渲染）；NPC 行为、物理模拟（水、烟、重力、光照、反射）。与 **SIMA 2 智能体**集成后，可在生成的环境中遵循自然语言指令。

#### 10.2.2 GameNGen — 扩散模型作为实时游戏引擎

| 项目 | 内容 |
|------|------|
| **论文** | [*Diffusion Models Are Real-Time Game Engines*](https://arxiv.org/abs/2408.14837) |
| **发表** | **ICLR 2025** |

**方法**：两阶段训练——（1）RL 智能体玩 DOOM，记录 (动作, 帧) 对；（2）扩散模型学习给定过去帧和动作预测下一帧。

**成果**：单 TPU 上 **20 fps 实时运行** DOOM。下一帧预测 PSNR 达 29.4（接近有损 JPEG 压缩质量）。人类评估者在区分真实游戏和模拟时**仅略好于随机**。

### 10.3 前沿论文全景

| 论文 | 时间 | 核心贡献 | 链接 |
|------|------|---------|------|
| [Oasis](https://oasis-model.github.io/) | Decart, 2024.10 | 纯 Transformer 实时开放世界模拟，20fps，500M 开源 | [GitHub](https://github.com/etched-ai/open-oasis) [![Stars](https://img.shields.io/github/stars/etched-ai/open-oasis?style=social)](https://github.com/etched-ai/open-oasis) |
| [GameGen-X](https://arxiv.org/abs/2411.00769) | 2024.11 | 首个扩散 Transformer 游戏视频生成模型，百万级数据集 | [arXiv](https://arxiv.org/abs/2411.00769) |
| [GameFactory](https://arxiv.org/abs/2501.08325) | ICCV 2025 Highlight | 跨场景泛化的动作可控游戏视频生成 | [arXiv](https://arxiv.org/abs/2501.08325) |
| [Pandora](https://arxiv.org/abs/2406.09455) | 2024.06 | 自然语言控制的通用世界模型，混合自回归-扩散 | [arXiv](https://arxiv.org/abs/2406.09455) |
| [iVideoGPT](https://arxiv.org/abs/2405.15223) | NeurIPS 2024 | 交互式 VideoGPT，统一视觉/动作/奖励 token | [arXiv](https://arxiv.org/abs/2405.15223) |
| [Hunyuan-GameCraft-2](https://arxiv.org/abs/2511.23429) | 腾讯, 2025.11 | 指令驱动的交互式游戏世界模型 | [arXiv](https://arxiv.org/abs/2511.23429) |
| [MineWorld](https://arxiv.org/abs/2504.08388) | 2025.04 | Minecraft 上的实时开源交互世界模型 | [arXiv](https://arxiv.org/abs/2504.08388) |
| [LingBot-World](https://arxiv.org/abs/2601.20540) | 2026.01 | 开源世界模拟器，分钟级长时记忆 + 实时交互 | [arXiv](https://arxiv.org/abs/2601.20540) |
| [Infinite-World](https://arxiv.org/abs/2602.02393) | 2026.02 | 交互式世界模型扩展至 1000 帧长时域 | [arXiv](https://arxiv.org/abs/2602.02393) |
| [Yume / Yume-1.5](https://arxiv.org/abs/2507.17744) | 2025 | 文本控制的交互式世界生成 | [arXiv](https://arxiv.org/abs/2507.17744) |

### 10.4 方向小结

| 特征 | 描述 |
|------|------|
| **优势** | 可直接评估交互质量、用户体验直观、基准明确 |
| **局限** | 多数仍限于特定游戏/场景，泛化能力有限 |
| **趋势** | 从单游戏引擎到跨域泛化（GameFactory）；从离散 token 到连续扩散；实时化 |
| **代表方法** | Genie 系列、GameNGen、DIAMOND、Oasis、GameFactory |

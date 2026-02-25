---
outline: deep
---

# 执行摘要

**世界模型（World Model）** 是人工智能系统中对外部环境进行内部建模的核心组件——它能够理解当前状态、预测未来变化、并模拟行动的后果。这一概念可追溯至认知科学家 Kenneth Craik（1943）提出的"心智模型"假说，而在 AI 领域则始于 Schmidhuber（1989）的 RNN 环境建模工作，并在 Ha & Schmidhuber（2018）的经典论文中被正式定义和系统化。

**截至 2026 年 2 月，世界模型研究已经历三次范式跃迁：**

| 阶段 | 时间 | 代表工作 | 核心特征 |
|------|------|---------|---------|
| **1.0 时代** | 1989–2022 | Schmidhuber (1989)、Ha & Schmidhuber (2018)、PlaNet、Dreamer 系列、[MuZero](https://arxiv.org/abs/1911.08265) | 任务特定的 RL 世界模型，在潜在空间中学习环境动力学 |
| **2.0 时代** | 2023–2024 | [Sora](https://openai.com/index/video-generation-models-as-world-simulators/)、[Genie](https://arxiv.org/abs/2402.15391)、[DreamerV3](https://arxiv.org/abs/2301.04104)、[GAIA-1](https://arxiv.org/abs/2309.17080) | 基础世界模型（Foundation World Model），在互联网规模的视频数据上训练，涌现出世界模拟能力 |
| **3.0 时代** | 2025– | [NVIDIA Cosmos](https://arxiv.org/abs/2501.03575)、[Genie 3](https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/)、[Sora 2](https://openai.com/blog/sora-2)、[VideoWorld](https://arxiv.org/abs/2501.09781)、[Aether](https://arxiv.org/abs/2503.18945)、[DreamZero](https://arxiv.org/abs/2602.15922) | 开源世界模型平台、实时交互式生成、3D/4D 几何感知、VLA+WM 融合、具身 AI 世界模型训练 |

**六大标志性事件定义了当前格局：**

1. **OpenAI Sora / Sora 2（2024.2 → 2025.9）**：证明扩展视频扩散 Transformer 可以涌现出 3D 一致性、物体持久性、基础物理等世界模拟能力；Sora 2 大幅提升物理精度并支持多镜头复杂指令和逼真音频。

2. **Google DeepMind Genie 1→2→3（2024.2 → 2024.12 → 2025.8）**：实现了从单张图片生成动作可控的交互式 3D 世界；Genie 3 成为**首个实时交互世界模型**（24fps/720p），标志着世界模型的新前沿。

3. **NVIDIA Cosmos 平台（2025.1–）**：发布了首个面向"物理 AI"（机器人、自动驾驶）的开源世界基础模型平台（13 个仓库，Apache-2.0），后续推出 Predict 2.5、Reason1、Transfer1、Drive-Dreams 等升级。

4. **具身 AI 世界模型爆发（2025–2026）**：[DreamZero](https://arxiv.org/abs/2602.15922)（14B 参数世界动作模型，7Hz 实时闭环控制）、[World-Gymnast](https://arxiv.org/abs/2602.02454)（在世界模型中 RL 微调 VLA，比 SFT 提升 18×）、[FLARE](https://arxiv.org/abs/2505.15659)（隐式世界模型，近零推理开销）等工作将"在世界模型中训练机器人策略"从理论推向实践，VLA + World Model 融合成为主流范式。

5. **视频基座模型全球竞争（2024–2025）**：智谱（[CogVideoX](https://arxiv.org/abs/2408.06072)，ICLR 2025）、腾讯（[HunyuanVideo](https://arxiv.org/abs/2412.03603)，130 亿参数）、阿里（[Wan2.1](https://arxiv.org/abs/2503.20314) [![Stars](https://img.shields.io/github/stars/Wan-Video/Wan2.1?style=social)](https://github.com/Wan-Video/Wan2.1)）、昆仑万维（[SkyReels-V2](https://arxiv.org/abs/2504.13074)，VBench SOTA 83.9%）、字节（Seedance）、快手（可灵）、阶跃星辰（[Step-Video](https://arxiv.org/abs/2502.10248)，300 亿参数）等与 OpenAI、NVIDIA、Google DeepMind 形成全球多极竞争格局，且正从视频生成向世界模型方向系统性转型。

6. **JEPA 理论路线的持续推进（2022–2025）**：Yann LeCun 的 [JEPA](https://openreview.net/forum?id=BZ5a1r-kVsf)（联合嵌入预测架构）提供了一条截然不同的理论路径——在抽象表征空间中预测而非在像素空间中生成；[V-JEPA 2](https://arxiv.org/abs/2506.09985) 实现理解、预测与规划的统一，V-JEPA 2-AC 将其扩展到具身控制。

**当前最活跃的五个交叉前沿：**
1. **世界模型 × 具身 AI** → 机器人在想象中学习（DreamZero、World-Gymnast、FLARE、UWM）← **2026 年最活跃方向**
2. **世界模型 × 视频生成** → 世界模拟器（Sora 2、Genie 3、Cosmos、Causal-Forcing）
3. **世界模型 × 自动驾驶** → 仿真数据 + 端到端规划（GAIA-3、Vista、Cosmos-Drive-Dreams）
4. **世界模型 × LLM Agent** → Agent 规划与推理（Affordances、WebDreamer、WALL-E 2.0）
5. **世界模型 × 3D/4D 生成** → 可交互虚拟世界（HunyuanWorld、WorldGen、OmniWorld）

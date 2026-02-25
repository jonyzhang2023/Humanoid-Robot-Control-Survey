---
outline: deep
---

# 方向四：具身 AI 世界模型

### 7.1 方向概述

具身 AI 是 **2026 年世界模型研究最活跃的方向**（占全部论文约 30%）。核心目标是为机器人操作、导航、运动控制构建世界模型，实现在想象中学习和规划。2025–2026 年，**VLA（Vision-Language-Action）与世界模型的深度融合**成为最重要的技术趋势，多个重量级工作验证了"在世界模型中训练机器人策略"的可行性。

> 📖 最新综述 [World Models for Embodied AI](https://arxiv.org/abs/2510.16732) 系统梳理了具身场景下的世界模型技术路线。[Robotic Manipulation World Models](https://arxiv.org/abs/2511.02097) 专注于机器人操作的世界模型研究。[Video in Robotic Manipulation](https://arxiv.org/abs/2601.07823) 则从视频预测角度审视了机器人操作中的视频世界模型。

### 7.2 关键论文深度解析

#### 7.2.1 DreamZero — 世界模型即策略

| 项目 | 内容 |
|------|------|
| **论文** | [*DreamZero: World Action Models are Zero-shot Policies*](https://arxiv.org/abs/2602.15922) |
| **机构** | Google DeepMind |
| **日期** | 2026.02 |

**方法**：14B 参数视频扩散模型（World Action Model, WAM）基于 Wan2.1-I2V 骨干，联合建模视频和动作，作为 zero-shot 策略直接输出机器人动作。

**训练数据策略**：
- **500 小时**异构遥操作数据，覆盖 **22 种环境**
- 平均每个 episode 包含 **42 个子任务**
- 核心哲学：**"多样性 > 重复性"**——更多不同场景比同一场景重复采集更有价值
- DROID-Franka 子集交叉验证了该数据哲学的有效性

**推理加速**：从朴素推理 5.7 秒加速到 **150ms**（**38× 提速**），技术栈包括：
- CFG 并行化
- DiT 缓存（Cache）
- torch.compile 优化
- NVFP4 量化
- Flash 解耦噪声

**核心突破**：
- **世界模型本身就是策略**——不需要额外的策略网络
- **7Hz 实时闭环控制**（150ms/帧）
- 泛化能力比 SOTA VLA 提升 **2× 以上**（已见任务 62.2% vs VLA 最优 27.4%，未见任务 39.5% vs 16.3%）
- 仅需 **10–20 分钟视频**即可跨具身形态迁移
- **关键洞见**：失败的标志是视频预测质量下降——"如果世界模型预测的画面变模糊，说明策略错了"
- **缩放效应**：14B >> 5B；VLA 在同等数据下完全失败（0%）

#### 7.2.2 FLARE — 隐式世界模型

| 项目 | 内容 |
|------|------|
| **论文** | [*FLARE: Implicit World Models for Robotic Learning*](https://arxiv.org/abs/2505.15659) |
| **机构** | NVIDIA，集成 Isaac GR00T |
| **日期** | 2025.05 |

**核心洞见**：世界模型不一定要显式生成未来，只需让策略网络"隐式地预测未来"就能大幅提升性能。

**架构细节**：
- 在扩散 Transformer 中添加 **32 个未来预测 token**
- **Q-former** 压缩未来观测为紧凑嵌入
- 在**第 6/8 层**对齐特征，损失权重 **λ=0.2**，EMA 目标网络 **τ=0.995**
- 约 **3000 小时**跨具身跨任务数据，在 **256 块 H100** 上预训练

**成果**：
- 模拟环境：24 个 RoboCasa 任务提升 **26%** 至 **70.1%**，**近零推理开销**
- **真实机器人**：GR-1 人形机器人达到 **95.1% 成功率**（每任务 100 条轨迹）
- **Few-shot 泛化**：1 条真实演示 + 人类视频 → **60% 成功率**；10 条演示 → **80%**
- 是实用性最强的世界模型增强方法之一

> 🔍 **DreamZero vs FLARE 范式光谱**：DreamZero（显式 WAM，14B 参数，150ms/帧）和 FLARE（隐式预测，近零开销）代表了"重量级 vs 轻量级"两个极端。DreamZero 追求最大泛化能力，FLARE 追求最小推理成本。二者互补，适用于不同部署场景。

#### 7.2.3 V-JEPA 2-AC — 表征空间的具身控制

| 项目 | 内容 |
|------|------|
| **论文** | [*V-JEPA 2: Self-Supervised Video Model for Understanding, Prediction and Planning*](https://arxiv.org/abs/2506.09985) |
| **机构** | Meta AI |
| **日期** | 2025.06 |

V-JEPA 2 系列的 Action-Conditioned 变体将 JEPA 的表征空间预测扩展到具身控制场景。在表示空间（而非像素空间）进行预测和规划，实现了理解、预测与规划的统一。

### 7.3 VLA + World Model 融合：五大范式

VLA 与世界模型的融合是 2025–2026 年最重要的技术趋势。当前已形成五种成熟范式：

#### 范式 1：世界模型作为 RL 模拟器

在动作条件视频世界模型中对 VLA 做 RL 微调，VLM 提供奖励信号。

| 工作 | 方法 | 效果 |
|------|------|------|
| [**World-Gymnast**](https://arxiv.org/abs/2602.02454) | 视频 WM 中 RL 微调 VLA，VLM 奖励 | **比 SFT 提升 18×，比模拟器提升 2×** |
| [GigaBrain-0.5M](https://arxiv.org/abs/2602.12099) | RAMP（RL via World Model）优化 VLA | 操控任务提升约 30% |

#### 范式 2：VLA 与世界模型迭代共进化

VLA 策略与世界模型交替迭代训练，双方同时改进。

| 工作 | 方法 | 效果 |
|------|------|------|
| [**VLAW**](https://arxiv.org/abs/2602.12063) | VLA 与 WM 交替迭代训练 | 绝对性能提升 **+39.2%** |
| [World-VLA-Loop](https://arxiv.org/abs/2602.06508) | 视频 WM 与 VLA 闭环学习 | 双方同时改进 |

#### 范式 3：隐式世界模型增强 VLA

不显式生成未来，通过辅助损失对齐未来表征（仅训练时使用）。

| 工作 | 方法 | 效果 |
|------|------|------|
| [**FLARE**](https://arxiv.org/abs/2505.15659) | 扩散 Transformer + 少量预测 token | **提升 26%，近零推理开销** |
| [VLA-JEPA](https://arxiv.org/abs/2602.10098) | 潜在世界模型增强 VLA | 超越基线 |

#### 范式 4：统一世界-动作模型（WAM）

视频扩散骨干联合建模视频预测和动作预测。

| 工作 | 方法 | 效果 |
|------|------|------|
| [**DreamZero**](https://arxiv.org/abs/2602.15922) | 14B WAM 联合建模视频+动作 | **泛化 2×+，30min 数据跨具身迁移** |
| [UWM](https://arxiv.org/abs/2504.02792) | 统一 Transformer 中视频+动作扩散 | 支持有/无动作标注混合训练 |

#### 范式 5：潜在动作预训练

从互联网视频（无动作标签）中学习潜在动作表示，再微调到真实动作。

| 工作 | 方法 | 效果 |
|------|------|------|
| [**LAPA**](https://arxiv.org/abs/2410.11758) | VQ-VAE 从视频提取潜在动作 | **超越有真实动作标签训练的 SOTA VLA**（ICLR 2025） |
| [Motus](https://github.com/thu-ml/Motus) | 统一潜在动作世界模型 | 无需动作标签的通用预训练 |

### 7.4 数据范式变革：从"重复采集"到"多样性优先"

具身 AI 世界模型的数据策略正在经历根本性转变：

| 数据范式 | 代表工作 | 核心思想 | 规模 |
|---------|---------|---------|------|
| **互联网视频 → 潜在动作** | LAPA、Motus | 从无动作标签的人类视频中学习潜在动作表示 | 仅 **272 H100-hours**（vs OpenVLA 21,500 A100-hours，**30–40× 效率**） |
| **异构遥操作** | DreamZero | "多样性 > 重复性"，22 种环境、42 子任务/episode | 500 小时 |
| **跨具身预训练** | FLARE | 跨机器人形态的大规模统一预训练 | ~3000 小时，256×H100 |
| **模拟 + 少量真实** | World-Gymnast | 在视频 WM 中做 RL，少量真实数据微调 | — |

**关键洞察**：LAPA 证明纯人类视频预训练（无任何动作标签）即可超越 OpenVLA（50.1% vs 43.9%），这意味着**互联网视频的潜在价值远未被充分利用**。DreamZero 进一步验证了"多样性优先"数据哲学——14B 模型在 500 小时异构数据上训练，而 VLA 在同等数据上完全失败（0%），说明 WAM 架构本身具有更强的数据利用效率。

### 7.5 Sim-to-Real 定量对比

| 方法 | vs SFT 基线 | vs 软件模拟器 | 真实机器人成功率 | 备注 |
|------|-----------|-------------|---------------|------|
| **World-Gymnast** | **18×** | **2×** | — | 视频 WM 作为 RL 模拟器 |
| **DreamZero** | — | — | 已见 62.2%，未见 39.5% | VLA 最优仅 27.4% / 16.3% |
| **FLARE** | — | — | **95.1%**（GR-1） | 最高真实成功率 |
| **LAPA** | — | — | — | 超越 OpenVLA（50.1% vs 43.9%） |

> 🏆 World-Gymnast 的"18× vs SFT"和"2× vs 模拟器"是极强信号：视频世界模型作为 RL 环境比传统软件模拟器更有效。这验证了"在世界模型中训练策略"路线的商业可行性。

### 7.6 产业生态：关键玩家

#### NVIDIA 全栈布局

NVIDIA 在具身 AI × 世界模型领域构建了最完整的技术栈：

```
Cosmos（视频世界基座）→ FLARE（隐式 WM 增强）→ GR00T N1（人形策略）→ Isaac Sim（模拟环境）→ Jetson Thor（部署芯片）
```

这一"从训练到部署"的闭环布局使 NVIDIA 成为具身 AI 世界模型基础设施的事实标准。

#### 其他关键玩家

| 公司 | 代表工作/产品 | 方向 |
|------|-------------|------|
| **Google DeepMind** | DreamZero (WAM)、Genie 2 | 显式世界-动作模型 |
| **Physical Intelligence (π)** | [π₀](https://arxiv.org/abs/2410.24164) / π₀.5 | Flow Matching VLA，覆盖多种具身形态 |
| **Meta AI** | V-JEPA 2-AC | 表征空间具身控制 |
| **AgiBot** | DreamZero 合作平台 | 中国人形机器人硬件+数据平台 |
| **Figure AI** | Helix | 自回归 VLA + 世界建模 |
| **Tesla** | Optimus Gen 2 | 端到端视觉-动作（未公开 WM 细节） |

### 7.7 评估基准

具身 AI 世界模型的评估尚缺统一标准。当前主要基准：

| 基准 | 侧重 | 任务数 | 说明 |
|------|------|--------|------|
| **CALVIN** | 桌面操控，长程组合任务 | 34 | 最常用的语言条件操控基准 |
| **RLBench** | 多样化操控任务 | 100+ | 用于 RL 和模仿学习评估 |
| **SIMPLER** | 真实-模拟对齐 | — | 评估 Sim-to-Real 迁移效果 |
| **Bridge / DROID** | 真实机器人数据集 | — | Bridge v2 (60K demos)、DROID (76K demos) |
| **RoboCasa** | 家庭环境操控 | 24 | FLARE 使用的主要评估平台 |
| **RoboArena / PolaRiS** | 竞技评估 | — | 新兴的对战式评估框架 |

> ⚠️ 当前评估的关键缺陷：大部分基准只评估**单任务成功率**，缺乏对**泛化性**（未见任务/环境/具身形态）和**长程规划**能力的系统评估。DreamZero 提出的"已见 vs 未见"分离评估是更合理的范式。

### 7.8 前沿论文全景

| 论文 | 会议/时间 | 核心贡献 | 链接 |
|------|----------|---------|------|
| [DWL](https://arxiv.org/abs/2408.14472) | RSS 2024 最佳论文入围 | 去噪世界模型学习用于人形运动 | [arXiv](https://arxiv.org/abs/2408.14472) |
| [ManiGaussian](https://arxiv.org/abs/2403.08321) | 2024.03 | 高斯溅射用于多任务机器人操控 | [arXiv](https://arxiv.org/abs/2403.08321) |
| [AdaWorld](https://arxiv.org/abs/2503.18938) | 2025.03 | 带潜在动作的可适应世界模型 | [arXiv](https://arxiv.org/abs/2503.18938) |
| [Humanoid World Models](https://arxiv.org/abs/2506.01182) | 2025.06 | 开放世界人形机器人基础模型 | [arXiv](https://arxiv.org/abs/2506.01182) |
| [GWM](https://arxiv.org/abs/2508.17600) | ICCV 2025 | 可扩展高斯世界模型用于操控 | [arXiv](https://arxiv.org/abs/2508.17600) |
| [GigaBrain-0](https://arxiv.org/abs/2510.19430) | 2025.10 | 世界模型驱动的 VLA 策略学习 | [arXiv](https://arxiv.org/abs/2510.19430) |
| [PointWorld](https://arxiv.org/abs/2601.03782) | 2026.01 | 3D 点云世界模型用于真实世界机器人操控 | [arXiv](https://arxiv.org/abs/2601.03782) |
| [DreamDojo](https://arxiv.org/abs/2602.06949) | 2026.02 | 从大规模人类视频学习通用机器人世界模型 | [arXiv](https://arxiv.org/abs/2602.06949) |
| [RWM-U](https://arxiv.org/abs/2504.16680) | 2025.04 | 不确定性感知世界模型，真实四足/人形部署 | [arXiv](https://arxiv.org/abs/2504.16680) |
| [π₀](https://arxiv.org/abs/2410.24164) | RSS 2025 | Flow Matching VLA 基础模型，覆盖多种具身形态 | [arXiv](https://arxiv.org/abs/2410.24164) |
| [OpenVLA](https://arxiv.org/abs/2406.09246) | 2024.06 | 开源 7B VLA，7× 更少参数超越 RT-2-X | [arXiv](https://arxiv.org/abs/2406.09246) |

### 7.9 方向小结

| 特征 | 描述 |
|------|------|
| **优势** | 直接服务机器人部署、VLA+WM 融合趋势不可逆、互联网视频可作为免费训练数据（LAPA 验证） |
| **局限** | 长时域误差累积、实时推理（100Hz+）仍需攻克（DreamZero 7Hz 是当前上限）、跨形态迁移困难、评估标准碎片化 |
| **数据范式** | "多样性 > 重复性"（DreamZero）、互联网视频潜在动作（LAPA，30–40× 效率）、跨具身预训练（FLARE，3000h） |
| **趋势** | DreamZero 和 World-Gymnast 标志着"在世界模型中训练策略"从理论走向实践；NVIDIA 全栈布局（Cosmos→FLARE→GR00T→Isaac→Jetson）成为行业基础设施 |
| **代表方法** | DreamZero、FLARE、World-Gymnast、UWM、V-JEPA 2-AC、LAPA、π₀ |

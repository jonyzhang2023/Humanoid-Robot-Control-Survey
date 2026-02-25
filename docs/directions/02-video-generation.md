---
outline: deep
---

# 方向二：视频生成作为世界模拟

### 5.1 方向概述

2024 年 Sora 的发布标志着一个范式转换：**大规模视频生成模型本身就是世界模拟器**。这一路线主张，在互联网规模的视频数据上训练的扩散模型会涌现出对 3D 空间、物理规律、物体交互的理解。然而，这一命题也引发了最激烈的学术争议。批评方的核心论点包括：

1. **视觉逼真度 ≠ 物理理解**：模型可生成逼真画面但违反基本物理约束（[From Generative Engines to Actionable Simulators](https://arxiv.org/abs/2601.15533)）
2. **缺乏因果推理**：视频模型捕获的是统计相关性而非因果结构（[Simulating the Visual World: A Roadmap](https://arxiv.org/abs/2511.08585)）
3. **闭环评估缺失**：大多数视频模型只在开环（无交互）条件下评估，不足以证明世界理解能力

> 西方商业生态中，Runway Gen-3 Alpha、Luma Dream Machine、Pika 等闭源产品同样活跃，但因未发表学术论文，本报告侧重开源和有学术贡献的工作。

### 5.2 关键论文深度解析

#### 5.2.1 Sora 系列技术演进（2024–2025）

| 维度 | **Sora 1**（2024.02） | **Sora 2**（2025.09） |
|------|------|------|
| **架构** | 扩散 Transformer (DiT) + 时空 patch | 架构升级（细节未公开） |
| **核心创新** | 时空 patch 表示；可变分辨率/时长/宽高比；DALL·E 3 重标注 | 物理精度大幅提升（正确模拟碰撞反弹等）；多镜头复杂指令；逼真音频生成 |
| **涌现能力** | 3D 一致性、物体持久性、基础物理交互、零样本 Minecraft 模拟 | 精确物理模拟、"客串"功能、iOS 原生应用 |
| **局限** | 无法准确模拟玻璃破碎等复杂物理；空间混淆（左/右） | 部分复杂场景仍有伪影 |
| **开放性** | 闭源，仅技术报告 | 闭源，API + iOS 应用 |
| **关键意义** | 将"视频生成 = 世界模拟"推向学术前台 | 证明缩放效应可持续改善物理精度 |

**Sora 1 的学术影响**：将"视频生成模型是否可以成为世界模拟器"从学术假设提升为领域中心议题。缩放效应的证据（1×、4×、32× 计算量下质量显著提升）表明这是一条可行的路径。

#### 5.2.2 VideoWorld — 纯视频学习知识

| 项目 | 内容 |
|------|------|
| **论文** | [*VideoWorld: Exploring Knowledge Learning from Unlabeled Videos*](https://arxiv.org/abs/2501.09781) |
| **日期** | 2025.01 |
| **开源** | 代码、数据、模型全部开源 |

**核心发现**：
1. **纯视频训练**提供了足够信息来学习规则、推理和规划能力
2. 引入**潜在动力学模型（Latent Dynamics Model, LDM）**作为知识获取的核心组件
3. 仅 3 亿参数模型**从视频达到围棋五段水平**，无需搜索算法或奖励机制
4. 在机器人任务（CALVIN、RLBench）中有效学习多样控制操作

**意义**：为"视频预测模型就是真正的世界模型"提供了最强证据——它们能从纯视觉观察中学习规则、物理和策略。

### 5.3 前沿论文全景

| 论文 | 机构/时间 | 核心贡献 | 链接 |
|------|----------|---------|------|
| [WorldDreamer](https://arxiv.org/abs/2401.09985) | 清华/GigaAI, 2024.01 | 首个通用世界模型：遮蔽 token 预测统一 T2V/I2V/编辑 | [arXiv](https://arxiv.org/abs/2401.09985) |
| [LVM](https://arxiv.org/abs/2312.00785) | UC Berkeley, 2023.12 | 大视觉模型：4200 亿视觉 token 上 next-token 预测 | [arXiv](https://arxiv.org/abs/2312.00785) |
| [**CogVideoX**](https://arxiv.org/abs/2408.06072) | 智谱 AI/清华, ICLR 2025 | 3D VAE + Expert DiT，10 秒连续视频 | [GitHub](https://github.com/THUDM/CogVideo) [![Stars](https://img.shields.io/github/stars/THUDM/CogVideo?style=social)](https://github.com/THUDM/CogVideo) |
| [**HunyuanVideo**](https://arxiv.org/abs/2412.03603) | 腾讯, 2024.12 | 130 亿参数，双流→单流 DiT + MLLM 编码器 | [GitHub](https://github.com/Tencent/HunyuanVideo) [![Stars](https://img.shields.io/github/stars/Tencent/HunyuanVideo?style=social)](https://github.com/Tencent/HunyuanVideo) |
| [**Wan2.1**](https://arxiv.org/abs/2503.20314) | 阿里巴巴, 2025.03 | 14B 参数，VBench 83.7%，Wan-VAE 支持无限长度 1080P | [GitHub](https://github.com/Wan-Video/Wan2.1) [![Stars](https://img.shields.io/github/stars/Wan-Video/Wan2.1?style=social)](https://github.com/Wan-Video/Wan2.1) |
| [**Step-Video-T2V**](https://arxiv.org/abs/2502.10248) | 阶跃星辰, 2025.02 | 300 亿参数，首创 Video-DPO 对齐技术 | [GitHub](https://github.com/stepfun-ai/Step-Video-T2V) [![Stars](https://img.shields.io/github/stars/stepfun-ai/Step-Video-T2V?style=social)](https://github.com/stepfun-ai/Step-Video-T2V) |
| [**SkyReels-V2**](https://arxiv.org/abs/2504.13074) | 昆仑万维, 2025.04 | **首个开源 Diffusion Forcing 模型**，VBench SOTA 83.9% | [GitHub](https://github.com/SkyworkAI/SkyReels-V2) [![Stars](https://img.shields.io/github/stars/SkyworkAI/SkyReels-V2?style=social)](https://github.com/SkyworkAI/SkyReels-V2) |
| **Seedance 1.0→2.0** | 字节跳动 | 闭源；2.0 统一多模态架构，导演级控制 | 产品：即梦/豆包 |
| **可灵 Kling** | 快手 | 闭源；MVL 方法，中国市场占有率领先 | [klingai.com](https://klingai.com) |
| [AniSora](https://arxiv.org/abs/2412.10255) | 哔哩哔哩, 2024.12 | 首个动画视频生成系统，扩展到艺术/幻想世界模拟 | [GitHub](https://github.com/bilibili/Index-anisora) [![Stars](https://img.shields.io/github/stars/bilibili/Index-anisora?style=social)](https://github.com/bilibili/Index-anisora) |
| [Open-Sora](https://github.com/hpcaitech/Open-Sora) | 2024–2025 | 最大规模 Sora 开源复现，110 亿参数 v2.0 仅 $200K 训练成本 | [GitHub](https://github.com/hpcaitech/Open-Sora) [![Stars](https://img.shields.io/github/stars/hpcaitech/Open-Sora?style=social)](https://github.com/hpcaitech/Open-Sora) |
| [Open-Sora-Plan](https://github.com/PKU-YuanGroup/Open-Sora-Plan) | 北大, 2024 | 开源 Sora 复现，支持长视频生成 | [GitHub](https://github.com/PKU-YuanGroup/Open-Sora-Plan) [![Stars](https://img.shields.io/github/stars/PKU-YuanGroup/Open-Sora-Plan?style=social)](https://github.com/PKU-YuanGroup/Open-Sora-Plan) |
| [VideoReward / Flow-DPO](https://arxiv.org/abs/2501.13918) | 2025.01 | 视频生成的 RLHF 对齐：多维度奖励模型 + 流模型 DPO | [arXiv](https://arxiv.org/abs/2501.13918) |
| [Causal-Forcing](https://arxiv.org/abs/2602.02214) | 清华 thu-ml, 2026.02 | 自回归扩散蒸馏用于高质量实时交互视频生成 | [GitHub](https://github.com/thu-ml/Causal-Forcing) [![Stars](https://img.shields.io/github/stars/thu-ml/Causal-Forcing?style=social)](https://github.com/thu-ml/Causal-Forcing) |
| [Matrix-Game 2.0](https://arxiv.org/abs/2508.13009) | SkyworkAI, 2025 | 开源实时流式交互式世界模型 | [GitHub](https://github.com/SkyworkAI/Matrix-Game) [![Stars](https://img.shields.io/github/stars/SkyworkAI/Matrix-Game?style=social)](https://github.com/SkyworkAI/Matrix-Game) |
| [LongVie 2](https://arxiv.org/abs/2512.13604) | 2025.12 | 多模态可控超长视频世界模型 | [arXiv](https://arxiv.org/abs/2512.13604) |
| [LIVE](https://arxiv.org/abs/2602.03747) | 2026.02 | 长时交互式视频世界建模 | [arXiv](https://arxiv.org/abs/2602.03747) |
| [VerseCrafter](https://arxiv.org/abs/2601.05138) | TencentARC, 2026.01 | 动态真实视频世界模型 + 4D 几何控制 | [arXiv](https://arxiv.org/abs/2601.05138) |
| [Astra](https://arxiv.org/abs/2512.08931) | 2025.12 | 自回归去噪的通用交互世界模型 | [arXiv](https://arxiv.org/abs/2512.08931) |

### 5.4 开源 vs 闭源竞争格局：超越"开源碾压"叙事

#### 5.4.1 架构趋同：事实与边界

全球主要**开源**视频模型在架构上确已高度趋同——**DiT + 3D VAE + Flow Matching** 成为共识技术栈：

| 开源模型 | 架构 | 关键差异点 |
|---------|------|-----------|
| **Wan2.1** (阿里) | DiT + Flow Matching + Wan-VAE | Wan-VAE 支持无限长度 1080P |
| **CogVideoX** (智谱) | Expert DiT + 3D VAE | 专家 Transformer 路由 |
| **HunyuanVideo** (腾讯) | 双流→单流 DiT + FM + MLLM 编码器 | MLLM 替代 T5 作为文本编码器 |
| **SkyReels-V2** (昆仑万维) | DiT + FM + Diffusion Forcing + DPO | 首个开源 Diffusion Forcing + Video-DPO |

> ⚠️ **重要边界**：架构趋同仅限于**开源阵营可观察的范围**。闭源模型（Sora 2、Runway Gen-4、Kling O1、Luma Ray3、Pika 2.0）的架构均未公开，将闭源归入同一架构趋同叙事属于推测。

#### 5.4.2 开源 vs 闭源：量化对比

**自动化基准**（VBench 得分，越高越好）：

| 模型 | VBench 得分 | 类型 |
|------|-----------|------|
| **SkyReels-V2** | **83.9%** | 开源 |
| **Wan2.1** | **83.7%** | 开源 |
| HunyuanVideo | 82.7% | 开源 |

**人类评估**（SkyReels-Bench，1020 prompts，5 分制）：

| 任务 | 开源最优 | 得分 | 闭源最优 | 得分 | 结论 |
|------|---------|------|---------|------|------|
| **T2V**（文生视频） | SkyReels-V2 | **3.14** | Kling-1.6 | 2.99 | 🟢 **开源领先** |
| **I2V**（图生视频） | SkyReels-V2 | 3.29 | Runway Gen-4 / Kling Pro | **3.39–3.40** | 🔴 **闭源领先** |
| I2V 运动质量 | SkyReels-V2 | 2.93–3.01 | Runway / Kling | **3.37–3.41** | 🔴 **闭源显著领先** |

> 📊 数据来源：[SkyReels-V2 论文](https://arxiv.org/abs/2504.13074) 表 3/4。T2V 领域开源已超越闭源，但 I2V 尤其是运动质量方面闭源仍有明显优势。

#### 5.4.3 闭源阵营的真实护城河

将竞争简化为"开源碾压闭源"忽略了闭源产品的关键差异化优势：

| 维度 | 闭源优势 | 开源现状 |
|------|---------|---------|
| **训练数据** | 海量高质量私有数据（商业视频、用户生成内容）⭐⭐⭐⭐⭐ | 依赖公开数据集，质量和规模受限 |
| **I2V 运动质量** | 运动评分 3.37–3.41 ⭐⭐⭐⭐ | 运动评分 2.93–3.01，差距明显 |
| **商业功能** | HDR、V2V 编辑、角色参考、音频生成 ⭐⭐⭐⭐ | 多数功能缺失 |
| **后训练优化** | 大规模用户反馈 + DPO/RLHF ⭐⭐⭐⭐ | 开源 DPO 刚起步（SkyReels-V2、Step-Video） |
| **产品化** | 端到端 API + 应用（即梦、可灵 App）⭐⭐⭐ | 需自行部署 |

#### 5.4.4 真实差异化因素排序

架构趋同之后，竞争焦点转向以下维度（按重要性排序）：

| 排名 | 差异化因素 | 重要性 | 说明 |
|------|-----------|-------|------|
| 1 | **训练数据质量与规模** | ⭐⭐⭐⭐⭐ | 最终决定上限的核心壁垒 |
| 2 | **后训练策略（DPO/RL/RLHF）** | ⭐⭐⭐⭐ | Video-DPO（Step-Video）、Diffusion Forcing（SkyReels-V2）正在改变游戏规则 |
| 3 | **VAE 设计** | ⭐⭐⭐⭐ | Wan-VAE 无限长度 vs CogVideoX 3D VAE，决定视频质量下限 |
| 4 | **文本编码器** | ⭐⭐⭐ | MLLM（HunyuanVideo）vs T5，影响指令跟随精度 |
| 5 | **长视频/Diffusion Forcing** | ⭐⭐⭐ | 超越单 chunk 生成，迈向分钟级连贯视频 |

> 🔍 **LLM 轨迹类比**：视频生成领域的演化轨迹与 LLM 高度相似——架构趋同（Transformer）→ 开源追赶基础能力（Llama 系列）→ 竞争转向后训练与数据（RLHF/DPO）→ 差异化在生态与商业功能。当前视频生成正处于"竞争转向后训练"阶段。

### 5.5 方向小结

| 特征 | 描述 |
|------|------|
| **优势** | 视觉丰富、可利用互联网规模数据、涌现能力显著 |
| **局限** | 物理精度不足、缺乏动作条件化、计算成本极高 |
| **核心争议** | "视频生成 ≠ 世界理解"——视觉逼真度是世界理解的不可靠代理 |
| **趋势** | 从被动生成走向动作可控的交互式模拟；实时性成为新要求；RLHF 对齐技术迁入；T2V 开源已超越闭源，I2V 闭源仍领先 |
| **竞争格局** | 架构趋同（开源已确认，闭源未知）→ 竞争转向数据、后训练、VAE 和商业功能；与 LLM 演化轨迹高度相似 |
| **代表方法** | Sora 系列、VideoWorld、CogVideoX、HunyuanVideo、Wan2.1、SkyReels-V2 |

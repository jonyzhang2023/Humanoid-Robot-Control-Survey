---
outline: deep
---

# 全球企业与机构布局

### 13.1 科技巨头战略图谱

| 机构 | 代表成果 | 战略定位 | 关键特征 |
|------|---------|---------|---------|
| **NVIDIA** | [Cosmos](https://arxiv.org/abs/2501.03575)、Cosmos-Transfer1、Cosmos-Reason1 | 物理世界基础模型 + 数据飞轮 | 全栈布局：预训练→微调→部署；开源 Cosmos 系列；DGX 云服务闭环 |
| **Meta (FAIR)** | [V-JEPA 2](https://arxiv.org/abs/2412.04468)、V-JEPA 2-AC、JEPA 路线 | 非生成式世界理解 | LeCun 主导 JEPA 路线；不追求像素生成，聚焦语义预测；具身 AI 闭环 |
| **Google DeepMind** | [Genie 2](https://arxiv.org/abs/2501.18517)、[SIMA 2](https://arxiv.org/abs/2502.16399)、Dreamer V4 | 交互式环境模拟 | Genie 系列创造交互世界；SIMA 系列实现跨游戏通用智能体；强化学习基因 |
| **OpenAI** | Sora / Sora 2 | 视频生成定义者 | 首次将视频生成定义为"世界模拟器"；引爆行业关注；策略转向产品 |
| **Microsoft** | [WorldDreamer](https://arxiv.org/abs/2401.09985)、DIAMOND | 多模态 + 游戏 | 收购 Activision 后在游戏世界模型发力；DIAMOND 证明扩散模型可替代传统 RL 环境 |
| **腾讯** | [HunyuanVideo](https://arxiv.org/abs/2412.03603)、[HunyuanWorld](https://arxiv.org/abs/2501.12513) | 视频+3D 双线 | HunyuanVideo 开源高质量基座；HunyuanWorld 探索 3D 驾驶模拟；微信生态应用 |
| **字节跳动** | [Seedance](https://arxiv.org/abs/2503.07703)、SkyReels-V2、[AniSora](https://arxiv.org/abs/2412.10255) | 视频生成工厂 | Seedance 高一致性动画；SkyReels 无限时长；AniSora 动漫可控；抖音生态 |
| **阿里巴巴** | [Wan2.1](https://arxiv.org/abs/2503.20314)、[CogVideoX](https://arxiv.org/abs/2408.06072) | 开源视频生态 | Wan2.1 全面开源（1.3B–14B）；CogVideoX 全链路开源；通义系列 |
| **快手** | [Step-Video](https://arxiv.org/abs/2502.10248)、[Kling](https://klingai.kuaishou.com) | 长视频+物理一致 | Step-Video 步长自适应；Kling 实时物理模拟；快手 APP 内嵌 |
| **Wayve** | [GAIA-1/2/3](https://arxiv.org/abs/2309.17080) | 端到端自动驾驶 | GAIA 系列从规划到世界模型的全栈方案；伦敦路测；融资 $10.6 亿 |
| **1X Technologies** | [World Model for Humanoid Robot](https://arxiv.org/abs/2501.10100) | 人形机器人 | 世界模型驱动的人形机器人运动规划；实体部署；挪威独角兽 |
| **Runway** | Gen-3 Alpha | 创意视频工具 | 视频生成创业标杆；从工具走向平台；融资 $15 亿 |

### 13.2 核心学术机构

| 机构 | 代表方向 | 关键成果 |
|------|---------|---------|
| **UC Berkeley** | RL + 视频 | UniSim、Dreamer 系列合作、DIAMOND |
| **MIT** | 认知科学 + RL | MuZero 理论、认知世界模型 |
| **NYU (Yann LeCun 组)** | JEPA | I-JEPA、V-JEPA、IWM，JEPA 路线图的核心产出地 |
| **CMU** | 具身 AI | 多个 VLA+WM 融合工作 |
| **清华大学** | 多方向 | CogVideoX、AniSora、多个具身 AI 工作 |
| **北京大学** | 视频 + 3D | Aether、World3D 相关 |
| **上海 AI Lab** | 视频+驾驶 | DriveDreamer 系列、Vista |
| **Google Research / DeepMind** | 全方向 | Genie 系列、Dreamer 系列、SIMA 系列 |

### 13.3 视频基座模型架构趋同分析

2024–2025 年间，各机构的**开源**视频生成世界模型在架构选择上出现高度趋同，形成 **DiT + 3D VAE + Flow Matching** 的主流技术栈：

| 技术栈组件 | 选择 | 采用者 | 替代方案 |
|-----------|------|--------|---------|
| **骨干网络** | DiT (Diffusion Transformer) | Sora、HunyuanVideo、Wan2.1、Step-Video、SkyReels-V2、Seedance | U-Net (早期方案，已淡出) |
| **视频编码器** | 3D VAE / Causal 3D VAE | HunyuanVideo、CogVideoX、Wan2.1、COSMOS | 2D VAE + 时间层 (效率低) |
| **采样策略** | Flow Matching (Rectified Flow) | Wan2.1、SkyReels-V2、HunyuanVideo | DDPM/DDIM (步数多，效率低) |
| **文本编码器** | 双编码器 (CLIP + T5/LLM) | CogVideoX、Step-Video、Wan2.1 | 单 CLIP (语义不足) |
| **长度扩展** | 分块推理 / 滑窗 / 无限AR | SkyReels-V2、Kling、Wan2.1 | 全序列注意力 (显存爆炸) |

> ⚠️ **重要边界**：架构趋同仅限于**开源可观察的范围**。Sora 2、Runway Gen-4、Kling O1 等闭源模型的架构细节均未公开，将其归入同一趋同叙事属于推测。闭源阵营的真实护城河在于数据规模、后训练优化和商业功能（详见 §5.4）。

**趋同驱动力**：

1. **DiT 的可扩展性**：Transformer 架构天然适配大规模并行训练，scaling law 明确
2. **3D VAE 的时空压缩效率**：将视频从像素空间压缩到紧凑的潜在空间，减少 $16 \times$ 以上计算量
3. **Flow Matching 的采样效率**：直线传输路径使 4–8 步采样即可达到高质量，远优于 DDPM 的 50–1000 步
4. **训练稳定性**：三者组合在大规模训练中表现出更好的梯度行为和收敛特性

### 13.4 全球竞争格局分析

**三大阵营**：

1. **北美 — 技术定义者**：OpenAI（产品化路线）、NVIDIA（全栈基座）、Meta（非生成路线）、Google（交互智能体）
2. **中国 — 开源追赶者**：腾讯/阿里/字节/快手在视频生成领域快速跟进并大规模开源，形成独特的"大厂+开源"模式。上海 AI Lab、清华等在自动驾驶和具身 AI 方向领先
3. **欧洲 — 垂直深耕者**：Wayve（自动驾驶）、1X（人形机器人）、NNAISENSE（工业 RL）在细分场景深度积累

**竞争趋势**：
- 视频生成方向架构趋同后竞争转向数据质量、后训练策略和商业功能（T2V 开源已领先，I2V 闭源仍有优势）
- 具身 AI 方向成为新高地，NVIDIA（FLARE + GR00T 全栈）、Google DeepMind（DreamZero）投入最大
- 3D/4D 方向 World Labs（Fei-Fei Li 创立）和腾讯 HunyuanWorld 系列形成最活跃生态
- 自动驾驶方向由 Wayve、NVIDIA、上海 AI Lab 三足鼎立
- 开源力度加大：中国大厂和 NVIDIA 主导开源浪潮

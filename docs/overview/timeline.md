---
outline: deep
---

# 发展历程与里程碑时间线

> 下方可视化时间线图涵盖了世界模型从 1943 年认知科学奠基到 2026 年基础世界模型时代的全部关键里程碑，按 9 个研究方向着色。点击图片可放大查看。

<a href="/world-model-survey/timeline.svg" target="_blank" rel="noopener">

![世界模型发展历程时间线](/timeline.svg)

</a>

---

### 3.1 早期奠基（1943–2017）

| 年份 | 工作 | 作者/机构 | 贡献 |
|------|------|----------|------|
| 1943 | *The Nature of Explanation* | Kenneth Craik | **认知科学奠基**——首次提出"心智模型"概念：人脑构建外部世界的"小比例模型"来预测事件 |
| 1989 | *Making the World Differentiable* | Schmidhuber | **AI 奠基之作**——首次提出用 RNN 学习环境模型，使控制器可以通过世界模型的梯度学习 |
| 2011 | [PILCO](https://arxiv.org/abs/1102.0283) | Deisenroth & Rasmussen | 用高斯过程建模环境动力学，实现高样本效率的模型基强化学习 |
| 2015 | *On Learning to Think* | Schmidhuber | 统一框架：RNN 同时充当世界模型和控制器，提出"在想象中思考"的范式 |
| 2016 | [The Predictron](https://arxiv.org/abs/1612.08810) | Silver 等（DeepMind） | 将学习到的 MDP 模型集成到价值函数预测中 |
| 2017 | [Imagination-Augmented Agents](https://arxiv.org/abs/1707.06203) (I2A) | Weber 等（DeepMind） | 利用学习到的环境模型增强无模型智能体的想象力 |

### 3.2 经典世界模型时代（2018–2022）

| 年份 | 工作 | 作者/机构 | 贡献 |
|------|------|----------|------|
| 2018 | [**World Models**](https://arxiv.org/abs/1803.10122) ⭐ | Ha & Schmidhuber（Google Brain / NNAISENSE） | **里程碑论文**：提出 VAE + MDN-RNN + Controller (V-M-C) 三组件架构；首次实现在学习到的"梦境"中训练策略并迁移到真实环境 |
| 2019 | [PlaNet](https://arxiv.org/abs/1811.04551) | Hafner 等（DeepMind） | 纯粹在潜在空间中进行规划的模型基 RL，无需重建观测 |
| 2020 | [DreamerV1](https://arxiv.org/abs/1912.01603) | Hafner 等 | 在学习到的世界模型中使用 Actor-Critic 进行行为学习 |
| 2020 | [**MuZero**](https://arxiv.org/abs/1911.08265) | Schrittwieser 等（DeepMind） | **Nature 2020**：学习模型无需环境规则，统治棋类与 Atari，验证世界模型+规划搜索的威力 |
| 2021 | [DreamerV2](https://arxiv.org/abs/2010.02193) | Hafner 等 | 引入离散表征（categorical representations），在 Atari 上达到人类水平 |
| 2022 | [**LeCun 立场论文**](https://openreview.net/forum?id=BZ5a1r-kVsf) ⭐ | Yann LeCun（Meta AI） | 提出 **JEPA** 架构作为世界模型的核心范式：在抽象表征空间中预测，而非在像素空间中生成 |
| 2022 | [MILE](https://arxiv.org/abs/2210.07729) | Hu 等 | **NeurIPS 2022**：首个基于模型的模仿学习用于城市自动驾驶 |

### 3.3 基础世界模型时代（2023–2026）

| 日期 | 工作 | 机构 | 贡献 |
|------|------|------|------|
| 2023.01 | [**I-JEPA**](https://arxiv.org/abs/2301.08243) | Meta AI | **ICCV 2023**：图像 JEPA——通过预测遮蔽区域的表征（而非像素）实现自监督学习 |
| 2023.01 | [**DreamerV3**](https://arxiv.org/abs/2301.04104) ⭐ | Hafner 等 | 通用世界模型 RL 智能体：单一配置跨 150+ 任务；首个在 Minecraft 中从零收集钻石的算法；**2025 年发表于 Nature** |
| 2023.01 | [**Othello-GPT**](https://arxiv.org/abs/2210.13382) ⭐ | Li 等 | **ICLR 2023 Top 5%**：GPT 在棋步序列上训练后涌现出因果性棋盘状态表征——序列模型内部隐含世界模型的里程碑证据 |
| 2023.02 | [**IRIS**](https://arxiv.org/abs/2209.00588) | Micheli 等 | **ICLR 2023 Top 5%**：Transformer 作为采样高效世界模型，离散 token 化方法影响了 Genie 系列 |
| 2023.05 | [**RAP**](https://arxiv.org/abs/2305.14992) | Hao 等 | **EMNLP 2023**：将 LLM 同时用作世界模型和智能体，结合 MCTS 实现规划。LLaMA-33B+RAP 超越 GPT-4+CoT 33% |
| 2023.09 | [**GAIA-1**](https://arxiv.org/abs/2309.17080) ⭐ | Wayve | 90 亿参数自动驾驶世界模型；证明视频世界模型遵循类似 LLM 的幂律缩放定律 |
| 2023.10 | [**UniSim**](https://arxiv.org/abs/2310.06114) ⭐ | DeepMind / Berkeley / MIT | 通用交互式真实世界模拟器；训练的 RL 和 VL 策略可零样本部署到真实世界 |
| 2023.10 | [**TD-MPC2**](https://arxiv.org/abs/2310.16828) | UC San Diego | **ICLR 2024**：隐式世界模型；单个 3.17 亿参数智能体跨 80 个任务 |
| 2023.10 | [LLM 表征空间与时间](https://arxiv.org/abs/2310.02207) | Gurnee & Tegmark（MIT） | Llama-2 内部学习到了空间坐标和时间信息的线性表征 |
| 2023.11 | [**Copilot4D**](https://arxiv.org/abs/2311.01017) | Waabi / 多伦多大学 | **ICLR 2024**：LiDAR 点云世界模型（VQVAE + 离散扩散），比 SOTA 提升 65%+ |
| 2023.12 | [**LAW 框架**](https://arxiv.org/abs/2312.05230) | Hu & Shu | **NeurIPS 2023 Tutorial**：语言模型(L)、智能体模型(A)、世界模型(W) 三位一体框架 |
| 2024.01 | [WorldDreamer](https://arxiv.org/abs/2401.09985) | 清华 / GigaAI | 首个通用世界模型：通过遮蔽 token 预测统一文本到视频、图像到视频、视频编辑 |
| 2024.02 | [**Sora**](https://openai.com/index/video-generation-models-as-world-simulators/) ⭐ | OpenAI | 扩散 Transformer + 时空 patch：涌现出 3D 一致性、物体持久性、物理交互能力。明确提出"视频生成模型即世界模拟器" |
| 2024.02 | [**Genie 1**](https://arxiv.org/abs/2402.15391) ⭐ | Google DeepMind | 110 亿参数交互式环境生成器：从无标注视频中无监督学习，自动发现潜在动作空间 |
| 2024.02 | [**V-JEPA**](https://arxiv.org/abs/2404.08471) | Meta AI | 视频 JEPA：在抽象空间预测遮蔽视频区域，训练效率提升 1.5-6 倍 |
| 2024.05 | [**DIAMOND**](https://arxiv.org/abs/2405.12399) ⭐ | Alonso 等 | **NeurIPS 2024 Spotlight**：首个基于扩散的世界模型用于 RL，Atari 100k 达到 1.46 HNS 新 SOTA |
| 2024.05 | [**Vista**](https://arxiv.org/abs/2405.17398) | HKUST / 图宾根大学 | **NeurIPS 2024**：驾驶世界模型 SOTA，FID 改善 55%，首次实现自监督驾驶奖励 |
| 2024.08 | [**GameNGen**](https://arxiv.org/abs/2408.14837) ⭐ | Google | **ICLR 2025**：扩散模型作为实时游戏引擎，在 DOOM 中实现 20fps 实时交互 |
| 2024.08 | [**CogVideoX**](https://arxiv.org/abs/2408.06072) | 智谱 AI / 清华 | **ICLR 2025**：3D VAE + Expert DiT，首个被顶会录取的视频生成模型之一 |
| 2024.10 | [**Oasis**](https://oasis-model.github.io/) ⭐ | Decart / Etched | 纯 Transformer 实时开放世界模拟（类 Minecraft），20fps，500M 模型开源 |
| 2024.12 | [**Genie 2**](https://deepmind.google/discover/blog/genie-2-a-large-scale-foundation-world-model/) ⭐ | Google DeepMind | 基础世界模型：从单张图片生成丰富 3D 世界，含 NPC、物理、最长 1 分钟一致性 |
| 2024.12 | [**HunyuanVideo**](https://arxiv.org/abs/2412.03603) | 腾讯 | 130 亿+ 参数，最大开源视频模型；双流→单流 DiT + MLLM 编码器 |
| 2025.01 | [**NVIDIA Cosmos**](https://arxiv.org/abs/2501.03575) ⭐ | NVIDIA | 首个开源世界基础模型平台：13 个代码仓库，完整物理 AI 管线（Apache-2.0） |
| 2025.01 | [**VideoWorld**](https://arxiv.org/abs/2501.09781) ⭐ | Ren 等 | 纯视频学习知识：3 亿参数模型仅从视频达到围棋五段水平，无需搜索或奖励 |
| 2025.02 | [**Step-Video-T2V**](https://arxiv.org/abs/2502.10248) | 阶跃星辰 | 300 亿参数，首创 Video-DPO 对齐技术 |
| 2025.03 | [**Wan2.1**](https://arxiv.org/abs/2503.20314) | 阿里巴巴 | 14B 参数，VBench 83.7%，Wan-VAE 支持无限长度 1080P [![Stars](https://img.shields.io/github/stars/Wan-Video/Wan2.1?style=social)](https://github.com/Wan-Video/Wan2.1) |
| 2025.03 | [**GAIA-2**](https://arxiv.org/abs/2503.20523) | Wayve | 可控多视角生成世界模型 |
| 2025.04 | [**SkyReels-V2**](https://arxiv.org/abs/2504.13074) | 昆仑万维 | **首个开源 Diffusion Forcing 模型**，VBench SOTA 83.9%，无限长度视频 |
| 2025.05 | [**FLARE**](https://arxiv.org/abs/2505.15659) | NVIDIA | 隐式世界模型用于机器人学习，集成 Isaac GR00T，近零推理开销提升 26% |
| 2025.06 | [**V-JEPA 2**](https://arxiv.org/abs/2506.09985) | Meta AI | 自监督视频模型实现理解、预测和规划的统一；V-JEPA 2-AC 扩展到具身控制 |
| 2025.06 | [**Cosmos-Drive-Dreams**](https://arxiv.org/abs/2506.09042) | NVIDIA | 可扩展合成驾驶数据生成 |
| 2025.07 | [**HunyuanWorld 1.0**](https://arxiv.org/abs/2507.21809) | 腾讯 | 从文字/图像生成沉浸式可探索交互 3D 世界 |
| 2025.08 | [**Genie 3**](https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/) ⭐ | Google DeepMind | **首个实时交互世界模型**：24fps/720p 生成逼真可交互 3D 世界 |
| 2025.09 | [**Sora 2**](https://openai.com/blog/sora-2) ⭐ | OpenAI | 物理精度大幅提升，多镜头复杂指令，逼真音频生成，iOS 应用 |
| 2025.09 | [**Dreamer4**](https://arxiv.org/abs/2509.24527) | Hafner | 可扩展的世界模型内训练智能体 |
| 2025.10 | [**GAIA-3**](https://wayve.ai/thinking/gaia-3/) | Wayve | 15B 参数驾驶世界模型，9 国 3 大洲数据，5× 计算 10× 数据 |
| 2025.10 | [**Aether**](https://arxiv.org/abs/2503.18945) | InternRobotics | **ICCV 2025 杰出论文 & RIWM Outstanding Paper**：几何感知的统一世界建模 |
| 2025.11 | [**SIMA 2**](https://deepmind.google/blog/sima-2-an-agent-that-plays-reasons-and-learns-with-you-in-virtual-3d-worlds/) | Google DeepMind | Gemini 驱动的通用 3D 虚拟世界智能体，适配 Genie 3 世界 |
| 2026.02 | [**DreamZero**](https://arxiv.org/abs/2602.15922) | Google DeepMind | 14B 视频扩散世界动作模型，7Hz 实时闭环控制，泛化比 SOTA VLA 提升 2×+ |
| 2026.02 | [**World-Gymnast**](https://arxiv.org/abs/2602.02454) | Stanford | 在视频世界模型中对 VLA 做 RL 微调，比 SFT 提升 18× |
| 2026.02 | 研究爆发期 | — | 仅 2026 年前两月，arXiv 上 World Model 相关论文已超百篇 |

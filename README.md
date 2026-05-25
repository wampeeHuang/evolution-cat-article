# 进化猫 · 公众号文章写作

> 10 步长文生产管线 — 从选题到配图，全流程编排。核心原则：线索 → 6 维搜索 + Burke 跨域类比 → 撞到意外 → 那才是真正的选题。没有意外 = 杀稿。

## 这是谁的工具？

为 **需要稳定产出深度长文的创作者** 设计。如果你：
- 写 2000+ 字公众号文章，需要研究方法论驱动的内容生产
- 受够了"AI 味儿"——需要系统化的去 AI 味流程和机械质检
- 做"进化猫"品牌内容——需要统一的写作 DNA 和风格门禁

那这是你的工具。写短文、朋友圈、纯娱乐内容 → 不适用。

## 30 秒跑起来

```
克隆到 Claude Code skills 目录。
触发词：写进化猫文章 / 写公众号文章 / 进化猫选题写作 / 把选题写成文章
```

Agent 自动加载 production-sop.md → 从飞书选题库拉选题 → 6 维搜索 → 杀稿门禁 → 创意会 → 双门禁 → 写作 → 去 AI 味 → 质检 → 配图。

## 核心设计：骨架层 + 血肉层分离

```
references/
├── skeleton/          ← 骨架层：质量基线，开源通用，不可通过 retro 修改
│   ├── fact-check.md       事实校验 + 数字核验
│   ├── source-trace.md     6 维度搜索 + 素材包 + 追溯
│   ├── honesty-gate.md     三跑道门禁 + 5 种节奏原型
│   ├── density-gate.md     开头门禁 + 硬指标 + 术语降维 + 禁止词库
│   └── structure-gate.md   角度自检 + 清晰度 + 活人感检查
├── flesh/             ← 血肉层：风格生长，可 retro 优化
│   ├── voice-signals.md    ≤20 条风格信号
│   ├── hard-preferences.md ≤5 条硬偏好
│   └── avoid-list.md       ≤10 条回避项
├── production-sop.md  ← 生产指令
├── humanizer-zh.md    ← 去 AI 味（24 种模式检测）
├── final-review.md    ← 机械质检（5 项）+ 编辑判断（双签）
└── image-generation.md← 配图生成
```

**为什么分开**：骨架是质量地板——改了可能破坏整条流水线的质量基线。血肉是风格天花板——生产越多越精准。

## 生产流水线

```
搜索 → 意外发现暂停(杀稿门禁) → 创意会(Beast+Karpathy 双跑道)
→ PG+Feynman 双门禁 → Tim 开头+Sugarman 全文 → 机械初审
→ 去 AI 味(24 模式检测) → 机械质检(5 项) → 编辑判断(BS+PG 双签) ⏸
→ 配图 → 可选复盘
```

**杀稿门禁**：搜索后无意外发现 → 终止。不写"已知结论的扩写"。

**双门禁系统**：
- PG 门禁（Paul Graham）：每个段落是否承载了新信息？砍掉不承载新信息的段落
- Feynman 门禁：大一新生能懂吗？术语降维了吗？

**去 AI 味**：24 种 AI 写作模式检测（"总而言之"、虚假转折、平均主义段落长度……）

## 风格触发

Agent 自动匹配 5 种节奏原型之一（费曼式 / Karpathy 式 / PG 式 / 匕首式 / 编织式），取决于选题类型和内容调性。

## 前置条件

飞书选题库中必须有状态 = `已入选` 的选题。无 → 终止。

## 输出路径

```
D:/HHH/自媒体/进化猫/AI/{YYYYMMDD}_{标题}/
├── article.md        # 正文
├── cover.png         # 封面图
└── image_*.png       # 配图 ≥2 张
```

## 目录结构

```
evolution-cat-article/
├── SKILL.md                    # Skill 入口：触发条件 + 10 步流程
├── README.md                   # 本文件
├── references/
│   ├── production-sop.md       # 分步生产指令
│   ├── humanizer-zh.md         # 去 AI 味（24 种模式）
│   ├── final-review.md         # 机械质检（5a）+ 编辑判断（5b）
│   ├── image-generation.md     # 配图生成
│   ├── self-audit.md           # 工匠框架自审计
│   ├── system-diagram.html     # 流水线可视化
│   ├── skeleton/               # 骨架层（5 个门禁文件）
│   └── flesh/                  # 血肉层（3 个风格文件）
└── examples/                   # 输出案例
```

## 部署（Agent 自部署指令）

```bash
git clone https://github.com/wampeeHuang/evolution-cat-article.git
# 放到 Claude Code skills 目录
# 触发词见上。纯文本 reference 文件，零运行时依赖。
```

**依赖**：无。所有 reference 为 Markdown。配图生成需 AI 图像 API（aigoapi/gpt-image-2），密钥通过环境变量注入，不进仓库。

## 设计哲学

**没有意外 = 杀稿。** 这是整条流水线最根本的价值观。不是"写得好不好"——是"有没有新信息"。6 维搜索的目的不是收集素材，是撞到意外。撞不到意外说明这个选题不值得写。

**骨架/血肉分离。** 骨架层（skeleton/）是质量地板，开源通用，不可通过复盘修改。血肉层（flesh/）是风格天花板，每篇文章复盘后生长。同一套骨架可以被多个品牌复用，只需各维护自己的血肉层。这解决了开源 Skill 的核心矛盾：如何既分享方法论又不暴露品牌指纹。

**两道杀稿门禁。** Step 1.5 "搜索后无意外则杀"是第一道；Step 5b "BS+PG 双签"是第二道，预期杀稿率 30-40%。不是每篇选题都值得写成文章——不发一篇烂文章胜过发十篇平庸文章。

**spawn 子 agent 架构。** 创意会的 Beast + Karpathy 双跑道、事实校验的独立验证、去 AI 味的 24 模式检测——每个子任务是独立的 spawn，有独立的 prompt、独立的输出文件、独立的验证标准。写和审彻底分离，用认知框架冲突（Sugarman 的钩子逻辑 vs Feynman 的大一新生检验）替代人在回路中的逐字审校。

## 诚实边界

- **信息截止 2026-05**。写作工具和平台规则变化后可能需要调整
- **品牌特定**：写作 DNA（骨架层 + 血肉层）为"进化猫"品牌校准。复用骨架层到其他品牌需重校血肉层
- **需要飞书**：选题管理依赖飞书 Base。不用飞书的用户需替换选题来源
- **人审不可跳过**：Step 5b 编辑判断（BS+PG 双签）是人工暂停点，Agent 不可声称通过
- **杀稿率**：约 30-40% 的选题在搜索阶段被杀。这是设计如此，不是 bug

## 关联项目

- [evolution-cat-infographic](https://github.com/wampeeHuang/evolution-cat-infographic) — 图文卡片生产（本 Skill 的姊妹项目）
- [social-image-publisher](https://github.com/wampeeHuang/social-image-publisher) — 矩阵图文发布
- [skill-craftsmanship-framework](https://github.com/wampeeHuang/skill-craftsmanship-framework) — Skill 工匠框架（本 Skill 的质检系统）

## License

MIT

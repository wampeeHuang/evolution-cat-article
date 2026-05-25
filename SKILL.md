---
name: evolution-cat-article
description: |
  进化猫公众号文章写作全流程编排。核心原则：线索（好奇心）→ 6维搜索 + Burke跨域类比 → 撞到意外 → 那才是真正的选题。没有意外 = 杀稿。

  10步串行（Step 7 可选复盘）：搜索→意外发现暂停(杀稿门禁)→创意会两跑道门禁→PG+Feynman双门禁→Tim开头+Sugarman全文→机械初审→去AI味→机械质检(5项)→编辑判断(BS+PG双签)⏸→配图→可选复盘。

  触发：写进化猫文章、写公众号文章、进化猫选题写作、把选题写成文章。
  也匹配含"进化猫"+"写"的任意表达。

  **触发互斥：**
  - 用户说"文章""长文""公众号""写一篇""2000字"→ 触发本 Skill
  - 用户说"图文""小绿书""信息图""卡片""1080×1440"→ 触发 evolution-cat-infographic
  - 用户说"写作方向""研究写作"→ 追问：图文还是文章？

  Do NOT trigger when: 小绿书/图文（走 infographic）、通用写作建议、非进化猫品牌。
---

# 进化猫文章写作 · 全流程编排

> v4.0 — 核心原则：线索（好奇心）→ 6维搜索 + Burke跨域类比 → 撞到意外 → 那才是真正的选题。

## 架构

```
references/
├── skeleton/          ← 骨架层：质量基线，开源通用，不可通过 retro 修改
│   ├── fact-check.md
│   ├── density-gate.md
│   ├── honesty-gate.md
│   ├── source-trace.md
│   └── structure-gate.md
├── flesh/             ← 血肉层：风格生长，≤20 条信号 + ≤5 硬偏好 + ≤10 回避
│   ├── voice-signals.md
│   ├── hard-preferences.md
│   └── avoid-list.md
├── production-sop.md  ← 生产指令
├── humanizer-zh.md    ← 去 AI 味（24 模式）
├── image-generation.md← 配图生成
├── final-review.md    ← 机械质检（5a）+ 编辑判断（5b）
└── self-audit.md      ← 工匠框架自审计
```

## 自动加载

每次启动自动加载：
- `references/production-sop.md`

按需加载（production-sop.md 中 `>> 读取` 触发时）：
- `references/skeleton/fact-check.md` — Step 1（事实校验 + 数字核验）
- `references/skeleton/source-trace.md` — Step 1（6 维度搜索 + 素材包 + 追溯）
- `references/skeleton/honesty-gate.md` — Step 2（三跑道门禁 + 5 种节奏原型）
- `references/skeleton/density-gate.md` — Step 3（开头门禁 + 硬指标 + 术语降维 + 禁止词库）
- `references/skeleton/structure-gate.md` — Step 2.5/3.5/4（角度自检 + 清晰度 + 活人感检查）
- `references/humanizer-zh.md` — Step 4（24 种 AI 模式检测）
- `references/final-review.md` — Step 5a/5b（机械质检 + 编辑判断）
- `references/image-generation.md` — Step 6（配图）

---

## 前置条件

飞书选题库中必须有状态=`已入选` 的选题。无 → 终止。

---

## 输出路径（不可违反）

所有产物落盘到 `D:/HHH/自媒体/进化猫/AI/{YYYYMMDD}_{标题}/`：
- md 文件 + 封面图 ≥1 + 配图 ≥2
- 写文件前先建目录

---

## 执行流程

```
搜索 → 意外发现暂停(杀稿门禁) → 创意会(Beast+Karpathy) → PG+Feynman双门禁
→ Tim开头+Sugarman全文 → 机械初审 → 去AI味
→ 机械质检(5项) → 编辑判断(BS+PG双签) ⏸ → 配图 → 可选复盘
```

| 步骤 | 做什么 | 角色 | 门禁 |
|------|--------|------|------|
| 1 | 6 维度搜索（含跨领域类比）+ 事实校验 | Burke（跨域类比） | ≥3 来源 + 素材包落盘 |
| **1.5** | **意外发现暂停** | **主 session 自问** | **≥1 条意外 → 继续；0 条 → 杀稿** |
| 2 | 标题 + 诚实关 | Beast + Karpathy | 标题 PASS + 诚实 PASS |
| 2.5 | 清晰度 + 大纲 + Surprising Idea | **Feynman（清晰度）+ PG（大纲+意外）** | 清晰度 PASS + 大纲 PASS + Surprising Idea PASS |
| 3 | 开头 + 全文 | **Tim Pan（开头+术语降维）+ Sugarman（全文滑滑梯）** | 开头硬门禁 + 字数 + 引用可追溯 |
| 3.5 | 机械初审 | Feynman（仅错别字/句长/段长） | 机械通过 |
| 4 | 去 AI 味（24 模式 + grep 禁止词库） | 主 session | 全文 0 命中 AI 高频词 |
| **5a** | **机械质检（5 项）** | **Ben Smith** | **5 项全过** |
| **5b** | **编辑判断（双签）** | **Ben Smith + PG** | **双 PASS = 发；BS ①②③ FAIL = 杀稿** |
| 6 | Ogilvy 生成配图（spawn） | Ogilvy | 封面 1 + 配图 ≥2 |
| 7 | 可选复盘生长（最多 3 个诊断问题） | 主 session + 用户 | — |

⏸ 暂停等人审：Step 5b 后（双签通过，配图前最后确认）。配图 API 有成本。

## 角色分工

| 角色 | 位置 | 职责 |
|------|------|------|
| James Burke | Step 1 跨领域类比 | 在无关领域间找到隐藏连线 |
| Beast | Step 2 Gate 1 | 标题够不够炸 |
| Karpathy | Step 2 Gate 2 | 诚实：数字可追溯 + 壳核一致 + 不确定处标注 |
| **Feynman** | **Step 2.5 清晰度守门 + Step 3.5 机械初审** | **写前：每个 section 能用日常语言讲清楚吗？写后：错别字/句长/段长** |
| Paul Graham | Step 2.5 大纲门禁 + Step 5b 编辑判断 | 大纲：Surprising Idea + 递进链 + 论据追溯 + 逻辑断层；终审：递进链还在吗？读者能说出三个收获吗？ |
| **Tim Pan** | **Step 3 开头 + 术语降维** | **壳理论：让意外发现变成钩子 + 技术术语配日常类比** |
| Sugarman | Step 3 全文写作 | 滑滑梯节奏：每句推着读者读下一句 |
| Ben Smith | Step 5a 机械质检 + Step 5b 编辑判断 | 5a：反向映射/高频词/字数/死链/落盘；5b：Signal/Noise + 承诺兑现 + 反面论证 + 上帝之声 |

> 全部 spawn 子 agent 独立执行。Gate 检查人物可由 flesh/hard-preferences.md 切换。

---

## 约束红线

| # | 红线 |
|---|------|
| 1 | 禁止虚假链接和死链 |
| 2 | 禁止标注"待确认"后发布 |
| 3 | 禁止跳过任一道门禁 |
| 4 | 禁止编造第一人称体验（全自动场景） |
| 5 | 禁止 AI 高频词（此外/至关重要/标志着等） |
| 6 | 术语首次出现：类比在前术语在后 |
| 7 | 每 300 字 ≥1 个可验证数字或专有名词 |
| 8 | 禁止跳过配图参考库直接写提示词 |
| 9 | retro 回流只能写入 flesh/，不能改 skeleton/ |
| **10** | **Step 1.5 无意外发现 → 必须杀稿，不硬写** |
| **11** | **Step 5b 双签 FAIL（Signal/Noise 或 承诺兑现 或 反面论证）→ 必须杀稿，不硬发** |

---

## 完成标志

- [ ] md 文件已保存
- [ ] 封面图 1 张 + 配图 ≥2 张
- [ ] 机械质检 5 项全部通过
- [ ] 编辑判断 BS + PG 双签 PASS
- [ ] `这里是进化猫，陪你一起看世界✨` 结尾

---

## 诚实边界

- **设计截止 2026-05-22**。v4.0 核心变更：线索→搜索→意外→真正选题；Feynman 从节奏检查转为清晰度守门；新增 Tim Pan 开头+降维；Ben Smith 终审拆为 5a 机械质检 + 5b 编辑判断双签；PG 新增 Surprising Idea 门禁和终审编辑判断
- **实战验证有限**：v4.0 pipeline 尚未跑过完整文章。门禁有效性基于逻辑推演，非 A/B 对照
- 门禁人物默认值（Beast/Karpathy/PG/Feynman/Tim/Sugarman/Ben Smith），血肉层生长后可切换
- **不适用场景**：深度调查报道（需实地采访）、纯叙事散文（无方法论可提取）、时效 <24h 快讯（流程太重）、高度技术文档（读者画像不匹配）
- 骨架层开源后别人直接用；血肉层从空开始长，跑 10 篇后生长出个人风格指纹
- 门禁判断质量取决于 agent 对规则的执行力度 + 子 agent 独立验证
- **杀稿门禁（1.5 + 5b）是 v4.0 最关键的变更**——但杀稿标准（"没有意外""读者在别处能拿到"）的判准依赖 agent 判断力。可能假阳性（有意外但 agent 没识别）或假阴性（没意外但 agent 觉得有）
- **裁判常识盲区**（2026-05-25 实战暴露）：所有 perspective agent 的领域知识限于其 SKILL.md 蒸馏文档 + 英文市场为主的训练数据。当选题涉及中国市场的读者认知/品牌知名度/讨论语境时，裁判的"常识判断"可能系统性偏离中国读者实际。缓解方式：source-pack 的"读者上下文"字段为裁判提供事实锚点，但不能完全消除偏差。裁判涉及非自身文化语境的常识判断应标注为 🔮 常识推断

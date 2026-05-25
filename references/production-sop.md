# 生产指令 (SOP)

> v4.0 — 核心原则：线索（好奇心）→ 6维搜索 + Burke跨域类比 → 撞到意外 → 那才是真正的选题。没有意外 = 杀稿。

---

## 两层架构

| 层 | 内容 | 可变性 |
|----|------|--------|
| **骨架层** (`skeleton/`) | 事实校验、信息密度、门禁、源头追溯、结构自检 | 不可通过 retro 回流修改，只能通过版本级架构决策变更 |
| **血肉层** (`flesh/`) | 风格信号、硬偏好、回避模式 | 通过 Step 7 可选复盘写入，随作者生长 |

> 骨架管质量底线（开源通用），血肉管"这听起来是不是你"（自生长）。

## AI 与人的边界

| AI 擅长 | 人必须做 |
|---------|---------|
| 补充背景、找证据 | 核心观点判断 |
| 结构建议、风格检查 | 个人经历注入 |
| 数字核验、链接验证 | 情绪节点 |
| 类比候选生成 | 最终定稿 |
| 机械质检（反向映射/高频词/死链） | 编辑判断（值不值发/有没有意外） |

---

## 输入

飞书表格，状态=`已入选` 的条目：
- 中文标题 / 链接 / 来源 / 日报概览 / 入选理由

---

## 输出

所有产物落盘到 `D:/HHH/自媒体/进化猫/AI/{YYYYMMDD}_{标题}/`：
- md 文件 + 封面图 ≥1 + 配图 ≥2
- 字数 2000-6000

---

## 步骤 1：搜索 + 素材核验

```
>> 读取 skeleton/source-trace.md
>> 6 维度并行搜索（source-trace.md §一）
>> 第 6 维度（跨领域类比）与其他 5 个并行启动，spawn Burke（perspective-james-burke）
   - 输出：历史、电影、日常、商业类比各 1-2 个
   - 用途：供 Step 3 术语降维和 Step 1.5 意外发现
>> 第 7 维度（读者上下文搜索）：搜索目标读者群体的讨论语境
   - 主题在读者群中的知名度级别（搜索指数/社区讨论量/提及频率）
   - 读者对此主题的现有认知（知道什么/不知道什么/误解什么）
   - 读者讨论此话题的语气和用词（小红书/即刻/微信/微博）
   - 输出到 source-pack "读者上下文"字段
>> 每个数字从源头核实（skeleton/fact-check.md §三）
>> 逐条过事实校验铁律（skeleton/fact-check.md §一）
>> 输出素材包 → _runtime/article-source-pack.md（source-trace.md §二，含读者上下文字段）
>> 输出数据-来源对照表 + 关键数据交叉验证卡 → 写入同一文件
```

**🚪 门禁**：_runtime/article-source-pack.md 存在 + ≥3 个独立来源印证核心事实 → Step 1.5。

---

## 步骤 1.5：意外发现暂停（硬门禁）

```
>> 前置：_runtime/article-source-pack.md 存在 → 不存则硬阻断
>> 读完整素材包。Burke 类比一并看。不写、不判断——先问自己：

   ① 有没有哪个事实让我停下来想了超过 3 秒？
   ② 有没有哪个数据跟我之前的假设对不上？
   ③ 有没有哪个类比让我觉得"操，原来可以这样想"？
   ④ 有没有哪条信息，我愿意马上讲给朋友听？

>> 把意外发现写入 _runtime/surprise-findings.md（3-5 条，每条一句话）
   - 格式：`意外 #N: [具体发现] | 为什么意外: [之前的假设 vs 实际事实]`
```

**🚪 杀稿门禁**：surprise-findings.md 为空 → **杀稿。** 说明搜完没有意外，每一条都在验证已知。此时杀不可惜——写出来也是 Ben Smith 说的"读者在别处能拿到的东西"。

**有意外** → 围绕最强的 1-2 个意外重定方向。原始选题只是线索，意外发现才是真正的选题。

```
>> 输出 _runtime/surprise-findings.md（落盘即 PASS）
```

**🚪 门禁**：surprise-findings.md 存在且 ≥1 条意外发现 → Step 2。

---

## 步骤 2：创意会 — 三跑道门禁（两阶段 spawn）

```
>> 前置：素材包 + surprise-findings.md 已落盘
>> 读取 skeleton/honesty-gate.md
>> 根据选题确认节奏原型 → 原型自带门禁列表（honesty-gate.md §三），不适用则不 spawn
>> 标题和角度围绕 surprise-findings.md 的最强意外来建

>> 阶段 1：spawn Beast（perspective-mrbeast，可由 flesh/hard-preferences.md 切换）
   输入：素材包（含读者上下文） + surprise-findings.md + 选题
   指令：生成 ≥3 个标题候选，按 Beast 公式评估，输出最优 + 评分理由。注意 source-pack 的读者上下文字段——标题的口吻和锚点必须匹配读者对这个主题的熟悉度。如果读者上下文显示该主题知名度≥4级，不要用"揭秘""你不知道的X"等引入式标题
   输出：_runtime/gate-1-title.md（含 PASS/FAIL）
>> 🚪 gate-1-title.md 不存在或 FAIL → 硬阻断，不得进入阶段 2

>> 阶段 2：spawn Karpathy（perspective-andrej-karpathy，默认）
   输入：素材包（含读者上下文） + gate-1-title.md + surprise-findings.md
   指令：
     - 数字可追溯性：标题里的每一个量化承诺，素材包能撑住吗？
     - 壳核一致性：标题的承诺和意外发现的内核一致吗？（标题是壳，surprise-findings 是核）
     - 不确定处是否标注
     - 常识自检：你对文章主题/公司/人物的判断，有没有依赖你自身训练数据中的"常识"而非素材包？如有——尤其是涉及非英语市场的判断——标注为 🔮 常识推断。你对自己不知道的东西不知道——如果一个判断你觉得"确定"但素材包里没有对应数据，这恰恰是最危险的盲区
   输出：_runtime/gate-2-honesty.md（含 PASS/FAIL）

>> 🚪 gate-1-title.md + gate-2-honesty.md 全部存在且 PASS → 继续
>> 🚪 任一 FAIL → 硬阻断，回对应步骤修复
>> 全自动场景禁用调查实验型
>> 确认叙述策略：全文引用式（honesty-gate.md §四）
>> 输出 _runtime/creative-brief.md（标题 + 角度 + 节奏原型 + 叙述策略 + 一句话读者收获 + 核心意外发现）
```

**🚪 门禁**：原型要求的所有 gate 文件存在且 PASS + creative-brief.md 落盘 → Step 2.5。

> 肉层回流后，检查人物可能切换。执行时先检查 flesh/hard-preferences.md 中是否有 character_choice 类型的偏好，有则用那个视角 spawn 子 agent。

---

## 步骤 2.5：PG + Feynman 双门禁

```
>> 前置：_runtime/creative-brief.md + _runtime/article-source-pack.md + _runtime/surprise-findings.md 存在 → 不存则硬阻断

>> 阶段 1：spawn Feynman（perspective-richard-feynman）— 清晰度守门
   输入：creative-brief.md + source-pack.md（含读者上下文）
   指令：
     - 追问：这 3-5 个 section，随便抽一个，能用日常语言口头给朋友讲一遍吗？
     - 讲不出来 → 标注该 section PASS/FAIL + 理由
     - 术语是否在素材包里有对应日常类比？
     - Feynman 不问节奏、不问错别字——只问"一个午休刷手机的人，这段话能一眼看懂吗？"
     - 注意 source-pack 读者上下文：你解释的起点必须从读者"已知"的地方出发。如果读者已经熟悉某个概念，不要从零解释——那会让读者觉得"这篇不是写给我的"
   输出：_runtime/gate-clarity.md（逐 section PASS/FAIL）

>> 🚪 gate-clarity.md 存在且 ≥3/5 section PASS → 进入阶段 2
>> 🚪 <3/5 PASS → 回 Step 2 重定角度（问题不是表达，是理解不透）

>> 阶段 2：spawn Paul Graham（perspective-paul-graham）— 大纲 + Surprising Idea
   输入：creative-brief.md + source-pack.md（含读者上下文） + surprise-findings.md + gate-clarity.md
   指令：
     - ① Surprising Idea 检查：这篇文章的核心论点是自己撞出来的还是早就知道的？
       如果是早就知道的 → FAIL。"好的 essay 是写作本身生成了想法，不是把已有想法包装成文章。"
     - ② section 递进检查：3-5 个 section 之间有递进关系吗？（不是并列堆料）
     - ③ 论据追溯：每个 section 的核心论据能反向映射到素材包吗？映射不到的标 ⚠️
     - ④ 逻辑断层扫描：读者读完第 N 节到第 N+1 节，逻辑上会不会断？
     - ⑤ 角度杀伤力（仅观点论证型）：structure-gate.md §一 4 条 → 判断有无反常识拐点
     - ⑥ 读者画像匹配（新增）：大纲的叙述起点和引用语境是否匹配 source-pack 的读者上下文？如果文章写的是读者熟悉的话题，大纲却从"这是什么"开始——这是 FAIL。Surprising Idea 不要求从零科普——意外可以建立在读者已知的基础上
     - 输出：_runtime/outline-review.md（逐节 PASS/FAIL + 修改建议）
>> 🚪 outline-review.md 存在且 PASS（含 ① Surprising Idea PASS），section 数 3-5 且递进链完整 → 继续
>> 🚪 ① Surprising Idea FAIL → 杀稿或回 Step 1.5 重找意外
>> 🚪 其他 FAIL → 调 section 结构，不改正文，最多 2 轮
```

**🚪 门禁**：gate-clarity.md PASS + outline-review.md PASS（含 Surprising Idea）→ Step 3。

> 人物可由 flesh/hard-preferences.md 切换。观点论证型多跑 ⑤ 角度杀伤力。全体原型跑 ①②③④。Feynman 全体原型 spawn。

---

## 步骤 3：写文章（Tim Pan + Sugarman 配对 spawn）

```
>> 前置检查：_runtime/creative-brief.md + _runtime/article-source-pack.md + _runtime/outline-review.md + _runtime/gate-clarity.md + _runtime/surprise-findings.md 存在 → 不存则硬阻断
>> 读取 skeleton/density-gate.md

>> 阶段 1：spawn Tim Pan（perspective-tim-pan）— 开头 + 技术降维
   输入：creative-brief.md + surprise-findings.md + source-pack.md（含读者上下文） + density-gate.md + flesh/*
   指令：
     - 只写开头（前 300 字）——让一个午休刷手机的人停下滑滑梯
     - 开头硬门禁（density-gate.md §一）：第一句必须是具体事件/数据/场景
     - 壳理论应用于开头：把 surprise-findings 里最意外的**矛盾**变成钩子——让读者想知道"怎么做到的？""为什么？"。**壳理论约束：钩子制造好奇心，不揭示结论。** 开头可以给出矛盾数字制造认知冲突（"三件事同时成立，账不平"），但不给出解析框架（"因为是废热回收"）。读者应在 outline-review.md 指定的翻牌点（通常 Section 03）才被核心意外击中。自检：删掉正文只读开头，读者能说出全文结论 → 开头剧透了核心意外 → FAIL
     - 术语降维：每个技术术语配日常类比（类比在前术语在后）
     - 口吻匹配读者熟悉度：对照 source-pack 读者上下文——如果主题在读者群中知名度≥4级，开头不要用"有一家公司叫X""你可能不知道的是"等介绍式口吻。从读者已经知道的地方出发，不是从零科普
     - 输出开头 + 全文中需降维的术语对照表
   输出：_runtime/opening-draft.md（含术语降维表）

>> 🚪 opening-draft.md PASS（主 session 审：第一句是具体事件/数据/场景？+ 术语降维表覆盖所有技术词？）→ 阶段 2

>> 阶段 2：spawn Sugarman（perspective-joseph-sugarman）— 全文滑滑梯
   输入：creative-brief.md + source-pack.md（含读者上下文） + outline-review.md + opening-draft.md + density-gate.md + flesh/*
   指令：
     - 继承 Tim 的开头和术语降维表
     - 按 creative-brief 的标题/角度/节奏原型/叙述策略写完全文
     - 认知引渡原则（density-gate.md §二）：从读者已知渡到未知——读者上下文字段告诉你读者已知什么
     - 禁止词库避开（density-gate.md §五）
     - 滑滑梯节奏：每句推着读者读下一句
     - 口吻约束：全文叙述语气必须匹配 source-pack 读者上下文中读者的讨论方式。如果读者用"幻方""梁文锋"直呼，你也用——不要用"这家中国AI公司""其创始人"等译文腔
     - 文末：参考来源 + 这里是进化猫，陪你一起看世界✨
     - 全自动场景：全文引用式叙述
   输出：_runtime/draft-v1.md

>> 硬阻断：draft-v1.md 不存在 → 重 spawn
>> 主 session 读 draft-v1.md → 逐条过风格硬指标（density-gate.md §三）
>> 字数检查（2000-6000）+ 引用可追溯检查
>> 不通过 → 标注具体违规项 → 退回 Sugarman spawn 修改，最多 2 轮
```

**🚪 门禁**：开头硬门禁通过 + 无不自然段落 + 2000-6000 字 + 引用可追溯 → Step 3.5。

> flesh/hard-preferences.md character_choice 可切换 Writer 人物，执行时检查。

---

## 步骤 3.5：机械初审

```
>> spawn Feynman（perspective-richard-feynman）— 仅机械检查
   输入：draft-v1.md
   指令：
     - 机械检查：错别字/病句/标点、单句 >45 字、段落 >200 字、连续 3 段等长无变化
     - 输出问题列表，不全文重写
     - 注意：Feynman 的清晰度检查已在 Step 2.5 完成，此处不做
   输出：_runtime/editor-review.md
>> 主 session 读取 editor-review.md → 修具体问题 → 存 draft-v2.md
```

**🚪 门禁**：校对/机械通过 + draft-v2.md 落盘 → Step 4。

> Step 3.5 只做机械检查。Feynman 的核心价值（清晰度守门）已在 Step 2.5 前置完成——写之前确保能讲清楚，比写之后改表达更高效。

---

## 步骤 4：去 AI 味

```
>> 前置：检查 draft-v2.md 存在 → 不存则硬阻断
>> 读取 humanizer-zh.md
>> 扫描 24 种 AI 写作模式，重写问题片段
>> 活人感检查 7 项逐条打勾（skeleton/structure-gate.md §四）
>> 全文 grep AI 高频词列表（humanizer-zh.md §7）——命中 = 不通过（纯机械扫描，不 spawn persona）
>> 存 draft-v3.md
```

**🚪 门禁**：全文 0 命中 AI 高频词 + 活人感 7 项全过 + draft-v3.md 落盘 → Step 5a。

---

## 步骤 5a：机械质检（spawn Ben Smith）

```
>> 前置：检查 draft-v3.md 存在 → 不存则硬阻断
>> 读取 final-review.md §机械质检
>> spawn Ben Smith（perspective-ben-smith），加载 final-review.md
   输入：draft-v3.md + _runtime/article-source-pack.md
   指令：5 项机械质检，逐项 PASS/FAIL
   输出：_runtime/mechanical-qc-report.md
```

| # | 检查项 | PASS 标准 | 不通过 |
|---|--------|----------|--------|
| 1 | 反向映射 | 文中每个具体事实可反向映射到素材包具体来源 | 标疑或删除 |
| 2 | AI 味 | 高频词 0 命中 | 回 Step 4 |
| 3 | 字数 | 2000-6000 | 回 Step 3 |
| 4 | 参考来源 | 逐条 URL 可访问 | 删除死链 |
| 5 | 落盘检查 | md + 封面 + 配图文件确认 | 补文件 |

> 机械质检是工厂质检——尺寸对吗、标签贴了吗。不影响文章值不值得发。值不值得发是 Step 5b 的事。

**🚪 门禁**：5 项全过 + mechanical-qc-report.md 落盘 → Step 5b。

---

## 步骤 5b：编辑判断（spawn Ben Smith + PG，双签）

```
>> 前置：_runtime/mechanical-qc-report.md + draft-v3.md 存在 → 不存则硬阻断

>> 并行 spawn 两个子 agent：

   Ben Smith（perspective-ben-smith）— 外部价值判断
   输入：draft-v3.md + creative-brief.md + surprise-findings.md + source-pack.md（含读者上下文）
   指令：
     - ① Signal/Noise：「这篇东西，读者在别处能拿到吗？」能拿到 → FAIL
     - ② 承诺兑现：Beast 标题炸的点，正文兑现了吗？标题是壳，正文是核——壳核对齐了吗？
     - ③ 反面论证：文章有没有展示最有力的反对论证？（不找稻草人，找你真正尊重但不同意的观点）
     - ④ 上帝之声：有没有装全知全能？（"专家分析""深度解读""毋庸置疑"）
     - ⑤ 身份钩子：读者转发时在对朋友说什么？正文配得上这个身份承诺吗？
     - ⑥ 读者读感（新增）：文章的口吻、节奏、用典、情绪起伏是否匹配 source-pack 读者上下文中的读者画像？裁判自问：读者读完全文，会觉得"这篇是写给我的"还是"这篇翻译自英文tech blog"？如果文章把读者熟悉的东西当陌生事物介绍 → FAIL
   输出：_runtime/editorial-judgment-bs.md（逐项 PASS/FAIL + 杀稿建议）

   Paul Graham（perspective-paul-graham）— 内部逻辑判断
   输入：draft-v3.md + outline-review.md + surprise-findings.md + source-pack.md（含读者上下文）
   指令：
     - ① 递进链是否还在？（写的过程中有没有偏离 PG 大纲？）
     - ② 读者能不能说出 3 个收获？（读完觉得"学到了"还是"看完了"？）
     - ③ Surprising Idea 有没有被写淡？（意外发现在终稿里的冲击力还在不在？）
     - ④ 有没有逻辑断层？（不是大纲层面的——是终稿实际文本层面的）
     - ⑤ 读者画像匹配（新增）：终稿叙述口吻是否匹配 source-pack 读者上下文？如果文章把中国读者家喻户晓的品牌当成陌生事物介绍 → FAIL。叙述的起点必须从读者已知出发
   输出：_runtime/editorial-judgment-pg.md（逐项 PASS/FAIL + 修改建议）
```

**🚪 双签门禁**：

| Ben Smith 结果 | PG 结果 | 动作 |
|---------------|---------|------|
| PASS | PASS | 发 |
| FAIL（①②③任一）| — | **杀稿。** Signal/Noise FAIL = 读者能在别处拿到。承诺兑现 FAIL = 标题诈骗。反面论证 FAIL = 装上帝。这些修不了——是选题和角度层面的问题。 |
| ⑥ FAIL（①②③PASS）| — | 回 Step 3 Sugarman 重写（注入读者上下文），最多 1 轮。读者读感 FAIL 可修——叙述口吻调整。 |
| PASS | FAIL | 回 Step 3 Sugarman 重写（PG 的诊断给 Sugarman），最多 1 轮 |
| ①④⑤ FAIL | PASS | 回对应步骤修（④→改语气/⑤→改开头），最多 1 轮 |

> 这是编辑判断，不是机械清单。Ben Smith 管"值不值发"，PG 管"逻辑对不对"。两个都说行才是真行。

**⏸ 暂停等人审**：5b 双签 PASS 后，配图前最后确认。配图 API 有成本。

---

## 步骤 5c：终稿事实复验

```
>> 前置：draft-v3.md + _runtime/article-source-pack.md 存在 → 不存则硬阻断
>> spawn Karpathy（perspective-andrej-karpathy）
   输入：draft-v3.md + article-source-pack.md
   指令：
     - 逐条提取 draft-v3.md 中所有具体数字、日期、价格、专有名词、产品名、型号
     - 逐一反向映射到 source-pack 的具体来源行号
     - 映射不到或来源冲突 → 标 🔴 严重错误（必须修改）
     - 来源支持但表述有偏差（缺"预计"/"估算"等限定词、数字四舍五入失真）→ 标 🟡 需修正
     - 自检：你对数据/公司/人物的判断，有没有依赖训练数据中的"常识"而非素材包？如有 → 标 🔮 常识推断，同时给出素材包中可验证的替代方案
   输出：_runtime/fact-check-final.md（逐条 PASS / 🔴 / 🟡 / 🔮）
```

**🚪 门禁**：0 🔴 严重错误 → 继续。有 🔴 → 回 draft-v3.md 修正对应行，修正后重跑 Step 5c。

> Step 1 事实校验在写作前跑。Step 5c 在终稿后重新核验——写作过程中新引入的数据（改 lede、换例子、加行业对照）此前从未被任何人核对过。v4.0 实战暴露：改 lede 时临时加入的"HBM涨五倍"和"Opus 4.6 $15/$75"从 Step 1 之后一路绿灯到发布前，7 个门禁角色无一人验证数据准确性。Step 5c 是写作后的事实刹车。

---

## 改后重检规则

改完 draft-v3.md 任何内容后，按改动范围决定重跑哪些门禁。不跑全流程——只跑受影响的。

### 改动分级

| 级别 | 定义 | 示例 |
|------|------|------|
| **小改** | 修措辞/错别字/单句，不动数据不动结构 | 改"发现不对"→"反应过来"，修标点 |
| **中改** | 改段落/换例子/调数据/改 lede/加行业对照 | 换 Section 04 例子，lede 加新数据点，调定价倍数 |
| **大改** | 动结构/重写 section/改核心论点 | 砍掉整个 section，重写叙事弧线 |

### 重检矩阵

| 改动级别 | 必跑步骤 | 原因 |
|---------|---------|------|
| **小改** | 3.5（机械初审）+ 4（去AI味） | 新文字可能引入错别字/AI高频词 |
| **中改** | 3.5 + 4 + 5a（机械质检）+ **5c（事实复验）** | 新数据必须核源，新段落可能引入不可追溯的事实 |
| **大改** | 从 Step 2 全流程重跑 | 结构变了，大纲/开头/节奏全受影响 |

### 中改特别警告

中改最危险——不是改得多，是改得"刚刚好能绕过直觉审查"。加一行行业数据、换一个例子里的数字、修一个定价——这些改动单看很小，但每一步都可能引入未经核实的事实。**中改后不跑 5c = 裸奔。**

> 本文档的迭代方式表只覆盖"改架构规则改哪个文件"。此处的重检矩阵覆盖"改文章后重跑哪些门禁"。两表互补。

---

## 步骤 6：生成配图（spawn Ogilvy）

```
>> 前置：draft-v3.md + _runtime/mechanical-qc-report.md + _runtime/editorial-judgment-bs.md + _runtime/editorial-judgment-pg.md 存在 → 不存则硬阻断
>> 读取 image-generation.md
>> spawn Ogilvy（perspective-david-ogilvy），加载 image-generation.md
   输入：draft-v3.md + image-generation.md + surprise-findings.md
   指令：
     - Step 6.0：查参考提示词库（不可跳过）
     - 文章论点 → 视觉概念 → 提示词
     - 成图后审：是否服务于文章论点？视觉风格是否一致？
     - 封面图优先呼应 surprise-findings 的核心意外
     - 优先级 1：gpt-image-2 API
     - 失败 → 降级 2：即梦网页版
     - 失败 → 降级 3：image-prompts.txt（兜底）
   输出：_runtime/image-brief.md（含提示词 + 成图审查意见）
```

**🚪 门禁**：封面 1 + 配图 ≥2；仅 txt 标记"待补"不阻断。→ Step 7。

---

## 步骤 7：复盘 & 生长（自动触发）

**发布完成后自动触发。** 不等人问——agent 主动弹出复盘。

```
>> 发布成功 → 自动进入复盘，不跳过
>> agent 通读终稿，对比上一版 diff，诊断当篇最弱的 3 个点

### 跳过

→ 文章落盘，流程结束，不写 retro。

### 复盘

```
>> agent 通读全文，诊断当篇最弱的 3 个点
   （角度？节奏？开头？类比？某段太散？）
>> 提 3 个问题，逐个问用户
>> 用户挑想答的答，不想答说"过"
>> 能提取的风格信号写入 flesh/voice-signals.md
   - 单次最多新增 3 条、修改 2 条
   - 新信号标记 pending，连续 2 篇触发转 active
>> 检查是否有信号置信度 ≥3 → 候选晋升硬偏好
   - 暂停展示，等用户确认后写入 flesh/hard-preferences.md
>> 用户随时喊停，不硬凑 3 个问题
```

**复盘约束**：
- 只能写入 `flesh/`，不能改 `skeleton/`
- 每 10 次 retro 触发一次元审计：
  - 血肉层信号中连续 5 篇未触发 >30% → 清理
  - 硬偏好与近期 5 篇风格不符 → 降级
  - retro 写入内容无法对应到当篇文章 → 删除
  - skeleton 是否被 retro 触及 → 是则拒绝并回滚

---

## 流程总览

```
搜索 → 意外发现暂停(杀稿门禁) → 创意会(Beast+Karpathy) → PG+Feynman双门禁
→ 写文章(Tim开头+Sugarman全文) → 机械初审 → 去AI味
→ 机械质检(5项) → 编辑判断(BS+PG双签) → 事实复验(终稿核源) ⏸ → 配图 → 可选复盘
```

| 步骤 | 做什么 | 角色 | 门禁 |
|------|--------|------|------|
| 1 | 6 维度搜索 + 事实校验 | Burke（跨域类比） | ≥3 来源 + 素材包落盘 |
| **1.5** | **意外发现暂停** | **主 session 自问** | **≥1 条意外 → 继续；0 条 → 杀稿** |
| 2 | 标题 + 诚实关 | Beast + Karpathy | 标题 PASS + 诚实 PASS |
| 2.5 | 清晰度 + 大纲 + Surprising Idea | **Feynman（清晰度）+ PG（大纲+意外）** | 清晰度 PASS + 大纲 PASS + Surprising Idea PASS |
| 3 | 开头 + 全文 | **Tim Pan（开头）+ Sugarman（全文）** | 开头硬门禁 + 字数 + 引用可追溯 |
| 3.5 | 机械初审 | Feynman（仅机械） | 错别字/句长/段长通过 |
| 4 | 去 AI 味 | 主 session + humanizer-zh | 高频词 0 + 活人感 7 项 |
| **5a** | **机械质检** | **Ben Smith（5 项）** | **5 项全过** |
| **5b** | **编辑判断** | **Ben Smith + PG 双签** | **双 PASS = 发；BS ①②③ FAIL = 杀稿** |
| **5c** | **终稿事实复验** | **Karpathy** | **0 🔴 严重错误；有 🔴 → 修后重跑** |
| 6 | 配图 | Ogilvy | 封面 1 + 配图 ≥2 |
| 7 | 可选复盘 | 主 session + 用户 | — |

---

## 全流程禁则

- ❌ 文件写 home 目录或盘符根目录
- ❌ 数据不核实就进分析
- ❌ 伪造第一人称体验——全自动场景一律引用式
- ❌ 跳过 awesome-gpt-image-2 参考库
- ❌ 门禁不通过强行推进
- ❌ retro 回流写入 skeleton/（骨架层只能版本级变更）
- ❌ Step 1.5 无意外不杀稿
- ❌ Step 5b 双签 FAIL 不杀稿
- ❌ 改 SKILL.md 或 reference 文件不更新 system-diagram.html（图必须和源文件同步，落后=失去可信度）

---

## 迭代方式

| 要改什么 | 改哪里 |
|---------|-------|
| 事实校验规则 | skeleton/fact-check.md |
| 信息密度/字数/开头/术语降维/禁止词 | skeleton/density-gate.md |
| 门禁逻辑/节奏原型/诚实规则 | skeleton/honesty-gate.md |
| 搜索维度/素材包/追溯规则 | skeleton/source-trace.md |
| 角度自检/节奏自检/活人感检查 | skeleton/structure-gate.md |
| 清晰度门禁/机械初审 | skeleton/structure-gate.md |
| 机械质检/编辑判断 | final-review.md |
| 终稿事实复验 | Step 5c（本文件） |
| 改后重检规则 | 本文件 §改后重检规则 |
| 配图 | image-generation.md |
| 风格信号/硬偏好/回避模式 | flesh/*.md（仅通过 retro 回流） |

---

## 配套

| Skill | 用途 |
|-------|------|
| humanizer-zh | 去 AI 味（已内化） |
| baoyu-post-to-wechat | Markdown → 微信草稿箱 |
| perspective-james-burke | Step 1 跨领域类比搜索 |
| perspective-mrbeast | Step 2 Gate 1 标题（默认，可切换） |
| perspective-andrej-karpathy | Step 2 Gate 2 诚实 + 壳核一致（默认，可切换） |
| perspective-richard-feynman | Step 2.5 清晰度守门 + Step 3.5 机械初审 |
| perspective-paul-graham | Step 2.5 大纲 + Surprising Idea + Step 5b 编辑判断 |
| perspective-tim-pan | Step 3 开头 + 术语降维 |
| perspective-joseph-sugarman | Step 3 全文滑滑梯写作 |
| perspective-ben-smith | Step 5a 机械质检 + Step 5b 编辑判断 |
| perspective-david-ogilvy | Step 6 配图生成 + 视觉审查 |

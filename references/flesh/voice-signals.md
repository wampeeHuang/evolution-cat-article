# 风格信号池

> 血肉层，≤20 条。每篇复盘可写入，自动驱逐 + 冷却。

## 数据结构

每条信号格式：
```yaml
- id: S001
  pattern: "一句话描述这个风格模式"
  type: positive | negative    # 正=要保持的风格，反=要回避的模式
  confidence: 1-5             # 连续触发+1，连续不触发-1，归零=淘汰
  status: pending | active     # 新信号pending，连续2篇触发转active
  last_hit: "YYYY-MM-DD"
  source_article: "文章标题"   # 首次触发的那篇
```

## 驱逐规则

- 容量满 20 条 → 淘汰置信度最低 + 最久未命中
- 连续 3 篇未触发 → 置信度 -1
- 连续 3 篇触发 + 用户确认保留 → 置信度 +1
- 置信度归零 → 自动淘汰
- 单次 retro 最多写入 3 条、修改 2 条

## 晋升规则

- 置信度 ≥ 3 → 候选晋升硬偏好
- 晋升时暂停，展示信号，等用户确认
- 硬偏好容量 ≤ 5 条（见 hard-preferences.md）

---

## 信号列表

（初始为空，随文章执行增长）

<!-- SIGNALS_START -->

- id: S001
  pattern: "类比浅尝辄止——提出一个好类比（Red Hat/Linux内核）但只用来做一段装饰，不推到边界条件和失效点。"
  type: negative
  confidence: 3
  status: active
  last_hit: "2026-05-22"
  source_article: "DeepSeek-Harness对决ClaudeCode"
  detail: "v4已改善：新增'Linux内核确定，大模型不确定——AI Harness比Red Hat更难'段落，类比推到了边界。置信度从4降到3，状态从pending转active。"

- id: S002
  pattern: "论证自噬——一个子论点（价差28倍）的篇幅和语气压过核心论点（护城河在Harness），读者读完不知道作者到底站哪边。"
  type: negative
  confidence: 4
  status: pending
  last_hit: "2026-05-22"
  source_article: "DeepSeek-Harness对决ClaudeCode"
  detail: "PG：如果essay讲的是Harness是新战场，价格部分应该两句话结束。费曼：做费曼测试——如果明天Anthropic也降到同价，你的论证还剩多少说服力？如果塌了一半，说明那一半本来就不是核心。"

- id: S003
  pattern: "零件清单式解释——用组件名称清单（上下文管理/工具调用/文件读写/终端执行）代替运作原理。读者能说出'有什么'但说不出'为什么难'。"
  type: negative
  confidence: 4
  status: pending
  last_hit: "2026-05-22"
  source_article: "DeepSeek-Harness对决ClaudeCode"
  detail: "费曼：知道名字≠理解。你告诉读者Harness包含四个组件，没告诉他们这四个组件为什么难做——模型输出不确定的行号怎么处理？改完验证循环什么时候停？上下文长了丢什么保留什么？零件清单不叫解释。"

- id: S004
  pattern: "内行人写给内行人看——默认读者和作者共享同一套知识背景。提到Red Hat时不解释Linus是谁，提Transformer时不解释Google 2017年的论文，用英文术语killer app/commodity时不翻译。"
  type: negative
  confidence: 5
  status: pending
  last_hit: "2026-05-22"
  source_article: "DeepSeek-Harness对决ClaudeCode"
  detail: "读者反馈：'Red Hat是谁，Linus Torvalds是谁，我的视角对这个案例没有认知，案例是好的，但得让我了解它是什么。'写作者天然高估读者的领域知识。检验标准：一个不写代码不看科技新闻的朋友读完，能不能理解每一个专有名词？如果不能，加一句话解释。→ 已晋升硬偏好：锚点先行。"

- id: S005
  pattern: "数字瀑布——论证关键段落前半段密集堆砌财务数据（25亿/90亿/440亿/296亿/650亿），读者在数字洪流中失去方向感。数字不是论证，趋势和因果才是。"
  type: negative
  confidence: 3
  status: pending
  last_hit: "2026-05-22"
  source_article: "DeepSeek-Harness对决ClaudeCode"
  detail: "谁在付钱？段九行塞了八个数字。每段核心数字≤3个，其余放参考来源。"

- id: S006
  pattern: "结尾停在抽象结论而非具体画面。逻辑收住了但读者合上页面没有能记住的画面。开头有Linus/340亿/Red Hat全是具体的东西，结尾只有一句话。"
  type: negative
  confidence: 3
  status: pending
  last_hit: "2026-05-22"
  source_article: "DeepSeek-Harness对决ClaudeCode"
  detail: "建议：结尾给一个读者能带走的画面——比如'你明天早上打开的终端里，跑的不是模型参数，是几百个工程师写的Harness代码，在模型胡说八道的时候帮你兜底。'"

<!-- SIGNALS_END -->

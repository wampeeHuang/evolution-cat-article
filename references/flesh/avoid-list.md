# 回避模式

> 血肉层，≤15 条。你的个人风格禁区，比骨架层禁止词库更具体。

## 数据结构

```yaml
- id: A001
  pattern: "具体要回避的表达/语调/结构"
  reason: "为什么你觉得不像自己"
  confidence: 1-5
  last_hit: "YYYY-MM-DD"
```

## 与骨架禁止词库的区别

- 骨架禁止词库：通用的 AI 病（"此外""标志着""随着…发展"）
- 回避模式：你的个人风格禁区

## 容量控制

- 上限 15 条
- 满时淘汰置信度最低 + 最久未命中

---

## 回避列表

<!-- AVOID_START -->

- id: A001
  pattern: "编造第一人称体验——'我试了X发现Y''我读了一下午''书里的每个段落都在回答我'"
  reason: "全自动场景 Agent 没有真实经历。替作者发明体验是第一人称写作最致命的病灶——读者看得出。除非确为作者本人坐下来敲进去的经历，否则一律用'你'或第三人称。"
  confidence: 5
  source_article: "39副心智眼镜——不是模仿，是理解"
  last_hit: "2026-05-22"

- id: A002
  pattern: "新闻导语式开头——'X月X日，XX官网悄然上线XX''同一天，XX发布XX'。把日期、地点、事件按时间线排列当开头。"
  reason: "PG：你在报道，不在思考。读者不需要日期和地点，需要知道这事为什么重要。新闻是essay的由头，不是essay本身。正确做法：用类比或核心论点开场。"
  confidence: 4
  source_article: "DeepSeek-Harness对决ClaudeCode"
  last_hit: "2026-05-22"

- id: A003
  pattern: "'说实话'/'说真的'/'老实说'/'不骗你'——口头禅式真诚声明"
  reason: "PG：每次出现都在暗示前面说的不是实话。删。真诚不需要声明。"
  confidence: 5
  source_article: "DeepSeek-Harness对决ClaudeCode"
  last_hit: "2026-06-13"

- id: A004
  pattern: "模糊信号词——'值得关注的信号''引发深思''值得思考'。说了关注但没说为什么关注。"
  reason: "费曼：说清楚为什么值得关注。如果说不清楚，说明你没想清楚值不值得关注。要么删，要么展开到具体可验证的理由。"
  confidence: 4
  source_article: "DeepSeek-Harness对决ClaudeCode"
  last_hit: "2026-05-22"

- id: A005
  pattern: "专有名词/人名不做背景介绍——'Red Hat''Linus Torvalds''Tim Berners-Lee''Transformer'直接使用，假设读者知道是什么。"
  reason: "读者视角：案例是好案例，但读者不知道Linus是谁、Red Hat做了什么。好类比需要先给锚点。提到任何非大众级专有名词时，用一句话说清楚：谁、做了什么、为什么不付钱也能用。"
  confidence: 5
  source_article: "DeepSeek-Harness对决ClaudeCode"
  last_hit: "2026-05-22"

- id: A006
  pattern: "英文术语直接使用不做翻译/解释——'killer app''commodity'直接写英文，读者不知道怎么读、什么意思。"
  reason: "读者视角：killer app = 杀手级应用（一个应用好到让人愿意为它买底层平台）。commodity = 大宗商品/标准化商品（功能趋同、竞争靠价格）。技术写作不是炫英文，是降低理解门槛。首次出现必须给中文翻译+一句话解释。"
  confidence: 5
  source_article: "DeepSeek-Harness对决ClaudeCode"
  last_hit: "2026-05-22"

- id: A007
  pattern: "万能废句结尾过渡——'我们能做的，是留意趋势、调整交互、用好手上已有的东西''关注我们能关注的，做我们能做的'。什么都没说，占一行。"
  reason: "PG：如果这句话去掉之后段落意思没变，就去掉。过渡句不说具体内容，只起填充作用——读者读完不知道具体要留意什么、调整什么。要么删，要么换成具体到可验证的东西。"
  confidence: 4
  source_article: "别把AI当知识引擎"
  last_hit: "2026-06-13"

- id: A008
  pattern: "'说白了'——AI高频踩雷词，一出现立刻暴露机器味。"
  reason: "进化猫个人禁区：这个词在AI生成文本中出现频率远高于真人写作。替代：'坦率的讲''其实就是'。"
  confidence: 3
  source_article: "humanizer-zh 个人禁止词提取"
  last_hit: ""

- id: A009
  pattern: "'意味着什么''这意味着'——AI标志性句式，用 rhetorical question 填充过渡。"
  reason: "进化猫个人禁区：不替读者问问题，直接给答案。替代：'那结果呢''所以呢'。"
  confidence: 3
  source_article: "humanizer-zh 个人禁止词提取"
  last_hit: ""

- id: A010
  pattern: "'本质上'——太学术，不像聊天。"
  reason: "进化猫个人禁区：口语场景中'本质上'=我在写论文。替代：'说到底''其实'。"
  confidence: 3
  source_article: "humanizer-zh 个人禁止词提取"
  last_hit: ""

- id: A011
  pattern: "'不可否认'——套话，直接删。"
  reason: "进化猫个人禁区：任何以'不可否认'开头的内容，删掉这四个字意思不变。用正面陈述替代。"
  confidence: 3
  source_article: "humanizer-zh 个人禁止词提取"
  last_hit: ""

- id: A012
  pattern: "'值得注意的是''不难发现'——上帝之声变体。"
  reason: "进化猫个人禁区：跟'毋庸置疑''众所周知'同类，是站在讲台上对读者说话的语气。删掉，直接说。"
  confidence: 3
  source_article: "humanizer-zh 个人禁止词提取"
  last_hit: ""

- id: A013
  pattern: "'首先…其次…最后'——教科书结构，暴露AI骨架。"
  reason: "进化猫个人禁区：三段落式列举是LLM的标志性结构偏好。替代：自然转场词，不编号。"
  confidence: 3
  source_article: "humanizer-zh 个人禁止词提取"
  last_hit: ""

- id: A014
  pattern: "'在当今…的时代''随着…发展'——万能废开头。"
  reason: "进化猫个人禁区：任何以时间状语宏大叙事开场的文章，读者第一句就划走了。替代：具体事件/场景切入。"
  confidence: 3
  source_article: "humanizer-zh 个人禁止词提取"
  last_hit: ""

<!-- AVOID_END -->

# 配图生成

> Step 5 执行指令。三级降级策略 + 提示词构建规范。

---

## 一、三级降级策略

严禁卡死在任一级。前一级失败自动切下一级。

### 优先级 1：gpt-image-2 API（首选）

API 配置读取顺序：① skill 目录下 `config.yaml`（如存在）→ ② 环境变量 `IMAGE_API_KEY` / `IMAGE_API_URL` → ③ 无显式配置时使用已知端点（aigoapi.com, gpt-image-2, timeout≥180s）。

#### 1a. 合并裁切策略（配图 ≥2 张时优先）

> 一次 API 调用生成纵向合并图 → Python 裁切多张。省 33-50% 调用 + 配图风格天然统一。

**适用条件**：
- 配图 ≥ 2 张且风格一致 → 合并
- 封面图 → 单独调用（门面，不缩水）
- 配图仅 1 张 → 单独调用

**流程**：

1. 构建合并 prompt：描述 N 格纵向排列，每格一张配图场景。"PANEL 1 (top): ... PANEL 2 (middle): ... PANEL 3 (bottom): ... Subtle visual separation with thin horizon lines between panels."
2. POST 请求：`{"model": "gpt-image-2", "prompt": "...", "n": 1, "size": "1024x1792"}`（竖版）
3. 下载合并图
4. Python 裁切：
```python
from PIL import Image
img = Image.open('combined.png')
w, h = img.size
panel_h = h // N
for i in range(N):
    y1 = i * panel_h
    y2 = (i + 1) * panel_h if i < N - 1 else h
    panel = img.crop((0, y1, w, y2))
    # 裁切后 ≈ 1024×597，接近 16:9，手机端够用
    panel.save(f'body-{i+1}.png', 'PNG', optimize=True)
```
5. 裁切后图片落盘文章目录

**失败处理**：合并图生成/裁切失败 → 降级为逐张调用（1b），不触发优先级 2。

#### 1b. 单张调用流程（封面图 / 配图仅 1 张 / 合并裁切失败降级）

1. 构建英文提示词（prompt 用英文，**画面输出文字必须简体中文**）
2. POST 请求，body: `{"model": "gpt-image-2", "prompt": "英文提示词", "n": 1, "size": "1792x1024"}`（16:9 横版）
3. Header: `Authorization: Bearer <api_key>`, `Content-Type: application/json`
4. 超时 ≥ 180s，等待返回
5. 从响应解析 `r['data'][0]['url']` 获取图片 URL
6. 下载图片到文章目录

**失败判定**（任一触发即降级到优先级 2）：
- 超时无响应
- 返回错误
- `data[0].url` 不存在
- 图片下载失败

### 优先级 2：即梦网页版（降级）

> 降级到这级时打日志："gpt-image-2 生图失败（{原因}），降级到即梦网页版。"

即梦网址：`https://jimeng.jianying.com/ai-tool/image/generate`

浏览器自动化操作：打开页面 → 登录（如过期）→ 填提示词 → 选 16:9 → 生成 → 下载。详细流程：ChromeDevTools 模拟键鼠。

**提示词**：中文（即梦对中文理解更好）。

**失败判定**（任一触发即降级到优先级 3）：
- 网页崩溃/超时/账号异常
- 生成超时 > 5 分钟

### 优先级 3：生成提示词 txt（兜底）

> 降级到这级时打日志："即梦生图失败（{原因}），生成提示词 txt。"

生成 `image-prompts.txt` 到文章目录，内容包含：
- 封面图提示词（英文 + 中文）
- 每张配图提示词（英文 + 中文 + 绑定段落 + 推荐比例）
- 失败原因标注

供人工手动生图后补入，不阻断流程。

---

## 二、Step 5.0：查参考提示词库（生图前执行，不可跳过）

397 个已验证案例 + 20+ 套可复用模板，覆盖 13 个分类。直接参考比从零写效果好得多。

### 第 1 步：匹配分类

根据文章主题确定对应的 gallery 分类：

| 文章类型 | 匹配分类 | 用途 |
|---------|---------|------|
| 工具/产品上手 | UI & Interfaces / Products & E-commerce | 产品界面图、功能展示 |
| 新闻/趋势解读 | Charts & Infographics / Posters & Typography | 信息图、数据可视化 |
| 观点/方法论 | Illustration & Art / Photography & Realism | 概念插画、隐喻图 |
| 所有类型（封面） | Posters & Typography / Scenes & Storytelling | 封面图参考 |

### 第 2 步：查案例

用 web_fetch 拉取匹配分类的案例：

- 案例索引：`https://raw.githubusercontent.com/freestylefly/awesome-gpt-image-2/main/docs/gallery.md`
- 分册 1（Case 1-165）：`https://raw.githubusercontent.com/freestylefly/awesome-gpt-image-2/main/docs/gallery-part-1.md`
- 分册 2（Case 166-400）：`https://raw.githubusercontent.com/freestylefly/awesome-gpt-image-2/main/docs/gallery-part-2.md`
- 模板（含 JSON Agent 格式）：`https://raw.githubusercontent.com/freestylefly/awesome-gpt-image-2/main/docs/templates.md`
- 可视化浏览：`https://gpt-image2.canghe.ai/#gallery`（看效果图，提示词在 GitHub）

每个案例结构：`[输出格式] + [主体+场景] + [内容清单] + [风格关键词栈] + [排除约束]`

### 第 3 步：提取模式

从 2-3 个匹配案例中提取：

| 提取项 | 说明 | 用法 |
|--------|------|------|
| 提示词结构顺序 | 该分类先说什么后说什么 | 本文提示词的骨架 |
| 风格关键词栈 | 该分类常用形容词链（如 "engineering white paper + scientific atlas, crisp lines, 8K"） | 直接复用 |
| 负面约束 | 该分类常见的 "no X / must show Y / avoid Z" | 加到禁止元素 |
| 比例约定 | 该分类最常用的宽高比 | 确认 16:9 是否合适 |

### 第 4 步：构建本文提示词

将提取的模式作为骨架，填入文章具体内容。每张图五段结构：

1. 输出格式
2. 主体 + 场景/动作
3. 内容清单（标注、标题、说明文字用**简体中文**）
4. 风格关键词栈（有具体参照案例，不凭空编造）
5. 负面约束（排除该分类常见的生成问题，**包含"no English text labels"**）

**提示词构建规则**（适用 API 和即梦两级）：
- 每张配图绑定一个具体段落或概念，不是装饰性插图
- 提示词结构：主体 + 场景/动作 + 风格 + 情绪 + 禁止元素
- 避免抽象概念直译（如"AI焦虑"→ 用人+环境表达，不画一颗脑子）
- 封面图和所有配图保持一致的视觉风格（科技感、现代感、干净）

生成前自检：
- [ ] 每张图的提示词包含完整五段
- [ ] 画面文字语言约束已注入：标注/标题/标签 → 简体中文；代码/专有名词 → 保留原文
- [ ] 风格关键词有具体参照案例（不是凭空编造）
- [ ] 负面约束到位，**包含"no long English paragraphs"**
- [ ] 封面图与配图风格一致（来自同一批案例的风格参考）

> 跳过此步直接写提示词 → 质量无保障。

---

## 三、风格一致性

- 封面图和所有配图保持一致的视觉风格
- 风格关键词来自同一批案例参考
- 16:9 横版，科技感、现代感、干净

---

## 四、生成清单

| # | 内容 | 要求 |
|---|------|------|
| 1 | 封面图 ×1 | 文件名以「封面」开头，确保目录中一眼可识别 |
| 2 | 配图 ×2+ | 每张绑定具体段落或概念，不是装饰性插图 |
| 3 | 文件名 | 英文或拼音，不含中文（避免 Markdown 引用路径问题） |
| 4 | 保存位置 | 所有图片保存到文章目录（与 md 文件同目录） |
| 5 | **封面图置顶** | **文章正文第一行插入 `![](cover.png)`，确保封面图内嵌到正文首位**——微信发布时可直接右键设为封面，无需二次上传 |

---

## 五、失败处理

- gpt-image-2 失败 → 日志："gpt-image-2 生图失败（{原因}），降级到即梦网页版。"
- 即梦失败 → 日志："即梦生图失败（{原因}），生成提示词 txt。"
- 仅 txt 时：流程继续但终审第 8 项标记"配图待补"

**通过标准**：封面图 1 张 + 配图 ≥ 2 张，全部生成并保存到文章目录。仅 txt 时不视为通过但也不阻断流程。

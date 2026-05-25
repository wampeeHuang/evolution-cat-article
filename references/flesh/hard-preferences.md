# 硬偏好

> 血肉层，≤5 条。从 voice-signals 晋升（置信度 ≥ 3 + 用户确认）。

## 数据结构

```yaml
- preference: "偏好描述"
  type: must_do | must_avoid | character_choice
  source_signal: "S001"       # 来源信号 ID
  confirmed: "YYYY-MM-DD"
```

## 容量控制

- 上限 5 条
- 新晋升挤掉最旧的
- 元审计发现与近期 5 篇风格不符 → 降级回 voice-signals

---

## 硬偏好列表

（初始为空）

<!-- PREFERENCES_START -->

- preference: "锚点先行——引入任何读者可能不熟悉的专有名词/概念/人名前，先用已知概念当踏脚石。Red Hat→先说'一家把免费Linux打包成企业产品的公司'再说名字。Harness→先说'Agent去掉模型那层'再下定义。类比在前术语在后，故事在名字前。"
  type: must_do
  source_signal: "S004"
  confirmed: "2026-05-22"

<!-- PREFERENCES_END -->

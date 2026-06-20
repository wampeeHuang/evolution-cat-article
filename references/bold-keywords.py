"""加粗规则优先级：

1. 对比/反转句：不是X而是Y / 不是X，是Y / 不在X在Y
2. 短判定句（10-28中文字）：长篇叙述后的独立 punchline
3. 锚词句：本质/真正/根本/核心/关键 等强判断
4. 总结句：可以说/一句话/说白了/归根结底/这意味着

跳过：已加粗句 / 引用块内 / 标题行 / 图片行 / 代码块
"""


import re
import sys

def is_heading(line):
    return bool(re.match(r'^#{1,6}\s', line))

def is_in_blockquote(lines, idx):
    for j in range(idx, -1, -1):
        if lines[j].strip() == '':
            continue
        return lines[j].startswith('>')
    return False

def is_in_image_line(line):
    return bool(re.match(r'^!\[.*\]\(.*\)', line))

def count_chinese_chars(text):
    return len(re.findall(r'[一-鿿]', text))

def should_bold(sentence, prev_sentence='', next_sentence=''):
    text = sentence.strip()
    if not text or len(text) < 6:
        return False

    # Skip already bolded (check first 4 chars for ** markers)
    if '**' in text[:4]:
        return False

    cc = count_chinese_chars(text)

    # Incomplete contrast first half: "问题不在AI。" alone needs "在..." continuation
    if re.search(r'不在[^，。；]{0,8}。$', text):
        return False
    # Also check: standalone "...不在X。" where X is short (<=3 chars)
    if re.match(r'^[^。]{0,6}不在[^，。；]{1,3}。$', text):
        return False

    # Rule 1: Contrast patterns
    contrast_patterns = [
        r'不是[^，。；]*而是',
        r'不是[^，。；]*，是',
        r'不在[^，。；]*在[^，。]',
        r'问题不[^，。；]*[在是]',
        r'关键不是[^，。；]*是',
    ]
    for pat in contrast_patterns:
        if re.search(pat, text):
            return True

    # Rule 2: Short punch line (10-28 Chinese chars)
    if 10 <= cc <= 28:
        if re.match(r'^[这那所AI你在问因如]', text) and count_chinese_chars(prev_sentence) >= 25:
            return True

    # Rule 3: Anchor words
    anchor_words = ['本质上是', '真正的区别', '根本原因', '核心不在', '关键是', '最难的是']
    for aw in anchor_words:
        if aw in text:
            return True

    # Rule 4: Summary punch
    summary_starters = ['可以说', '一句话', '说白了', '归根结底', '本质上', '这意味着']
    for ss in summary_starters:
        if text.startswith(ss) and cc <= 35:
            return True

    return False

def split_sentences(paragraph):
    """Split a paragraph into sentences by Chinese punctuation markers."""
    # Split on  。；！？ but keep the delimiter
    parts = re.split(r'(?<=[。；！？])', paragraph)
    return [p for p in parts if p.strip()]

def process_markdown(content):
    """Process markdown content and bold key sentences."""
    lines = content.split('\n')
    output_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]

        # Skip headings, images, empty lines, blockquotes, hr, HTML
        if (is_heading(line) or is_in_image_line(line) or
            line.strip() == '' or line.strip().startswith('>') or
            line.strip() == '---' or line.strip() == '--' or
            line.strip().startswith('```') or line.strip().startswith('<!--') or
            line.strip().startswith('<p ') or line.strip().startswith('</') or
            line.strip().startswith('<')):
            output_lines.append(line)
            i += 1
            continue

        # Process paragraph text (non-special lines)
        # Collect the full paragraph
        para_lines = []
        j = i
        while j < len(lines):
            l = lines[j]
            if (is_heading(l) or is_in_image_line(l) or
                l.strip() == '' or l.strip().startswith('>') or
                l.strip() == '---' or l.strip() == '--' or
                l.strip().startswith('```') or l.strip().startswith('<!--') or
                l.strip().startswith('<p ') or l.strip().startswith('</') or
                l.strip().startswith('<')):
                break
            para_lines.append(l)
            j += 1

        if para_lines:
            para_text = ' '.join(pl.strip() for pl in para_lines)
            sentences = split_sentences(para_text)

            if len(sentences) >= 2:
                bolded_sentences = []
                for si, s in enumerate(sentences):
                    prev = sentences[si-1] if si > 0 else ''
                    next_s = sentences[si+1] if si < len(sentences)-1 else ''

                    # Skip if already bolded
                    if s.strip().startswith('**') and s.strip().endswith('**'):
                        bolded_sentences.append(s)
                        continue

                    if should_bold(s, prev, next_s):
                        bolded_sentences.append(f'**{s}**')
                    else:
                        bolded_sentences.append(s)

                # Rebuild paragraph
                output_lines.append(''.join(bolded_sentences))
            else:
                # Single sentence paragraph - still check
                s = para_text.strip()
                if should_bold(s) and not (s.startswith('**') and s.endswith('**')):
                    output_lines.append(f'**{s}**')
                else:
                    output_lines.extend(para_lines)

            i = j
        else:
            i += 1

    return '\n'.join(output_lines)

def find_candidates(content):
    """Dry run: find all candidate sentences without modifying."""
    lines = content.split('\n')
    candidates = []
    line_no = 0
    for i, line in enumerate(lines):
        if (is_heading(line) or is_in_image_line(line) or
            line.strip() == '' or line.strip().startswith('>') or
            line.strip() == '---' or line.strip() == '--' or
            line.strip().startswith('```') or line.strip().startswith('<!--') or
            line.strip().startswith('<p ') or line.strip().startswith('</') or
            line.strip().startswith('<')):
            continue

        sentences = split_sentences(line.strip())
        for s in sentences:
            s = s.strip()
            if not s:
                continue
            # Find approximate line number
            if should_bold(s):
                candidates.append((i+1, s[:80]))

    return candidates


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python bold-keywords.py <markdown_file> [--apply]")
        sys.exit(1)

    filepath = sys.argv[1]
    apply_flag = '--apply' in sys.argv

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    candidates = find_candidates(content)
    print(f"=== 候选加粗句 ({len(candidates)} 处) ===\n")
    for ln, text in candidates:
        print(f"  L{ln}: {text}")

    if apply_flag:
        result = process_markdown(content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(result)
        print(f"\n[DONE] Written to {filepath}")
    else:
        print(f"\n[DRY RUN] Add --apply to write.")

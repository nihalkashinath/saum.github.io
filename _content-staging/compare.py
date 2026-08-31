#!/usr/bin/env python3
"""Compare extracted content with markdown file to find differences."""

import difflib

# Read extracted content
with open('_content-staging/extracted-content.txt', 'r', encoding='utf-8') as f:
    extracted_lines = f.readlines()

# Read markdown file (skip front matter)
with open('_posts/2026-09-01-complete-guide-ayodhya-varanasi-pilgrimage.md', 'r', encoding='utf-8') as f:
    md_lines = f.readlines()
    
# Skip front matter in markdown (lines between --- markers)
md_start = 0
for i, line in enumerate(md_lines):
    if i > 0 and line.strip() == '---':
        md_start = i + 1
        break

md_content = md_lines[md_start:]

# Find differences
differ = difflib.unified_diff(
    md_content,
    extracted_lines,
    fromfile='markdown',
    tofile='extracted',
    lineterm=''
)

differences = list(differ)
if differences:
    print("Found differences:")
    for line in differences[:50]:  # Show first 50 lines of diff
        print(line)
else:
    print("No differences found in content")

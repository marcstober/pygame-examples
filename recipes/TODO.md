# Some ideas from Copilot about how to display the diffs between template.py and the other examples


---

### 🐍 Python + Rich Library (Markdown + Syntax Highlighting)

You can use the [`rich`](https://github.com/Textualize/rich) library to generate beautiful diffs with Python syntax highlighting right in the terminal or exportable to HTML:

```python
from rich.console import Console
from rich.syntax import Syntax
from rich.diff import Diff

console = Console()

with open("file1.py") as f1, open("file2.py") as f2:
    code1 = f1.read()
    code2 = f2.read()

diff = Diff(code1, code2, language="python")
console.print(diff)
```

This gives you a colorized diff with Python syntax awareness — perfect for terminal viewing or capturing as HTML with `console.export_html()`.

---

### 🧰 HTML Output with Inline Highlighting

If you want to share the diff in a browser or embed it in a Markdown file with HTML support, you can use `difflib.HtmlDiff`:

```python
import difflib

with open("file1.py") as f1, open("file2.py") as f2:
    lines1 = f1.readlines()
    lines2 = f2.readlines()

html_diff = difflib.HtmlDiff().make_file(lines1, lines2, fromdesc="file1.py", todesc="file2.py")

with open("diff_output.html", "w") as output:
    output.write(html_diff)
```

This creates a side-by-side HTML diff with inline changes. You can then add syntax highlighting using a library like [highlight.js](https://highlightjs.org/) or [Pygments](https://pygments.org/) if you want to style it further.

---

### 🌐 Online Tools That Support Python Highlighting

- [TextDiffChecker](https://textdiffchecker.com/compare/python): Paste both files and get a side-by-side diff with Python syntax highlighting.
- [DiffChecker](https://www.diffchecker.com/python): Another solid option with syntax-aware rendering.
- [Mergely](https://www.mergely.com/): Real-time diff viewer with syntax support and embeddable output.

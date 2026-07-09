"""
Updates JSON file to the current work.

Current implementation:
- User manually selects an HTML file
- Parsed content is exported to JSON
- Flask reads JSON for display

Future goal:
- Accept an AO3 URL directly to generate JSON
"""

import json
from pathlib import Path

import parser_functions  # imports parser_functions.py (because it's in the same folder)

def export_work_to_json(html_file: str | Path, out_file: str | Path) -> None:
    html_file = Path(html_file)
    out_file = Path(out_file)

    soup = parser_functions.load_soup(html_file)

    data = {
        "tags": parser_functions.extract_tags(soup),
        "title": parser_functions.extract_title(soup),
        "author": parser_functions.extract_author(soup),
        "summary": parser_functions.extract_summary(soup),
        "story_chapters": parser_functions.extract_chapters(soup),
    }

    with out_file.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"Wrote: {out_file}")


if __name__ == "__main__":
    html_path = Path("Works") / "Broooooo.html"
    out_path = Path("current_work.json")
    export_work_to_json(html_path, out_path)
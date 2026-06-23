import json
from pathlib import Path

import ao3_parser  # imports ao3_parser.py (because it's in the same folder)

def export_work_to_json(html_file: str | Path, out_file: str | Path) -> None:
    html_file = Path(html_file)
    out_file = Path(out_file)

    soup = ao3_parser.load_soup(html_file)

    data = {
        "tags": ao3_parser.extract_tags(soup),
        "title": ao3_parser.extract_title(soup),
        "author": ao3_parser.extract_author(soup),
        "summary": ao3_parser.extract_summary(soup),
        "story_chapters": ao3_parser.extract_chapters(soup),
    }

    with out_file.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"Wrote: {out_file}")


if __name__ == "__main__":
    html_path = Path("Works") / "Never_knew_it.html"
    out_path = Path("test.json")
    export_work_to_json(html_path, out_path)
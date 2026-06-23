from pathlib import Path
from bs4 import BeautifulSoup

# soup param refers to the loaded work!!
# so work = load_soup, and soup == work when calling

def load_soup(html_path):
    with open(html_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        return soup

def extract_tags(soup): # this one needs more review!!
    tag_class = soup.find("dl", class_="tags")
    class_children = tag_class.find_all(["dt", "dd"], recursive = False)

    current_label = None
    tags = {}

    for child in class_children:
        if child.name == "dt":
            current_label = child.get_text(strip=True)
            tags[current_label] = []
        elif child.name == "dd" and current_label is not None:
            tags[current_label].append(child.get_text(strip=True))
    return tags

def extract_title(soup):
    meta = soup.find("div", class_="meta")
    title = meta.find('h1').get_text(strip=True)
    return title

def extract_author(soup):
    by_line = soup.find("div", class_="byline")
    author = by_line.find('a').get_text(strip=True)
    return f"by {author}"

def extract_summary(soup):
    blockquote = soup.find("blockquote", class_="userstuff")
    summary = blockquote.find_all('p')
    return [p.get_text(strip=True) for p in summary]

def extract_paragraphs(soup):
    userstuff = soup.find("div", class_="userstuff")
    paragraphs = userstuff.find_all('p')
    return [p.get_text(strip=True) for p in paragraphs]

def extract_chapters(soup):
    chapters_div = soup.find(id="chapters")
    print("Has #chapters:", chapters_div is not None) # delete debug

    if chapters_div is None:
        return []

    chapters_list = []
    headings = chapters_div.find_all("h2", class_="heading")
    print("Heading count:", len(headings)) # delete debug


    # --- ONE-SHOT FALLBACK ---
    if len(headings) == 0:
        # grab the first userstuff content div inside chapters
        content_div = chapters_div.find("div", class_="userstuff")
        if content_div is None:
            return []

        paragraphs = [p.get_text(strip=True) for p in content_div.find_all("p")]

        chapters_list.append({
            "title": "One-shot",
            "paragraphs": paragraphs
        })
        return chapters_list

    # --- MULTI-CHAPTER ---
    for h2 in headings:
        title = h2.get_text(strip=True)
        meta_block = h2.find_parent("div")
        if meta_block is None:
            continue

        content_div = meta_block.find_next(
            lambda tag: tag.name == "div" and "userstuff" in (tag.get("class") or [])
        )
        if content_div is None:
            continue

        paragraphs = [p.get_text(strip=True) for p in content_div.find_all("p")]

        chapters_list.append({
            "title": title,
            "paragraphs": paragraphs
        })

    return chapters_list

def parse_work(soup):
    return {
        "title": extract_title(soup),
        "author": extract_author(soup),
        "tags": extract_tags(soup),
        "summary": extract_summary(soup),
        "chapters": extract_chapters(soup),
    }

work = load_soup("works/Never_knew_it.html")
data = parse_work(work)

# title, author
print(data["title"])
print(data["author"])
print()

# tags
for label, values in data["tags"].items():
    print(f"{label} ({', '.join(values)})")

print()

#summary
for p in data["summary"]:
    print(p)

print()

#chapters
chapters = data["chapters"]
print(f"Chapters found: {len(chapters)}\n")

for i, chapter in enumerate(chapters, start=1):
    print(f"{i}. {chapter['title']}")
    print(f"Paragraphs: {len(chapter['paragraphs'])}")
    print("-" * 40)



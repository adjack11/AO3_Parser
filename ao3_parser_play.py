# from bs4 import BeautifulSoup
#
# with open("works/love_us_together.html", 'r', encoding="utf-8") as f:
#     soup = BeautifulSoup(f.read(), "html.parser")
#
#     # f = file object. represents contents of the HTML file. Think of it as a stream of text coming from the file
#     # BeautifulSoup(f, "html.parser") creates BS object, HTML content (f), and instructions on how to read 'html.parser' which is from bs4 not vanilla python
#     # html parser tells BS to interpret the text using HTML rules (lxml, but worry abt later)
#     # soup is a parsed DOM tree of th HTML which makes the text structured and can find diff things like <h2>, <p>, etc
#
# # title = soup.find("h1", class_="meta").get_text(strip=True) this looks for a <h1> with a class attribute "meta"
# # h1 doesn't havea class attribute at all, but is under the div.meta (div of class meta)
#
# meta = soup.find("div", class_="meta")
# title = meta.find('h1').get_text(strip=True)
#
# print(title)
#
# # step 1 find the div and its class
# # step 2, find the elements you want under the class, 2-step process if the tag has no attributes
# # if tag has a class, you can stop at step one
#
# userstuff = soup.find("div", class_="userstuff")
# paragraphs = userstuff.find_all('p')
# for paragraph in paragraphs:
#     print(paragraph.get_text(strip=True))

# ------------------------------------------------------ #
from bs4 import BeautifulSoup

# soup param refers to the loaded work!!
# so work = load_soup, and soup == work when calling

def load_soup(html_path):
    with open(html_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        return soup

def extract_tags(soup):
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
    userstuff = soup.find("div", id="chapters", class_="userstuff")
    # list of dictionaries, each chap is item in list and key-vale pairs = chap name, chap summary, title, content
    chapters_list = []
    individual_chapter = {}
    individual_chapter
    return chapter

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

print(data)
print(data["title"])
print(data["author"])
print(data["summary"]

Notes Tha
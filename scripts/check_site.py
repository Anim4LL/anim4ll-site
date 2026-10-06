"""Check static pages and their local resources without third-party packages."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import argparse
import re


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path = path
        self.ids = set()
        self.refs = []
        self.h1 = 0
        self.lang = None
        self.images = 0
        self.title = False
        self.feed(path.read_text(encoding="utf-8"))

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            if attrs["id"] in self.ids:
                raise ValueError(f"{self.path.name}: duplicate ID {attrs['id']}")
            self.ids.add(attrs["id"])
        if tag == "html":
            self.lang = attrs.get("lang")
        if tag == "h1":
            self.h1 += 1
        if tag == "title":
            self.title = True
        for name in ("href", "src"):
            if name in attrs:
                self.refs.append(attrs[name])
        if "srcset" in attrs:
            self.refs.extend(part.strip().split()[0] for part in attrs["srcset"].split(","))
        if tag == "img":
            self.images += 1
            for name in ("src", "alt", "width", "height"):
                if name not in attrs:
                    raise ValueError(f"{self.path.name}: image missing {name}")
            if int(attrs["width"]) <= 0 or int(attrs["height"]) <= 0:
                raise ValueError("Image dimensions must be positive")


def check(root):
    pages = {path.resolve(): Page(path) for path in root.glob("*.html")}
    if not pages:
        raise ValueError("No HTML pages found")
    checked = 0
    for path, page in pages.items():
        if page.lang != "pt-BR" or page.h1 != 1 or not page.title:
            raise ValueError(f"{path.name}: check language, title and unique h1")
        if "conteudo" not in page.ids or "#conteudo" not in page.refs:
            raise ValueError(f"{path.name}: missing skip-link destination")
        for ref in page.refs:
            url = urlsplit(ref)
            if url.scheme or url.netloc:
                continue
            if url.path.startswith("/"):
                raise ValueError(f"{path.name}: absolute path incompatible with file opening: {ref}")
            target = (path.parent / (unquote(url.path) or path.name)).resolve()
            if not target.is_relative_to(root) or not target.is_file():
                raise ValueError(f"{path.name}: missing or unsafe resource: {ref}")
            if url.fragment and (target not in pages or unquote(url.fragment) not in pages[target].ids):
                raise ValueError(f"{path.name}: missing anchor: {ref}")
            checked += 1
        print(f"PASS {path.name}: {page.images} images; local resources and anchors")
    for css in root.glob("*.css"):
        for ref in re.findall(r"url\(\s*['\"]?([^)'\"]+)", css.read_text(encoding="utf-8")):
            if not urlsplit(ref).scheme and not (css.parent / ref).is_file():
                raise ValueError(f"{css.name}: missing resource {ref}")
    print(f"PASS {len(pages)} pages, {checked} local references. No build required.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        check(args.root.resolve())
    except (ValueError, OSError) as error:
        parser.exit(1, f"FAIL: {error}\n")

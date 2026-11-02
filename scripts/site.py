"""Prepare shared resources, build both languages, and preview the combined site."""

import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
LANGUAGES = {"en": "zensical.toml", "ko": "zensical.ko.toml"}
SITEMAP_NS = "http://www.sitemaps.org/schemas/sitemap/0.9"


class PreviewHandler(SimpleHTTPRequestHandler):
    """Mirror GitHub Pages: serve the root 404.html with HTTP status 404."""

    def send_error(self, code, message=None, explain=None):
        error_page = Path(self.directory) / "404.html"
        if code != 404 or not error_page.is_file():
            return super().send_error(code, message, explain)
        body = error_page.read_bytes()
        self.send_response(404)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("X-Robots-Tag", "noindex, follow")
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(body)


def prepare():
    # The page-preserving language selector requires matching source paths.
    english = {p.relative_to(ROOT / "docs/en") for p in (ROOT / "docs/en").rglob("*.md") if "assets" not in p.parts}
    korean = {p.relative_to(ROOT / "docs/ko") for p in (ROOT / "docs/ko").rglob("*.md") if "assets" not in p.parts}
    if english != korean:
        raise ValueError(
            "Language paths must match. Missing English: "
            f"{sorted(map(str, korean - english))}; missing Korean: "
            f"{sorted(map(str, english - korean))}"
        )
    # Generated copies keep relative image links identical in both editions.
    for language in LANGUAGES:
        for resource in ("assets", "stylesheets"):
            destination = ROOT / "docs" / language / resource
            if destination.exists():
                shutil.rmtree(destination)
            shutil.copytree(ROOT / "docs" / resource, destination)


def build():
    prepare()
    # English cleans site/ first; Korean then builds into site/ko/.
    for config in LANGUAGES.values():
        subprocess.run(
            [sys.executable, "-m", "zensical", "build", "--clean", "--strict", "-f", config],
            cwd=ROOT,
            check=True,
        )
    # Publish a single sitemap covering both independently built editions.
    sitemap = ROOT / "site" / "sitemap.xml"
    english = ET.parse(sitemap)
    korean = ET.parse(ROOT / "site" / "ko" / "sitemap.xml")
    english.getroot().extend(korean.getroot())
    ET.register_namespace("", SITEMAP_NS)
    english.write(sitemap, encoding="utf-8", xml_declaration=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("prepare", "build", "serve"))
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()
    if args.command == "prepare":
        prepare()
        return
    build()
    if args.command == "serve":
        handler = partial(PreviewHandler, directory=str(ROOT / "site"))
        with ThreadingHTTPServer(("127.0.0.1", args.port), handler) as server:
            print(f"Preview: http://127.0.0.1:{args.port} (rebuild after editing)", flush=True)
            try:
                server.serve_forever()
            except KeyboardInterrupt:
                pass


if __name__ == "__main__":
    main()

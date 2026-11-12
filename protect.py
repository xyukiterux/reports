"""Shared 'protect' step for the public sites (owner 11-10): copyright LICENSE + no-AI-training tags on every page.
It deters crawlers and states the rights; it cannot stop a person copying a public page."""
import os, re
META = '<meta name="robots" content="noai, noimageai, noarchive"><meta name="googlebot" content="noarchive">'
LICENSE = """Copyright (c) 2026 Yukiteru. All rights reserved.

The content, data, layouts and code on this site are published for personal viewing only.
No licence is granted to copy, modify, redistribute, re-host, or use any part of it,
including to train or prompt AI models or to generate derivative sites, without written permission.
"""
AI_TXT = "# No AI training, scraping or derivative generation.\nUser-agent: *\nDisallow: /\n"

def protect(site):
    with open(os.path.join(site, "LICENSE"), "w", encoding="utf-8", newline="\n") as f: f.write(LICENSE)
    with open(os.path.join(site, "ai.txt"), "w", encoding="utf-8", newline="\n") as f: f.write(AI_TXT)
    n = 0
    for root, dirs, files in os.walk(site):
        dirs[:] = [d for d in dirs if d != ".git"]
        for fn in files:
            if fn.endswith(".html"):
                p = os.path.join(root, fn)
                t = open(p, encoding="utf-8", errors="replace").read()
                if 'content="noai' in t: continue
                t2, k = re.subn(r"(<head[^>]*>)", r"\1" + META, t, count=1, flags=re.I)
                if k: open(p, "w", encoding="utf-8", newline="").write(t2); n += 1
    return n

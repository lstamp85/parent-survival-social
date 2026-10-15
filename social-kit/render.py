# Python/Playwright equivalent of render.mjs, used for the PS-W1 batch.
# Usage: python3 render.py  -> writes ../posts/<post-id>/*.png
import pathlib
from playwright.sync_api import sync_playwright

KIT = pathlib.Path(__file__).resolve().parent
OUT = KIT.parent / "posts"
SIZES = ["1080x1350", "1080x1080", "1080x1920", "1200x628"]
JOBS = [("PS-W1-01", "4A", "out-the-door"), ("PS-W1-03", "4C", "free-check-in")]

with sync_playwright() as p:
    b = p.chromium.launch()
    ctx = b.new_context(ignore_https_errors=True)
    pg = ctx.new_page()
    for post, cid, slug in JOBS:
        d = OUT / post; d.mkdir(parents=True, exist_ok=True)
        for s in SIZES:
            w, h = map(int, s.split("x"))
            pg.set_viewport_size({"width": w, "height": h})
            pg.goto(f"{(KIT/'template.html').as_uri()}?id={cid}&size={s}", wait_until="networkidle")
            pg.evaluate("document.fonts.ready")
            pg.screenshot(path=str(d / f"{post}-{slug}-{s}.png"), clip={"x": 0, "y": 0, "width": w, "height": h})
    d = OUT / "PS-W1-02"; d.mkdir(parents=True, exist_ok=True)
    pg.set_viewport_size({"width": 1080, "height": 1350})
    for i in range(1, 7):
        pg.goto(f"{(KIT/'carousel.html').as_uri()}?slide={i}", wait_until="networkidle")
        pg.evaluate("document.fonts.ready")
        pg.screenshot(path=str(d / f"PS-W1-02-slide{i}-1080x1350.png"), clip={"x": 0, "y": 0, "width": 1080, "height": 1350})
    b.close()
print("done")

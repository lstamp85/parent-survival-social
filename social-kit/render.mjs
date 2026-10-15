// Export every concept × size to PNG.
// Usage: npm i puppeteer && node render.mjs   → writes ./out/<id>-<name>-<size>.png
import puppeteer from 'puppeteer';
import { pathToFileURL } from 'node:url';
import fs from 'node:fs';
import vm from 'node:vm';

const ctx = { window: {} };
vm.runInNewContext(fs.readFileSync('concepts.js', 'utf8'), ctx);
const concepts = ctx.window.CONCEPTS;
const sizes = ['1200x628', '1080x1920', '1080x1350', '1080x1080'];
const base = pathToFileURL('template.html').href;
fs.mkdirSync('out', { recursive: true });

const browser = await puppeteer.launch();
const page = await browser.newPage();
for (const c of concepts) {
  for (const s of sizes) {
    const [w, h] = s.split('x').map(Number);
    await page.setViewport({ width: w, height: h, deviceScaleFactor: 1 });
    await page.goto(`${base}?id=${c.id}&size=${s}`, { waitUntil: 'networkidle0' });
    await page.evaluate(() => document.fonts.ready);
    const slug = c.name.toLowerCase().replace(/[^a-z0-9]+/g, '-');
    await page.screenshot({ path: `out/${c.id}-${slug}-${s}.png`, clip: { x: 0, y: 0, width: w, height: h } });
    console.log('✓', c.id, s);
  }
}
await browser.close();

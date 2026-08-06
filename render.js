const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const dir = '.';
  const fileUrl = 'file://' + path.join(dir, 'parichay-patra-kaptan-singh.html');

  const browser = await chromium.launch({ args: ['--no-sandbox'] });
  const page = await browser.newPage({ viewport: { width: 900, height: 1200 }, deviceScaleFactor: 2 });

  await page.goto(fileUrl, { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(600);

  // PDF (A4, with backgrounds)
  await page.pdf({
    path: path.join(dir, 'Bio-Data-Kaptan-Singh.pdf'),
    format: 'A4',
    printBackground: true,
    margin: { top: '0', bottom: '0', left: '0', right: '0' },
  });
  console.log('PDF saved');

  // Full preview PNG
  await page.screenshot({
    path: path.join(dir, 'Bio-Data-Preview.png'),
    fullPage: true,
  });
  console.log('Full PNG saved');

  // Page-1 only PNG (main page, for quick sharing)
  const firstPage = page.locator('.page').first();
  await firstPage.screenshot({ path: path.join(dir, 'Bio-Data-Page1.png') });
  console.log('Page1 PNG saved');

  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });

const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const dir = '/projects/sandbox/Virali_insta_facebook_account';
  const fileUrl = 'file://' + path.join(dir, 'bio-data-gemini.html');

  const browser = await chromium.launch({ args: ['--no-sandbox'] });
  const page = await browser.newPage({ viewport: { width: 900, height: 1400 }, deviceScaleFactor: 2 });

  await page.goto(fileUrl, { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(800);

  await page.pdf({
    path: path.join(dir, 'Bio-Data-Kaptan-Singh-Gemini.pdf'),
    format: 'A4',
    printBackground: true,
    margin: { top: '0', bottom: '0', left: '0', right: '0' },
  });
  console.log('PDF saved');

  await page.screenshot({ path: path.join(dir, 'Bio-Data-Gemini-Preview.png'), fullPage: true });
  console.log('PNG saved');

  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });

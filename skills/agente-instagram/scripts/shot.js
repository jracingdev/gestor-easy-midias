// Renderiza cada .html da pasta em PNG e confere se o conteúdo invade a bandeira/rodapé.
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
(async () => {
  const dir = process.argv[2], out = process.argv[3]; fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch();
  for (const f of fs.readdirSync(dir).filter(f => f.endsWith('.html') && (!process.argv[4] || f.includes(process.argv[4])))) {
    const h = f.includes('story') ? 1920 : 1080;
    const p = await b.newPage({ viewport: { width: 1080, height: h } });
    await p.goto('file://' + path.resolve(dir, f)); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(150);
    const m = await p.evaluate(() => ({ chips: Math.round(document.querySelector('.chips').getBoundingClientRect().bottom), flag: Math.round(document.querySelector('.flag').getBoundingClientRect().top), sw: document.documentElement.scrollWidth }));
    console.log(f, JSON.stringify(m), m.chips > m.flag - 10 ? 'ESTOURO' : '');
    await p.screenshot({ path: path.join(out, f.replace('.html', '.png')) }); await p.close();
  }
  await b.close();
})();

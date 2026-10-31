// Short vertical 1080x1920 a partir da arte de story: entra cada bloco em sequência, foto com zoom lento,
// chuva caindo (quando houver) e pulso no WhatsApp no fim. Uso: node video.js <story.html> <saida.mp4> "<seletores em ordem>"
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path'), { execFileSync } = require('child_process');
const FPS = 30, DUR = 15;
(async () => {
  const [src, out, sel] = process.argv.slice(2);
  const frames = path.join(path.dirname(out), 'frames-' + path.basename(out, '.mp4'));
  fs.rmSync(frames, { recursive: true, force: true }); fs.mkdirSync(frames, { recursive: true });
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  await p.goto('file://' + path.resolve(src)); await p.evaluate(() => document.fonts.ready);
  await p.evaluate((sel) => {
    const seq = [];
    const add = (els, gap) => els.forEach(el => seq.push({ el, gap }));
    add([...document.querySelectorAll('.top')], 0.3);
    add([...document.querySelectorAll('h1')], 0.5);
    add([...document.querySelectorAll('.sub')], 1.2);
    sel.split('|').forEach(s => add([...document.querySelectorAll(s)], 0.55));
    add([...document.querySelectorAll('.chip')], 0.4);
    let t = 0;
    seq.forEach(s => { t += s.gap; s.at = t; s.el.style.willChange = 'opacity,transform'; });
    const ph = document.querySelector('.photo'), drops = [...document.querySelectorAll('.rain i')].map(i => ({ i, y: parseFloat(i.style.top) }));
    const cta = document.querySelector('.cta');
    window.render = (time) => {
      for (const s of seq) {
        const k = Math.max(0, Math.min(1, (time - s.at) / 0.45)), ease = 1 - Math.pow(1 - k, 3);
        s.el.style.opacity = ease; s.el.style.transform = `translateY(${(1 - ease) * 40}px)`;
      }
      ph.style.transform = `scale(${1.12 - 0.12 * time / 15})`;
      drops.forEach(d => { d.i.style.top = (((d.y + time * 1400) % 1050) - 120) + 'px'; });
      const pu = time > 12 ? Math.sin((time - 12) * Math.PI * 1.6) : 0;
      cta.style.transform = `scale(${1 + Math.max(0, pu) * 0.05})`; cta.style.transformOrigin = 'left center';
    };
  }, sel);
  for (let f = 0; f < FPS * DUR; f++) {
    await p.evaluate(t => window.render(t), f / FPS);
    await p.screenshot({ path: path.join(frames, String(f).padStart(4, '0') + '.jpg'), type: 'jpeg', quality: 92 });
  }
  await b.close();
  execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-framerate', String(FPS), '-i', path.join(frames, '%04d.jpg'),
    '-f', 'lavfi', '-i', 'anullsrc=r=44100:cl=stereo', '-shortest', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-profile:v', 'high',
    '-crf', '20', '-c:a', 'aac', '-b:a', '128k', '-movflags', '+faststart', out]);
  fs.rmSync(frames, { recursive: true, force: true });
  console.log('ok', out);
})();

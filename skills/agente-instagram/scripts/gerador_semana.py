# Gerador das artes da semana (feed 1080x1080 e story 1080x1920) no estilo Gestor Easy.
# Copie este arquivo para <pasta da semana>/_fonte/semana.py, troque as funções v_* e a lista T pelos temas novos e rode:
# python3 semana.py <pasta icones lucide> <pasta html>   (a pasta html precisa de logo.png e das fotos .webp)
# Os 6 temas abaixo (semana 03-08/11/2026) ficam como exemplo de visual e de texto.
import os, re, html, sys
ICONS, OUT = sys.argv[1], sys.argv[2]
R = '#ED3237'
e = html.escape


def icon(name, color='currentColor', size=24, sw=2):
    svg = open(os.path.join(ICONS, name + '.svg')).read()
    svg = re.sub(r'<!--.*?-->', '', svg, flags=re.S)
    svg = re.sub(r'class="[^"]*"', '', svg)
    svg = svg.replace('width="24"', f'width="{size}"').replace('height="24"', f'height="{size}"')
    return svg.replace('stroke="currentColor"', f'stroke="{color}"').replace('stroke-width="2"', f'stroke-width="{sw}"')


CSS = """
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:var(--H)}
body{background:#1E1C1D;font-family:'Inter',sans-serif;color:#fff;position:relative;overflow:hidden}
.photo{position:absolute;left:0;right:0;top:0;height:var(--PH);background-size:cover;background-position:var(--PP,center)}
.photo:after{content:'';position:absolute;inset:0;background:linear-gradient(180deg,rgba(30,28,29,.55) 0%,rgba(30,28,29,.5) 30%,rgba(30,28,29,.88) 70%,#1E1C1D 100%)}
.rain{position:absolute;left:0;right:0;top:0;height:var(--PH);overflow:hidden;opacity:.55}
.rain i{position:absolute;width:2px;background:linear-gradient(transparent,rgba(220,235,255,.9));transform:rotate(14deg)}
.stripes{position:absolute;top:-40px;right:-70px;width:420px;height:var(--SH)}
.stripes i{position:absolute;top:0;height:100%;transform:skewX(-28deg)}
.wrap{position:relative;padding:var(--PT) 62px 0}
.top{display:flex;align-items:center;gap:18px}
.lg{background:#fff;border-radius:16px;padding:8px 12px;display:flex;box-shadow:0 10px 30px -10px rgba(0,0,0,.6)}
.lg img{height:var(--LH)}
.tag{background:#ED3237;color:#fff;font-weight:800;font-size:var(--TG);letter-spacing:1.6px;padding:9px 18px;text-transform:uppercase}
h1{font-family:'Inter Display';font-weight:800;font-size:var(--FS);line-height:1.02;letter-spacing:-2.2px;margin-top:var(--H1);text-shadow:0 4px 24px rgba(0,0,0,.55)}
h1 .o{color:#ED3237}
.sub{font-size:var(--SB);font-weight:500;color:#D8D6D3;margin-top:14px;line-height:1.35;max-width:900px}
.vis{margin-top:var(--VM)}
.card{background:#fff;color:#2A2829;border-radius:20px;box-shadow:0 28px 60px -18px rgba(0,0,0,.8)}
.chips{display:grid;grid-template-columns:var(--CC);gap:12px;margin-top:var(--CM)}
.chip{display:flex;align-items:center;gap:12px;font-size:var(--PF);font-weight:700;background:rgba(255,255,255,.06);border:1.5px solid rgba(255,255,255,.14);border-radius:14px;padding:var(--CP) 16px;line-height:1.2}
.chip .ic{flex:0 0 auto;width:calc(var(--PF) * 1.9);height:calc(var(--PF) * 1.9);border-radius:10px;background:rgba(237,50,55,.16);display:flex;align-items:center;justify-content:center}
.flag{position:absolute;left:0;right:0;bottom:calc(var(--FO) + 104px);height:12px;background:repeating-conic-gradient(#fff 0 25%,#1E1C1D 0 50%) 0 0/12px 12px;opacity:.9}
.foot{position:absolute;left:0;right:0;bottom:var(--FO);height:104px;background:#2C2A2B;display:flex;align-items:center;justify-content:space-between;padding:0 62px 0 0}
.below{position:absolute;left:0;right:0;bottom:0;height:var(--FO);background:#2C2A2B}
.cta{height:100%;display:flex;align-items:center;gap:14px;background:#ED3237;color:#fff;padding:0 46px 0 62px;clip-path:polygon(0 0,100% 0,calc(100% - 34px) 100%,0 100%);font-weight:800;font-size:30px;font-family:'Inter Display'}
.cta small{display:block;font-family:'Inter';font-weight:600;font-size:15px;opacity:.9}
.site{display:flex;align-items:center;gap:12px;font-weight:700;font-size:25px;font-family:'Inter Display'}
.site small{display:block;font-family:'Inter';font-weight:500;font-size:15px;color:#BDBBB8}
.note{font-size:13px;color:#9A9794;margin-top:10px}
/* componentes dos visuais */
.hd{display:flex;align-items:center;gap:12px;padding:18px 22px;border-bottom:1.5px solid #ECEAE6;font-weight:800;font-size:calc(var(--K) * 20px)}
.hd small{display:block;font-weight:600;font-size:calc(var(--K) * 13px);color:#6B7079}
.hd .r{margin-left:auto}
.pill{display:inline-flex;align-items:center;gap:6px;white-space:nowrap;border-radius:999px;font-weight:800;font-size:calc(var(--K) * 13px);padding:5px 11px}
.p-red{background:#FFE3E3;color:#C21F26}.p-amb{background:#FFF1CC;color:#8A5A00}.p-gry{background:#EEEDEA;color:#55595F}
.p-blu{background:#E3EEFF;color:#1F4FA8}.p-grn{background:#DDF5E7;color:#17703F}.p-dark{background:#2A2829;color:#fff}
.row{display:grid;align-items:center;gap:12px;padding:calc(var(--K) * 12px) 22px;border-bottom:1px solid #F0EEEA;font-size:calc(var(--K) * 16px);font-weight:600}
.row:last-child{border-bottom:0}
.row .q{font-family:'Inter Display';font-weight:800;font-size:calc(var(--K) * 22px);text-align:right}
.row .q small{font-family:'Inter';font-size:calc(var(--K) * 12px);color:#6B7079;font-weight:600}
.mut{color:#6B7079;font-size:calc(var(--K) * 13px);font-weight:600}
.btn{display:inline-flex;align-items:center;gap:8px;background:#ED3237;color:#fff;font-weight:800;border-radius:12px;padding:10px 16px;font-size:calc(var(--K) * 15px)}
"""

FMT = {
    'feed': dict(H='1080px', PH='600px', SH='120px', PT='40px', LH='58px', TG='14px', FS='68px', H1='24px', SB='21px', VM='24px',
                 CC='1fr 1fr', CM='18px', PF='18px', CP='12px', FO='0px', K='1.12'),
    'story': dict(H='1920px', PH='900px', SH='340px', PT='236px', LH='80px', TG='17px', FS='84px', H1='40px', SB='27px', VM='36px',
                  CC='1fr', CM='26px', PF='22px', CP='14px', FO='220px', K='1.3'),
}

STR = ('<div class="stripes"><i style="left:120px;width:70px;background:#ED3237"></i>'
       '<i style="left:215px;width:34px;background:#fff;opacity:.85"></i>'
       '<i style="left:272px;width:18px;background:#ED3237;opacity:.55"></i></div>')


def rain(n=70, h=900):
    import random
    random.seed(7)
    s = ''
    for _ in range(n):
        x, y, L = random.randint(-40, 1100), random.randint(-120, h), random.randint(40, 120)
        s += f'<i style="left:{x}px;top:{y}px;height:{L}px;opacity:{random.uniform(.3, 1):.2f}"></i>'
    return f'<div class="rain">{s}</div>'


# ---------------------------------------------------------------- visuais
def ico_box(i, bg='#FFE3E3', c=R):
    return (f'<span style="flex:0 0 auto;width:calc(var(--K)*38px);height:calc(var(--K)*38px);border-radius:10px;background:{bg};'
            f'display:flex;align-items:center;justify-content:center">{icon(i, c, 20, 2.4)}</span>')


def v_cashback(st):
    rows = [
        ('shopping-bag', 'Compra de peças · R$ 400,00', '5% de cashback', '+ R$ 20,00', '#17703F'),
        ('calendar', 'Segunda é cashback em dobro', 'campanha da loja', '+ R$ 8,00', '#17703F'),
        ('wrench', 'Troca de óleo no balcão', 'usou o saldo no PDV', '− R$ 20,00', '#C21F26'),
    ]
    li = ''.join(f'<div class="row" style="grid-template-columns:auto 1fr auto">{ico_box(i)}<div><div style="font-weight:800">{e(t)}</div>'
                 f'<div class="mut">{e(s)}</div></div><div class="q" style="color:{c}">{v}</div></div>' for i, t, s, v, c in rows)
    return (f'<div class="card"><div class="hd">{icon("wallet", R, 26, 2.4)}<div>Carteira do cliente · Carlos<small>extrato de cashback</small></div>'
            f'<div class="r" style="text-align:right"><div class="mut">Saldo para usar</div><div style="font-family:Inter Display;font-weight:800;font-size:calc(var(--K)*30px);color:#17703F">R$ 8,00</div></div></div>{li}'
            f'<div class="row" style="grid-template-columns:1fr auto;background:#FAF9F7;border-radius:0 0 20px 20px"><span class="mut">Saldo vale por 90 dias · resgate mínimo de R$ 5,00</span>'
            f'<span class="pill p-amb">{icon("clock", "#8A5A00", 14, 2.5)}Expira em 12/02</span></div></div>')


def qr(n=25, px=7):
    import random
    random.seed(11)
    cells = ''
    for y in range(n):
        for x in range(n):
            fin = any(x0 <= x < x0 + 7 and y0 <= y < y0 + 7 for x0, y0 in [(0, 0), (n - 7, 0), (0, n - 7)])
            if fin:
                dx, dy = min(abs(x - (0 if x < 7 else n - 7)), 0), 0
                lx = x if x < 7 else x - (n - 7)
                ly = y if y < 7 else y - (n - 7)
                on = lx in (0, 6) or ly in (0, 6) or (2 <= lx <= 4 and 2 <= ly <= 4)
            else:
                on = random.random() < .48 and not ((x < 8 and y < 8) or (x >= n - 8 and y < 8) or (x < 8 and y >= n - 8))
            if on:
                cells += f'<rect x="{x}" y="{y}" width="1" height="1"/>'
    s = n * px
    return f'<svg width="{s}" height="{s}" viewBox="0 0 {n} {n}" shape-rendering="crispEdges" fill="#1B1A1B">{cells}</svg>'


def v_pix(st):
    return (f'<div class="card" style="display:grid;grid-template-columns:auto 1fr;overflow:hidden">'
            f'<div style="padding:22px;border-right:1.5px solid #ECEAE6;display:flex;flex-direction:column;align-items:center;gap:10px;background:#FAF9F7">'
            f'<div style="background:#fff;padding:12px;border-radius:14px;border:1.5px solid #ECEAE6">{qr(25, 8 if st else 7)}</div>'
            f'<span class="pill p-gry">{icon("copy", "#55595F", 14, 2.5)}Pix copia e cola</span></div>'
            f'<div style="display:flex;flex-direction:column"><div class="hd">{icon("monitor", R, 24, 2.4)}<div>PDV · Venda 1042<small>Caixa 1 · balcão</small></div></div>'
            f'<div class="row" style="grid-template-columns:1fr auto"><div>Capacete fechado 58</div><div class="q">R$ 349,90</div></div>'
            f'<div class="row" style="grid-template-columns:1fr auto"><div>Viseira fumê</div><div class="q">R$ 59,90</div></div>'
            f'<div class="row" style="grid-template-columns:1fr auto;border-bottom:0"><div style="font-weight:800">Total no Pix</div><div class="q" style="color:{R}">R$ 409,80</div></div>'
            f'<div style="margin-top:auto;padding:14px 22px 18px;display:flex;flex-direction:column;gap:8px">'
            f'<span class="pill p-grn" style="font-size:calc(var(--K)*16px);padding:8px 14px;align-self:flex-start">{icon("circle-check-big", "#17703F", 18, 2.5)}Pagamento confirmado</span>'
            f'<span class="mut">Baixa feita sozinha no financeiro</span></div></div></div>')


def v_lotes(st):
    alert = (f'<div class="card" style="border:3px solid {R};padding:16px 20px;display:flex;gap:14px;align-items:center">'
             f'{ico_box("ban")}<div><div style="font-weight:800;font-size:calc(var(--K)*18px);color:#C21F26">Venda bloqueada no PDV</div>'
             f'<div style="font-weight:600;font-size:calc(var(--K)*15px)">Óleo 10W30 1 L · lote 2309-B venceu em 12/10/2026</div></div></div>')
    rows = [
        ('droplet', 'Fluido de freio DOT 4', 'lote 2410-A · vence 03/2027', '<span class="pill p-grn">Vende primeiro</span>'),
        ('battery', 'Bateria 5Ah · série 8841-207', 'vendida em 14/08 para João S.', '<span class="pill p-blu">Garantia confere</span>'),
        ('triangle-alert', 'Recall do lote 2405-C', 'vendido para 7 clientes', '<span class="pill p-amb">Lista para avisar</span>'),
    ]
    li = ''.join(f'<div class="row" style="grid-template-columns:auto 1fr auto">{ico_box(i)}<div><div style="font-weight:800">{e(t)}</div>'
                 f'<div class="mut">{e(s)}</div></div>{p}</div>' for i, t, s, p in rows)
    return f'{alert}<div class="card" style="margin-top:14px"><div class="hd" style="padding:12px 22px">{icon("scan-barcode", R, 22, 2.4)}<div>Lotes e números de série</div></div>{li}</div>'


def v_twin(st):
    chat = ('<div style="background:#E9E2D8;border-radius:20px;padding:18px 20px 20px">'
            '<div style="display:flex;align-items:center;gap:10px;font-weight:800;color:#3D4A4F;font-size:calc(var(--K)*15px);margin-bottom:12px">'
            + icon('message-circle', '#1E9E57', 20, 2.4) + 'WhatsApp · cliente novo</div>'
            '<div style="background:#fff;color:#1B1A1B;border-radius:14px 14px 14px 4px;padding:12px 16px;font-size:calc(var(--K)*17px);font-weight:500;margin-right:120px">'
            'Boa tarde! Tem pastilha de freio da Bros 160? Quanto fica?</div></div>')
    sug = (f'<div class="card" style="margin-top:14px;border:3px solid #1E9E57"><div class="hd" style="padding:12px 22px">{icon("sparkles", R, 22, 2.4)}'
           f'<div>Sugestão do Twin<small>no estilo do Rafa, seu melhor vendedor</small></div></div>'
           f'<div style="padding:14px 22px;font-size:calc(var(--K)*17px);font-weight:500;line-height:1.4">Fala, parceiro! Tem sim 🔥 A pastilha dianteira da Bros 160 sai por <b>R$ 39,90</b> e tenho <b>14 aqui</b>. Quer que eu separe pra você?</div>'
           f'<div class="row" style="grid-template-columns:auto auto 1fr auto auto;background:#FAF9F7;border-radius:0 0 20px 20px">'
           f'<span class="pill p-grn">{icon("tag", "#17703F", 14, 2.5)}preço do cadastro</span><span class="pill p-grn">{icon("package", "#17703F", 14, 2.5)}estoque real</span><span></span>'
           f'<span class="pill p-gry" style="padding:9px 14px">{icon("pencil", "#55595F", 14, 2.5)}Editar</span><span class="btn">{icon("send", "#fff", 16, 2.4)}Enviar</span></div></div>')
    return chat + sug


def v_metas(st):
    rows = [
        ('Vendas no balcão · Ana', 'R$ 18.400 de R$ 30.000', 61, 50, 'p-grn', 'No ritmo'),
        ('Pneu 90/90-18', '22 de 60 unidades', 37, 50, 'p-red', 'Abaixo do ritmo'),
        ('Ticket médio da loja', 'R$ 186 de R$ 200', 93, 100, 'p-amb', 'Atenção'),
        ('Margem bruta', '31% de 30%', 100, 100, 'p-grn', 'Batida'),
    ]
    col = {'p-grn': '#1E9E57', 'p-red': R, 'p-amb': '#E0A100'}
    li = ''.join(
        f'<div class="row" style="grid-template-columns:1fr auto;row-gap:8px"><div><div style="font-weight:800">{e(t)}</div><div class="mut">{e(s)}</div></div>'
        f'<span class="pill {c}">{e(lb)}</span><div style="grid-column:1/3;position:relative;height:calc(var(--K)*10px);border-radius:99px;background:#EEEDEA">'
        f'<div style="width:{p}%;height:100%;border-radius:99px;background:{col[c]}"></div>'
        f'<i style="position:absolute;left:{x}%;top:-5px;bottom:-5px;width:3px;background:#2A2829;border-radius:2px"></i></div></div>'
        for t, s, p, x, c, lb in rows if x < 100 or p >= x or True)
    return (f'<div class="card"><div class="hd">{icon("target", R, 26, 2.4)}<div>Metas de novembro<small>dia 15 · esperado até hoje: 50%</small></div>'
            f'<span class="r pill p-red">{icon("bell", "#C21F26", 14, 2.5)}1 meta fora do ritmo</span></div>{li}</div>')


def v_contador(st):
    dre = [('Receita de vendas', 'R$ 142.380', ''), ('Custo das mercadorias', '− R$ 86.910', 'color:#C21F26'),
           ('Despesas', '− R$ 31.240', 'color:#C21F26'), ('Resultado do mês', 'R$ 24.230', 'color:#17703F;font-size:calc(var(--K)*26px)')]
    li = ''.join(f'<div class="row" style="grid-template-columns:1fr auto"><div>{e(a)}</div><div class="q" style="{s}">{b}</div></div>' for a, b, s in dre)
    obr = [('SPED Fiscal', 'p-grn', 'Gerado'), ('EFD-Reinf', 'p-grn', 'Gerado'), ('PGDAS', 'p-amb', 'Conferir'), ('Extrato OFX', 'p-blu', 'Conciliado')]
    pills = ''.join(f'<div style="border:1.5px solid #ECEAE6;border-radius:12px;padding:10px 12px"><div style="font-weight:800;font-size:calc(var(--K)*15px)">{a}</div>'
                    f'<span class="pill {c}" style="margin-top:6px">{b}</span></div>' for a, c, b in obr)
    return (f'<div class="card"><div class="hd">{icon("chart-column", R, 26, 2.4)}<div>DRE · outubro até hoje<small>montado com as vendas, compras e o financeiro do ERP</small></div></div>{li}'
            f'<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:10px;padding:14px 18px 18px;background:#FAF9F7;border-radius:0 0 20px 20px">{pills}</div></div>'
            '<div class="note">Valores ilustrativos. Arquivos gerados para conferência; o envio ao governo continua com o seu contador.</div>')


T = [
    dict(slug='1-cashback', tag='Fidelidade & Cashback', photo='auto-pecas.webp', pp='center 50%',
         hf='Dinheiro de volta que<br><span class="o">traz o cliente de volta.</span>',
         hs='Dinheiro de volta<br>que <span class="o">traz o cliente<br>de volta.</span>',
         sub='Parte de cada compra vira saldo para o cliente gastar na próxima vez, na sua loja.',
         vis=v_cashback,
         chips=[('calendar', 'Cashback em dobro, aniversário e 1ª compra'), ('clock', 'Validade e resgate mínimo do saldo'),
                ('receipt', 'Extrato de cada cliente'), ('monitor', 'Usa no PDV e na loja virtual')]),
    dict(slug='2-pix-balcao', tag='Pagamentos via Pix', photo='concessionaria.webp', pp='center 35%',
         hf='Recebeu, caiu,<br><span class="o">baixou.</span>',
         hs='Recebeu,<br>caiu, <span class="o">baixou.</span>',
         sub='Pix com QR Code no valor exato de cada venda, direto na tela do PDV.',
         vis=v_pix, ks='1.55', kf='1.1',
         chips=[('qr-code', 'QR Code dinâmico por venda'), ('message-circle', 'Copia e cola para quem compra no WhatsApp'),
                ('landmark', 'Pela sua conta Asaas ou Efí'), ('list-checks', 'Painel de pagos, pendentes e expirados')]),
    dict(slug='3-lotes-validade', tag='Lotes e Séries', photo='oficina-express.webp', pp='center 40%',
         hf='Óleo vencido<br><span class="o">não passa no balcão.</span>',
         hs='Óleo vencido<br><span class="o">não passa<br>no balcão.</span>',
         sub='Lote, validade e número de série de cada peça, do recebimento até o cliente.',
         vis=v_lotes, ks='1.3',
         chips=[('calendar-clock', 'O que vence primeiro sai primeiro'), ('hash', 'Número de série por unidade'),
                ('users', 'Recall com a lista de clientes'), ('file-check', 'Lote segue na NF-e')]),
    dict(slug='4-twin-vendedor', tag='Twin · atendimento com IA', photo='moto-pecas.webp', pp='center 35%',
         hf='O jeito do seu melhor vendedor<br><span class="o">em toda a equipe.</span>',
         hs='O jeito do seu<br>melhor vendedor<br><span class="o">em toda a equipe.</span>',
         sub='O Twin aprende como ele conversa e sugere a resposta no mesmo tom.',
         vis=v_twin, ks='1.4', kf='1.08',
         chips=[('message-square', 'Aprende com conversas do WhatsApp'), ('package', 'Preço e estoque reais do ERP'),
                ('user-check', 'Uma pessoa revisa e envia'), ('shield-check', 'LGPD: termo assinado e CPF apagado')]),
    dict(slug='5-metas', tag='Gestor de Metas', photo='moto-pecas-performance.webp', pp='center 50%',
         hf='Descubra no dia 15.<br><span class="o">Não no dia 30.</span>',
         hs='Descubra<br>no dia 15.<br><span class="o">Não no dia 30.</span>',
         sub='O vendido comparado com o esperado até hoje, e o aviso do que está fora do ritmo.',
         vis=v_metas, ks='1.25', kf='1.02',
         chips=[('users', 'Por vendedor, produto ou marca'), ('percent', 'Margem, ticket médio e despesas'),
                ('sparkles', 'Valor sugerido pelas últimas vendas'), ('bell', 'Alerta de meta abaixo do ritmo')]),
    dict(slug='6-contador', tag='Gestor Contador', photo='distribuidora.webp', pp='center 50%',
         hf='O DRE da loja<br>sem esperar <span class="o">o fim do mês.</span>',
         hs='O DRE da loja<br>sem esperar<br><span class="o">o fim do mês.</span>',
         sub='Seu contador com tudo na mão, a partir do que já está no ERP.',
         vis=v_contador, ks='1.22', kf='1.0',
         chips=[('file-up', 'Extrato do banco (OFX) para conciliar'), ('calculator', 'Apuração com memorial para conferir'),
                ('folder-check', 'SPED, EFD-Reinf e PGDAS para revisão'), ('calendar-check', 'Calendário de obrigações')]),
]

os.makedirs(OUT, exist_ok=True)
for t in T:
    for fmt, P in FMT.items():
        st = fmt == 'story'
        P = dict(P, K=t.get('ks' if st else 'kf', P['K']))
        var = ';'.join(f'--{k}:{v}' for k, v in P.items()) + f';--PP:{t["pp"]}'
        chips = ''.join(f'<div class="chip"><span class="ic">{icon(i, R, int(P["PF"][:-2]) + 6, 2.4)}</span>{e(x)}</div>' for i, x in t['chips'])
        sub = f'<div class="sub">{e(t["sub"])}</div>'
        doc = f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS}</style></head><body style="{var}">
<div class="photo" style="background-image:url({t['photo']})"></div>{rain(110 if st else 70, int(P['PH'][:-2])) if t.get('rain') else ''}
{STR}
<div class="wrap">
 <div class="top"><div class="lg"><img src="logo.png" alt="Gestor Easy"></div><div class="tag">{e(t['tag'])}</div></div>
 <h1>{t['hs'] if st else t['hf']}</h1>{sub}
 <div class="vis">{t['vis'](st)}</div>
 <div class="chips">{chips}</div>
</div>
<div class="flag"></div><div class="foot"><div class="cta">{icon("message-circle", "#fff", 34)}<div><small>Fale com a gente no WhatsApp</small>(21) 98233-6975</div></div><div class="site">{icon("globe", R, 30)}<div><small>Acesse</small>erp.gestoreasy.com.br</div></div></div>{'<div class="below"></div>' if st else ''}
</body></html>"""
        open(os.path.join(OUT, f'{t["slug"]}-{fmt}.html'), 'w').write(doc)
print('ok')

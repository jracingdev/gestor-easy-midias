# Gera a narração (edge-tts, voz masculina pt-BR) a partir de narracao-voz.json.
# Uso (no PC):  python gerar_voz.py  -> cria a pasta narracao\ com n01.mp3 ... n33.mp3
import asyncio, json, os, edge_tts
AQUI=os.path.dirname(os.path.abspath(__file__))
VOZ='pt-BR-AntonioNeural'; RATE='+6%'
async def main():
    os.makedirs(os.path.join(AQUI,'narracao'),exist_ok=True)
    for k,t in json.load(open(os.path.join(AQUI,'narracao-voz.json'),encoding='utf-8')):
        out=os.path.join(AQUI,'narracao',k+'.mp3')
        await edge_tts.Communicate(t,VOZ,rate=RATE).save(out)
        print(k,'ok')
asyncio.run(main())

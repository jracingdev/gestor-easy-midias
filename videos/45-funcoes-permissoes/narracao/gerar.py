# Gera as falas do vídeo "Funções e permissões" (edge-tts, pt-BR-AntonioNeural, +6%).
# Uso no PC: py -3.14 gerar.py   (precisa: py -3.14 -m pip install edge-tts)
import asyncio, json, pathlib, edge_tts
aqui = pathlib.Path(__file__).parent
falas = json.loads((aqui / "texto-voz.json").read_text(encoding="utf-8"))
async def main():
    for nome, texto in falas:
        destino = aqui / f"{nome}.mp3"
        await edge_tts.Communicate(texto, "pt-BR-AntonioNeural", rate="+6%").save(str(destino))
        print("ok", destino.name, destino.stat().st_size)
asyncio.run(main())

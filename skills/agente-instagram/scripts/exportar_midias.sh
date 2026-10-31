#!/usr/bin/env bash
# Converte as artes PNG da semana em JPEG (o Metricool aceita melhor) e copia artes + Shorts para o repo público de mídias.
# Uso: exportar_midias.sh <pasta da semana> <clone do gestor-easy-midias> <pasta no repo, ex. instagram/2026-11-semana-10a15>
# Saída: lista das URLs raw.githubusercontent.com que vão no "media" do Metricool (troque BRANCH pela branch do push).
set -euo pipefail
SEM="$1"; REPO="$2"; DEST="$3"
mkdir -p "$REPO/$DEST"
for f in "$SEM"/feed-1080x1080/*.png;   do convert "$f" -quality 92 "$REPO/$DEST/$(basename "${f%.png}")-feed.jpg"; done
for f in "$SEM"/stories-1080x1920/*.png; do convert "$f" -quality 92 "$REPO/$DEST/$(basename "${f%.png}")-story.jpg"; done
cp "$SEM"/videos/*.mp4 "$REPO/$DEST/" 2>/dev/null || true
ls "$REPO/$DEST" | sed "s#^#https://raw.githubusercontent.com/jracingdev/gestor-easy-midias/BRANCH/$DEST/#"

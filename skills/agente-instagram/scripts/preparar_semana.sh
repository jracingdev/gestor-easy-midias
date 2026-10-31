#!/usr/bin/env bash
# Prepara a pasta de trabalho da semana: ícones lucide, logo e fotos de fundo do ERP.
# Uso: preparar_semana.sh <pasta da semana> <clone do gestor-easy-sistema>
#   ex.: preparar_semana.sh /mnt/project-files/divulgacao-whatsapp-instagram/semana-2026-11-10 /home/user/gestor-easy-sistema
set -euo pipefail
SEM="$1"; ERP="$2"
mkdir -p "$SEM"/{_fonte,html,feed-1080x1080,stories-1080x1920,videos}
TMP="${TMPDIR:-/tmp}/lucide"
if [ ! -d "$TMP/package/icons" ]; then
  mkdir -p "$TMP" && (cd "$TMP" && npm pack lucide-static --silent >/dev/null && tar xzf lucide-static-*.tgz)
fi
cp "$ERP/public/images/logo_dark.png" "$SEM/html/logo.png"
cp "$ERP"/public/assets/images/ecommerce-templates/*.webp "$SEM/html/" 2>/dev/null || echo "aviso: fotos .webp não encontradas"
echo "Ícones: $TMP/package/icons"
echo "Fotos disponíveis:"; ls "$SEM/html" | grep webp || true

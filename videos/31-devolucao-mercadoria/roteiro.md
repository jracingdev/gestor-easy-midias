# Devolução de mercadoria na prática

Vídeo narrado (25/11/2026), versões pc (1080x1080), celular (1080x1080) e vertical (1080x1920). Gravado no ERP real em ambiente de homologação, com dados fictícios (loja "Duas Rodas Motopeças" do RJ, cliente Carlos Eduardo Souza, venda PDV 1052 com NFC-e 3408, fornecedor "Rio Peças Distribuidora"). Nada foi enviado à SEFAZ: a autorização da NF-e de devolução foi simulada no banco de teste.

Base: NT 2025.002 (regra VC02-14, em produção desde 16/11/2026): NF-e com finalidade 4 tem de referenciar o documento original, no cabeçalho (refNFe, uma nota só) ou por item (grupo DFeReferenciado, chave + nItem opcional), nunca nos dois. Sem isso, rejeição 321.

Exemplos: devolução de venda com ST (CFOP 1411, CST 60, 1 de 2 pastilhas); devolução de compra com ST (CFOP 5411, ICMS próprio 20% de R$ 112,00 = R$ 22,40, ST = 192,39 x 20% - 22,40 = R$ 16,08, total R$ 128,08).

## Narração

**01. Abertura**
O cliente devolveu a peça, ou é você que precisa devolver ao fornecedor? Desde 16 de novembro, a SEFAZ rejeita a nota de devolução que não aponta a nota original. Veja como fazer certo no Gestor Easy.

**02. O que a SEFAZ exige (finalidade 4 e DF-e referenciado)**
Devolução é uma NF-e com finalidade 4. Ela precisa trazer a chave de acesso da nota original: no cabeçalho, uma nota só, ou em cada item, no grupo DF-e referenciado. Nunca nos dois ao mesmo tempo. Sem isso, a nota volta rejeitada.

**03. Quem emite a nota de devolução**
Quem emite? Na devolução de venda, se o cliente é empresa com inscrição estadual, ele emite a nota e você confere a chave. Se é consumidor, a sua loja emite uma nota de entrada. Na devolução de compra, quem emite é você: uma nota de saída para o fornecedor.

**04. PDV · Troca e Devolução**
No balcão, o Carlos voltou com uma pastilha que não serve na moto dele. No PDV, em Troca e Devolução, busco a venda pelo número.

**05. Caixa trava a devolução com NFC-e autorizada**
A venda saiu com NFC-e autorizada. Por isso o caixa trava a devolução até existir a NF-e de devolução que aponta essa NFC-e. E já mostra a chave dela para copiar.

**06. Fiscal 2026 · Nova NF-e de devolução**
Em Fiscal 2026, Nova NF-e: tipo Entrada e finalidade Devolução. Na hora, cada item ganha o campo da nota original.

**07. CFOP 1411 e CST 60 (venda com ST)**
Busco o cliente e a pastilha. Ela foi vendida com ST, então o CFOP é 1411 e o CST continua 60. Sem ST, seria 1202. A quantidade é só a que voltou, pelo valor da venda.

**08. Chave da NFC-e no item**
No item, colo a chave da NFC-e. O número do item na nota original pode ficar em branco: quando a venda está no Gestor Easy, o sistema encontra sozinho.

**09. Chave errada barrada na prévia**
E se a chave tiver um dígito errado? Salvo e abro a pré-visualização: o sistema confere a chave e barra antes de ir à SEFAZ, dizendo o item e o que corrigir.

**10. Corrigir e prévia pronta (XML com DF-e referenciado)**
Em Corrigir, acerto a chave. A prévia monta o XML com o DF-e referenciado e mostra: pronta para autorizar. Tudo aqui em homologação, sem valor fiscal.

**11. Vincular a NF-e no PDV**
Com a nota de devolução autorizada, volto ao PDV. O sistema já sugere essa nota, eu vinculo, e a devolução fica liberada.

**12. Devolução parcial, valor e estoque**
Escolho devolução parcial: uma pastilha. Confirmo, o valor volta para o cliente e a pastilha volta para o estoque.

**13. Devolução de compra ao fornecedor**
Agora o outro lado: um kit relação chegou com defeito da Rio Peças. Nova NF-e, tipo Saída, finalidade Devolução, e o destinatário é o fornecedor.

**14. CFOP 5411, ICMS próprio e ST**
O kit entrou com ICMS-ST retido, então o CFOP é 5411, ou 6411 se o fornecedor for de outro estado. Sem ST, 5202 ou 6202. Os impostos seguem a nota de compra, proporcionais à quantidade: ICMS próprio e ST destacados como vieram.

**15. Chave e item da nota do fornecedor**
Colo a chave da nota do fornecedor e o número do item, que está no XML dele. Prévia: pronta para autorizar.

**16. Resumo**
Resumindo: finalidade devolução, CFOP de devolução, os mesmos impostos da nota original e a chave dela, no cabeçalho ou nos itens. Regras e créditos variam por estado, então confirme com o seu contador.

**17. Encerramento**
Gestor Easy. Devolução certa, sem rejeição. Acesse erp.gestoreasy.com.br ou chame no WhatsApp.

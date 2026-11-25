# Roteiro: Cadastro de produtos e importações

Vídeo narrado (2min32) mostrando, em telas reais com dados fictícios da "Duas Rodas Motopeças", o cadastro de produtos (/product-service) e as importações: planilha com mapeamento, fotos em lote, catálogo PDF do fornecedor e a Central de Importações (/import-center) com saldos do sistema antigo. Fecha com a Movimentação (kardex) no detalhe do item. Versões: `produtos-importacoes-pc.mp4` e `produtos-importacoes-celular.mp4` (1080x1080) e `produtos-importacoes-vertical.mp4` (1080x1920).

Voz: edge-tts pt-BR-AntonioNeural +6%. No texto da voz: "Gestor Ízi", "pê dê éfe", "cê ésse vê", "Blíng, Ômie e Táini" e "erp ponto gestorízi ponto com ponto bê érre" (ver `_fonte/narracao-voz.json`).

Arquivos fictícios usados (em `_fonte/`): `planilhas/produtos-sistema-antigo.csv` (8 itens, um com estoque -2), `fotos-lote` (fotos com o nome do SKU), `catalogo/Catalogo RotaSul Acessorios nov-2026.pdf` (12 itens, layout InDesign), `planilhas/saldos-estoque-sistema-antigo.csv` (com o PF-XRE300 inexistente, para mostrar o erro crítico) e `planilhas/saldos-estoque-corrigido.csv` (total 145).

| Cena | Tela | Narração |
|---|---|---|
| Abertura | /product-service | Cadastro de produtos e importações no Gestor Easy. Traga seus itens de uma planilha, do catálogo do fornecedor ou do sistema antigo, sem digitar um por um. |
| 1. Gerenciar itens | Atalhos e Colunas (preço, estoque, categoria) | Em Gerenciar itens ficam todos os produtos, com foto, código e atalhos para consultar, importar e ajustar em lote. Em Colunas, você escolhe o que a lista mostra: preço, estoque e categoria. |
| 2. Busca e filtros | Busca "pastilha", Mostrar filtros | A busca acha pelo nome ou pelo código, e os filtros separam por categoria, tipo e aplicação na moto. |
| 3. Importar planilha | Planilha, modelo, envio do CSV | Para trazer muitos itens de uma vez, use Planilha. Baixe o modelo ou envie a planilha que você já tem, em CSV ou Excel. |
| 3. Mapear colunas | DESCRICAO → Nome | O sistema lê o cabeçalho e sugere cada coluna. Aqui, a descrição do sistema antigo é o nome do produto: é só trocar na lista. |
| 3. Resultado | 8 novos, GR-SPRAY com saldo zerado | Importar. Oito itens novos. A linha com estoque negativo entra com saldo zero e fica listada para você conferir. Planilhas grandes vão para a fila, com barra de progresso. |
| 4. Fotos em lote | 8 fotos encontradas pelo SKU | As fotos vêm em lote: com cada arquivo salvo pelo código do produto, a imagem encontra o seu item sozinha. |
| 5. Catálogo PDF | Enviar e processar o catálogo RotaSul | Recebeu o catálogo do fornecedor em PDF? Envie e mande processar. O sistema lê código, nome, ficha, preço e quantidade por caixa, e recorta a foto de cada peça. |
| 5. Revisar e importar | Categoria Acessórios, margem, importar selecionados | Na revisão, você confere, ajusta o que quiser, escolhe a categoria e a margem de venda, e importa os selecionados. |
| 6. Central de Importações | /import-center, cartões e 3 passos | Vindo de outro sistema? A Central de Importações traz vendas, estoque e financeiro, com modelos para Bling, Omie e Tiny, sempre em três passos: modelo, validação e confirmação. |
| 6. Validação | Linha PF-XRE300 crítica, importação bloqueada | Na validação, nada é gravado. O produto que não existe no cadastro aparece como crítico, e a importação fica bloqueada até corrigir. |
| 6. Confirmação e conciliação | Arquivo corrigido, baseline 145, histórico e execução | Com o arquivo corrigido e o total do sistema antigo informado, confirme. A central confere origem e destino, e cada execução fica no histórico, com revisão e opção de desfazer. |
| 7. Movimentação do item | Kit relação CG 160, kardex com 10 movimentos | E no detalhe do item, a Movimentação mostra o caminho de cada peça: o saldo importado, compras, vendas no balcão e nos marketplaces, devoluções e inventário, com o saldo depois de cada movimento. |
| Encerramento | Cartão final | Gestor Easy. Seu cadastro em ordem desde o primeiro dia. Acesse erp.gestoreasy.com.br. |

# Roteiro: Workflows e automações (Gestor Easy)

Vídeo narrado de 2min14 (pc e celular 1080x1080, vertical 1080x1920), gravado nas telas reais do ERP com dados fictícios: loja "Rota Sul Motopeças", cliente Oficina Vieira Motos. Substitui, como vídeo de treinamento, o vídeo legendado antigo (10-workflows-automacoes).

O fluxo foi montado e disparado de verdade: a venda no PDV baixou o estoque, o evento de estoque baixo rodou o fluxo e a mensagem foi gerada pelo ERP. O lado do Telegram aparece num painel identificado como "Simulação do app Telegram" (Bot API simulada na gravação, nenhuma mensagem real foi enviada).

Tela inteira o tempo todo; aproximação curta só em destaques pequenos. Voz: edge-tts pt-BR-AntonioNeural +6% (Workflows pronunciado "Uórk flôus").

| # | Cena | Narração | Tela |
|---|---|---|---|
| 01 | Abertura | Tem tarefa que se repete todo dia na loja? Avisar a equipe que uma peça está acabando, agradecer o cliente que pagou, mandar o resumo das vendas no fim do dia. No Gestor Easy, os Workflows fazem isso sozinhos. | /workflows/dashboard |
| 02 | Painel e modelos | No painel você vê quantos fluxos existem, quantos estão ativos e as execuções dos últimos dias. Para começar rápido, a vitrine traz modelos prontos de pós-venda, cobrança e gestão da loja. | Painel com totais e execuções; vitrine de modelos |
| 03 | Editor visual | Mas vamos criar um do zero, no editor visual. À esquerda ficam os blocos: gatilhos, ações, condições, tempo e dados do ERP. | /workflows/builder, paleta de blocos |
| 04 | Gatilho | Todo fluxo começa por um gatilho. Arraste o bloco Evento para a área de montagem e escolha: estoque abaixo do mínimo. | Bloco Evento: Estoque abaixo do mínimo |
| 05 | Ação | Agora a ação. Arraste o bloco Telegram, ligue ao gatilho e escolha enviar para a equipe. Na mensagem, as variáveis entre chaves viram o nome do produto, o saldo e o mínimo. | Bloco Telegram ligado ao gatilho, destino Equipe, mensagem com {{produto.nome}}, {{produto.saldo}}, {{produto.minimo}} |
| 06 | Publicar | Dê um nome ao fluxo e clique em Publicar. Pronto: o fluxo está ativo. | Nome "Aviso de estoque mínimo no Telegram", Publicar |
| 07 | Venda no PDV | Agora veja funcionando. No PDV sai uma venda de pastilha de freio, e o saldo chega ao estoque mínimo. | /pos: venda da Pastilha dianteira CG160 em dinheiro; saldo 5 → 4 (mínimo 4) |
| 08 | Aviso no Telegram | Na mesma hora, o grupo da equipe recebe o aviso no Telegram, com o nome da peça e o saldo. | Painel "Simulação do app Telegram": grupo da equipe recebe o aviso |
| 09 | Histórico | E na página do fluxo fica o histórico: cada execução, com data, situação e o que disparou. | Página do fluxo: execução com data, situação e gatilho "Estoque Baixo" |
| 10 | Se / então | Os fluxos também decidem. Neste, o gatilho é fatura paga. O bloco Se, então confere o valor: a partir de quinhentos reais, o cliente recebe um agradecimento no Telegram; abaixo disso, por e-mail. | Fluxo "Agradecer pagamento da fatura": Fatura paga → Se valor ≥ 500 → Telegram ao cliente, senão e-mail |
| 11 | Agendado | E podem rodar no horário. Com o gatilho Agendado, todo dia às dezoito horas, o bloco Vendas do dia soma o PDV e as faturas, e o Telegram leva o resumo para a equipe. | Fluxo "Resumo das vendas às 18h": Agendado 18:00 → Vendas do dia → Telegram à equipe |
| 12 | Executar agora | Quer conferir antes da hora? Clique em Executar manualmente, e o resumo chega na hora. | Executar manualmente; resumo chega no grupo |
| 13 | Fechamento | Workflows do Gestor Easy: a loja trabalhando sozinha, sem esquecer nada. Conheça em erp.gestoreasy.com.br. | Painel de Workflows, site |

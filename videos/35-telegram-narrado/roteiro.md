# Roteiro: Telegram da empresa (Gestor Easy)

Vídeo narrado de cerca de 2min56 (pc e celular 1080x1080, vertical 1080x1920), gravado nas telas reais do ERP com dados fictícios: loja "Rota Sul Motopeças", bot @RotaSulMotopecasBot, cliente Oficina Vieira Motos (Marcos Vieira), equipe com Bruno Teixeira. Substitui, como vídeo de treinamento, o vídeo de lançamento legendado (11-telegram).

O lado do Telegram (grupo da equipe e chat do cliente) aparece num painel identificado como "Simulação do app Telegram": as mensagens e os botões são exatamente os que o ERP enviou para a Bot API (simulada na gravação, nenhuma mensagem real foi enviada).

Tela inteira o tempo todo; aproximação curta só em destaques pequenos.

| # | Cena | Narração | Tela |
|---|---|---|---|
| 01 | Abertura | Sua equipe e seus clientes usam Telegram? No Gestor Easy, cada empresa tem o próprio bot: ele avisa a equipe na hora e atende o cliente com fatura, boleto e nota, sem ninguém precisar abrir o sistema. | /integracoes/telegram (bot ainda não conectado) |
| 02 | Criar o bot | O caminho é Integrações, Telegram. No passo 1, abra o BotFather no Telegram, mande o comando newbot, escolha o nome do bot e copie o token que ele devolve. | Passo 1: instruções do BotFather e /newbot |
| 03 | Conectar o bot | Cole o token aqui e clique em Conectar. O sistema confere o token com o Telegram, registra o bot e já mostra tudo conectado. | Token colado, Conectar, faixa "Conectado ao bot @RotaSulMotopecasBot" |
| 04 | O que o bot faz | Nas opções, você decide o que o bot faz: avisos automáticos aos clientes, alerta a cada venda e a cada pagamento, mensagens dos clientes encaminhadas para o grupo e um resumo diário no horário que você escolher. | Chaves: avisos aos clientes, alerta de venda e pagamento, encaminhar mensagens, resumo diário 18:00 |
| 05 | Grupo da equipe | No passo 2, crie um grupo com a sua equipe, adicione o bot e mande no grupo o comando barra equipe com este código. Na hora, o grupo aparece cadastrado. | Passo 2: código da equipe; /equipe no grupo (painel do Telegram); "Grupo cadastrado" |
| 06 | Alertas da equipe | Em Alertas da equipe, ligue só o que interessa: pergunta, venda e reclamação no Mercado Livre, venda e devolução na Shopee, estoque mínimo, nota rejeitada, certificado perto de vencer e boleto recusado pelo banco. | Alertas da equipe (Marketplaces e Operação), consulta de estoque, Salvar alertas |
| 07 | Alerta com botão | Cada alerta chega no grupo com um botão para abrir direto no sistema. Aqui, a pastilha da CG 160 bateu o estoque mínimo, e a equipe já sabe que é hora de repor. | Alerta "Estoque no mínimo" no grupo, botão Abrir item → Detalhe do item |
| 08 | Convidar clientes | No passo 3, convide os clientes. Busque pelo nome ou telefone e gere o link de convite. Ele vale trinta dias e só pode ser usado uma vez. | Passo 3: busca "Vieira", Gerar link, Copiar |
| 09 | Cliente vinculado | Quando o cliente toca no link, fica vinculado e aparece em Contatos vinculados. A partir daí, recebe pelo Telegram os mesmos avisos do WhatsApp: fatura, pagamento, boleto, Pix, nota autorizada e lembretes. | /start do cliente (painel), boas-vindas com botões, Contatos vinculados |
| 10 | Boleto e nota pelo bot | E ele se atende sozinho. Em segunda via do boleto, toca no boleto e recebe o PDF com a linha digitável. Em Notas fiscais, recebe o DANFE das notas autorizadas. | Cliente toca em 2ª via do boleto → Boleto.pdf com linha digitável; /nota → DANFE |
| 11 | Foto e resposta | Se o cliente manda uma mensagem ou a foto de uma peça, ela chega no grupo da equipe. Quem responde àquela mensagem no grupo responde direto ao cliente. | Foto da peça chega no grupo; Bruno responde e o cliente recebe |
| 12 | Conversas no ERP | E tudo fica em Conversas, como no WhatsApp: o histórico de cada contato, a foto que ele mandou e o painel com o cadastro do cliente no sistema. | /integracoes/telegram/conversas: histórico, foto, painel ERP |
| 13 | /estoque | A equipe também consulta pelo bot. Barra estoque com o código ou o nome do item mostra o saldo e o preço, com sinal verde, laranja ou vermelho. | Conversas, chat do Bruno: /estoque pastilha cg 160 |
| 14 | /resumo e /vencidas | Barra resumo traz as vendas e o que entrou hoje, com as faturas vencidas. E barra vencidas lista o que está em atraso. | /resumo e /vencidas |
| 15 | Bloco nos Workflows | Nos Workflows, o bloco Telegram leva o aviso que você quiser para a equipe ou para o cliente, dentro das suas automações. Gestor Easy: erp.gestoreasy.com.br. | Editor de Workflows: Evento + bloco Telegram (equipe, mensagem) |

Pronúncia no texto da voz: Gestor Ízi, BotFather = "Bót Fáder", newbot = "níu bót", Workflows = "Uórk flôus", Shopee = "Xópi", Pix = "píks", PDF = "pê dê éfe", DANFE = "dânfe", site = "erp ponto gestorízi ponto com ponto bê érre".

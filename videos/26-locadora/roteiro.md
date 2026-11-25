# Roteiro: Locadora de veículos (Gestor Easy)

Vídeo narrado de 2min33 (pc e celular 1080x1080, vertical 1080x1920), gravado nas telas reais do módulo Locadora com dados fictícios da "Rota Livre Locadora". A consulta de débitos foi gravada com um simulador local da API Brasil: nenhuma consulta real foi feita.

| # | Cena | Narração | Tela |
|---|---|---|---|
| 01 | Abertura | Tem locadora de motos ou de carros? No Gestor Easy, o módulo Locadora cuida da frota, dos contratos, das reservas e até das multas, tudo num lugar só. | /locadora/dashboard |
| 02 | Painel | O painel mostra na hora quantos veículos estão disponíveis, locados e em manutenção, os contratos abertos, a receita dos últimos trinta dias e a taxa de ocupação. | /locadora/dashboard (cards) |
| 03 | Cadastro do veículo | Para cadastrar um veículo, informe placa, marca, modelo, chassi, RENAVAM e o valor da diária. Seguro e validade do CRLV ficam na mesma ficha. | /locadora/frota/create |
| 04 | Ficha do veículo | Na ficha do veículo você guarda os anexos, como CRLV e apólice, e acompanha o histórico de todos os contratos daquela placa. | ficha do veículo (anexos, histórico de contratos) |
| 05 | Catálogo on-line | A locadora ganha um catálogo on-line com o endereço da sua empresa. O cliente escolhe o veículo, as datas e pede a reserva sozinho. | /locadora/e/{empresa}/catalogo e pedido de reserva |
| 06 | Pedido vira contrato | O pedido cai em Solicitações do portal. Você confere os dados do cliente e o período, aprova e transforma em contrato com um clique. | /locadora/solicitacoes: aprovar e converter |
| 07 | Contrato no balcão | Também dá para abrir o contrato direto no balcão: escolha o cliente e o veículo, as datas, e o sistema calcula os dias e o valor total. | /locadora/contratos/create |
| 08 | Checklist de saída | Na saída, faça o checklist: pneus, estepe, combustível, documentos e avarias, com o nome de quem conferiu. | contrato: Novo Checklist |
| 09 | Pagamentos | Os pagamentos do contrato são lançados ali mesmo, em dinheiro, cartão, Pix ou boleto, e o que falta pagar fica sempre à vista. | contrato: Pagamentos |
| 10 | Devolução | Na devolução, informe a quilometragem de retorno e algum valor adicional. O contrato é finalizado e o veículo volta a ficar disponível. | contrato: Finalizar Contrato |
| 11 | Débitos pela placa | E as multas? Em Débitos dos veículos, consulte pela placa as multas, o IPVA e o licenciamento. Antes de cada consulta o sistema mostra o valor e pede sua confirmação. | /locadora/debitos: Consultar (aviso do valor + confirmação) |
| 12 | Multa no locatário | O resultado separa multas, IPVA e licenciamento. Multa nova aparece destacada, e o sistema já sugere o contrato que estava em vigor na data, para lançar a cobrança no locatário. | resultado da consulta: multa nova e Lançar no contrato |
| 13 | Consulta automática | Se preferir, ligue a consulta automática dos veículos locados, toda semana, a cada quinze dias ou uma vez por mês, sempre com o seu aceite. | /locadora/debitos: consulta automática com aceite |
| 14 | Relatórios | Nos relatórios você acompanha contratos, disponibilidade da frota, manutenções, financeiro e o SLA da equipe. | /locadora/relatorios e Financeiro |
| 15 | Encerramento | Gestor Easy. Sua locadora organizada, do cadastro à devolução. Acesse erp.gestoreasy.com.br. | cartão final |

Pronúncia no texto da voz: Pix = "píks", site = "erp ponto gestorízi ponto com ponto bê érre", CRLV = "cê érre éle vê", RENAVAM = "renavã", SLA = "ésse éle á", on-line = "onláine".

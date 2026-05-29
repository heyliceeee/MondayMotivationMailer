# Monday Motivation Mailer

O **Monday Motivation Mailer** é uma pequena automação que envia, todas as segundas‑feiras, uma mensagem de motivação diretamente para o email do destinatário. O objetivo é começar a semana com foco, energia e uma frase inspiradora escolhida aleatoriamente a partir de uma lista pré-definida.

## Como funciona

- Verifica automaticamente o dia da semana.  
- Se for segunda‑feira, seleciona uma citação motivacional de um ficheiro de texto.  
- Constrói uma mensagem simples com assunto e conteúdo motivacional.  
- Envia o email através de um servidor SMTP configurado por variáveis de ambiente.  
- Nos restantes dias, a automação permanece inativa.

## Estrutura do projeto

- **data/quotes.txt** — lista de citações motivacionais utilizadas no envio semanal.  
- **Variáveis de ambiente** — definem as credenciais e parâmetros do servidor SMTP.  
- **Script principal** — coordena a leitura das citações, a seleção aleatória e o envio do email.

## Objetivo

Criar uma rotina leve e automática que incentive consistência, disciplina e bem‑estar ao início de cada semana, através de mensagens positivas enviadas por email.

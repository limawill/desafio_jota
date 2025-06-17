# desafio_jota

## Fila de Mensagens

- **RabbitMQ**: Broker de mensagens, acessível em `http://localhost:15672` (usuário: `rabbit`, senha: `rabbit`).
- **Celery**: Processa notícias assincronamente. Worker roda como serviço `celery`.
- **Teste**: Envie um webhook para `/webhook/news/` com Insomnia. Verifique a fila `celery` no RabbitMQ e a notícia no admin.

# desafio_jota

## Fila de Mensagens

- **RabbitMQ**: Broker de mensagens, acessível em `http://localhost:15672` (usuário: `rabbit`, senha: `rabbit`).
- **Celery**: Processa notícias assincronamente. Worker roda como serviço `celery`.
- **Teste**: Envie um webhook para `/webhook/news/` com Insomnia. Verifique a fila `celery` no RabbitMQ e a notícia no admin.

## Classificação de Notícias

- **Lógica**: Classificação baseada em palavras-chave para sentimento (Positivo, Negativo, Neutro) e relevância (score 0-100).
- **Implementação**: Função `classify_news` na app `classification`, integrada à task Celery.
- **Visualização**: Resultados em `/admin/classification/classification/`, com filtros por sentimento e categoria.
- **Teste**: Envie um webhook e verifique as classificações no admin.

## Consultas

- **Endpoint**: `GET /api/news/`
- **Filtros**:
  - `is_urgent`: `true` ou `false` (ex.: `?is_urgent=true`).
  - `category__name`: Nome da categoria (ex.: `?category__name=Ciência`).
  - `classifications__sentiment`: Sentimento (`POS`, `NEG`, `NEU`) (ex.: `?classifications__sentiment=POS`).
  - `search`: Busca em título/conteúdo (ex.: `?search=reforma`).
- **Ordenação**: `publication_date`, `classifications__relevance_score` (ex.: `?ordering=-relevance_score`).
- **Paginação**: 10 notícias por página.
- **Teste**: Use Insomnia para enviar requisições e verifique resultados no admin (`http://localhost:5746/admin/`).

## Solução de Problemas

- **Erro 404**: Verifique `news_api/urls.py` e `api/urls.py`. Rebuild com `docker compose up --build`.

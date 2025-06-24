# 🗞️ News API - Sistema de Classificação de Notícias

Solução para processamento, classificação e consulta de notícias usando Django, Celery e spaCy.

## 🚀 Tecnologias Utilizadas

- **Django** (framework web)
- **Celery** (processamento assíncrono)
- **RabbitMQ** (broker de mensagens)
- **PostgreSQL** (banco de dados)
- **spaCy** (processamento de linguagem natural)
- **Docker** (containerização)

## ⚙️ Arquitetura do Projeto

```bash
├── .gitignore
├── Dockerfile
├── LICENSE
├── README.md
├── docker-compose.yml
├── entrypoint.sh
├── etapas.md
├── manage.py
├── news_api
│   ├── apps
│   │   ├── api           # Endpoints REST para consulta
│   │   ├── classification# Lógica de classificação
│   │   ├── core          # Modelos de dados principais
│   │   └── webhook       # Recebimento de webhooks
│   ├── asgi.py
│   ├── celery.py         # Configuração Celery
│   ├── settings.py       # Configurações Django
│   ├── urls.py           # Rotas principais
│   └── wsgi.py
├── pytest.ini            # Configuração de testes
├── requirements.txt      # Dependências
├── teste.py
└── wait-for-it.sh        # Script de inicialização
```

## 🔧 Como Executar

### Pré-requisitos

- Docker

- Docker Compose

### Passo a Passo

```bash

# 1. Clone o repositório

git clone https://github.com/limawill/desafio_jota

cd desafio_jota

# 2. Inicie os serviços

docker compose up --build -d

# 3. Acesse os serviços:

```

| Serviço | URL | Credenciais |

|-----------------|------------------------------|-------------------|

| Django App | http://localhost:5746 | - |

| Django Admin | http://localhost:5746/admin | user: admin, senha: admin (criar com `createsuperuser`) |

| RabbitMQ Manager| http://localhost:15672 | user: rabbit, senha: rabbit |

## 🌟 Funcionalidades Principais

### 1. Recebimento de Webhooks

**Endpoint**: `POST /webhook/news/`

**Exemplo de payload**:

```json
{
  "title": "Descoberta arqueológica na China",

  "content": "Arqueólogos encontraram um crânio que pode reescrever a história...",

  "source": "Ciência Hoje",

  "publication_date": "2025-06-24T10:30:00Z",

  "category": "Ciência",

  "subcategory": "Arqueologia",

  "tags": ["fóssil", "evolução"],

  "is_urgent": true
}
```

### 2. Classificação Automática

- **Sentimento**: POS (Positivo), NEG (Negativo), NEU (Neutro)

- **Relevância**: Score de 0-100 baseado em palavras-chave

- **Tags dinâmicas**: Extraídas automaticamente usando spaCy

### 3. API de Consulta

**Endpoint**: `GET /api/news/`

**Parâmetros**:

- `is_urgent`: true/false

- `category__name`: Nome da categoria

- `classifications__sentiment`: POS/NEG/NEU

- `search`: Busca em título/conteúdo

- `ordering`: `-publication_date` (data decrescente)

**Exemplo**:

```

/api/news/?is_urgent=true&category__name=Ciência&ordering=-publication_date

```

## 🧪 Testando o Sistema

### 1. Envio de webhook

Use o Insomnia/Postman para enviar payloads para:

```

POST http://localhost:5746/webhook/news/

```

### 2. Monitoramento

- Verifique filas no RabbitMQ: http://localhost:15672

- Confira notícias no Admin: http://localhost:5746/admin

- Consulte via API: http://localhost:5746/api/news/

## ✅ Status de Implementação

### 🟢 Etapas Concluídas (1-7)

1. **Configuração do Ambiente**

   - Docker Compose com serviços: app (Django), db (PostgreSQL), RabbitMQ, Redis
   - Persistência de dados com volume PostgreSQL
   - Dependências instaladas via `requirements.txt`

2. **Modelagem do Banco de Dados**

   - Modelos: `Category`, `Subcategory`, `Tag`, `News`
   - Relacionamentos configurados (categoria obrigatória, subcategoria/tags opcionais)
   - Painel admin para gerenciamento

3. **Endpoint para Webhooks**

   - POST `/webhook/news/` para receber notícias
   - Validação de payload com serializers
   - Criação/recuperação de categorias e tags

4. **Armazenamento em Fila**

   - RabbitMQ como broker de mensagens
   - Configuração do Celery para tarefas assíncronas
   - Processamento de notícias em background

5. **Classificação de Notícias**

   - Modelo `Classification` com sentimentos (POS/NEG/NEU) e relevância
   - Lógica baseada em palavras-chave
   - Integração com task Celery

6. **API REST para Consulta**

   - GET `/api/news/` com filtros e ordenação
   - Serialização de notícias com classificações
   - Paginação (10 itens por página)

7. **Agrupamento por Temática**
   - Extração de tags dinâmicas com spaCy
   - Adição automática de tags ao modelo `News`
   - Filtro por tags na API

### 🔴 Etapas Pendentes (8-12)

8. **Testes Unitários**

   - Cobertura de testes com pytest
   - Testes para modelos, views e tasks

9. **Segurança**

   - Autenticação JWT para API
   - Validações avançadas e proteções (CORS/CSRF)

10. **Observabilidade**

    - Configuração de logs estruturados
    - Métricas de desempenho

11. **Documentação**

    - Diagramas de arquitetura
    - Documentação OpenAPI (drf-spectacular)

12. **Notificações WhatsApp**
    - Integração com API de mensagens
    - Envio assíncrono de alertas

> **Nota**: As etapas 8-12 não foram implementadas devido a restrições de tempo, mas representam melhorias importantes para versões futuras do projeto.

## 📝 Licença

Este projeto está sob licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

---

Desenvolvido por [Will Lima](https://github.com/limawill) - 2025

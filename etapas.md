Lista de Etapas Atualizada (Sem AWS, Foco Local)
Com base na descrição do desafio e na sua preferência por uma solução containerizada, aqui está a lista revisada de etapas, mantendo o formato que você gostou e ajustando para evitar dependências na AWS. Cada etapa explica o que foi feito (concluídas) ou o que falta (pendentes), sem código.
Etapas Concluídas
Etapa 1: Configuração do Ambiente
Descrição: Configuração do ambiente de desenvolvimento com Docker, incluindo contêineres para a aplicação Django e o banco PostgreSQL. Instalação de dependências como Python 3.11, Django 5.2.3, e Django REST Framework. Configuração de persistência de dados.

O que foi feito:
Docker Compose configurado com serviços app (Django) e db (PostgreSQL 15).

Volume postgres_data implementado para persistir dados do banco.

Dependências instaladas via requirements.txt (Django, DRF).

Servidor Django rodando em http://localhost:5746.

Problemas de persistência resolvidos, garantindo que os dados sejam mantidos.

Etapa 2: Modelagem do Banco de Dados
Descrição: Criação de modelos para armazenar notícias, categorias, subcategorias, e tags, com relacionamentos apropriados. Configuração do painel admin para testes manuais.

O que foi feito:
Modelos Category, Subcategory, Tag, e News criados na app core.

Relacionamentos definidos: News vinculada a Category (obrigatória), Subcategory (opcional), e Tags (opcional, ManyToMany).

Campos em News: title, content, source, publication_date, is_urgent, created_at, updated_at.

Migrações aplicadas, criando tabelas no banco.

Painel admin configurado para gerenciar modelos, com filtros e busca.

Dados de teste criados (ex.: categoria "Tributos", subcategoria "Aposta da Semana", tag "Imposto de Renda").

Etapa 3: Endpoint para Webhooks
Descrição: Implementação de um endpoint REST para receber notícias via webhooks em formato JSON, validando e enviando os dados para processamento.

O que foi feito:
Endpoint /webhook/news/ criado na app webhook com Django REST Framework.

Serializer configurado para validar o payload (title, content, source, publication_date, category, subcategory opcional, tags opcional, is_urgent).

Lógica para criar ou reutilizar Category, Subcategory, e Tag.

Testado com Insomnia, retornando 201 (sucesso) e 400 (erro).

Dados confirmados no admin, com persistência validada.

Etapas Pendentes
Etapa 4: Armazenamento de Notícias em Fila
Descrição: Configuração de uma fila de mensagens local (RabbitMQ ou Redis) para armazenar notícias recebidas pelo webhook, permitindo processamento assíncrono em um ambiente containerizado.

O que falta fazer:
Adicionar RabbitMQ (ou Redis) ao docker-compose.yml como serviço.

Configurar Celery para gerenciar tarefas assíncronas, usando RabbitMQ (ou Redis) como broker.

Modificar o webhook para enviar notícias à fila.

Criar uma task Celery para consumir mensagens e salvar no banco.

Documentar a escolha (RabbitMQ para aprendizado ou Redis para simplicidade).

Etapa 5: Classificação de Notícias
Descrição: Desenvolvimento de um sistema de classificação para atribuir metadados às notícias (ex.: sentimento, relevância) com base em palavras-chave no título e corpo, usando Python puro ou bibliotecas como NLTK.

O que falta fazer:
Criar um modelo Classification na app classification (ex.: campos sentiment, relevance_score).

Implementar uma lógica de classificação simples (ex.: regras baseadas em palavras-chave).

Integrar a classificação à task Celery que processa a fila.

Configurar o admin para visualizar classificações.

Etapa 6: API REST para Consulta
Descrição: Criação de uma API REST na app api para a equipe editorial consultar notícias classificadas, com filtros por categoria, subcategoria, tags, urgência, e data, e permitir marcar notícias como urgentes.

O que falta fazer:
Criar serializers e views para listar e detalhar notícias.

Implementar endpoints GET /api/news/ (com filtros) e PATCH /api/news/<id>/ (para atualizar is_urgent).

Configurar URLs na app api e incluí-las no projeto.

Testar endpoints com Insomnia.

Etapa 7: Agrupamento por Temática
Descrição: Extensão da classificação para gerar tags automaticamente com base no conteúdo da notícia, permitindo filtragem por temática na API.

O que falta fazer:
Aprimorar a lógica de classificação para extrair tags dinâmicas (ex.: usando NLTK ou spaCy).

Atualizar o modelo News para suportar tags geradas automaticamente.

Adicionar filtro por tags no endpoint GET /api/news/.

Etapa 8: Testes Unitários e de Integração
Descrição: Escrita de testes com pytest para cobrir modelos, serializers, views, endpoints, e lógica de classificação, garantindo qualidade do código.

O que falta fazer:
Instalar pytest e pytest-django.

Configurar pytest.ini para integração com Django.

Escrever testes para modelos, serializers, views, webhook, e classificação.

Executar testes no contêiner e verificar cobertura.

Etapa 9: Segurança
Descrição: Aplicação de práticas de segurança, como autenticação na API, validação de entradas, e proteção contra ataques comuns.

O que falta fazer:
Configurar autenticação para a API de consulta (ex.: JWT).

Adicionar validações robustas no serializer do webhook.

Configurar CORS e CSRF.

Documentar práticas de segurança no README.md.

Etapa 10: Observabilidade
Descrição: Configuração de logging e métricas para monitorar desempenho e identificar gargalos.

O que falta fazer:
Configurar logging no Django (ex.: logs em arquivo ou stdout).

Adicionar métricas simples (ex.: tempo de processamento do webhook).

Documentar como acessar logs no ambiente containerizado.

Etapa 11: Documentação
Descrição: Criação de documentação detalhada com instruções de execução, descrição dos endpoints, e arquitetura da solução.

O que falta fazer:
Atualizar README.md com instruções para rodar o projeto, testar endpoints, e executar testes.

Criar um diagrama da arquitetura (ex.: Draw.io).

Opcional: Configurar drf-spectacular para documentação OpenAPI.

Etapa 12: Notificações via WhatsApp (Opcional)
Descrição: Integração com uma API de WhatsApp para enviar notificações de notícias urgentes.

O que falta fazer:
Escolher uma API de WhatsApp (ex.: Twilio).

Configurar uma task Celery para enviar notificações quando is_urgent for verdadeiro.

Simular o envio localmente (ex.: logs em vez de chamadas reais à API).

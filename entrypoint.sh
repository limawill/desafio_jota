#!/bin/bash
set -e

# Instalar modelos do spaCy
python -m spacy download pt_core_news_sm || echo "Modelo pt_core_news_sm já instalado"
python -m spacy download pt_core_news_lg || echo "Modelo pt_core_news_lg já instalado"

# Executar o comando passado
exec "$@"
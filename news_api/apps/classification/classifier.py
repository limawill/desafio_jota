import string

def classify_news(title, content, category):
    # Dicionários de palavras-chave
    positive_keywords = ['descoberta', 'avanço', 'revelação', 'interessante', 'redução', 'isenção', 'sucesso']
    negative_keywords = ['crise', 'tragédia', 'problema', 'aumento', 'rejeição', 'desastre']
    category_keywords = {
        'Tributos': ['tributária', 'imposto', 'ir', 'fiscal', 'reforma', 'congresso'],
        'Ciência': ['dna', 'evolução', 'fóssil', 'pesquisa', 'descoberta', 'crânio'],
        'Outros': []
    }

    # Pré-processamento: concatenar título e corpo, converter para minúsculas, remover pontuação
    text = f"{title} {content}".lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()

    # Contar palavras-chave para sentimento
    positive_count = sum(1 for word in words if word in positive_keywords)
    negative_count = sum(1 for word in words if word in negative_keywords)

    # Determinar sentimento
    if positive_count > negative_count:
        sentiment = 'POS'
    elif negative_count > positive_count:
        sentiment = 'NEG'
    else:
        sentiment = 'NEU'

    # Determinar palavras-chave de relevância
    if category in category_keywords:
        keywords = category_keywords[category]
    else:
        # Usar palavras do título como fallback
        keywords = title.lower().split()

    # Contar palavras-chave para relevância
    keyword_count = sum(1 for word in words if word in keywords)
    total_words = len(words) if len(words) > 0 else 1
    relevance_score = (keyword_count / total_words) * 100

    return {
        'sentiment': sentiment,
        'relevance_score': relevance_score,
        'category': category or 'Outros'
    }
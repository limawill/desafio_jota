import spacy
nlp = spacy.load('pt_core_news_sm')
doc = nlp("Arqueólogos encontraram um crânio na China que pode mudar a história da evolução humana.")
for ent in doc.ents:
    print(ent.text, ent.label_)
for token in doc:
    if token.pos_ == 'NOUN':
        print(token.text, token.pos_)
exit()
# importacoes nescessarias para o codigo 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np 
import nltk
from nltk.corpus import stopwords
import string 
import pandas as pd 
# cleaning and organizing the database
tabela = pd.read_excel(r"games.xlsx")
linhas, colunas = tabela.shape
list(tabela.columns)
# transfrmacao de texto 
stop_words = set(stopwords.words('english'))
def remove_stopwords(texto):
    if isinstance(texto, str):  # Verifica se o valor é uma string
        return ' '.join([words for words in texto.split() if words not in stop_words])
    else:
        return ''
tabela['cleaned_full_desc'] = tabela['full_desc'].apply(remove_stopwords)
pd.set_option('display.max_colwidth', None)
textos = tabela['cleaned_full_desc']
vectorizer = TfidfVectorizer()
tx_vetor= vectorizer.fit_transform(textos)
similaridade_cosseno = cosine_similarity(tx_vetor)
tabela_pandas = pd.DataFrame(similaridade_cosseno, index=tabela["name"], columns=tabela["name"])
tabela_pandas.to_hdf('similaridade_cosseno.h5', key='df', mode='w', complib='blosc')





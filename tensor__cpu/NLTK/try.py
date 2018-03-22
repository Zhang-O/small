# 去除标点符号等特殊字符的正则表达式分词器


from pandas import DataFrame
import pandas as pd
d = ['pets insurance','pets insure','pet insurance','pet insur','pet insurance"','pet insu']
df = DataFrame(d)
df.columns = ['Words']
import nltk
from nltk.stem import WordNetLemmatizer
wnl = WordNetLemmatizer()

tokenizer = nltk.RegexpTokenizer(r'w+')

df["Stemming Words"] = ""
df["Count"] = 1

j = 0
while (j <= 5):
    print(df["Words"][j])
    print(tokenizer.tokenize(df["Words"][j]))
#     for word in tokenizer.tokenize(df["Words"][j]):
#         print(wnl.lemmatize(word))
#         df["Stemming Words"][j] = df["Stemming Words"][j] + " " + wnl.lemmatize(word)
    j = j + 1

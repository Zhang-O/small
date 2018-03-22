# -*- code:utf-8 -*-

"""
application of nltk in classification
"""

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from gensim import corpora, models, similarities
import csv
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix, classification_report
from sklearn import tree
from sklearn.linear_model import SGDClassifier
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.cluster import KMeans, MiniBatchKMeans
from collections import defaultdict
from itertools import chain
from operator import itemgetter
import re


# 对文本进行预处理
def preprocessing(text):

    tokens = [ word for sentence in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sentence)]
    stop  = stopwords.words('english')
    # print(stop)

    # remove the stopwords
    tokens = [token for token in tokens if token not in stop]
    # removing words whose length are less than 3
    tokens = [word for word in tokens if len(word) >= 3]
    tokens = [word.lower() for word in tokens]  # lowering alphabat

    # 词形还原
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    processed_text = ' '.join(tokens)

    return processed_text


# open txt file, extract data and label
sms = open('./Machine-Learning-with-R-datasets-master/SMSSpamCollection.txt', encoding='utf8')
sms_datas = []
sms_labels = []
csv_reader = csv.reader(sms, delimiter='\t')
for line in csv_reader:
    sms_labels.append(line[0])
    sms_datas.append(preprocessing(line[1]))
sms.close()


# sampling  for  train and test
train_set_size = int(round(len(sms_labels)*0.70))

# print('The training set size for this classifier is ' + str(train_set_size) + '\n')
# x_train_set = np.array([''.join(el) for el in sms_datas[0: train_set_size]])
# y_train_set = np.array([el for el in sms_labels[0: train_set_size]])
# x_test_set = np.array([''.join(el) for el in sms_datas[train_set_size+1:len(sms_datas)]])
# y_test_set = np.array([el for el in sms_labels[train_set_size+1:len(sms_labels)]])

print('train set size :' + str(train_set_size) + '\n')

# should consider ramdoning the data later
x_train_set = np.array(sms_datas[0:train_set_size])
y_train_set = np.array(sms_labels[0:train_set_size])

x_test_set = np.array(sms_datas[train_set_size:-1])
y_test_set = np.array(sms_labels[train_set_size:-1])

# print(x_train_set)
# print(y_train_set)


# extract features
sms_exp = []
print('sms_datas length :' + str(len(sms_datas)))  # 5572
for line in sms_datas:
    sms_exp.append(preprocessing(line))
print('sms_exp length :' + str(len(sms_exp)))  # 5572


vectorizer = CountVectorizer(min_df=1, encoding='utf-8')
# return csr matrix of shape = (len(sms_exp), tokens)
X_exp = vectorizer.fit_transform(sms_exp)
# print(X_exp)
# print('||'.join(vectorizer.get_feature_names()))
# print(X_exp.toarray())

vectorizer_1 = TfidfVectorizer(min_df=2, ngram_range=(1, 2), stop_words='english',
                               strip_accents='unicode', norm='l2')
X_train_set = vectorizer_1.fit_transform(x_train_set)
X_test_set = vectorizer_1.transform(x_test_set)

# print(X_train_set)
# print(X_test_set)



# --------------------  Naive Bayes CLS  -------------------------------
print('# --------------------  Naive Bayes CLS  -------------------------------')

classifier_naive_bayes = MultinomialNB().fit(X_train_set, y_train_set)
y_bayes_predict = classifier_naive_bayes.predict(X_test_set)

# print(y_bayes_predict)
print('\n confusion_matrix \n')
confusion_M = confusion_matrix(y_test_set,y_bayes_predict)
# print(y_test_set)
print(confusion_M)

print('\n Here is the classification report:')
print(classification_report(y_test_set,y_bayes_predict))

feature_names = vectorizer_1.get_feature_names()

# print(classifier_naive_bayes.coef_)
# print(classifier_naive_bayes.intercept_)
'''
[[-7.98987527 -8.22274866 -7.24524555 ..., -8.51681462 -8.73944109
  -8.69659372]]
'''
# coefs_with_fns = sorted(zip(classifier_naive_bayes.coef_[0], feature_names))
# _n = 10
# top = zip(coefs_with_fns[0: _n], coefs_with_fns[-_n:])
# for (coe1, fea1), (coe2, fea2) in top:
#     print('\t%.4f\t%-15s\t%.4f\t%-15s' %(coe1, fea1, coe2, fea2))


# --------------------  decision tree CLS  -------------------------------
print('\n--------------------  decision tree CLS  -------------------------------\n')
clf_tree = tree.DecisionTreeClassifier().fit(X_train_set, y_train_set)
y_tree_prediction = clf_tree.predict(X_test_set)

print('\n confusion_matrix \n')
confusion_M_tree = confusion_matrix(y_test_set,y_tree_prediction)
print(confusion_M_tree)

# print(y_tree_prediction)
print('\n Here is the classification report:')
print(classification_report(y_test_set, y_tree_prediction))


# --------------------   sgd CLS -------------------------------
print('\n--------------------  sgd CLS  -------------------------------\n')
clf_sgd = SGDClassifier().fit(X_train_set, y_train_set)
y_sgd_prediction = clf_sgd.predict(X_test_set)
# print(y_sgd_prediction)

print('\n confusion_matrix \n')
confusion_M_sgd = confusion_matrix(y_test_set,y_sgd_prediction)
print(confusion_M_sgd)

print('\n Here is the classification report:')
print(classification_report(y_test_set, y_sgd_prediction))


# --------------------  SVM  -------------------------------
print('\n--------------------  SVM CLS  -------------------------------\n')

cls_svm = LinearSVC().fit(X_train_set, y_train_set)
y_svm_prediction = cls_svm.predict(X_test_set)

print('\n confusion_matrix \n')
confusion_M_svm = confusion_matrix(y_test_set,y_svm_prediction)
print(confusion_M_svm)

print('\n Here is the classification report:')
print(classification_report(y_test_set, y_svm_prediction))


# --------------------  Random Forest -------------------------------
print('\n--------------------  Random Forest CLS  -------------------------------\n')

cls_rf = RandomForestClassifier().fit(X_train_set, y_train_set)
y_rf_prediction = cls_rf.predict(X_test_set)

print('\n confusion_matrix \n')
confusion_M_rf = confusion_matrix(y_test_set,y_rf_prediction)
print(confusion_M_rf)

print('\n Here is the classification report:')
print(classification_report(y_test_set, y_rf_prediction))


# --------------------  Random Forest -------------------------------
print('\n--------------------  Logistic Regression CLS  -------------------------------\n')

cls_logit = LogisticRegression().fit(X_train_set, y_train_set)
y_logit_prediction = cls_logit.predict(X_test_set)

print('\n confusion_matrix \n')
confusion_M_logit = confusion_matrix(y_test_set,y_logit_prediction)
print(confusion_M_logit)

print('\n Here is the classification report:')
print(classification_report(y_test_set, y_logit_prediction))


# --------------------  cluster -------------------------------
print('\n--------------------  kmeans cluster  -------------------------------\n')

true_k = 5
km = KMeans(n_clusters = true_k, init='k-means++', max_iter=100, n_init= 1)
kmini = MiniBatchKMeans(n_clusters=true_k, init='k-means++', n_init=1, init_size=1000, batch_size=1000, verbose=2)
km_model = km.fit(X_train_set)
kmini_model = kmini.fit(X_train_set)
print("For K-mean clustering ")
clustering = defaultdict(list)
for idx, label in enumerate(km_model.labels_):
    clustering[label].append(idx)
print("For K-mean Mini batch clustering ")
clustering = defaultdict(list)
for idx, label in enumerate(kmini_model.labels_):
    clustering[label].append(idx)


# --------------------  topic model -------------------------------
print('\n--------------------  topic model with gensim  -------------------------------\n')

docs = [doc for doc in sms_datas]
stoplist = stopwords.words('english')
texts = [[word for word in text.lower().split() if word not in stoplist] for text in docs]
# print(texts)

dictionary = corpora.Dictionary(texts)
# genaerate a doc-word-frequency matrix
corpus = [dictionary.doc2bow(text) for text in texts]
# print(corpus)

# generate a doc-word-tf-idf matrix
tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]
print('-----tf-idf value-------')
print(corpus_tfidf[0])
print(corpus_tfidf[1])
print(corpus_tfidf)

print('\n-----lsi topic model-------\n')
lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=1000)
corpus_lsi = lsi[corpus_tfidf]
print('\n-----lsi value-------\n')
print(corpus_lsi[0])
print(corpus_lsi[1])
print(lsi.print_topics(1))


print('\n-----build index for similarity-------\n')
# build index for similarity
index = similarities.MatrixSimilarity(lsi[corpus_lsi])
# query = "gold silver truck"
query = "Lol your always so convincing"
query_bow = dictionary.doc2bow(query.lower().split())
print(query_bow)
query_lsi = lsi[query_bow]
print(query_lsi)
sims = index[query_lsi]
print(list(enumerate(sims))[26])
sort_sims = sorted(enumerate(sims), key=lambda item: -item[1])[:10]
print(sort_sims)


print('\n----- LDA -------\n')
n_topics = 5
lda = models.LdaModel(corpus_tfidf, id2word = dictionary, num_topics = n_topics)
for i in range(0, n_topics):
    temp = lda.show_topic(i, 10)
    terms = []
    for term in temp:
        terms.append(str(term[0]))
    print("Top 10 terms for topic #" + str(i) + ": " + ",".join(terms))


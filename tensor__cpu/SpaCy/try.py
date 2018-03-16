import spacy

nlp = spacy.load('en_core_web_md')

from spacy.tokens import Doc
from spacy.vocab import Vocab

doc = nlp(u'I like coffee') # original Doc
# print(doc[0].vector)
# print(doc[1].vector)
# print(doc[2].vector)
# print(doc.vector * 3)
# print(doc[0].vector + doc[1].vector + doc[2].vector )

print(doc[1].i)


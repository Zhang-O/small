# -*- coding: utf-8 -*-

a = None
with open('./2222.txt', 'r', encoding='GBK') as f:
    a = f.read()
    print(a)

# with open('./2222.txt', 'w', encoding='utf-8') as f:
#     f.write(a)
#     print(a)


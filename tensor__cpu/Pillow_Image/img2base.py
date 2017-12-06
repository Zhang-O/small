# -*- coding: utf-8 -*-

import base64
from PIL import Image
import io


p = "C:/zhang/项目/身份证识别/img_data/zhangkaiguo1/140122199708130026_康乐_照片反面.jpg"

# with open(p, "rb") as f:
#     # b64encode是编码，b64decode是解码
#     base64_data = base64.b64encode(f.read())
#     # base64.b64decode(base64data)
#     print(base64_data)
#     with open('./1.txt', 'wb') as f:
#         f.write(base64_data)

im = Image.open(p)
im.show()

# b = im.tobytes()
# # print(b)
output = io.BytesIO()
im.save(output, format='JPEG')
base64_data = base64.b64encode(output.getvalue())
print(base64_data)

with open('./2.txt', 'wb') as f:
    f.write(base64_data)




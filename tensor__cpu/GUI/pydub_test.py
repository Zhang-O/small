from pydub import AudioSegment
from pydub.silence import split_on_silence
import random
import sys

file = "./QT-742440ans.mp3"
sound = AudioSegment.from_mp3(file)
print(sound)

# time_start = "00:00"
# time_end = "00:60"
#
# song = AudioSegment.from_mp3(file)
# start = (int(time_start.split(':')[0])*60 + int(time_start.split(':')[1]))*1000
# end = (int(time_end.split(':')[0])*60 + int(time_end.split(':')[1]))*1000
# # print(start, end)
# word = song[start:end]
# words = split_on_silence(word, min_silence_len=700, silence_thresh=-32)
# silent = AudioSegment.silent(duration=1000)
#
# def run(m, n):
#     new = AudioSegment.empty()
#     for i in range(n):
#         new += words[m+i*5]+silent
#     # 每列保存为一个音频文件
#     new.export('%d_row.mp3' % m, format='mp3')
#
# for i in range(5):
#     if i == 0:
#         run(i, 11) # 第一列有 11 个音
#     else:
#         run(i, 10)
#
# random.shuffle(words) # 对五十音进行随机排列
# new = AudioSegment.empty()
# for i in words:
#     new += i + silent
# # 保存为一个用来听写的音频文件
# new.export('listening.mp3', format='mp3')

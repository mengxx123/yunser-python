# print("Hello, World!");

# for letter in 'asd':
#     print(letter)

import jieba
s = u'我想和女朋友一起去北京故宫博物院参观和闲逛。'

cut = jieba.cut(s)

print('【Output】')
print(cut)
print(','.join(cut))

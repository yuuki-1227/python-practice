# print('Hello, world!')
# print(1 + 2)

# # 演算
# print(1 + 1)
# print(1-1)
# print(1*2)

# 変数
# test = 'l_size'
# tall = 5
# weight = 5.5

# # print(login_id + test)

# # 条件分岐と関係演算子

# if tall > 3:
#     print('ooii')
# else:
#   print('sukunai')

# 関数 引数arg
# def test_python(arg):
#     test_status = arg

# if(test_status < 10):
# return 'sukunai'
# else:
# return 'ooi'


# print(test_python(9))

# list
# test_list = ['test_samll', 'test_medium', 'test_large']
# print(test_list[1])

# for
# for index in range(11):
# print(test_python(index))

# for item in test_list:
# print(item)

# with 開始から終わりまでを自動で行ってくれる
# open()
# with open('./test.txt', 'r') as file:
#     print(file.read())

# class
import numpy
import math


# class Card:
#     def __init__(self, date, user_name):
#         self.date = date
#         self.user_name = user_name

#     def message(self):
#         return 'この投稿は' + self.user_name + 'さんが' + self.date + 'に投稿しました'


# date_a = '2021-01-01'
# user_name_a = 'Taro'
# card_a = Card(date_a, user_name_a)

# date_b = '2021-01-02'
# user_name_b = 'kayoko'
# card_b = Card(date_b, user_name_b)

# print(card_b.message())

# import
# 標準ライブラリ math　　math.pi 円周率
# import math
# print(math.pi)

# 外部ライブラリ（モジュール）
# NumPy ナムパイ
# Pandas
# Flask
# Django


numpy_list = [3, 2, 6, 7]
print(numpy.sum(numpy_list))

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
with open('./test.txt', 'r') as file:
    print(file.read())

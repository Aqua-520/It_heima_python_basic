# with open('./test_dir/瞎写的.txt', 'w+', encoding='utf-8') as file:
#     # 'w+' 模式：可读可写。但文件打开瞬间就会被【立即清空】！
#     # 如果此时直接 file.read()，因为文件已空且光标在开头，只会读到空字符串。
#
#     file.write('呵呵\n')
#     file.write('哈啊哈')
#
#     # 连续 write() 之后，文件指针（光标）停留在文件末尾。
#     # 如果不重置光标，直接 read() 会因为后面没有内容而读出空字符串。
#
#     file.seek(0)  # 将文件指针（光标）移动回文件开头 (0 字节处)
#     content = file.read()  # 从开头重新读取刚刚写入的完整内容
#     print(content)
#
with open('./test_dir/瞎写的.txt', 'r+', encoding='utf-8') as file:
    # 如果打开后不 read()，直接 write()：
    # 光标在位置 0，新写入的内容会【从头覆盖】原文件的等长字符！
    file.write('yesyesyes\n')

    # 读写模式,文件必须存在
    content = file.read()
    print(content)
    # 光标从0开始,读完内容,光标到了文字末尾

    # 然后从文字末尾开始写入的,变成了假追加操作
    file.write('草尼玛\n')
    file.write('你麻痹')

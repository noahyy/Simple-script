import os
def read_content():
    word_limt = input("请输入限制字数")
    s = int(word_limt)
    words = ""
    read_files = open("C:\\Users\\杨贤宇\\Desktop\\小说.txt","r",encoding='UTF-8')
    for i in read_files.read():
        i = i.strip("\r\n")
        words = words + i
        if len(words) == s:
            break
    read_files.close()
    return words
def write_words(file):
    if os.path.exists("C:\\Users\\杨贤宇\\Desktop\\1.txt"):
        os.remove("C:\\Users\\杨贤宇\\Desktop\\1.txt")
        print("已将该文件删除，后面写入信息会自动生成该文件")
    else:
        print("文件不存在，已创建该文件")
    write_file = open("C:\\Users\\杨贤宇\\Desktop\\1.txt","a",encoding='UTF-8')
    print(file[-1])
    write_file.write(file)
    write_file.close()
if __name__ == "__main__":
    functions = read_content()
    write_words(functions)
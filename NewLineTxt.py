import transpose


path = r"C:\Users\DM\Desktop\830\python.txt"
path2 = r"C:\Users\DM\Desktop\830\71.txt"
save_path = r"C:\Users\DM\Desktop\830\新建文本文档 (2).txt"
final_path = r"C:\Users\DM\Desktop\830\新建文本文档.txt"

# 读取文本对每行进行去重
def read_txt_return_set(file_path):
    lines = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            for word in line:
                lines.append(word)
    return list(set(lines))

data = data2 = ''
with open(path, 'r', encoding='utf-8') as f:
    data = f.read()
with open(path2, 'r', encoding='utf-8') as fp:
    data2 = fp.read()
data += "\n"
data += data2
with open(save_path, "w", encoding='utf-8') as f2:
    f2.write(data)

with open(final_path, "w", encoding='utf-8') as f3:
    t = read_txt_return_set(save_path)
    print(len(t))
    for line in t:
        for word in line:
            f3.write(word + '\n')








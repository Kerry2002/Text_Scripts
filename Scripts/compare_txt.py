
def read_txt_return_list(file_path):
    lines = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip().replace('\n', '').replace(' ', '').replace("、", "")
            for font in line:
                lines.append(font)
    return list(set(lines))


# 读取文本对每行进行去重
def read_txt_return_set(file_path):
    lines = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            if "," in line:
                print(line)
                for font in line.split(','):
                    lines.append(font.strip().replace('\n', ''))
            elif " " in line:
                print('space', line)
                for font in line.split(' '):
                    lines.append(font.strip().replace('\n', ''))
            else:
                lines.append(line.strip().replace('\n', ''))
    return list(set(lines))


# L2L3不在699中的
L2L3 = read_txt_return_list(r"C:\Users\DM\Desktop\830\已有Python_2573字.txt")
print(len(L2L3))
# _699 = read_txt_return_list("../处理的文本/class_name735.txt")
_2829 = read_txt_return_list(r"C:\Users\DM\Desktop\830\L1+L2+L3汇总去重_1279字.txt")
# print(L2L3)
# print(_699)
# # print(len(_2829))
for i in _2829:
    if i not in L2L3:
        print(i)
        with open(r"C:\Users\DM\Desktop\830\需求6不在Python字库_780字.txt", 'a', encoding='utf-8') as f:
            f.write(i + '\n')

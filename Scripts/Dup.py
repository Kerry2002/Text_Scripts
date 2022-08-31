# Txt去重并输出字数

def read_txt_return_list(file_path):
    lines = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip().replace('\n', '').replace(' ', '').replace("、", "")
            for font in line:
                lines.append(font)
    return list(set(lines))

# save_path = r"C:\Users\DM\Desktop\822 去重\需求1\L2_诗词.txt"
#
# d = {}
# for line in open(save_path, 'r', encoding='utf-8'):
#     d[line] = d.get(line, 0) + 1
# fd = open(r"C:\Users\DM\Desktop\822 去重\需求1\L2_诗词_去重.txt", 'w')
# for k, v in d.items():
#     if v > 1:
#         fd.write(k)
# fd.close()

# L2L3 = read_txt_return_list(r"C:\Users\DM\Desktop\822 去重\需求1\L2_诗词无去重.txt")
# print(len(L2L3))

part_2 = read_txt_return_list(r"C:\Users\DM\Desktop\830\python - 副本.txt")
print(len(part_2))
# for i in part_2:
#     with open(r"C:\Users\DM\Desktop\822 去重\需求8\dup.txt" ,'a', encoding='utf-8') as f:
#         f.write(i + '\n')

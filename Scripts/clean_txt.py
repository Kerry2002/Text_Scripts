# 删除标点符号,保留中文
def clean_punc(text):
    x = """！？｡＂＃＄％＆＇（）＊＋－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘'‛“”„‟…‧﹏()，。《》〈〉《》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟 """
    for c in x:
        text = text.replace(c, "")
    return text


def clean_chinese():
    with open(r"C:\Users\DM\Desktop\829\3_.txt", "r", encoding="utf-8") as f:
        for line in f.readlines():
            if line == "\n":
                continue
            res = clean_punc(line.replace("\n", ""))
            for c in res:
                if c >= "\u4e00" and c <= "\u9fa5":
                    print(c)
                with open(r"C:\Users\DM\Desktop\829\L1基础结构-诗词范字_.txt", "a", encoding="utf-8") as f:
                    f.write(c + "\n")


# 读取文本生成列表返回
def read_txt_return_list(file_path):
    lines = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            lines.append(line.strip().replace('\n', ''))
    return lines


# 读取文本对每行进行去重
def read_txt_return_set(file_path):
    lines = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            lines.append(line.strip().replace('\n', ''))
    return list(set(lines))


base_path = r"C:\Users\DM\Desktop\829\3_.txt"
a = read_txt_return_set(base_path)
clean_chinese()


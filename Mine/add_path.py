

import os
import shutil
import glob

# 数据位置
data_dir = r'Y:\3Q\全集字库补充字采集+分类标注需求_500367424\汉字检测框标注\数据结果\小学生硬笔书写体数据需求_332464606_5072'
# 存放位置
save_dir = r"Y:\3Q\全集字库补充字采集+分类标注需求_500367424\汉字检测框标注\json"


print(os.path.dirname(data_dir))

file_names = os.listdir(data_dir)  # 获取文件夹内所有文件的名字

for name in file_names:  # 如果某个文件名在file_names内
    old_name = data_dir + '/' + name  # 获取旧文件的名字，注意名字要带路径名
    new_name = data_dir + '/' + '小学生硬笔书写体数据需求_332464606_5072_' + name  # 定义新文件的名字，这里给每个文件名前加了前缀 a_
    os.rename(old_name, new_name)  # 用rename()函数重命名
    print(new_name)  # 打印新的文件名字

for file in glob.glob(os.path.join(data_dir, "*.json")):
    shutil.move(file, save_dir)


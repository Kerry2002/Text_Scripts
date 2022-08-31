import glob
import shutil
import os

path = r'Y:\3Q\20220816网格点检测_数据采集_570230720\标注数据\处理后数据\image'
save_path = r"Y:\3Q\20220816网格点检测_数据采集_570230720\标注数据\处理后数据\json"

for file in glob.glob(os.path.join(path, "*.json")):
    shutil.move(file, save_path)
import os

# male_1_1_fengjuan#yuxiaocui.json
# male_2_1_fengjuan#yuxiaocui.json

ch_path = r'Y:\3Q\全集字库补充字采集+分类标注需求_500367424\汉字检测框标注\image'

fileList = os.listdir(ch_path)

os.chdir(ch_path)

for i in fileList:
    new_name = i.replace('阶段3_6年级_米字格_350_', '阶段3_6年级_米字格_280_')
    print(new_name)
    os.rename(i, new_name)



# def change_middle_name(file_path ,old , new):
#     with open(file_path, "r", encoding='utf8') as f:
#         fileList = os.listdir(f)
#         os.chdir(f)
#         for i in fileList:
#             new_name = i.replace(old, new)
#             print(new_name)
#             os.rename(i, new_name)
#
# change_middle_name(ch_path,'e_1','e_2')
import re

# test = '用户输入的正则表达式'
# if re.match(r'正则表达式', test):
#     print('ok')
# else:
#     print('failed')

print(re.split(r'\s+', 'a b   c'))
# 正则表达式识别连续空格
print( re.split(r'[\s\,\;\;]+', 'a,b, c  d;;e'))
# 正则识别连续多种分割符号/空格

# m = re.match(r'^\d{3}\-\d{3,8}$', '010-12345') # 错误示范
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
# (xxx)-(xxx)形式定义两个group
# print(m.group(1))

re.match(r'^(\d+)(0*)$', '102300').groups()
# ('102300', '') 贪婪匹配--全部末尾数字0
re.match(r'^(\d+?)(0*)$', '102300').groups()
# ('1023', '00') 非贪婪匹配 -

re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_telephone.match('010-12345').groups())
# 提前编译好电话号码拆分，后续直接使用

# re_email = re.compile(r'^([a-zA-Z][0-9a-zA-Z-.]{0, 19})@([0-9a-zA-Z]{3,8})+(\.[a-zA-Z0-9_-]+){0,4}$')
re_email = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
print(re_email.match('hello.world@163.com'))
# 验证输入是电子邮箱

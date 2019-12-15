'''Python标准库有序字典''' 

from collections import OrderedDict 

# 有序字典
favorite_languages = OrderedDict()
# print(favorite_languages)

favorite_languages['jen'] = 'python'
favorite_languages['Julian']  = '口琴' 
favorite_languages['zhuliyan'] = 'running' 

for key, values in favorite_languages.items(): 
    print("Key is : %s, Values is: %s" % (key, values))

# print(favorite_languages['jen'])
# print(type(favorite_languages))
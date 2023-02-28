import re

"""
#1

txt1 = 'abcd axyz xyz abbbbbbbbbbbbb dac ab'

t = re.findall("ab*", txt1)

print(t)

#2
y = re.findall("ab{2,3}", txt1)

print(y)

#3
txt2 = 'abc ab_cd xyz z_w'

t = re.findall("[a-z]+_[a-z]+", txt2)

print(t)

#4


y = re.findall("[A-Z][a-z]+",txt2)

print(y)

#5

txt3 = 'abcd abe xyz abbcd ab'

t = re.findall('ab.*b', txt3)

print(t)
"""

#6

string = "My name is Dimash. And i'm studying in KBTU "
new_string = re.sub('[ ,.]', ':', string)
print(new_string)

"""
#8

txt4 = "AbbCdfsVgbnDfrt"
d = re.findall('[A-Z][^A-Z]*', txt4)
print(d)

"""
"""#9

txt5 = "AdcfHfgrTyjhUrel"
f = re.sub('(?<!^)(?=[A-Z])', ' ', txt5)
print(f)
"""
"""
#10

camel_case_string = "HoDatBoi"
snake_case_string = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_case_string).lower()
print(snake_case_string)
"""
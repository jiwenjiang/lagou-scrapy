import re

a = input()

print(re.findall('^[\w,.?;]{6,12}$', a))

# a = 'ASSD8GGGA2'
# print(re.match('[A-Z]{5,7}', a))

import re

str = 'aksdjflkaskdjjdflaskjfalskdjflksadf'

# match只能从头开始匹配，不是从头开始拿不到结果
result = re.match('aks',str)
print(result)

print(result.group())
print(result.span())

# search 可持续寻找，找到第一个匹配的
search_result = re.search('skjfa',str)

print(f'search_method {result}')

# findall 查询多个
findall_result = re.findall('kdj',str)

print(f'findall_result {findall_result}')


# fullmatch全字段匹配
fullmatch_result = re.fullmatch('dflask',str)
print(f'fullmatch_result {fullmatch_result}')
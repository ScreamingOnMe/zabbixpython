import itertools

str = input('请输入一个字符串:')
lst = []
for i in range(1, len(str)+1):
    lst1 = [''.join(x) for x in itertools.permutations(str, i)]
    lst += lst1

print(lst)

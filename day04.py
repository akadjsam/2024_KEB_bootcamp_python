# #sub = ['a','b','c']
# sub = ['a',['b','c'],'d']
# a = sub
# b = sub.copy()
# c = list(sub)
# d = sub[:]
#
# print(sub,a,b,c,d)
# sub[1][1] = "x"
# print(sub,a,b,c,d) #얕은복사
#

import copy
# #sub = ['a','b','c']
sub = ['a',['b','c'],'d']
a = sub
b = sub.copy()
c = list(sub)
d = sub[:] #a~d 얕은복사
e = copy.deepcopy(a) #깊은복사
print(sub,a,b,c,d)
sub[1][1] = "x"
print(sub,a,b,c,d,e)

eng = "a","b","c"
fre = 'd','f','g'
z = dict(zip(eng,fre))
print(z)
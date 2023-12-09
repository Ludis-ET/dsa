dic = {1:False,2:False,}
a = {'a':1,'u':4,'e':0,'y':0}
b = {'sfgsd':12,'qewrsa':24,'drfsd':45}

print('leul' in dic)
print('ludis' in dic.values()) # linear searching algorithm


print(all(dic)) # for all
print(any(dic)) # there exists
print(len(dic)) # length
print(sorted(a,reverse = True)) # sorting in reverse
print(sorted(b,key = len)) # sorting in length
print(max(a.values()))
print(list(dic)[:2])
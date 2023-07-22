s = [1, 2, 3, 4]
t = iter(s)
print('t=',t)
print('iter(t)=',iter(t))
'如果 t 是iterator，则iter(t)=t'
s1= iter(s)
s2=iter(s)
print('第一个iter(s)=',s1)
print('第二个iter(s)=',s2)
'但是如果 s 不是iterator，则每一次的iter(s)都不一样，都是全新的'
"""next(t)
next(t)
iter(s)
next(iter(s))
next(iter(t))
next(iter(s))
next(iter(t))
next(t)"""

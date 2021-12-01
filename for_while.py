#!/usr/bin/env python3
# -*- coding: utf-8 -*-

k = ['Дмитрий', 'Олег', 'Даша', 'Антон', 'Коля', 'Юля', 'Алена']

sm = iter(k)
print(next(sm))
print(next(sm))

ks = iter(k)
print(ks)
x = next(ks)
length = len(k)
for i in k:
    print(f'{i} сколько будет 2+2*2?')

i = 0
while i < length:
    print(f'!{i} сколько будет 2+2*2?')
    i+=1
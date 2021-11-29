#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = 'Используйте срезы в замечательном языке Python!!!'
print(f'>{s}<')
print(f'>{s[2]}<')
print(f'>{s[-4]}<')
print(f'>{s[:5]}<')
print(f'>{s[:-3]}<')
print(f'>{s[::2]}<') # четные индексы
print(f'>{s[1::2]}<') # нечетные индексы
print(f'>{s[::-1]}<') # в обратном порядке
print(f'>{s[-4:9:-1]}<') # кроме первых 10 и последних 3 символов

print(f'{len(s)}') # длина строки
print(f'{len(s.split())}') # количество слов
print(f'{len(s.split())}') # слова в обратном порядке


print(f'>{" ".join(s.split()[::-1])}<')

print('END')


#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
只能使用不可变的对象（如字符串）作为字典的键值
使用符号构成	 	 d	=	{key	:	value1	,	key2	:	value2}		这样的形式，来成对地指定键值与值

"""
help(dict)

ab = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}
print("Swaroop's	address	is", ab['Swaroop'])
#	删除一对键值—值配对
del ab['Spammer']
print('\nThere	are	{}	contacts	in	the	address-book\n'.format(len(ab)))
for name, address in ab.items():
    print('Contact	{}	at	{}'.format(name, address))
#	添加一对键值—值配对
ab['Guido'] = 'guido@python.org'
if 'Guido' in ab:
    print("\nGuido's	address	is", ab['Guido'])

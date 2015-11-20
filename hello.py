#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math, time
from functools import reduce

#斐波那契
def Fib(x):
	if not isinstance(x, (int)):
		raise TypeError('bad type')
	if(x <= 0):
		return 0
	if(x <= 2):
		return 1
	else:
		return Fib(x - 1) + Fib(x - 2)
#二元一次方程
def quadratic(a, b, c):
	t = b * b - 4 * a * c
	if(t < 0):
		return None
	else:
		d = math.sqrt(t)
		return (-b + d) / (2 * a), (-b - d) / (2 * a)
#汉诺塔
def move(n, a, b, c):
	if n == 0:
		return None

	move(n-1, a, c, b)
	print(a, '->', c)
	move(n-1, b, a, c)

	return
#斐波那契构造器
def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a + b
		n = n + 1
	return
#杨辉三角
def triangles():
	b = [1]
	while True:
		yield b
		b = [1] + [b[i] + b[i + 1] for i in range(len(b) - 1)] + [1]

#str转int
def str2int(s):
	def fn(x, y):
		return x * 10 + y
	def char2num(s):
		return {'0': 0, '1': 1, '2': 2,'3': 3,'4': 4,'5': 5,'6': 6,
		'7': 7, '8': 8, '9': 9}[s]
	return reduce(fn, map(char2num, s))

#规范英文名
def normalize():
	return name[:1].upper() + name[1:].lower()

#利用reduce求list积
def prod(l):
	def multi(a, b):
		return a * b
	return reduce(multi, l)

#利用map和reduce str转float
def str2float(s):
	def fn(x ,y):
		return x * 10 + y
	def char2num(s):
		return {'0': 0, '1': 1, '2': 2,'3': 3,'4': 4,'5': 5,'6': 6,
		'7': 7, '8': 8, '9': 9}[s]
	return (reduce(fn, map(char2num, s.replace('.',''))) 
	/ (10 ** (len(s) - s.find('.') - 1)))

#使用filter的素数生成器

def _odd_iter():
	n = 1
	while True:
			n = n + 2
			yield n	
def _not_divisible(n):
	return lambda x: x % n > 0

def primes():
	yield 2
	it = _odd_iter() #初始序列
	while True:
		n = next(it) 
		yield n
		it = filter(_not_divisible(n), it) #构建新序列

#过滤非回数
def is_palindrome(n):
	return str(n) == str(n)[::-1]

#打印日志装饰器
def log(func):
	def wrapper(*args, **kw):
		print('call %s():' % func.__name__)
		return func(*args, **kw)
	return wrapper

@log
def now():
	print(time.strftime('%Y-%m-%d %H:%M:%S'))




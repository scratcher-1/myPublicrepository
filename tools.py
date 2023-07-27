#Python.py是一个实用的Python模块,包含各种工具、游戏、软件,只要是Python3用户都可以使用哦!
import random
import math


def intbox(msg:str):
	return int(input(msg))
def read_file(name:str,nnum:int):
	#
def strCut(txt:str, n:int):
	a=[]
	b=[]
	out=''
	for i in txt:
		a.append(i)

	j=len(a)-n
	for k in range(j):
	    b.append(txt[k])
	for i in b:
		out=out+i
	return out

def choicebox(msg:str,choices:list):
	j='请从'
	for i in choices:
		if i==choices[len(choices)]:
			print(j+i+'中选择一项来回答:')
			d=input(msg)
			if d not in choices:
				choicebox(msg,choices)
			else:
				return d
		else:
			j=j+i+'、'
def multibox(msg:str,fields:list):
	print(msg)
	returns={}
	for i in fields:
		if i['type']=='str':
			returns[i['name']]=input(i['name'])
		elif i['type']=='int':
			returns[i['name']]=intbox(i['name'])
		elif i['type']=='choice':
			returns[i['name']]=choicebox(i['name'],i['choices'])
		else:
			TypeError("the'fields'should be like:\n[{'name':'hello world!','type':'str'},{'name':'welcome','type':'int'},{'name':'choose one in them','type':'choice','choices':['A','B','C'],……],\nbut you dont write them in 'fields'.")
def print_2D_txt(txt:list):
	j=''
	for i in txt:
		print(i)
		j=j+i+'\n'
	return j
def radical_sign(x:int,y:int):#开根号√
	return math.pow(x,y)
def print_file(name:str):
	file=open(name,'r')
	print(file.read())
	return file.read()
	file.close()
def txt_replace(name:str,old:str,new:str):
	file=open(name,'r')
	filereader=file.read()
	filereader=filereader.replace(old,new)
	file.close()
	file=open(name,'w')
	file.write(filereader)
	file.close()
	file=open(name,'r')
	return file.read()
	file.close()
def pi():
	return math.pi() # type: ignore
def pixel_dots_game_setup(dots:list):
	print()
	a=''
	b=''
	c=''
	d=''
	i=[]
	if dots==[]:
		for d in range(8):
			for j in range(8):
				b=b+random.choice(['⬛️','⬜️'])
			i.append(b)
			b=''
	else:
		i=dots
	c=print_2D_txt(i)
	print()
	return c
def pixel_dots_game(dots:list):
	c=pixel_dots_game_setup(dots)
	a=intbox('上图中有多少个⬛️?')
	if a==c.count('⬛️'):
		print('答对啦!!!!!')
		return True
	else:
		print('恭喜答错')
		return False
		i=choicebox('现在你要:',['公布答案','再来一次'])
		if i=='公布答案':
			print('正确答案:'+str(dots.count('⬛️')))
		elif i=='再来一次':
			pixel_dots_game(dots)
def pixel_hunter_game_setup():
	hunter_x=random.randint(0,7)
	hunter_y=random.randint(0,7)
	food_x=random.randint(0,7)
	food_y=random.randint(0,7)
	while food_x==hunter_x and food_y==hunter_y:
		if random.choice([True,False]):
			food_x=random.randint(0,7)
			food_y=random.randint(0,7)
		else:
			hunter_x=random.randint(0,7)
			hunter_y=random.randint(0,7)
	game_xy={'hunter_x':hunter_x,'hunter_y':hunter_y,'food_x':food_x,'food_y':food_y}
	eat_foods=0
	print('玩家','⬛️')
	print('食物','🐷')
	input('规则:1.在一分钟内,你要不停的去碰到食物,碰到一次金币+2,一分钟计时结束后看看你增加了多少金币!(按回车即可)')
	input('2.使用箭头操作')
	input('按回车键开始游戏吧!')

import math
import pandas as pd
data = 'D:\\data.csv'
context = 'D:\\context.csv'
def average_value(List_assessment_users): #Функция для вычисления средней оценки
	count = 0 
	S =0
	for i in range(0, len(List_assessment_users)):
		if (int(List_assessment_users[i])!=-1):
			S += int(List_assessment_users[i])
			count+=1
	avg = S/count
	return avg

sim_uv = {}
def cosine_metric(u1, u2):#Функция для вычисления коэффициента похожести двух пользователей по формуле.
	u = 0
	v = 0
	uv = 0
	for i in range(0, len(u1)):
		if ((int(u1[i])!=-1) and (int(u2[i])!=-1)):
			u += int(u1[i])**2
			v += int(u2[i])**2
			uv += int(u1[i]) * int(u2[i])
	return uv / (math.sqrt(u) * math.sqrt(v))
	 

Users=pd.read_csv(data,encoding='ascii',index_col='Users') #Таблица
myuser = 35 #Мой вариант
User35=Users.iloc[myuser-1]#мой номер пользователя нумеруются с 0
result = {}
def Main(x): #Для расчета оценки r_ui по формуле 
	total_sim_uv=0
	r_u=round(average_value(User35),2)
	result=0
	users_neighbour =sim_uv.keys()
	for key in users_neighbour:
		r_vi=(Users.iloc[key])[x]
		if r_vi!=-1:
			r_v=average_value(Users.iloc[key])  
			result+=sim_uv[key]*(r_vi - r_v)
			total_sim_uv+=abs(sim_uv[key])
	r_ui = (r_u+result/total_sim_uv)
	return r_ui
for x in range(0,len(Users)):  # расчет схожести пользователей 
	if x!= (myuser - 1):
		sim_uv[x]=cosine_metric(Users.iloc[x], User35)

		
k =5
sim_uv=dict(sorted(sim_uv.items(), key=lambda x: x[1], reverse=True)[:k])# 5 человек, которые наиболее похожи на нашего user35 (к =5) и сортируем  по убыванию метрик и выбрать первые 5 записей
for x in range(0,len(User35)):
	if User35[x]==-1:
		result[x+1]=Main(x)

for i in result:
	print('Movie',i,':',round(result[i],2))


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
def cosine_metric(u1, u2): #Функция для вычисления коэффициента похожести двух пользователей по формуле.
	u = 0
	v = 0
	uv = 0
	for i in range(0, len(u1)):
		if ((int(u1[i])!=-1) and (int(u2[i])!=-1)):
			u += int(u1[i])**2
			v += int(u2[i])**2
			uv += int(u1[i]) * int(u2[i])
	sim_u_v = uv / (math.sqrt(u) * math.sqrt(v))
	return sim_u_v

Users=pd.read_csv(data,encoding='ascii',index_col='Users') #Читать данные из таблицы data.csv
myuser = 35
User35=Users.iloc[myuser-1]#мой номер пользователя нумеруются с 0
k =5
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
Cont=pd.read_csv(context,encoding='ascii',index_col='Users')#Читать данные из таблицы context.csv
film =[]
for f in range (0,30): # фильмы для рекомендации
    if int(User35[f])==-1:
        film.append(f)

for u in range(0,len(Users)):
    for f in range (0,30):
        dat= (Cont.iloc[u])[f]
        if (dat==' Sun'): #Порекомендовать в воськресеьне
            (Users.iloc[u])[f]=-1
for x in range(0,len(Users)):  # расчет схожести user
    if x!= (myuser-1):
        sim_uv[x]=cosine_metric(Users.iloc[x], User35)
sim_uv=dict(sorted(sim_uv.items(), key=lambda x: x[1], reverse=True)[:k])
for x in range(0,len(User35)):
    if User35[x]==-1:
        result[x+1]=Main(x)
result=dict(sorted(result.items(), key=lambda x: x[1], reverse=True)[:1])#сортируем по убыванию метрик и выбрать первый 1 записей
for i in result:
    print('Movie',i,':',round(result[i],2))

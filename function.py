import matplotlib.pyplot as plt
import numpy as np

def read_from_file(lst1,lst2,lst3,lst4):
    f=open("table.txt","r")
    lines=f.readlines()
    for x in lines:
        lst1.append(float(x.split(',')[3]))
        lst2.append(float(x.split(',')[4]))
        lst3.append(float(x.split(',')[2]))
        lst4.append(float(x.split(',')[5]))
    f.close()
    spisok = list(zip(lst1,lst2,lst3,lst4))
    return lst1,lst2,lst3,lst4,spisok


def OS(lst1,lst2,O_S,x):
    spisokup = []
    spisokdown = []
    for i in range(len(lst1)):
        if (lst1[i] - lst2[i]) ** x < O_S:
            spisokup.append(i)
        elif(lst2[i]-lst1[i]) ** x < O_S:
            spisokdown.append(i)
    return spisokup, spisokdown



def find_first_max(lst,step):
    maximumy = [max(i) for i in lst]
    a = max(maximumy)
    for j in range(len(maximumy) - 1, -1, -1): # цикл для нахождения индекса точки минимума и индекса точки рассчета через введенный пользователем шаг.
        if maximumy[j] == a:
            value = maximumy[j]
            index_ = j
            index_for_raschet = j + step
            return value, index_,index_for_raschet

def find_first_min(lst,step):
    minimumy = [min(i) for i in lst]
    a = min(minimumy)
    for j in range(len(minimumy) - 1, -1, -1): # цикл для нахождения индекса точки минимума и индекса точки рассчета через введенный пользователем шаг.
        if minimumy[j] == a:
            value = minimumy[j]
            index_ = j
            index_for_raschet = j + step
            return value, index_,index_for_raschet


def raschetmin(b,c,d,f):
    result = b + c * d / (f - 1) # рассчет для нахождения точки, через которую идет луч от минимума.
    return result

def raschetmax(b,c,d,f):
    result = b - c * d / (f - 1) # рассчет для нахождения точки, через которую идет луч от максимума
    return result


def last_min_rasschet(ind,lst,b,c,d,k,rasschet): #подается: индекс мин, список, шаг,  значение минимума, кол-во точек после запятой, коэф, и рассчет просчитанный для предидущего.
    minimumy = [min(i) for i in lst]
    c = min(minimumy)
    A_x = ind
    A_y = c
    B_x = ind + b
    B_y = raschetmin(c,k,b,d)
    for i in range(ind, len(lst)): # цикл для переноса луча при нахождении новой точки минимума(точки под лучем).
        if minimumy[i] < raschetmin(c, k, i - ind, d):
            ind = i
            c = minimumy[i]
            rasschet = raschetmin(c,k,b,d)
            A_x = i
            A_y = minimumy[i]
            B_x = i + b
            B_y = rasschet
        else:
            pass
    return A_x,A_y,B_x,B_y

def last_max_rasschet(ind,lst,b,c,d,k,rasschet): #подается: индекс макс, список, шаг,  значение максимума, кол-во точек после запятой, коэф, и рассчет просчитанный для предидущего.
    maximumy = [max(i) for i in lst]
    c = max(maximumy)
    A_x = ind
    A_y = c
    B_x = ind + b
    B_y = raschetmax(c,k,b,d)
    for i in range(ind, len(lst)): # цикл для переноса луча при нахождении новой точки минимума(точки под лучем).
        if maximumy[i] > raschetmax(c, k, i - ind, d):
            ind = i
            c = maximumy[i]
            rasschet = raschetmax(c,k,b,d)
            A_x = i
            A_y = maximumy[i]
            B_x = i + b
            B_y = rasschet
        else:
            pass
    return A_x,A_y,B_x,B_y

def parallelup(lst,last_index_graph_min,Max_y,koef,ostatok): #подается: список, индекс максимума, индекс минимум, значение максимума, кф, кол-во зн после запятой
    q = 2
    t = 3
    exitFlag = False
    maximumy = [max(i) for i in lst]
    A_x = last_index_graph_min
    B_x = len(lst)+1
    A_y = maximumy[len(maximumy)-1]
    B_y = raschetmin(A_y,koef,2,ostatok)
    find_max = maximumy[last_index_graph_min:len(lst)]
    B__y = raschetmin(Max_y,koef,len(find_max),ostatok) # находим точку рассчета. от значения 18, c шагом 5
    for i in range(Max_y,0,-1): # от 18, с шагом -1
        B__y = raschetmin(i,koef,len(find_max),ostatok)
        if(exitFlag):
                 break
        for j in range(len(find_max)-1,0,-1):# от 35, до 39
            if find_max[j]>=raschetmax(B_y,koef,len(find_max)-j-1,ostatok):
                q = find_max[j]
                t = j
                exitFlag = True
                A_x = len(lst)- len(find_max)
                B_x = len(lst) - 1
                A_y = raschetmax(q,koef,t,ostatok)
                B_y = raschetmin(q,koef,len(find_max)-t-1,ostatok)
                return A_x,A_y,B_x,B_y,q,t
            if(exitFlag):
                 break
    return A_x,A_y,B_x,B_y,q,t
def paralleldown(lst,last_index_graph_max,Max_y,koef,ostatok):
    q = 3
    t = 4
    exitFlag = False
    minimumy = [min(i) for i in lst]
    A_x = last_index_graph_max
    B_x = len(lst)+1
    A_y = minimumy[len(minimumy)-1]
    B_y = raschetmax(A_y,koef,2,ostatok)
    find_min = minimumy[last_index_graph_max:len(lst)] # (35, 7), (36, 9), (37, 15), (38, 11), (39, 15)
    B__y = raschetmax(0,koef,len(find_min),ostatok) # находим точку рассчета. от значения 18, c шагом 5
    for i in range(0,Max_y,1): # от 0 до 18, с шагом 1
        B__y = raschetmax(i,koef,len(find_min),ostatok)
        if(exitFlag):
                 break
        for j in range(len(find_min)-1,0,-1):# от 35, до 39
            if find_min[j]<=raschetmax(B__y,koef,len(find_min)-j-1,ostatok):
                q = find_min[j]
                t = j
                exitFlag = True
                A_x = len(lst)- len(find_min)
                B_x = len(lst) - 1
                return A_x,raschetmin(q, koef,t,ostatok),B_x,raschetmax(q,koef,len(find_min)-t-1, ostatok),t,q
            if(exitFlag):
                 break
    return A_x,A_y,B_x,B_y,q,t

def graph(lst,lst1,lst2,lst3,lst4,x1,x2,y1,y2,x3,x4,y3,y4,x5,x6,y5,y6,x7,x8,y7,y8):
    x = np.arange(0,len(lst1))
    y = np.array(lst1)
    u = np.array(lst2)
    l = np.array(lst3)
    m = np.array(lst4)

    plt.scatter(x, y,marker='.', color = "Red")
    plt.scatter(x, u,marker='.', color = "Orange")
    plt.scatter(x, l,marker='.', color = "Green")
    plt.scatter(x, m,marker='.', color = "Black")

    for i in range(0,len(lst)):
        a = max(lst[i])
        b = min(lst[i])
        plt.plot((i,i),(a,b), color = "Blue")

    j = (x1,x2)
    d = (y1,y2)
    e = (x3,x4)
    p = (y3,y4)
    v = (x5, x6)
    n = (y5, y6)
    z = (x7, x8)
    q = (y7, y8)
    plt.plot(j,d,color = "Red")
    plt.plot(e,p,color = "Red")
    plt.plot(v,n,color = "Black")
    plt.plot(z,q,color = "Black")
    return plt.show()
















"""
A_x = len(lst)- len(find_max)
                A_y = raschetmax(q, koef,t,ostatok)
                B_x = len(lst) - 1
                B_y = raschetmin(q,koef,len(find_max)-t-1, ostatok)
                q = find_max[j]
                t = j + len(lst)- len(find_max)
"""


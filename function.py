import matplotlib.pyplot as plt
import numpy as np

from variables import OS_down
#1
def read_from_file(lst1,lst2,lst3,lst4,lst5):
    f=open("table.txt","r")
    lines=f.readlines()
    for x in lines:
        lst1.append(float(x.split(',')[3]))
        lst2.append(float(x.split(',')[4]))
        lst3.append(float(x.split(',')[2]))
        lst4.append(float(x.split(',')[5]))
        lst5.append(str(x.split(',')[0])+str(x.split(',')[1]))
    f.close()
    spisok= list(zip(lst1,lst2,lst3,lst4))
    return lst1,lst2,lst3,lst4,spisok,lst5


#2
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

#3
def find_first_max(lst,step):
    maximumy = [max(i) for i in lst]
    a = max(maximumy)
    for j in range(len(maximumy) - 1, -1, -1): # цикл для нахождения индекса точки минимума и индекса точки рассчета через введенный пользователем шаг.
        if maximumy[j] == a:
            value = maximumy[j]
            index_ = j
            index_for_raschet = j + step
            return value, index_,index_for_raschet

def raschetmax(b,c,d,f):
    result = b - c * d / (f - 1) # рассчет для нахождения точки, через которую идет луч от максимума
    return result
#4
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

def OS(lst1,lst2,O_S,x):
    spisokup = []
    spisokdown = []
    for i in range(len(lst1)):
        if (lst1[i] - lst2[i]) *10 ** x < O_S:
            spisokup.append(i)
        elif(lst2[i]-lst1[i]) *10 ** x < O_S:
            spisokdown.append(i)
    return spisokup, spisokdown
def isInTriangle(A_x, A_y, B_x, B_y, C_x, C_y, P_x, P_y):
    ''' принадлежит ли точка P треугольнику ABC.

    :param A_x:
    :param A_y:
    :param B_x:
    :param B_y:
    :param C_x:
    :param C_y:
    :param P_x:
    :param P_y:
    :return: True - принадлежит False - не принадлежит
    '''
    a = (A_x - P_x) * (B_y - A_y) - (B_x - A_x) * (A_y - P_y)
    b = (B_x - P_x) * (C_y - B_y) - (C_x - B_x) * (B_y - P_y)
    c = (C_x - P_x) * (A_y - C_y) - (A_x - C_x) * (C_y - P_y)
    if (a >= 0 and b >= 0 and c >= 0) or (a <= 0 and b <= 0 and c <= 0):
        return True
    else:
        return False

def isInTrapezoid(A_x, A_y, B_x, B_y, C_x, C_y, D_x, D_y, M_x, M_y):
    '''

    :param A_x:
    :param A_y:
    :param B_x:
    :param B_y:
    :param C_x:
    :param C_y:
    :param D_x:
    :param D_y:
    :param M_x:
    :param M_y:
    :return:
    '''
    if isInTriangle(A_x,A_y, B_x, B_y, C_x, C_y,  M_x, M_y) \
            or isInTriangle(A_x, A_y, C_x, C_y, D_x, D_y, M_x, M_y) \
            or isInTriangle(A_x, A_y, B_x, B_y, D_x, D_y, M_x, M_y):
        return True
    return False
def raznica(lst,ostatok):
    razn = []
    c = lst.copy()
    c.sort()
    for i in range(1,len(c)):
        z = c[i] - c[i-1]
        if z !=0:
            razn.append(z)
    raznica = round(min(razn),ostatok)
    return raznica

def p_up(mini,maks, last_index_graph_min,koef,ostatok):
    z = raznica(maks,ostatok)
    a = round(min(maks),ostatok)
    k = - ostatok
    t = 1
    q = 1
    A_x = last_index_graph_min
 ## A_y = изменяется
    B_x = last_index_graph_min
    B_y = max(maks) + 10**ostatok
    C_y = max(maks) + 10**ostatok
    C_x = len(maks)
    D_x = len(maks)
    b = round(max(maks),ostatok)
 ## D_y = raschetmin(Max_y,koef,len(find_max),ostatok)

    vv = []
    for x in np.arange(a, b,z): # Для более точной работы нужно оставить for x in np.arange(0, b, 10**(k)), но быстродействие уменьшается.
        vv.append(x)
    vv.reverse()
    
    
    for i in vv:
        D_y = raschetmin(i,koef,len(maks)-last_index_graph_min,ostatok)
        for j in range(last_index_graph_min, len(maks)):
            if isInTrapezoid(A_x, i, B_x, B_y, C_x, C_y, D_x, D_y, j, maks[j]):
              
                return A_x,i,D_x,D_y,t,q
            else:
                pass
    return A_x,maks[last_index_graph_min],D_x+4,raschetmin(maks[last_index_graph_min],koef,5,ostatok),t,q
            

def p_down(mini,maks, last_index_graph_max,koef,ostatok):
    z = raznica(mini,ostatok)
    a = round(min(mini),ostatok)
    k = - ostatok
    t = 1
    q = 1
    A_x = last_index_graph_max
 ## A_y = изменяется
    B_x = last_index_graph_max
    B_y = 0.003
    C_y = 0.003
    C_x = len(mini)
    D_x = len(mini)
    b = round(max(mini),ostatok)
 ## D_y = raschetmin(Max_y,koef,len(find_max),ostatok)

    vv = []
    for x in np.arange(a, b,z): # Для более точной работы нужно оставить for x in np.arange(0, b, 10**(k)), но быстродействие уменьшается.
        vv.append(x)
    
    for i in vv:
        D_y = raschetmax(i,koef,len(mini)-last_index_graph_max,ostatok)
        for j in range(last_index_graph_max, len(mini)):
            if isInTrapezoid(A_x, i, B_x, B_y, C_x, C_y, D_x, D_y, j, mini[j]):
                return A_x,i,D_x,D_y,t,q
            else:
                pass
    return A_x,mini[last_index_graph_max],D_x+4,raschetmax(mini[last_index_graph_max],koef,5,ostatok),t,q


# x9,x10,y9,y10
def graph(lst,lst1,lst2,lst3,lst4,x1,x2,y1,y2,x3,x4,y3,y4,x5,x6,y5,y6,x7,x8,y7,y8,nuzn_trendovieA_x,nuzn_trendovieB_x,nuzn_trendovieA_y,nuzn_trendovieB_y):
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
    for i in range(0,len(nuzn_trendovieA_x)):
        plt.plot((nuzn_trendovieA_x,nuzn_trendovieB_x),(nuzn_trendovieA_y,nuzn_trendovieB_y), color = "Green")
 #   t = (x9, x10)
  #  r = (y9, y10)
    plt.plot(j,d,color = "Red")
    plt.plot(e,p,color = "Red")
    plt.plot(v,n,color = "Black")
    plt.plot(z,q,color = "Black")
  #  plt.plot(t,r,color = "Green")

    return plt.show()
def first_OS_down(OS_down,last_index_graph_min): # Находим последнюю точку для одного промежутка трендовой линии
    for i in OS_down:
        if i > index_first_min:
            first_OS_down = i
            return first_OS_down

def line(x1,x2,y1,y2,x0): # y = kx + b
    k = (y2-y1)/(x2-x1)
    b = y1 - k*x1
    y0 = k * x0 +b
    return y0

def line_position(k,x,b): # y = kx + b
    y = k*x + b
    return y

def angle(x1,x2,y1,y2): # y = kx + b
    k = (y2-y1)/(x2-x1)
    b = y1 - k*x1
    return b, k
def prov (mini, last_index_graph_min, index_bro, last_value_graph_min, bro,j):
    a = index_bro
    for i in range(last_index_graph_min+1, j+1):
        if mini[i] < line(last_index_graph_min, index_bro, last_value_graph_min, bro, i):
            index_bro = i
            bro = mini[i]
    else:
        pass
    b,k = angle(last_index_graph_min,index_bro,last_value_graph_min,bro)
    bo = line_position(k,j,b)
    return last_index_graph_min,last_value_graph_min, j, bro

def bliz_OS(maks,mini,OS_down,last_index_graph_min):
    for i in OS_down: # поэлементно проверяем спписок с ОС.
        if last_index_graph_min < i: # Находим индекс ближайшей ОС
            spisokmx = maks[last_index_graph_min:i+1] # Создаём список от точки внешней до ОС
            a = max(spisokmx) #Находим максимум на этом промежутке
            minimumy = mini[i:len(mini):] #Создаем список с минимальными значениями от ОС, до конца
            u = last_index_graph_min
            return a, u

def find_probitie(spisok,last_index_graph_min,maks,a,mini):
    for j in range(last_index_graph_min, len(spisok)): # Начинаем поиск пробития максимума или пробитие внешней линии.
            if maks[j] > a: #Сравнение значения с найденным максимальным
                 minimumy = mini[last_index_graph_min+1:j+1]
                 bro = min(minimumy)
                 index_bro = mini.index(bro, last_index_graph_min+1, len(mini))
                 return minimumy, bro, index_bro, j
            else:
                pass



def trend(spisok,OS_down,maks, mini, last_index_graph_min, last_value_graph_min,O_T):
    up = 3
    vse_trendovie = []
    nuzn_trendovieA_x = []
    nuzn_trendovieB_x = []
    nuzn_trendovieA_y = []
    nuzn_trendovieB_y = []


    while last_index_graph_min < len(spisok) - O_T-15:
        if len(vse_trendovie) ==0:

            a,i = bliz_OS(maks,mini,OS_down,last_index_graph_min)
            minimumy, bro, index_bro,j = find_probitie(spisok,last_index_graph_min,maks,a,mini)
            last_index_graph_min,last_value_graph_min, index_bro, bro = prov(mini, last_index_graph_min, index_bro, last_value_graph_min, bro,j)
            if index_bro - last_index_graph_min < O_T or index_bro - last_index_graph_min >= O_T:
                           vse_trendovie.append(last_index_graph_min)
                           vse_trendovie.append(last_value_graph_min)
                           vse_trendovie.append(index_bro)
                           vse_trendovie.append(bro)
            else:
                pass
            if index_bro - last_index_graph_min >= O_T:
                nuzn_trendovieA_x.append(last_index_graph_min)
                nuzn_trendovieA_y.append(last_value_graph_min)
                nuzn_trendovieB_x.append(index_bro)
                nuzn_trendovieB_y.append(bro)

            else:
                pass


            last_index_graph_min = vse_trendovie[-2]
            last_value_graph_min = vse_trendovie[-1]
        elif len(vse_trendovie) != 0:



            for i in range(len(vse_trendovie)-1, 0 ,-2):
               if vse_trendovie[i] >= bro:
                   pass
               else:
                   last_index_graph_min = vse_trendovie[i-1]
                   last_value_graph_min = vse_trendovie[i]
                   break

            a,i = bliz_OS(maks,mini,OS_down,last_index_graph_min)
            minimumy, bro, index_bro,j = find_probitie(spisok,last_index_graph_min,maks,a,mini)
            last_index_graph_min,last_value_graph_min, index_bro, bro = prov(mini, last_index_graph_min, index_bro, last_value_graph_min, bro,j)
            if index_bro - last_index_graph_min < O_T or index_bro - last_index_graph_min >= O_T:
               vse_trendovie.append(last_index_graph_min)
               vse_trendovie.append(last_value_graph_min)
               vse_trendovie.append(index_bro)
               vse_trendovie.append(bro)
            else:

                pass
            if index_bro - last_index_graph_min >= O_T:
                nuzn_trendovieA_x.append(last_index_graph_min)
                nuzn_trendovieA_y.append(last_value_graph_min)
                nuzn_trendovieB_x.append(index_bro)
                nuzn_trendovieB_y.append(bro)

            else:
                pass


            last_index_graph_min = vse_trendovie[-2]
            last_value_graph_min = vse_trendovie[-1]
    else:
        return nuzn_trendovieA_x,nuzn_trendovieB_x,nuzn_trendovieA_y,nuzn_trendovieB_y,vse_trendovie





"""
A_x = len(lst)- len(find_max)
                A_y = raschetmax(q, koef,t,ostatok)
                B_x = len(lst) - 1
                B_y = raschetmin(q,koef,len(find_max)-t-1, ostatok)
                q = find_max[j]
                t = j + len(lst)- len(find_max)
"""


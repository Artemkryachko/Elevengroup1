from function import *
from variables import *
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt


    



maks,mini,otkritie,zakritie,spisok,dates = read_from_file(maks,mini,otkritie,zakritie,c)  # заполняем 4  списка значений по столбцам, и один общий список.

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

value_first_min, index_first_min,minindex_first_for_raschet = find_first_min(spisok,step)
first_rasschet_min = raschetmin(value_first_min,koef,step,ostatok)

value_first_max, index_first_max,maxindex_first_for_raschet = find_first_max(spisok,step)
first_rasschet_max = raschetmax(value_first_max,koef,step,ostatok)

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

print()
print("Задание 1,2")
print()
print(f"Первая точка минимума на графике по x    [{index_first_min}]", f"Первая точка минимума на графике по y  [{value_first_min}]") # выводим на экран точку минимума и ее положение в списке.
print(f"Первая точка расчета для минимума на графике по x    [{minindex_first_for_raschet}]", f"Первая точка расчета для минимума на графике по y  [{round(first_rasschet_min, ostatok)}]") # выводим на экран точку рассчета через опр.отрезок, через которую пойдет луч и ее положение в списке.
print(f"Первая точка максимума на графике по x    [{index_first_max}]", f"Первая точка максимума на графике по y  [{value_first_max}]") # выводим на экран точку максимума и ее положение в списке.
print(f"Первая точка расчета для максимума на графике по x    [{maxindex_first_for_raschet}]", f"Первая точка расчета для максимума на графике по y  [{round(first_rasschet_max, ostatok)}]") # выводим на экран точку рассчета через опр.отрезок, через которую пойдет луч и ее положение в списке.
print()
print()


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

last_index_graph_min, last_value_graph_min, last_index_rasschet_min, last_value_rasschet_min = last_min_rasschet(index_first_min,spisok,step,value_first_min,ostatok,koef,first_rasschet_min)

last_index_graph_max, last_value_graph_max, last_index_rasschet_max, last_value_rasschet_max = last_max_rasschet(index_first_max,spisok,step,value_first_max,ostatok,koef,first_rasschet_max)

# / / /   Временный луч
luch_min = last_index_rasschet_min
last_index_rasschet_min = len(spisok) + 20
last_value_rasschet_min = raschetmin(last_value_rasschet_min, koef, len(spisok) - luch_min + 20, ostatok)

luch_max = last_index_rasschet_max
last_index_rasschet_max = len(spisok) + 20
last_value_rasschet_max = raschetmax(last_value_rasschet_max, koef, len(spisok) - luch_max + 20, ostatok)

# / / /
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

print("Задание 3")
print()
print(f"Значение искомой точки минимума на графике по x {last_index_graph_min}"  , f"Значение искомой точки минимума на графике по y {last_value_graph_min}", sep = "\n")
print(f"Значение искомой точки рассчета минимума по x {last_index_rasschet_min}"  , f"Значение искомой точки рассчета минимума по y {last_value_rasschet_min}", sep = "\n")
print()
print()
print(f"Значение искомой точки максимума на графике по x {last_index_graph_max}"  , f"Значение искомой точки максимума на графике по y {last_value_graph_max}", sep = "\n")
print(f"Значение искомой точки рассчета максимума по x {last_index_rasschet_max}"  , f"Значение искомой точки рассчета максимума по y {last_value_rasschet_max}", sep = "\n")



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



paral_up_left_ind,paral_up_left_value,paral_up_right_ind,paral_up_right_value,I_up,V_up = p_up(mini,maks, last_index_graph_min,koef,ostatok)

paral_down_left_ind,paral_down_left_value,paral_down_right_ind,paral_down_right_value,I_down,V_down = p_down(mini,maks, last_index_graph_max,koef,ostatok)

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

"""
print("Задание 4 - Построение параллелей")
print()
print(f"Точка через которую пойдет верхняя параллель по О.х [{len(spisok)-1-I_up}]",f"Точка через которую пойдет верхняя параллель по О.y [{V_up}]")
print(f"Точка через которую пойдет нижняя параллель по О.х [{len(spisok)-c+I_down}]",f"Точка через которую пойдет нижняя параллель по О.y [{V_down}]")
"""





# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

OS_up, OS_down = OS(otkritie,zakritie,O_S,ostatok)

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

#nuzn_trendovieA_x,nuzn_trendovieB_x,nuzn_trendovieA_y,nuzn_trendovieB_y, vse_trendovie = trend(spisok,OS_down,maks, mini, last_index_graph_min, last_value_graph_min,O_T)
#print(nuzn_trendovieA_x,nuzn_trendovieB_x,nuzn_trendovieA_y,nuzn_trendovieB_y,vse_trendovie)

print("Задание 5 - Индексы откатных свечей")
print()
print("Индексы для OS_up")
print(OS_up)
print("Индексы для OS_down")
print(OS_down)



#,y_1, x_1, bro, x_2
#graph(spisok,maks,mini,otkritie,zakritie,last_index_rasschet_min,last_index_graph_min,last_value_rasschet_min,last_value_graph_min,last_index_rasschet_max,last_index_graph_max,last_value_rasschet_max,last_value_graph_max,paral_up_right_ind,paral_up_left_ind,paral_up_right_value,paral_up_left_value,paral_down_right_ind,paral_down_left_ind,paral_down_right_value,paral_down_left_value,nuzn_trendovieA_x,nuzn_trendovieB_x,nuzn_trendovieA_y,nuzn_trendovieB_y)

fig = go.Figure(data=[go.Candlestick(x=dates,
                       open=otkritie, high=maks,
                       low=mini, close=zakritie)])

fig.add_shape(type="line",
    xref="x", yref="y",
    x0=last_index_graph_min, y0=last_value_graph_min, x1=last_index_rasschet_min, y1=last_value_rasschet_min,
    line=dict(
        color="Red",
        width=2,
    ),
)

fig.add_shape(type="line",
    xref="x", yref="y",
    x0=last_index_graph_max, y0=last_value_graph_max, x1=last_index_rasschet_max, y1=last_value_rasschet_max,
    line=dict(
        color="Red",
        width=2,
    ),
)
fig.add_shape(type="line",
    xref="x", yref="y",
    x0=paral_up_left_ind, y0=paral_up_left_value, x1=paral_up_right_ind, y1=paral_up_right_value,
    line=dict(
        color="Black",
        width=2,
    ),
)

fig.add_shape(type="line",
    xref="x", yref="y",
    x0=paral_down_left_ind, y0=paral_down_left_value, x1=paral_down_right_ind, y1=paral_down_right_value,
    line=dict(
        color="Black",
        width=2,
    ),
)
fig.show()












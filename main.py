from function import *
from variables import *
import matplotlib.pyplot as plt
import numpy as np

maks,mini,otkritie,zakritie,spisok = read_from_file(maks,mini,otkritie,zakritie) # заполняем 4  списка значений по столбцам, и один общий список.

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



paral_up_left_ind,paral_up_left_value,paral_up_right_ind,paral_up_right_value,I_up,V_up = parallelup(spisok,last_index_graph_min,int(round(value_first_max)),koef,ostatok)
paral_down_left_ind,paral_down_left_value,paral_down_right_ind,paral_down_right_value,I_down,V_down = paralleldown(spisok,last_index_graph_max,int(round(value_first_max)),koef,ostatok)

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



print("Задание 4 - Построение параллелей")
print()
print(f"Точка через которую пойдет верхняя параллель по О.х [{len(spisok)-1-I_up}]",f"Точка через которую пойдет верхняя параллель по О.y [{V_up}]")
print(f"Точка через которую пойдет нижняя параллель по О.х [{len(spisok)-1-I_down}]",f"Точка через которую пойдет нижняя параллель по О.y [{V_up}]")






# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

OS_up, OS_down = OS(otkritie,zakritie,O_S,ostatok)

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



print("Задание 5 - Индексы откатных свечей")
print()
print("Индексы для OS_up")
print(OS_up)
print("Индексы для OS_down")
print(OS_down)




graph(spisok,maks,mini,otkritie,zakritie,last_index_rasschet_min,last_index_graph_min,last_value_rasschet_min,last_value_graph_min,last_index_rasschet_max,last_index_graph_max,last_value_rasschet_max,last_value_graph_max,paral_up_right_ind,paral_up_left_ind,paral_up_right_value,paral_up_left_value,paral_down_right_ind,paral_down_left_ind,paral_down_right_value,paral_down_left_value)












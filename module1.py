def paralleldown(lst,last_index_graph_max,Max_y,koef,ostatok):
    exitFlag = False
    minimumy = [min(i) for i in lst]
    find_min = minimumy[last_index_graph_max:len(lst)] # (35, 7), (36, 9), (37, 15), (38, 11), (39, 15)
    B__y = raschetmax(0,koef,len(find_min),ostatok) # находим точку рассчета. от значения 18, c шагом 5
    for i in range(1,Max_y*10,1): # от 0 до 18, с шагом 1
        B__y = raschetmax(i/10,koef,len(find_min),ostatok)
        k=-1
        if(exitFlag):
                 break
        for j in range(len(find_min)-1,0,-1):# от 35, до 39
            k+=1
            if find_min[j]<=raschetmax(B__y,koef,k,ostatok):
                q = find_min[j]
                t = j
                exitFlag = True
                paral_down_left_ind = len(lst)- len(find_min)
                paral_down_left_value = raschetmin(q, koef,t,ostatok)
                paral_down_right_ind = len(lst) - 1
                paral_down_right_value = raschetmax(q,koef,len(find_min)-t-1,ostatok)
                I_down = find_min[j]
                V_down = j
                break
            if(exitFlag):
                 break
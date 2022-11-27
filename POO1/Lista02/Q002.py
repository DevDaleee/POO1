def imprime_lista(l):
    for sub_l in l:
        if (type(sub_l) == list):
            for item in sub_l:
                if (type(item) == list):
                    for sub_l_i in item:
                        print(sub_l_i, end=' ')
                else:
                    print(item, end=' ')
        else:
            print(sub_l, end=' ')
        
        
                

l3 = [0,1,[2,[3,4]],5]

imprime_lista(l3)
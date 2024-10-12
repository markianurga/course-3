# напиши код для виконання завдань тут

#tar = 0
#with open ('m5/u3/1/my_file.txt','r') as file:
#    for ret in file:
#        ter = ret.split(' ')
#        for tir in ter:
#            print(int(tir) == 1)
#            if int(tir) == 1:
#                tar += 1
#print(tar)

with open ('m5/u3/1/my_file.txt','r') as file:
    blek = file.readlines()
    op = blek[13].split(' ')
    print(op[7])
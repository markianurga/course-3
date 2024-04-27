kart = int(input(" введить баланс карти "))
pokypk = (input(" хочете зробити покупку (так/ні)  "))

while pokypk == 'так':
    pers= int(input("введить ціну "))
    if kart >= pers:
        kart -= pers
        print( kart) 
    else:
        print("недостатьно коштів")
    pokypk = (input(" хочете зробити покупку (так/ні)"))
    
print("доступний баланс ", kart ,"грн")
    
ret = input("чи у вас є ідея власного продукту")

if ret == 'так' :
    red = input("чи ви зацікавлений в отриманні інвестиці")
    if red == "так":
        print("У вас є всі шанси потрапити до бізнес-акселератора!")
    else:
        print("Рекомендуємо вам подати документи до бізнес-школи.")
elif ret == "ні":
    print("Дякую, що взяли участь в опитуванні!")

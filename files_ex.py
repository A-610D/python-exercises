#import os
#gtPath = os.path.join("txt-file","gt5.TXT")
#with open(gtPath, "r") as f:
#    print(f.read())

# Напишите программу, которая задает пользователю вопрос и сохраняет ответ
# в файл.
#import os
#value = input("Input, plz ")
#with open(os.path.join("txt-file","my-input.txt"), "w") as f:
#    f.write(value)

#Примите элементы в списке списков и запишите
#их в CSV-файл. Да нные каждого списка должны быть строкой в файле,
#при этом каждый элемент списка должен быть отделен запятой.

import os
import csv
LL = [["Звёздные войны",
  "Терминатор",
  "Искусственный интеллект"],
  ["Дурак",
  "Матильда",
  "Левиафан"],
  ["Люди в чёрном",
  "Я - робот",
  "Эволюция"]]
with open(os.path.join("txt-file","my-films.csv"), "w") as f:
    w = csv.writer(f, delimiter=",")
    for gf in LL:
        w.writerow(gf)
    


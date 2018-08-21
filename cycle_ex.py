#lst = ['asda','sadf','wer','wert']
#for name in lst:
#    print(name)

#for i in range(25,51):
#    print(i)

#lst = ['asda','sadf','wer','wert']
#for i,name in enumerate(lst):
#    print(str(i+1) + ' ' + name)

#Напишите программу с бесконечным циклом
#(с возможностью ввести букву X чтобы выйти) и списком чисел.
#При каждом переборе цикла предлагайте
#пользователю отгадать число из списка и сообщайте, правильно ли он отгадал.
#
#secret=['3','15','46']
#correct = False
#needExit = False
#while(not correct and not needExit):
#    val = input('Enter value or "X" for exit ')
#    if (val == 'X'):
#        break
#    correct = val in secret
#    if correct:
#        print('correct!')
#    else:
#        print('wrong')
    

#Умножьте все числа в списке [8, 19, 148, 4]
#на все числа в списке [9, 1, 33, 83]
#и поместите результаты в третий список

lst1 = [8, 19, 148, 4]
lst2 = [9, 1, 33, 83]
resLst = []
for val1 in lst1:
    for val2 in lst2:
        resLst.append(val1*val2)

for i,t in enumerate(resLst):
    print(str(i) + ' ' + str(t))
        

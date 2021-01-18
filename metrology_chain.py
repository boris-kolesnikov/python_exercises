#Начало метрологической цепи
exit = False
while exit == False:
        
        print('''Для ввода дробных чисел используй точки, а не запятые.
Это важно, иначе ничего не заработает
        
'Введите наименование измеряемого параметра и единицу  измерений [    ]
и нажмите клавишу Enter''');
        parameter_name = (input ())

        print('Введите номинальное значение переменной [    ]')
        nominal_value = float(input ())

        print('Ведите допустимое отклонение параметра +-[    ]')
        tolerance=float(input())
        print('допустимое отклонение в процентах? % (Введите 1 если "ДА",  0 если  "НЕТ")')
        toleranc_percente=float(input())
        if toleranc_percente >= 1: print('Отлично')
        if toleranc_percente <= 0:
                toleranc_percente_eqals=(100*tolerance/nominal_value)
                print(('Это будет ±'), toleranc_percente_eqals, ('%'))
        print('Укажите наименование средства измерений [    ]')
        device_name = (input())
        print('и его погрешность')
        deflection=float(input())
        print('Погрешность в процентах? Введите 1 если "ДА",  0 если  "НЕТ"')
        deflection_percente=float(input())
        if deflection_percente >= 1: print('Отлично')
        if deflection_percente <= 0:
                deflection_percente_eqals=(100*deflection/nominal_value)
                print(('Это будет ±'), deflection_percente_eqals, ('%'))
        print('Укажите требуемый коэффициен точности')
        accuracy_ratio=float(input())     
        result=tolerance/deflection
        if result < accuracy_ratio: print('ВНИМАНИЕ! КТ меньше требуемого! ')
        if result >= accuracy_ratio: print('Поздравляю! КТ соответствует требованию!')
        print(' ')
        print('Ваша метрологическая цепь имеет вид: ')
        print(" ")
        print("  ", parameter_name)
        print(('     НОМИНАЛЬНОЕ ЗНАЧ.:'), nominal_value)

        if toleranc_percente >= 1: print('     ДОПУСК: ±', tolerance, ' %')
        if toleranc_percente <= 0: print('     ДОПУСК: ±', toleranc_percente_eqals, ' %')
        print(('     НАЗВАНИЕ СИ:'), device_name)

        if deflection_percente >= 1: print('     ПОГРЕШНОСТЬ СИ: ±', deflection, ' %')
        if deflection_percente <= 0: print('     ПОГРЕШНОСТЬ СИ: ±', deflection_percente_eqals, ' %')

        print(('     ТРЕБ. КТ:'), accuracy_ratio)
        print(('     ФАКТ. КТ:'), result)
        print('''Нажмите  клавишу "Enter"что бы продолжить или 
введите "q", если хотите завершить работу''')
        if input() == 'q':
                exit = True

        

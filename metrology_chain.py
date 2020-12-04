#Начало метрологической цепи

print('Для ввода дробных чисел используй точки, а не запятые.')
print('Введите наименование измеряемого параметра и единицу еизмерений [    ]  и нажмите клавишу Enter');
parameter_name = (input ())

print('Введите номинальное значение переменной [    ]')
nominal_value = float(input ())

print('Ведите допустимое отклонение параметра +-[    ]')
tolerance=float(input ())

print('допустимое отклонение в процентах? % (Введите 1 если "ДА",  0 если  "НЕТ")')
toleranc_percente=float(input ())
if toleranc_percente >= 1: print('Отлично')
if toleranc_percente <= 0:
        toleranc_percente_eqals=(100*tolerance/nominal_value)
        print(('Это будет ±'), toleranc_percente_eqals, ('%'))
  
print('Укажите наименование средства измерений [    ]')
device_name = (input ())




print('и его погрешность')
deflection=float(input ())
print('Погрешность в процентах? Введите 1 если "ДА",  0 если  "НЕТ"')
deflection_percente=float(input ())
if deflection_percente >= 1: print('Отлично')
if deflection_percente <= 0:
        deflection_percente_eqals=(100*deflection/nominal_value)
        print(('Это будет ±'), deflection_percente_eqals, ('%'))





print('Укажите требуемый коэффициен точности')
accuracy_ratio=float(input ())



#Рассчет фактического значения коэффициента точности
result=tolerance/deflection
if result < accuracy_ratio: print('ВНИМАНИЕ! КТ меньше требуемого! ')
if result >= accuracy_ratio: print('Поздравляю! КТ соответствует требованию!')
print(' ')

print('Ваша метрологическая цепь имеет вид: ')

print(parameter_name, ('НОМИНАЛЬНОЕ ЗНАЧ.:'), nominal_value, ('     ДОПУСК: ±'), toleranc_percente_eqals, ('%'), ('     НАЗВАНИЕ СИ:'), device_name, ('     ПОГРЕШНОСТЬ СИ: ±'), int(deflection_percente_eqals), ('%'), ('     ТРЕБ. КТ:'), accuracy_ratio, ('     ФАКТ.КТ:'), result)

# Написал Крыков Александр 
# Работа скрипта проверена на Python 3.8.5 (32-bit)

x = int (input ("\nВведите число X \n> "))
n = ""                                      # строка для перевода входного числа в двоичный вид

i = int ()

line = ""                                   # строка для формирования двоичной записи выходного числа 

while x > 0:
    y = str(x % 2)
    n = y + n
    x = int(x / 2)
ml = list (n)                               # список с входным числом



fs_end = ml [ len (ml) - 3 ]
sd_end = ml [ len (ml) - 2 ]
th_end = ml [ len (ml) - 1 ] 

fs = ml [ 0 ]
sd = ml [ 1 ]
th = ml [ 2 ]

while i != 3 :
    ml.pop (len(ml) - 1)
    ml.pop (0)
    i += 1


end_list = list ()                          # cписок с выходным числом
end_list.append (fs_end)
end_list.append (sd_end)
end_list.append (th_end)
end_list.extend (ml)
end_list.append (fs)
end_list.append (sd)
end_list.append (th)


line =''.join(end_list)


print ("\n"+ str (int (line , 2 )))







import errors
import random
#coding: utf-8
print('Введите текст и выберите типы ошибок и шанс выпадения ошибок в тексте.')
print('Текст: ', end='')
text=input().split()
words=len(text)
print('Типы возможных ошибок:')
print()
print('0.Закончить выбор.')
print('1.Гласная где-то в слове(вместо "о" "а").')
print('2.Гласная где-то в слове(вместо "е" "и")')
print('3.Согласная где-то в слове(вместо "д" "т")')
print('4.Согласная где-то в слове(вместо "з" "с")')
print('5.Согласная где-то в слове(вместо "ж" "ш")')
print('6.Согласная где-то в слове(вместо "в" "ф")')
print('7.Согласная где-то в слове(вместо "б" "п")')
print('8.Замена слов на иные. ***Special*** ')
print('9.ё/е')
print('10.тся/ться')
print('11.почему/по чему')
print('12.зачем/за чем')
print('13.CAPS/caps (только латинские символы)')
print('14.Удалить слово')
print('15.Удалить точку')
print('16.Удалить запятую')
print('17.Удалить пробел между словами')
print('18.Их/ихний')
print('19.Что/что')
print('20.Ой, нажал на соседнюю клавишу в ряду(например вместо "л" нажал "д").')
#print('20.Зс(французский => Француский)') В разработке
#print('Непроизносимая согласная(например в слове "лестница" вы можете не написать непроизносимую согласную "т" т.е."лесница").') В разработке
#print('Написал на одну букву больше (например по невнимательности написал не "программа", а "программма").') В разработке
#print('Забыл слово(вместо "Костя пошел в лес" "Костя пошел в ").') В разработке
errs=[]
i=0
while b!=0:
    a=int(input())
    b=int(input())
    errs.append(a)
    i+=1

print('Введите шансы для каждой ошибки (от 1 до 100)')
chances=[]
for i in range(0,len(errs)):
    print('Шанс', errs[i], ': ', endl='')
    chances.append(int(input())/100)
cha=dict(zip(errs,chances))

print('Введите максимально возможное число ошибок в одном слове')
maxerr =  int(input())

#Работа с файлом.
f = open('text_input.txt', 'r')
txt = f.read()
words = txt.split()
f.close()
num_err = 0
for i in range(len(words)):
    if 8 in errs and num_err < maxerr:
        z = words[i]
        z = errors.zamena(z, cha[8])
        num_err = maxerr
    elif 2 in errs and num_err < maxerr:
        z = words[i]
        z = errors.switch_ei(z, cha[2])
        num_err+=1
    elif 3 in errs and num_err < maxerr:
        z = words[i]
        z = errors.switch_dt(z, cha[3])
        num_err+=1
    elif 4 in errs and num_err < maxerr:
        z = words[i]
        z = errors.switch_zs(z, cha[4])    
        num_err+=1
    elif 5 in errs and num_err < maxerr:
        z = words[i]
        z = errors.switch_zh_sh(z, cha[5])   
        num_err+=1
    elif 6 in errs and num_err < maxerr:
        z = words[i]
        z = errors.switch_vf(z, cha[6])
        num_err+=1
    elif 7 in errs and num_err < maxerr:
        z = words[i]
        z = errors.switch_bp(z, cha[7])
        num_err+=1
    elif 1 in errs:
        z = words[i]
        z = errors.switch_ao(z, cha[1])
        num_err+=1
    elif 9 in errs and num_err < maxerr:
        z = words[i]
        z = errors.toe(z, cha[9])     
        num_err+=1
    elif 10 in errs and num_err < maxerr:
        z = words[i]
        z = errors.switch_tsya(z, cha[10])
        num_err+=1
    elif 11 in errs and num_err < maxerr:
        z = words[i]
        z = errors.switch_pochemu(z, cha[11])        
        num_err+=1
    elif 12 in errs and num_err < maxerr:
        z = words[i]
        z = errors.switch_zachem(z, cha[12])
        num_err+=1
    elif 13 in errs and num_err < maxerr:
        z = words[i]
        z = errors.switch_caps(z, cha[13])   
        num_err+=1
    elif 14 in errs and num_err < maxerr:
        z = words[i]
        z = ''      
        num_err+=1
    elif 15 in errs and num_err < maxerr:
        z = words[i]
        z = errors.delete(dot, z, cha[15])
        num_err+=1
    elif 16 in errs and num_err < maxerr:
        z = words[i]
        z = errors.delete(comma, z, cha[16])
        num_err+=1
    elif 17 in errs and num_err < maxerr:
        if random.random() <= cha[15] and i != len(words)-1:
            z = words[i]
            z1 = words[i+1]
            words[i] = ''
            words[i+1] = z+z1
        num_err+=1
    elif 18 in errs and num_err < maxerr:
        z = words[i]
        z = errors.add_ihniy(cha[18])
        num_err+=1
    elif 19 in errs and num_err < maxerr:
        z = words[i]
        z = errors.switch_chto(cha[19])     
        num_err+=1
    elif 20 in errs and num_err < maxerr:
        z = words[i]
        pos_in_z = random.randrange(0, len(z))
        z = errors.switch_to_neigh(z[pos_in_z], cha[20])     
        num_err+=1    
        if key == 'delprev':
            z = z[:pos_in_z] + '' + z[pos_in_z + 1:]        
        if pos_in_z != len(z) - 1:
            if key == 'caps':
                z = z[:pos_in_z] + caps_lock(z[pos_in_z + 1:], 1)
    words[i] = z
st = str()
for i in range(0,len(words)):
        st += ' ' + words[i]
st = st[1:]
f = open('text_output.txt', 'w')
f.write(st)
f.close()
print("Смотри файл вывода text_output.txt")

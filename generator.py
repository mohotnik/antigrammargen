import errors
import random
#coding: utf-8
print('������� ����� � �������� ���� ������ � ���� ��������� ������ � ������.')
print('�����: ', end='')
text=input().split()
words=len(text)
print('���� ��������� ������:')
print()
print('0.��������� �����.')
print('1.������� ���-�� � �����(������ "�" "�").')
print('2.������� ���-�� � �����(������ "�" "�")')
print('3.��������� ���-�� � �����(������ "�" "�")')
print('4.��������� ���-�� � �����(������ "�" "�")')
print('5.��������� ���-�� � �����(������ "�" "�")')
print('6.��������� ���-�� � �����(������ "�" "�")')
print('7.��������� ���-�� � �����(������ "�" "�")')
print('8.������ ���� �� ����. ***Special*** ')
print('9.�/�')
print('10.���/����')
print('11.������/�� ����')
print('12.�����/�� ���')
print('13.CAPS/caps (������ ��������� �������)')
print('14.������� �����')
print('15.������� �����')
print('16.������� �������')
print('17.������� ������ ����� �������')
print('18.��/�����')
print('19.���/���')
print('20.��, ����� �� �������� ������� � ����(�������� ������ "�" ����� "�").')
#print('20.��(����������� => ����������)') � ����������
#print('�������������� ���������(�������� � ����� "��������" �� ������ �� �������� �������������� ��������� "�" �.�."�������").') � ����������
#print('������� �� ���� ����� ������ (�������� �� ���������������� ������� �� "���������", � "����������").') � ����������
#print('����� �����(������ "����� ����� � ���" "����� ����� � ").') � ����������
errs=[]
i=0
while b!=0:
    a=int(input())
    b=int(input())
    errs.append(a)
    i+=1

print('������� ����� ��� ������ ������ (�� 1 �� 100)')
chances=[]
for i in range(0,len(errs)):
    print('����', errs[i], ': ', endl='')
    chances.append(int(input())/100)
cha=dict(zip(errs,chances))

print('������� ����������� ��������� ����� ������ � ����� �����')
maxerr =  int(input())

#������ � ������.
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
print("������ ���� ������ text_output.txt")

import random
#coding: utf-8
'''
   0  1  2  3  4  5  6  7  8  9  10 11 12
   
0  `  1  2  3  4  5  6  7  8  9  0  -  =
1     q  w  e  r  t  y  u  i  o  p  [  ]
2     a  s  d  f  g  h  j  k  l  ;  '  \
3     z  x  c  v  b  n  m  ,  .  /
'''
left_slash = chr(92)
palka = chr(124)
keyboard_eng = [['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='], ['', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']'],['', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'", left_slash],['', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.',]]
keyboard_eng_caps = [['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', palka], ['', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '{','}'],['', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', '"'],['', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?', '']]
keyboard_rus = [['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='], ['', 'й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ъ'],['', 'ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л', 'д', 'ж', 'э'],['', 'я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю', '.']]
keyboard_rus_caps = [['Ё', '!', '"', '№', ';', '%', ':', '?', '*', '(', ')'], ['', 'Й', 'Ц', 'У', 'К', 'Е', 'Н', 'Г', 'Ш', 'Щ', 'З', 'Х', 'Ъ'],['', 'Ф', 'Ы', 'В', 'А', 'П', 'Р', 'О', 'Л', 'Д', 'Ж', 'Э'],['', 'Я', 'Ч', 'С', 'М', 'И', 'Т', 'Ь', 'Б', 'Ю', ',']]
Caps_all = ['Ё','Й', 'Ц', 'У', 'К', 'Е', 'Н', 'Г', 'Ш', 'Щ', 'З', 'Х', 'Ъ', 'Ф', 'Ы', 'В', 'А', 'П', 'Р', 'О', 'Л', 'Д', 'Ж', 'Э', 'Я', 'Ч', 'С', 'М', 'И', 'Т', 'Ь', 'Б', 'Ю', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
#Caps_rus = ['Ё','Й', 'Ц', 'У', 'К', 'Е', 'Н', 'Г', 'Ш', 'Щ', 'З', 'Х', 'Ъ', 'Ф', 'Ы', 'В', 'А', 'П', 'Р', 'О', 'Л', 'Д', 'Ж', 'Э', 'Я', 'Ч', 'С', 'М', 'И', 'Т', 'Ь', 'Б', 'Ю']
#Caps_eng =['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
Symbols_numb = ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=','[', ']', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '|', '{','}']
full_chance=1
def get_key_on_keyboard(pos_x, pos_y, english, caps):
    if pos_x == 0:
        if pos_y == 0:
            if english:
                if caps:
                    return '~'
                else:
                    return '`'
            else:
                if caps:
                    return 'Ё'
                else:
                    return 'ё'
    elif pos_x == 1:
        if pos_y == 0:
            if caps:
                return '!'
            else:
                return '1'
        elif pos_y == 1:
            if english:
                if caps:
                    return 'Q'
                else:
                    return 'q'
            else:
                if caps:
                    return 'Й'
                else:
                    return 'й'
        elif pos_y == 2:
            if english:
                if caps:
                    return 'A'
                else:
                    return 'a'
            else:
                if caps:
                    return 'Ф'
                else:
                    return 'ф'
        elif pos_y == 3:
            if english:
                if caps:
                    return 'Z'
                else:
                    return 'z'
            else:
                if caps:
                    return 'Я'
                else:
                    return 'я'
    elif pos_x == 2:
        if pos_y == 0:
            if caps:
                if english:
                    return '@'
                else:
                    return '"'
            else:
                return '2'
        elif pos_y == 1:
            if english:
                if caps:
                    return 'W'
                else:
                    return 'w'
            else:
                if caps:
                    return 'Ц'
                else:
                    return 'ц'
        elif pos_y == 2:
            if english:
                if caps:
                    return 'S'
                else:
                    return 's'
            else:
                if caps:
                    return 'Ы'
                else:
                    return 'ы'
        elif pos_y == 3:
            if english:
                if caps:
                    return 'X'
                else:
                    return 'x'
            else:
                if caps:
                    return 'Ч'
                else:
                    return 'ч'
        elif pos_y == 4:
            if random.random() <= 0.25:
                return ' '
    elif pos_x == 3:
        if pos_y == 0:
            if caps:
                if english:
                    return '#'
                else:
                    return '№'
            else:
                return '3'
        elif pos_y == 1:
            if english:
                if caps:
                    return 'E'
                else:
                    return 'e'
            else:
                if caps:
                    return 'У'
                else:
                    return 'у'
        elif pos_y == 2:
            if english:
                if caps:
                    return 'D'
                else:
                    return 'd'
            else:
                if caps:
                    return 'В'
                else:
                    return 'в'
        elif pos_y == 3:
            if english:
                if caps:
                    return 'C'
                else:
                    return 'c'
            else:
                if caps:
                    return 'С'
                else:
                    return 'с'
        elif pos_y == 4:
            return ' '
    elif pos_x == 4:
        if pos_y == 0:
            if caps:
                if english:
                    return '$'
                else:
                    return ';'
            else:
                return '4'
        elif pos_y == 1:
            if english:
                if caps:
                    return 'R'
                else:
                    return 'r'
            else:
                if caps:
                    return 'К'
                else:
                    return 'к'
        elif pos_y == 2:
            if english:
                if caps:
                    return 'F'
                else:
                    return 'f'
            else:
                if caps:
                    return 'А'
                else:
                    return 'а'
        elif pos_y == 3:
            if english:
                if caps:
                    return 'V'
                else:
                    return 'v'
            else:
                if caps:
                    return 'М'
                else:
                    return 'м'
        elif pos_y == 4:
            return ' '
    elif pos_x == 5:
        if pos_y == 0:
            if caps:
                return '%'
            else:
                return '5'
        elif pos_y == 1:
            if english:
                if caps:
                    return 'T'
                else:
                    return 't'
            else:
                if caps:
                    return 'Е'
                else:
                    return 'е'
        elif pos_y == 2:
            if english:
                if caps:
                    return 'G'
                else:
                    return 'g'
            else:
                if caps:
                    return 'П'
                else:
                    return 'п'
        elif pos_y == 3:
            if english:
                if caps:
                    return 'B'
                else:
                    return 'b'
            else:
                if caps:
                    return 'И'
                else:
                    return 'и'
        elif pos_y == 4:
            return ' '
    elif pos_x == 6:
        if pos_y == 0:
            if caps:
                if english:
                    return '^'
                else:
                    return ':'
            else:
                return '6'
        elif pos_y == 1:
            if english:
                if caps:
                    return 'Y'
                else:
                    return 'y'
            else:
                if caps:
                    return 'Н'
                else:
                    return 'н'
        elif pos_y == 2:
            if english:
                if caps:
                    return 'H'
                else:
                    return 'h'
            else:
                if caps:
                    return 'Р'
                else:
                    return 'р'
        elif pos_y == 3:
            if english:
                if caps:
                    return 'N'
                else:
                    return 'n'
            else:
                if caps:
                    return 'Т'
                else:
                    return 'т'
        elif pos_y == 4:
            return ' '
    elif pos_x == 7:
        if pos_y == 0:
            if caps:
                if english:
                    return '&'
                else:
                    return '?'
            else:
                return '7'
        elif pos_y == 1:
            if english:
                if caps:
                    return 'U'
                else:
                    return 'u'
            else:
                if caps:
                    return 'Г'
                else:
                    return 'г'
        elif pos_y == 2:
            if english:
                if caps:
                    return 'J'
                else:
                    return 'j'
            else:
                if caps:
                    return 'О'
                else:
                    return 'о'
        elif pos_y == 3:
            if english:
                if caps:
                    return 'M'
                else:
                    return 'm'
            else:
                if caps:
                    return 'Ь'
                else:
                    return 'ь'
        elif pos_y == 4:
            return ' '
    elif pos_x == 8:
        if pos_y == 0:
            if caps:
                return '*'
            else:
                return '8'
        elif pos_y == 1:
            if english:
                if caps:
                    return 'I'
                else:
                    return 'i'
            else:
                if caps:
                    return 'Ш'
                else:
                    return 'ш'
        elif pos_y == 2:
            if english:
                if caps:
                    return 'K'
                else:
                    return 'k'
            else:
                if caps:
                    return 'Л'
                else:
                    return 'л'
        elif pos_y == 3:
            if english:
                if caps:
                    return '<'
                else:
                    return ','
            else:
                if caps:
                    return 'Б'
                else:
                    return 'б'
        elif pos_y == 4:
            if random.random() <= 0.25:
                return ' '
            else:
                return ''
    elif pos_x == 9:
        if pos_y == 0:
            if caps:
                return '('
            else:
                return '9'
        elif pos_y == 1:
            if english:
                if caps:
                    return 'O'
                else:
                    return 'o'
            else:
                if caps:
                    return 'Щ'
                else:
                    return 'щ'
        elif pos_y == 2:
            if english:
                if caps:
                    return 'L'
                else:
                    return 'l'
            else:
                if caps:
                    return 'Д'
                else:
                    return 'д'
        elif pos_y == 3:
            if english:
                if caps:
                    return '>'
                else:
                    return '.'
            else:
                if caps:
                    return 'Ю'
                else:
                    return 'ю'
        elif pos_y == 4:
            return ''
    elif pos_x == 10:
        if pos_y == 0:
            if caps:
                return ')'
            else:
                return '0'
        elif pos_y == 1:
            if english:
                if caps:
                    return 'P'
                else:
                    return 'p'
            else:
                if caps:
                    return 'З'
                else:
                    return 'з'
        elif pos_y == 2:
            if english:
                if caps:
                    return ':'
                else:
                    return ';'
            else:
                if caps:
                    return 'Ж'
                else:
                    return 'ж'
        elif pos_y == 3:
            if english:
                if caps:
                    return '?'
                else:
                    return '/'
            else:
                if caps:
                    return ','
                else:
                    return '.'
        elif pos_y == 4:
            return ''
    elif pos_x == 11:
        if pos_y == 0:
            if caps:
                return '_'
            else:
                return '-'
        elif pos_y == 1:
            if english:
                if caps:
                    return '{'
                else:
                    return '['
            else:
                if caps:
                    return 'Х'
                else:
                    return 'х'
        elif pos_y == 2:
            if english:
                if caps:
                    return '"'
                else:
                    return "'"
            else:
                if caps:
                    return 'Э'
                else:
                    return 'э'
    elif pos_x == 12:
        if pos_y == 0:
            if caps:
                return '+'
            else:
                return '='
        elif pos_y == 1:
            if english:
                if caps:
                    return '}'
                else:
                    return ']'
            else:
                if caps:
                    return 'Ъ'
                else:
                    return 'ъ'
        elif pos_y == 2:
            if english:
                if caps:
                    return '|'
                else:
                    return '\\'
            else:
                if caps:
                    return '/'
                else:
                    return '\\'
    return ''
def get_key_pos(key, english):
    pos = [0, 0, 0, 0]  # [pos_x, pos_y, caps, english]
    if english:
        if key == '`' or key == '1' or key == '2' or key == '3' or key == '4' or key == '5' or key == '6' \
                or key == '7' or key == '8' or key == '9' or key == '0' or key == '-' or key == '=':
            pos[1] = 0
            pos[2] = 0
        elif key == '~' or key == '!' or key == '@' or key == '#' or key == '$' or key == '%' or key == '^' \
                or key == '&' or key == '*' or key == '(' or key == ')' or key == '_' or key == '+':
            pos[1] = 0
            pos[2] = 1
        elif key == 'q' or key == 'w' or key == 'e' or key == 'r' or key == 't' or key == 'y' or key == 'u' \
                or key == 'i' or key == 'o' or key == 'p' or key == '[' or key == ']':
            pos[1] = 1
            pos[2] = 0
        elif key == 'Q' or key == 'W' or key == 'E' or key == 'R' or key == 'T' or key == 'Y' or key == 'U' \
                or key == 'I' or key == 'O' or key == 'P' or key == '{' or key == '}':
            pos[1] = 1
            pos[2] = 1
        elif key == 'a' or key == 's' or key == 'd' or key == 'f' or key == 'g' or key == 'h' or key == 'j' \
                or key == 'k' or key == 'l' or key == ';' or key == "'" or key == '\\':
            pos[1] = 2
            pos[2] = 0
        elif key == 'A' or key == 'S' or key == 'D' or key == 'F' or key == 'G' or key == 'H' or key == 'J' \
                or key == 'K' or key == 'L' or key == ':' or key == '"' or key == '|':
            pos[1] = 2
            pos[2] = 1
        elif key == 'z' or key == 'x' or key == 'c' or key == 'v' or key == 'b' or key == 'n' or key == 'm' \
                or key == ',' or key == '.' or key == '/':
            pos[1] = 3
            pos[2] = 0
        elif key == 'Z' or key == 'X' or key == 'C' or key == 'V' or key == 'B' or key == 'N' or key == 'M' \
                or key == '<' or key == '>' or key == '?':
            pos[1] = 3
            pos[2] = 1
        if key == '`' or key == '~':
            pos[0] = 0
        elif key == '1' or key == '!' or key == 'q' or key == 'Q' or key == 'a' or key == 'A' or key == 'z' \
                or key == 'Z':
            pos[0] = 1
        elif key == '2' or key == '@' or key == 'w' or key == 'W' or key == 's' or key == 'S' or key == 'x' \
                or key == 'X':
            pos[0] = 2
        elif key == '3' or key == '#' or key == 'e' or key == 'E' or key == 'd' or key == 'D' or key == 'c' \
                or key == 'C':
            pos[0] = 3
        elif key == '4' or key == '$' or key == 'r' or key == 'R' or key == 'f' or key == 'F' or key == 'v' \
                or key == 'V':
            pos[0] = 4
        elif key == '5' or key == '%' or key == 't' or key == 'T' or key == 'g' or key == 'G' or key == 'b' \
                or key == 'B':
            pos[0] = 5
        elif key == '6' or key == '^' or key == 'y' or key == 'Y' or key == 'h' or key == 'H' or key == 'n' \
                or key == 'N':
            pos[0] = 6
        elif key == '7' or key == '&' or key == 'u' or key == 'U' or key == 'j' or key == 'J' or key == 'm' \
                or key == 'M':
            pos[0] = 7
        elif key == '8' or key == '*' or key == 'i' or key == 'I' or key == 'k' or key == 'K' or key == ',' \
                or key == '<':
            pos[0] = 8
        elif key == '9' or key == '(' or key == 'o' or key == 'O' or key == 'l' or key == 'L' or key == '.' \
                or key == '>':
            pos[0] = 9
        elif key == '0' or key == ')' or key == 'p' or key == 'P' or key == ';' or key == ':' or key == '/' \
                or key == '?':
            pos[0] = 10
        elif key == '-' or key == '_' or key == '[' or key == '{' or key == "'" or key == '"':
            pos[0] = 11
        elif key == '=' or key == '+' or key == ']' or key == '}' or key == '\\' or key == '|':
            pos[0] = 12
    else:
        if key == 'ё' or key == '1' or key == '2' or key == '3' or key == '4' or key == '5' or key == '6' \
                or key == '7' or key == '8' or key == '9' or key == '0' or key == '-' or key == '=':
            pos[1] = 0
            pos[2] = 0
        elif key == 'Ё' or key == '!' or key == '"' or key == '№' or key == ';' or key == '%' or key == ':' \
                or key == '?' or key == '*' or key == '(' or key == ')' or key == '_' or key == '+':
            pos[1] = 0
            pos[2] = 1
        elif key == 'й' or key == 'ц' or key == 'у' or key == 'к' or key == 'е' or key == 'н' or key == 'г' \
                or key == 'ш' or key == 'щ' or key == 'з' or key == 'х' or key == 'ъ':
            pos[1] = 1
            pos[2] = 0
        elif key == 'Й' or key == 'Ц' or key == 'У' or key == 'К' or key == 'Е' or key == 'Н' or key == 'Г' \
                or key == 'Ш' or key == 'Щ' or key == 'З' or key == 'Х' or key == 'Ъ':
            pos[1] = 1
            pos[2] = 1
        elif key == 'ф' or key == 'ы' or key == 'в' or key == 'а' or key == 'п' or key == 'р' or key == 'о' \
                or key == 'л' or key == 'д' or key == 'ж' or key == "э" or key == '\\':
            pos[1] = 2
            pos[2] = 0
        elif key == 'Ф' or key == 'Ы' or key == 'В' or key == 'А' or key == 'П' or key == 'Р' or key == 'О' \
                or key == 'Л' or key == 'Д' or key == 'Ж' or key == 'Э' or key == '/':
            pos[1] = 2
            pos[2] = 1
        elif key == 'я' or key == 'ч' or key == 'с' or key == 'м' or key == 'и' or key == 'т' or key == 'ь' \
                or key == 'б' or key == 'ю' or key == '.':
            pos[1] = 3
            pos[2] = 0
        elif key == 'Я' or key == 'Ч' or key == 'С' or key == 'М' or key == 'И' or key == 'Т' or key == 'Ь' \
                or key == 'Б' or key == 'Ю' or key == ',':
            pos[1] = 3
            pos[2] = 1
        if key == 'ё' or key == 'Ё':
            pos[0] = 0
        elif key == '1' or key == '!' or key == 'й' or key == 'Й' or key == 'ф' or key == 'Ф' or key == 'я' \
                or key == 'Я':
            pos[0] = 1
        elif key == '2' or key == '"' or key == 'ц' or key == 'Ц' or key == 'ы' or key == 'Ы' or key == 'ч' \
                or key == 'Ч':
            pos[0] = 2
        elif key == '3' or key == '№' or key == 'у' or key == 'У' or key == 'в' or key == 'В' or key == 'с' \
                or key == 'С':
            pos[0] = 3
        elif key == '4' or key == ';' or key == 'к' or key == 'К' or key == 'а' or key == 'А' or key == 'м' \
                or key == 'М':
            pos[0] = 4
        elif key == '5' or key == '%' or key == 'е' or key == 'Е' or key == 'п' or key == 'П' or key == 'и' \
                or key == 'И':
            pos[0] = 5
        elif key == '6' or key == ':' or key == 'н' or key == 'Н' or key == 'р' or key == 'Р' or key == 'т' \
                or key == 'Т':
            pos[0] = 6
        elif key == '7' or key == '?' or key == 'г' or key == 'Г' or key == 'о' or key == 'О' or key == 'ь' \
                or key == 'Ь':
            pos[0] = 7
        elif key == '8' or key == '*' or key == 'ш' or key == 'Ш' or key == 'л' or key == 'Л' or key == 'б' \
                or key == 'Б':
            pos[0] = 8
        elif key == '9' or key == '(' or key == 'щ' or key == 'Щ' or key == 'д' or key == 'Д' or key == 'ю' \
                or key == 'Ю':
            pos[0] = 9
        elif key == '0' or key == ')' or key == 'з' or key == 'З' or key == 'ж' or key == 'Ж' or key == '.' \
                or key == ',':
            pos[0] = 10
        elif key == '-' or key == '_' or key == 'х' or key == 'Х' or key == "э" or key == 'Э':
            pos[0] = 11
        elif key == '=' or key == '+' or key == 'ъ' or key == 'Ъ' or key == '\\' or key == '/':
            pos[0] = 12
    pos[3] = english
    return pos
def get_language(key):  # 1 - english; 2 - russian
    cod=ord(key)
    if ord('a')<=cod<=ord('z') or ord('A')<=cod<=ord('Z'):
        return 1
    elif ord('а')<=cod<=ord('я') or ord('А')<=cod<=ord('Я'):
        return 2
def get_caps(key):
    if key in Caps_all:
        return True
    else: 
        return False
def is_letter(char):
    if (ord('a') <= ord(char) <= ord('z')) or (ord('A') <= ord(char) <= ord('Z')) \
            or (ord('а') <= ord(char) <= ord('я')) or (ord('А') <= ord(char) <= ord('Я')):
        return True
    return False
'''def switch_keyboard_layout_all(slovo, chance):
        if random.random() <= chance:
            return switch_keyboard_layout_particle(slovo, full_chance)
        return slovo'''
def switch_keyboard_layout_particle(slovo, chance):
    i = 0
    while i < len(slovo):
        if is_letter(slovo[i]):
            bukva = slovo[i]
            lang_bukva = get_language(bukva)
            if lang_bukva == 2:
                lang_bukva = 0
            c = get_key_pos(bukva, lang_bukva)
            if get_caps(bukva):
                if lang_bukva:
                    bukva = keyboard_rus_caps[c[1]][c[0]]
                else:
                    bukva = keyboard_eng_caps[c[1]][c[0]]
            else:
                if lang_bukva:
                    bukva = keyboard_rus[c[1]][c[0]]
                else:
                    bukva = keyboard_eng[c[1]][c[0]]
            d = []
            if i + 1 <= len(slovo):
                d = slovo[i+1:]
            slovo = slovo[:i] + bukva + d
        i += 1
    return slovo
'''def switch_caps(slovo, chance):
    i = 0
    while i < len(slovo):
        if is_letter(slovo[i]):
            if random.random() <= chance:
                a = get_language(slovo[i])
                a = get_key_pos(slovo[i], a)
                if a[2]:
                    a[2] = 0
                else:
                    a[2] = 1
                slovo = slovo[:i] + get_key_on_keyboard(a[0], a[1], a[3], a[2]) + slovo[i + 1:]
        i += 1
    return slovo'''

def switch_tsya(slovo, chance):
    if slovo.endswith('тся'):
        if random.random() <= chance:
            slovo = slovo[:-2]
            slovo += 'ься'
    elif slovo.endswith('ться'):
        if random.random() <= chance:
            slovo = slovo[:-3]
            slovo += 'ся'
    return slovo

def switch_pochemu(chance):
    global words
    if 'почему' in words:
        a = words.find('почему')
        slovo = 'по чему'
    return slovo

def switch_zachem(chance):
    global words
    if 'зачем' in words:
        a = words.find('зачем')
        slovo = 'за чем'
    return slovo

def add_ihniy(chance):
    i = 0
    global words
    if random.random() <= chance:
        if 'их' in words:
            i = words.find('их')
            slovo = 'ихний'
    return i

def switch_ei(slovo, chance):
    i = 0
    while i < len(slovo):
        if slovo[i] == 'е':
            if random.random() <= chance:
                slovo = slovo[:i] + 'и' + slovo[i + 1:]
        elif slovo[i] == 'и':
            if random.random() <= chance:
                slovo = slovo[:i] + 'е' + slovo[i + 1:]
        i += 1
    return slovo

def switch_ao(slovo, chance):
    i = 0
    while i < len(slovo):
        if slovo[i] == 'а':
            if random.random() <= chance:
                slovo = slovo[:i] + 'о' + slovo[i + 1:]
        elif slovo[i] == 'о':
            if random.random() <= chance:
                slovo = slovo[:i] + 'а' + slovo[i + 1:]
        i += 1
    return slovo

def switch_chto(chance):
    global words
    if random.random() <= chance:
        if 'что' in words:
            a = words.find('что')
            slovo = 'што'
        elif 'что-то' in words:
            a = words.find('что-то')
            slovo = 'што-то'
def switch_dt(slovo, chance):
    i = 0
    while i < len(slovo):
        if slovo[i] == 'д':
            if random.random() <= chance:
                slovo = slovo[:i] + 'т' + slovo[i + 1:]
        elif slovo[i] == 'т':
            if random.random() <= chance:
                slovo = slovo[:i] + 'д' + slovo[i + 1:]
        i += 1
    return slovo

def switch_zs(slovo, chance):
    i = 0
    while i < len(slovo):
        if slovo[i] == 'з':
            if random.random() <= chance:
                slovo = slovo[:i] + 'с' + slovo[i + 1:]
        elif slovo[i] == 'с':
            if random.random() <= chance:
                slovo = slovo[:i] + 'з' + slovo[i + 1:]
        i += 1
    return slovo

def switch_zh_sh(slovo, chance):
    i = 0
    while i < len(slovo):
        if slovo[i] == 'ж':
            if random.random() <= chance:
                slovo = slovo[:i] + 'ш' + slovo[i + 1:]
        elif slovo[i] == 'ш':
            if random.random() <= chance:
                slovo = slovo[:i] + 'ж' + slovo[i + 1:]
        i += 1
    return slovo

def switch_vf(slovo, chance):
    i = 0
    while i < len(slovo):
        if slovo[i] == 'в':
            if random.random() <= chance:
                slovo = slovo[:i] + 'ф' + slovo[i + 1:]
        elif slovo[i] == 'ф':
            if random.random() <= chance:
                slovo = slovo[:i] + 'в' + slovo[i + 1:]
        i += 1
    return slovo

def switch_bp(slovo, chance):
    i = 0
    while i < len(slovo):
        if slovo[i] == 'б':
            if random.random() <= chance:
                slovo = slovo[:i] + 'п' + slovo[i + 1:]
        elif slovo[i] == 'п':
            if random.random() <= chance:
                slovo = slovo[:i] + 'б' + slovo[i + 1:]
        i += 1
    return slovo

def toe(slovo, chance):
    if random.random() <= chance:
        if slovo.count('ё')>0:
            for i in range(slovo.count('ё')):
                yo = slovo.find('ё')
                slovo = slovo[:yo] + 'е' + slovo[yo+1:]
    return slovo

def delete(argum, slovo, chance):
    if random.random() <= chance:
        if argum == 'spaces':
            i = 0
            while i < len(slovo):
                if slovo[i] == ' ':
                    if random.random() <= chance:
                        slovo = slovo[:i] + slovo[i + 1:]
                        i -= 1
                i += 1
            return slovo
    
        elif argum == 'comma':
            i = 0
            while i < len(slovo):
                if slovo[i] == ',':
                    if random.random() <= chance:
                        slovo = slovo[:i] + slovo[i + 1:]
                        i -= 1
                i += 1
            return slovo
    
        elif argum == 'dot':
            i = 0
            while i < len(slovo):
                if slovo[i] == '.':
                    if random.random() <= chance:
                        slovo = slovo[:i] + slovo[i + 1:]
                        i -= 1
                i += 1
            return slovo

def caps_lock(slovo, chance):
    if random.random() <= chance:
        i = 0
        while i < len(slovo):
            if is_letter(slovo[i]):
                a = get_language(slovo[i])
                a = get_key_pos(slovo[i], a)
                if a[2] == 0:
                    a[2] = 1
                slovo = slovo[:i] + get_key_on_keyboard(a[0], a[1], a[3], a[2]) + slovo[i + 1:]
            i += 1
    return slovo
'''def switch_to_neigh(key, chance): Версия с массивами
    if random.random() <= chance:
        key_lang = get_language(key)
        if key_lang == 2:
            key_lang = 0
        a = get_key_pos(key, key_lang)#a == [x y caps eng]
        ch = random.randrange(0,8)
        #if a[][] 
        #if y not in [1, 4] and x 
        x = a[0]
        y= a[1]
        if y != 0 and x not in [0, 1, 12] and (y != 2 and x != 11)and (y != 3 and x not in [2, 3, 4, 5, 6, 7, 8, 9, 10]):
            if a[2]:
                if key_lang == 0:#Russian & Caps
                    if ch == 0:
                        key = keyboard_rus_caps[y+1][x+1]
                    elif ch == 1:
                        key = keyboard_rus_caps[y+1][x]
                    elif ch == 2:
                        key = keyboard_rus_caps[y+1][x-1]
                    elif ch == 3:
                        key = keyboard_rus_caps[y][x+1]
                    elif ch == 4:
                        key = keyboard_rus_caps[y][x-1]
                    elif ch == 5:
                        key = keyboard_rus_caps[y-1][x+1]
                    elif ch == 6:
                        key = keyboard_rus_caps[y-1][x]
                    elif ch == 7:
                        key = keyboard_rus_caps[y-1][x-1]
                else:# English & Caps
                    if ch == 0:
                        key = keyboard_rus_caps[y+1][x+1]
                    elif ch == 1:
                        key = keyboard_rus_caps[y+1][x]
                    elif ch == 2:
                        key = keyboard_rus_caps[y+1][x-1]
                    elif ch == 3:
                        key = keyboard_rus_caps[y][x+1]
                    elif ch == 4:
                        key = keyboard_rus_caps[y][x-1]
                    elif ch == 5:
                        key = keyboard_rus_caps[y-1][x+1]
                    elif ch == 6:
                        key = keyboard_rus_caps[y-1][x]
                    elif ch == 7:
                        key = keyboard_rus_caps[y-1][x-1]
            else:
                if key_lang == 0:#Russian & NonCaps
                    if ch == 0:
                        key = keyboard_rus_caps[y+1][x+1]
                    elif ch == 1:
                        key = keyboard_rus_caps[y+1][x]
                    elif ch == 2:
                        key = keyboard_rus_caps[y+1][x-1]
                    elif ch == 3:
                        key = keyboard_rus_caps[y][x+1]
                    elif ch == 4:
                        key = keyboard_rus_caps[y][x-1]
                    elif ch == 5:
                        key = keyboard_rus_caps[y-1][x+1]
                    elif ch == 6:
                        key = keyboard_rus_caps[y-1][x]
                    elif ch == 7:
                        key = keyboard_rus_caps[y-1][x-1]
                else:# English & NonCaps
                    if ch == 0:
                        key = keyboard_rus_caps[y+1][x+1]
                    elif ch == 1:
                        key = keyboard_rus_caps[y+1][x]
                    elif ch == 2:
                        key = keyboard_rus_caps[y+1][x-1]
                    elif ch == 3:
                        key = keyboard_rus_caps[y][x+1]
                    elif ch == 4:
                        key = keyboard_rus_caps[y][x-1]
                    elif ch == 5:
                        key = keyboard_rus_caps[y-1][x+1]
                    elif ch == 6:
                        key = keyboard_rus_caps[y-1][x]
                    elif ch == 7:
                        key = keyboard_rus_caps[y-1][x-1]
        elif  x == 0 and y == 0:#Ё
            if a[2]:#Caps
                key = Symbols_numb[15]
            else:
                key = Symbols_numb[1]
        elif x == 1 and y == 0: #1!
            ch = random.randrange(0,4)
            if a[2]:
                if key == '1' and a[3]:#Eng
                    if ch == 0:
                        key = keyboard_eng[x-1][y]
                    elif ch == 1:
                        key = keyboard_eng[x+1][y]
                    elif ch == 2:
                        key = keyboard_eng[x][y+1]
                    elif ch == 3:
                        key = keyboard_eng[x+1][y+1]
                elif key == '!' and a[3]:#Eng Caps
                    if ch == 0:
                        key = keyboard_eng_caps[x-1][y]
                    elif ch == 1:
                        key = keyboard_eng_caps[x+1][y]
                    elif ch == 2:
                        key = keyboard_eng_caps[x][y+1]
                    elif ch == 3:
                        key = keyboard_eng_caps[x+1][y+1]
                elif key == '1' and a[3] == 0:# Rus
                    if ch == 0:
                        key = keyboard_rus[x-1][y]
                    elif ch == 1:
                        key = keyboard_rus[x+1][y]
                    elif ch == 2:
                        key = keyboard_rus[x][y+1]
                    elif ch == 3:
                        key = keyboard_rus[x+1][y+1]
                elif key == '!'  and a[3] == 0:#Rus Caps
                    if ch == 0:
                        key = keyboard_rus_caps[x-1][y]
                    elif ch == 1:
                        key = keyboard_rus_caps[x+1][y]
                    elif ch == 2:
                        key = keyboard_rus_caps[x][y+1]
                    elif ch == 3:
                        key = keyboard_rus_caps[x+1][y+1]
        elif x == 1 and y in [1, 2]:#q,a без капса и таба
            ch = random.randrange(0,6)
            if a[2]:
                if key == 'q':
                    if ch == 0:
                        key = keyboard_eng[y+1][x+1]
                    elif ch == 1:
                        key = keyboard_eng[y+1][x]
                    elif ch == 2:
                        key = keyboard_eng[y+1][x-1]
                    elif ch == 3:
                        key = keyboard_eng[y][x+1]
                    elif ch == 4:
                        key = keyboard_eng[y-1][x]
                    elif ch == 5:
                        key = keyboard_eng[y-1][x-1]
                elif key == 'a':
                    if ch == 0:
                        key = keyboard_eng[y+1][x+1]
                    elif ch == 1:
                        key = keyboard_eng[y+1][x]
                    elif ch == 2:
                        key = keyboard_eng[y][x+1]
                    elif ch == 3:
                        key = keyboard_eng[y-1][x]
                    elif ch == 4:
                        key = keyboard_eng[y-1][x+1]
                elif key == 'й':
                    if ch == 0:
                        key = keyboard_rus[y+1][x+1]
                    elif ch == 1:
                        key = keyboard_rus[y+1][x]
                    elif ch == 2:
                        key = keyboard_rus[y+1][x-1]
                    elif ch == 3:
                        key = keyboard_rus[y][x+1]
                    elif ch == 4:
                        key = keyboard_rus[y-1][x]
                    elif ch == 5:
                        key = keyboard_rus[y-1][x-1]
                elif key == 'ф':
                    if ch == 0:
                        key = keyboard_rus[y+1][x+1]
                    elif ch == 1:
                        key = keyboard_rus[y+1][x]
                    elif ch == 2:
                        key = keyboard_rus[y][x+1]
                    elif ch == 3:
                        key = keyboard_rus[y-1][x]
                    elif ch == 4:
                        key = keyboard_rus[y-1][x+1]            
            else:
                if key == 'Q':
                    if ch == 0:
                        key = keyboard_eng_caps[y+1][x+1]
                    elif ch == 1:
                        key = keyboard_eng_caps[y+1][x]
                    elif ch == 2:
                        key = keyboard_eng_caps[y+1][x-1]
                    elif ch == 3:
                        key = keyboard_eng_caps[y][x+1]
                    elif ch == 4:
                        key = keyboard_eng_caps[y-1][x]
                    elif ch == 5:
                        key = keyboard_eng_caps[y-1][x-1]
                elif key == 'A':
                    if ch == 0:
                        key = keyboard_eng_caps[y+1][x+1]
                    elif ch == 1:
                        key = keyboard_eng_caps[y+1][x]
                    elif ch == 2:
                        key = keyboard_eng_caps[y][x+1]
                    elif ch == 3:
                        key = keyboard_eng_caps[y-1][x]
                    elif ch == 4:
                        key = keyboard_eng_caps[y-1][x+1]    
                elif key == 'й':
                    if ch == 0:
                        key = keyboard_rus_caps[y+1][x+1]
                    elif ch == 1:
                        key = keyboard_rus_caps[y+1][x]
                    elif ch == 2:
                        key = keyboard_rus_caps[y+1][x-1]
                    elif ch == 3:
                        key = keyboard_rus_caps[y][x+1]
                    elif ch == 4:
                        key = keyboard_rus_caps[y-1][x]
                    elif ch == 5:
                        key = keyboard_rus_caps[y-1][x-1]
                elif key == 'Ф':
                    if ch == 0:
                        key = keyboard_rus_caps[y+1][x+1]
                    elif ch == 1:
                        key = keyboard_rus_caps[y+1][x]
                    elif ch == 2:
                        key = keyboard_rus_caps[y][x+1]
                    elif ch == 3:
                        key = keyboard_rus_caps[y-1][x]
                    elif ch == 4:
                        key = keyboard_rus_caps[y-1][x+1]
        elif 2<=x<=12 and y == 0:
            ch = random.randrange(0,5)
            if a[2]:#caps
                if a[3]:#eng
                    if ch == 0:
                        key = keyboard_eng_caps[y][x+1]
                    elif ch == 1:
                        key = keyboard_eng_caps[y][x-1]
                    elif ch == 2:
                        key = keyboard_eng_caps[y+1][x-1]
                    elif ch == 3:
                        key = keyboard_eng_caps[y+1][x+1]
                    elif ch == 4:
                        key = keyboard_eng_caps[y+1][x]
                else:#rus
                    if ch == 0:
                        key = keyboard_rus_caps[y][x+1]
                    elif ch == 1:
                        key = keyboard_rus_caps[y][x-1]
                    elif ch == 2:
                        key = keyboard_rus_caps[y+1][x-1]
                    elif ch == 3:
                        key = keyboard_rus_caps[y+1][x+1]
                    elif ch == 4:
                        key = keyboard_rus_caps[y+1][x]   
            else:
                if a[3]:
                    if ch == 0:
                        key = C
                    elif ch == 1:
                        key = keyboard_eng[y][x-1]
                    elif ch == 2:
                        key = keyboard_eng[y+1][x-1]
                    elif ch == 3:
                        key = keyboard_eng[y+1][x+1]
                    elif ch == 4:
                        key = keyboard_eng[y+1][x]  
                else:
                    if ch == 0:
                        key = keyboard_rus[y][x+1]
                    elif ch == 1:
                        key = keyboard_rus[y][x-1]
                    elif ch == 2:
                        key = keyboard_rus[y+1][x-1]
                    elif ch == 3:
                        key = keyboard_rus[y+1][x+1]
                    elif ch == 4:
                        key = keyboard_rus[y+1][x]                 
        elif x == 12 and y == 2:#\
            ch = random.random()
            if a[2]:#Caps
                if a[3]:#Eng
                    if ch:
                        key = '+'
                    else:
                        key = '}'
                else:
                    if ch:
                        key = '+'
                    else:
                        key = 'Ъ'
            else:
                if a[3]:#Eng
                    if ch:
                        key = '='
                    else:
                        key = ']'
                else:
                    if ch:
                        key = '='
                    else:
                        key = 'ъ'
        elif y == 3 and x == 1:
            ch = random.randint(0,3)
            if a[2]:#Caps
                if a[3]:#Eng
                    if ch == 0:
                        key = keyboard_eng_caps[y-1][x]
                    elif ch == 1:
                        key = keyboard_eng_caps[y-1][x+1]
                    elif ch == 2:
                        key = keyboard_eng_caps[y][x+1]
                else:#Rus
                    if ch == 0:
                        key = keyboard_rus_caps[y-1][x]
                    elif ch == 1:
                        key = keyboard_rus_caps[y-1][x+1]
                    elif ch == 2:
                        key = keyboard_rus_caps[y][x+1]  
            else:
                if a[3]:#Eng
                    if ch == 0:
                        key = keyboard_eng[y-1][x]
                    elif ch == 1:
                        key = keyboard_eng[y-1][x+1]
                    elif ch == 2:
                        key = keyboard_eng[y][x+1]
                else:#Rus
                    if ch == 0:
                        key = keyboard_rus[y-1][x]
                    elif ch == 1:
                        key = keyboard_rus[y-1][x+1]
                    elif ch == 2:
                        key = keyboard_rus[y][x+1]
        elif y==3 and 2 <= x <= 9:
            ch = random.randrange(0,5)
            if a[2]:#caps
                if a[3]:#eng
                    if ch == 0:
                        key = keyboard_eng_caps[y][x+1]
                    elif ch == 1:
                        key = keyboard_eng_caps[y][x-1]
                    elif ch == 2:
                        key = keyboard_eng_caps[y-1][x-1]
                    elif ch == 3:
                        key = keyboard_eng_caps[y-1][x+1]
                    elif ch == 4:
                        key = keyboard_eng_caps[y-1][x]
                else:#rus
                    if ch == 0:
                        key = keyboard_rus_caps[y][x+1]
                    elif ch == 1:
                        key = keyboard_rus_caps[y][x-1]
                    elif ch == 2:
                        key = keyboard_rus_caps[y-1][x-1]
                    elif ch == 3:
                        key = keyboard_rus_caps[y-1][x+1]
                    elif ch == 4:
                        key = keyboard_rus_caps[y-1][x]   
            else:
                if a[3]:
                    if ch == 0:
                        key = C
                    elif ch == 1:
                        key = keyboard_eng[y][x-1]
                    elif ch == 2:
                        key = keyboard_eng[y-1][x-1]
                    elif ch == 3:
                        key = keyboard_eng[y-1][x+1]
                    elif ch == 4:
                        key = keyboard_eng[y-1][x]  
                else:
                    if ch == 0:
                        key = keyboard_rus[y][x+1]
                    elif ch == 1:
                        key = keyboard_rus[y][x-1]
                    elif ch == 2:
                        key = keyboard_rus[y-1][x-1]
                    elif ch == 3:
                        key = keyboard_rus[y-1][x+1]
                    elif ch == 4:
                        key = keyboard_rus[y-1][x]  
        elif x == 10 and y == 3:#/
            ch = random.randint(0,3)
            if a[2]:
                if a[3]:
                    if ch == 0:
                        key = keyboard_eng_caps[y-1][x]
                    elif ch == 1:
                        key = keyboard_eng_caps[y-1][x-1]
                    elif ch == 2:       
                        key = keyboard_eng_caps[y][x-1]
                else:
                    if ch == 0:
                        key = keyboard_rus_caps[y-1][x]
                    elif ch == 1:
                        key = keyboard_rus_caps[y-1][x-1]
                    elif ch == 2:       
                        key = keyboard_rus_caps[y][x-1]
            else:
                if a[3]:
                    if ch == 0:
                        key = keyboard_eng[y-1][x]
                    elif ch == 1:
                        key = keyboard_eng[y-1][x-1]
                    elif ch == 2:       
                        key = keyboard_eng[y][x-1]
                else:
                    if ch == 0:
                        key = keyboard_rus[y-1][x]
                    elif ch == 1:
                        key = keyboard_rus[y-1][x-1]
                    elif ch == 2:       
                        key = keyboard_rus[y][x-1]      
    return key'''
def switch_to_neigh(key, chance):#Версия без кодирования соседей путём загрузки в массив
    if random.random() <= chance:
        key_lang = get_language(key)
        if key_lang == 2:
            key_lang = 0
        a = get_key_pos(key, key_lang)#a == [x y caps eng]
        #ch = random.randrange(0,8)
        #if a[][] 
        #if y not in [1, 4] and x 
        x = a[0]
        y= a[1]                
        '''if x == 12 and y == 2:#\
            ch = random.random()
            if a[2]:#Caps
                if a[3]:#Eng
                    if ch:
                        key = '+'
                    else:
                        key = '}'
                else:
                    if ch:
                        key = '+'
                    else:
                        key = 'Ъ'
            else:
                if a[3]:#Eng
                    if ch:
                        key = '='
                    else:
                        key = ']'
                else:
                    if ch:
                        key = '='
                    else:
                        key = 'ъ'  '''
        if key == '`' or key == 'ё':
            key = '1'
        elif key == '~' or key == 'Ё':
            key = '!'
        elif key == '1':
            ch = random.randrange(0, 9)
            if ch == 0:
                key = '`'
            elif ch == 1:
                key = '2'
            elif ch == 2:
                key = 'q'
            elif ch == 3:
                key = 'w'
            elif ch == 4:
                key = '    '
            elif ch == 5:
                key = 'ё'
            elif ch == 6:
                key = 'й'
            elif ch == 7:
                key = 'ц'
        elif key == '!':
            ch = random.randrange(0, 9)
            if ch == 0:
                key = '~'
            elif ch == 1:
                key = '@'
            elif ch == 2:
                key = 'q'
            elif ch == 3:
                key = 'w'
            elif ch == 4:
                key = '    '
            elif ch == 5:
                key = 'Ё'
            elif ch == 6:
                key = 'Й'
            elif ch == 7:
                key = 'Ц'    
            elif ch == 8:
                key = '"'  
        elif key == '2':
            ch = random.randrange(0, 8)
            if ch == 0:
                key = '1'
            elif ch == 1:
                key = 'q'
            elif ch == 2:
                key = 'w'
            elif ch == 3:
                key = 'e'
            elif ch == 4:
                key = '3'
            elif ch == 5:
                key = 'й'
            elif ch == 6:
                key = 'ц'
            elif ch == 7:
                key = 'у'    
        elif key == '@':
            ch = random.randrange(0, 5)
            if ch == 0:
                key = '!'
            elif ch == 1:
                key = 'Q'
            elif ch == 2:
                key = 'W'
            elif ch == 3:
                key = 'E'
            elif ch == 4:
                key = '#'
        elif key == '"':
            ch = random.randrange(0, 5)
            if ch == 0:
                key = '!'
            elif ch == 1:
                key = '№'
            elif ch == 2:
                key = 'У'
            elif ch == 3:
                key = 'Ц'
            elif ch == 4:
                key = 'Й'
            elif ch == 5:
                key = '?'
            elif ch == 6:
                key = ':'
            elif ch == 4:
                key = 'P'
            elif ch == 5:
                key = '{'
            elif ch == 6:
                key = '}'
            elif ch == 7:
                key = ' '#ОБРАТИ ВНИМАНИЕ, НЕДОРАБОТКА!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! тут типа энтер должон быть                
        elif key == '#':
            ch = random.randrange(0, 5)
            if ch == 0:
                key = '@'
            elif ch == 1:
                key = 'W'
            elif ch == 2:
                key = 'E'
            elif ch == 3:
                key = 'R'
            elif ch == 4:
                key = '$'   
        elif key == '3':
            ch = random.randrange(0, 8)
            if ch == 0:
                key = '2'
            elif ch == 1:
                key = 'w'
            elif ch == 2:
                key = 'e'
            elif ch == 3:
                key = 'r'
            elif ch == 4:
                key = '4'
            elif ch == 5:
                key = 'ц'
            elif ch == 6:
                key = 'у'
            elif ch == 7:
                key = 'к'   
        elif key == '№':
            ch = random.randrange(0, 5)
            if ch == 0:
                key = '"'
            elif ch == 1:
                key = 'Ц'
            elif ch == 2:
                key = 'У'
            elif ch == 3:
                key = 'К'
            elif ch == 4:
                key = ';'  
        elif key == ';':
            ch = random.randrange(0, 5)
            if ch == 0:
                key = '№'
            elif ch == 1:
                key = 'У'
            elif ch == 2:
                key = 'К'
            elif ch == 3:
                key = 'Е'
            elif ch == 4:
                key = '%'
            elif ch == 5:
                key = 'o'
            elif ch == 6:
                key = 'l'
            elif ch == 7:
                key = '.'
            elif ch == 8:
                key = '/'
            elif ch == 9:
                key = "'"
            elif ch == 10:
                key = '['
            elif ch == 11:
                key = 'p'
        elif key == '$':
            ch = random.randrange(0, 5)
            if ch == 0:
                key = '#'
            elif ch == 1:
                key = 'E'
            elif ch == 2:
                key = 'R'
            elif ch == 3:
                key = 'T'
            elif ch == 4:
                key = '%'  
        elif key == '4':
            ch = random.randrange(0, 8)
            if ch == 0:
                key = '3'
            elif ch == 1:
                key = 'e'
            elif ch == 2:
                key = 'r'
            elif ch == 3:
                key = 't'
            elif ch == 4:
                key = '5'
            elif ch == 5:
                key = 'у'
            elif ch == 6:
                key = 'к'
            elif ch == 7:
                key = 'е'   
        elif key == '5':
            ch = random.randrange(0, 8)
            if ch == 0:
                key = '4'
            elif ch == 1:
                key = 'r'
            elif ch == 2:
                key = 't'
            elif ch == 3:
                key = 'y'
            elif ch == 4:
                key = '6'
            elif ch == 5:
                key = 'к'
            elif ch == 6:
                key = 'е'
            elif ch == 7:
                key = 'н' 
  
        elif key == '%':
            ch = random.randrange(0, 8)
            if ch == 0:
                key = '$'
            elif ch == 1:
                key = ';'
            elif ch == 2:
                key = 'R'
            elif ch == 3:
                key = 'T'
            elif ch == 4:
                key = 'Y'
            elif ch == 5:
                key = '^'
            elif ch == 6:
                key = 'К'
            elif ch == 6:
                key = 'Е'
            elif ch == 6:
                key = 'Н'
            elif ch == 7:
                key = ':'  
        elif key == '6':
            ch = random.randrange(0, 8)
            if ch == 0:
                key = '5'
            elif ch == 1:
                key = 't'
            elif ch == 2:
                key = 'y'
            elif ch == 3:
                key = 'u'
            elif ch == 4:
                key = '7'
            elif ch == 5:
                key = 'е'
            elif ch == 6:
                key = 'н'
            elif ch == 7:
                key = 'г'   
        elif key == '^':
            ch = random.randrange(0, 5)
            if ch == 0:
                key = '%'
            elif ch == 1:
                key = 'T'
            elif ch == 2:
                key = 'Y'
            elif ch == 3:
                key = 'U'
            elif ch == 4:
                key = '&'   
        elif key == ':':
            ch = random.randrange(0, 11)
            if ch == 0:
                key = '%'
            elif ch == 1:
                key = 'Е'
            elif ch == 2:
                key = 'Н'
            elif ch == 3:
                key = 'Г'
            elif ch == 4:
                key = '?'
            elif ch == 5:
                key = 'O'
            elif ch == 6:
                key = 'L'
            elif ch == 7:
                key = '>'
            elif ch == 8:
                key = '"'
            elif ch == 9:
                key = '{'
            elif ch == 10:
                key = 'P'
        elif key == '7':
            ch = random.randrange(0, 8)
            if ch == 0:
                key = '6'
            elif ch == 1:
                key = 'y'
            elif ch == 2:
                key = 'u'
            elif ch == 3:
                key = 'i'
            elif ch == 4:
                key = '8'
            elif ch == 5:
                key = 'н'
            elif ch == 6:
                key = 'г'
            elif ch == 7:
                key = 'ш'    
        elif key == '&':
            ch = random.randrange(0, 5)
            if ch == 0:
                key = '^'
            elif ch == 1:
                key = 'Y'
            elif ch == 2:
                key = 'U'
            elif ch == 3:
                key = 'I'
            elif ch == 4:
                key = '*' 
  
        elif key == '?':
            ch = random.randrange(0, 8)
            if ch == 0:
                key = ':'
            elif ch == 1:
                key = 'Н'
            elif ch == 2:
                key = 'Г'
            elif ch == 3:
                key = 'Ш'
            elif ch == 4:
                key = '*'
            elif ch == 5:
                key = '>'
            elif ch == 6:
                key = ':'
            elif ch == 7:
                key = '"'    
        elif key == '8':
            ch = random.randrange(0, 8)
            if ch == 0:
                key = '7'
            elif ch == 1:
                key = 'u'
            elif ch == 2:
                key = 'i'
            elif ch == 3:
                key = 'o'
            elif ch == 4:
                key = '9'
            elif ch == 5:
                key = 'г'
            elif ch == 6:
                key = 'ш'
            elif ch == 7:
                key = 'щ'   
        elif key == '*':
            ch = random.randrange(0, 9)
            if ch == 0:
                key = '?'
            elif ch == 1:
                key = 'Г'
            elif ch == 2:
                key = 'Ш'
            elif ch == 3:
                key = 'Щ'
            elif ch == 4:
                key = '('
            elif ch == 5:
                key = 'I'
            elif ch == 6:
                key = 'U'
            elif ch == 7:
                key = 'Y'
            elif ch == 8:
                key = '&'
        elif key == '9':
            ch = random.randrange(0, 8)
            if ch == 0:
                key = '8'
            elif ch == 1:
                key = 'i'
            elif ch == 2:
                key = 'o'
            elif ch == 3:
                key = 'p'
            elif ch == 4:
                key = '0'
            elif ch == 5:
                key = 'ш'
            elif ch == 6:
                key = 'щ'
            elif ch == 7:
                key = 'з'
        elif key == '(':
            ch = random.randrange(0, 8)
            if ch == 0:
                key = '*'
            elif ch == 1:
                key = ')'
            elif ch == 2:
                key = 'I'
            elif ch == 3:
                key = 'O'
            elif ch == 4:
                key = 'Ш'
            elif ch == 5:
                key = 'Щ' 
            elif ch == 6:
                key = 'З' 
            elif ch == 7:
                key = 'P'            
        elif key == '0':
            ch = random.randrange(0, 8)
            if ch == 0:
                key = '9'
            elif ch == 1:
                key = 'щ'
            elif ch == 2:
                key = 'з'
            elif ch == 3:
                key = 'х'
            elif ch == 4:
                key = '-'
            elif ch == 5:
                key = '['
            elif ch == 6:
                key = 'p'
            elif ch == 7:
                key = 'o'    
        elif key == ')':
            ch = random.randrange(0, 8)
            if ch == 0:
                key = '('
            elif ch == 1:
                key = 'O'
            elif ch == 2:
                key = 'P'
            elif ch == 3:
                key = '{'
            elif ch == 4:
                key = '_'
            elif ch == 5:
                key = 'Щ'
            elif ch == 6:
                key = 'З'
            elif ch == 7:
                key = 'Х' 
  
        elif key == '-':
            ch = random.randrange(0, 8)
            if ch == 0:
                key = '0'
            elif ch == 1:
                key = 'p'
            elif ch == 2:
                key = '['
            elif ch == 3:
                key = ']'
            elif ch == 4:
                key = '='
            elif ch == 5:
                key = 'щ'
            elif ch == 6:
                key = 'з'
            elif ch == 7:
                key = 'х'    
        elif key == '_':
            ch = random.randrange(0, 8)
            if ch == 0:
                key = ')'
            elif ch == 1:
                key = 'P'
            elif ch == 2:
                key = '}'
            elif ch == 3:
                key = '{'
            elif ch == 4:
                key = '+'
            elif ch == 5:
                key = 'Щ'
            elif ch == 6:
                key = 'З'
            elif ch == 7:
                key = 'Х'   
        elif key == '=':
            ch = random.randrange(0, 7)
            if ch == 0:
                key = '-'
            elif ch == 1:
                key = '['
            elif ch == 2:
                key = ']'
            elif ch == 3:
                key = 'delnext'
            elif ch == 4:
                key = chr(92) 
            elif ch == 5:
                key = 'х'
            elif ch == 6:
                key = 'ъ'
        elif key == '+':
            ch = random.randrange(0, 7)
            if ch == 0:
                key = '_'
            elif ch == 1:
                key = '{'
            elif ch == 2:
                key = '}'
            elif ch == 3:
                key = '|'
            elif ch == 4:
                key = 'delnext'#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            elif ch == 5:
                key = 'Х'
            elif ch == 6:
                key = 'Ъ'  
        elif ord(key) == 92:
            ch = random.randrange(0, 5)
            if ch == 0:
                key = '='
            elif ch == 1:
                key = ']'
            elif ch == 2:
                key = 'delprev'#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            elif ch == 3:
                key = ' '
            elif ch == 4:
                key = ' '
            elif ch == 5:
                key = 'х' 
            elif ch == 6:
                key = 'ъ'                 
        elif key == '|':
            ch = random.randrange(0, 8)
            if ch == 0:
                key = '}'
            elif ch == 1:
                key = '{'
            elif ch == 2:
                key = 'delprev'
            elif ch == 3:
                key = ' '
            elif ch == 4:
                key = '_'  
        elif key == '/':
            ch = random.randrange(0, 7)
            if ch == 0:
                key = '='
            elif ch == 1:
                key = 'ъ'
            elif ch == 2:
                key = '.'
            elif ch == 3:
                key = ';'
            elif ch == 4:
                key = "'"
            elif ch == 5:
                key = ' '
            elif ch == 6:
                key = 'delprev'   
        elif key == 'Q':
            ch = random.randrange(0, 8)
            if ch == 0:
                key = '~'
            elif ch == 1:
                key = '!'
            elif ch == 2:
                key = '@'
            elif ch == 3:
                key = 'W'
            elif ch == 4:
                key = 'S'
            elif ch == 5:
                key = 'A'
            elif ch == 6:
                key = 'caps'
            elif ch == 7:
                key = '    '   
        elif key == 'q':
            ch = random.randrange(0, 8)
            if ch == 0:
                key = '`'
            elif ch == 1:
                key = '1'
            elif ch == 2:
                key = '2'
            elif ch == 3:
                key = 'w'
            elif ch == 4:
                key = 's'
            elif ch == 5:
                key = 'a'
            elif ch == 6:
                key = 'caps'
            elif ch == 7:
                key = '    '    
        elif key == 'Й':
            ch = random.randrange(0, 8)
            if ch == 0:
                key = 'Ё'
            elif ch == 1:
                key = '!'
            elif ch == 2:
                key = '"'
            elif ch == 3:
                key = 'Ц'
            elif ch == 4:
                key = 'Ы'
            elif ch == 5:
                key = 'Ф'
            elif ch == 6:
                key = 'caps'
            elif ch == 7:
                key = '    '   
        elif key == 'й':
            ch = random.randrange(0, 8)
            if ch == 0:
                key = 'ё'
            elif ch == 1:
                key = '1'
            elif ch == 2:
                key = '2'
            elif ch == 3:
                key = 'ц'
            elif ch == 4:
                key = 'ы'
            elif ch == 5:
                key = 'ф'
            elif ch == 6:
                key = 'caps'
            elif ch == 7:
                key = '    '    
        elif key == 'w':
            ch = random.randrange(0, 8)
            if ch == 0:
                key = 's'
            elif ch == 1:
                key = 'a'
            elif ch == 2:
                key = 'q'
            elif ch == 3:
                key = '1'
            elif ch == 4:
                key = '2'
            elif ch == 5:
                key = '3'
            elif ch == 6:
                key = 'e'
            elif ch == 7:
                key = 'd'   
        elif key == 'W':
            ch = random.randrange(0, 8)
            if ch == 0:
                key = 'E'
            elif ch == 1:
                key = 'D'
            elif ch == 2:
                key = 'S'
            elif ch == 3:
                key = 'A'
            elif ch == 4:
                key = 'Q'
            elif ch == 5:
                key = '!'
            elif ch == 6:
                key = '@'
            elif ch == 7:
                key = '#'    
        elif key == 'ц':
            ch = random.randrange(0, 8)
            if ch == 0:
                key = 'ы'
            elif ch == 1:
                key = 'ф'
            elif ch == 2:
                key = 'й'
            elif ch == 3:
                key = '1'
            elif ch == 4:
                key = '2'
            elif ch == 5:
                key = '3'
            elif ch == 6:
                key = 'у'
            elif ch == 7:
                key = 'в'   
        elif key == 'Ц':
            ch = random.randrange(0, 8)
            if ch == 0:
                key = 'У'
            elif ch == 1:
                key = 'В'
            elif ch == 2:
                key = 'Ы'
            elif ch == 3:
                key = 'Ф'
            elif ch == 4:
                key = 'Й'
            elif ch == 5:
                key = '!'
            elif ch == 6:
                key = '"'
            elif ch == 7:
                key = '№'    
        elif key == 'e':
            ch = random.randrange(0, 8)
            if ch == 0:
                key = 'r'
            elif ch == 1:
                key = 'f'
            elif ch == 2:
                key = 'd'
            elif ch == 3:
                key = 's'
            elif ch == 4:
                key = 'w'
            elif ch == 5:
                key = '2'
            elif ch == 6:
                key = '3'
            elif ch == 7:
                key = '4'   
        elif key == 'E':
            ch = random.randrange(0, 8)
            if ch == 0:
                key = 'R'
            elif ch == 1:
                key = 'F'
            elif ch == 2:
                key = 'D'
            elif ch == 3:
                key = 'S'
            elif ch == 4:
                key = 'W'
            elif ch == 5:
                key = '@'
            elif ch == 6:
                key = '#'
            elif ch == 7:
                key = '$'    
        elif key == 'У':
            ch = random.randrange(0, 8)
            if ch == 0:
                key = 'К'
            elif ch == 1:
                key = 'А'
            elif ch == 2:
                key = 'В'
            elif ch == 3:
                key = 'Ы'
            elif ch == 4:
                key = 'Ц'
            elif ch == 5:
                key = '"'
            elif ch == 6:
                key = '№'
            elif ch == 7:
                key = ';'   
        elif key == 'у':
            ch = random.randrange(0, 8)
            if ch == 0:
                key = 'к'
            elif ch == 1:
                key = 'а'
            elif ch == 2:
                key = 'в'
            elif ch == 3:
                key = 'ы'
            elif ch == 4:
                key = 'ц'
            elif ch == 5:
                key = '2'
            elif ch == 6:
                key = '3'
            else:
                key = '4'    
        elif key == 'r':
            kpyr = ['3', 'e', 'd', 'f', 'g', 't', '5', '4']
            key = kpyr[random.randrange(0, len(kpyr))]  
        elif key == 'R':
            kpyr = ['E', 'D', 'F', 'G', 'T', '%', '$', '#']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'к':
            kpyr = ['3', 'у', 'в', 'а', 'п', 'е', '6', '5']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'К':
            kpyr = ['У', 'В', 'А', 'П', 'Е', '№', ';', '%']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'е':
            kpyr = ['к', 'а', 'п', 'р', 'н', '4', '5', '6']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'Е':
            kpyr = ['К', 'А', 'П', 'Р', 'Н', ';', '%', ':']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 't':
            kpyr = ['r', 'f', 'g', 'h', 'y', '4', '5', '6']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'T':
            kpyr = ['R', 'F', 'G', 'H', 'Y', '$', '%', '^']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'y':
            kpyr = ['t', 'g', 'h', 'j', 'u', '5', '6', '7']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'Y':
            kpyr = ['T', 'G', 'H', 'J', 'U', '%', '^', '&']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'н':
            kpyr = ['е', 'п', 'р', 'о', 'г', '5', '6', '7']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'Н':
            kpyr = ['Е', 'П', 'Р', 'О', 'Г', '%', ':', '?']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'u':
            kpyr = ['y', 'h', 'j', 'k', 'i', '6', '7', '8']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'U':
            kpyr = ['Y', 'H', 'J', 'K', 'I', '^', '&', '*']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'г':
            kpyr = ['н', 'р', 'о', 'л', 'ш', '6', '7', '8']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'Г':
            kpyr = ['Н', 'Р', 'О', 'Л', 'Ш', '^', '&', '*']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'i':
            kpyr = ['u', 'j', 'k', 'l', 'o', '7', '8', '9']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'I':
            kpyr = ['U', 'J', 'K', 'L', 'O', '&', '*', '(']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'ш':
            kpyr = ['г', 'о', 'л', 'д', 'щ', '7', '8', '9']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'Ш':
            kpyr = ['Г', 'О', 'Л', 'Д', 'Щ', '&', '*', '(']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'o':
            kpyr = ['i', 'k', 'l', ';', 'p', '8', '9', '0']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'O':
            kpyr = ['I', 'K', 'L', ':', 'P', '*', '(', ')']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'щ':
            kpyr = ['ш', 'л', 'д', 'ж', 'з', '8', '9', '0']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'Щ':
            kpyr = ['Ш', 'Л', 'Д', 'Ж', 'З', '*', '(', ')']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'З':
            kpyr = ['Щ', 'Д', 'Ж', 'Э', 'Х', '_', ')', '(']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'з':
            kpyr = ['щ', 'д', 'ж', 'э', 'х', '0', '9', '8']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'P':
            kpyr = ['O', 'L', ':', '"', '{', '_', ')', '(']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'p':
            kpyr = ['o', 'l', ';', "'", '[', '-', '0', '9']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == '{':
            kpyr = ['P', ':', '"', '}', '+', '_', ')']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == '[':
            kpyr = ['p', ';', ']', '=', '-', '0', "'"]
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'х':
            kpyr = ['0', 'з', 'ж', 'э', 'ъ', '=', '-']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'Х':
            kpyr = [')', '_', '+', 'Ъ', 'Э', 'Ж', 'З']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == ']':
            kpyr = ['[', "'", '=', chr(92), 'delprev', ' ', ' ']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == '}':
            kpyr = ['"', '{', '_', '+', '|', 'delprev', ' ', ' ']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'ъ':
            kpyr = ['э', 'х', '-', '=', chr(92), 'delprev', ' ', ' ']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'Ъ':
            kpyr = ['Э', 'Х', '_', '+', '/', 'delprev', ' ', ' ']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'a':
            kpyr = ['q', 'w', 's', 'x', 'z', 'caps', '    ', '']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'A':
            kpyr = ['Q', 'W', 'S', 'X', 'Z', 'caps', '    ', '']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'Ф':
            kpyr = ['Й', 'Ц', 'Ы', 'Ч', 'Я', 'caps', '    ', '']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'ф':
            kpyr = ['й', 'ц', 'ы', 'ч', 'я', 'caps', '    ', '']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'ы':
            kpyr = ['й', 'ц', 'у', 'в', 'с', 'ч', 'я', 'ф']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'Ы':
            kpyr = ['Й', 'Ц', 'У', 'В', 'С', 'Ч', 'Я', 'Ф']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'd':
            kpyr = ['s', 'w', 'e', 'r', 'f', 'c', 'x', 'v']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'D':
            kpyr = ['S', 'W', 'E', 'R', 'F', 'V', 'C', 'X']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'в':
            kpyr = ['ц', 'у', 'к', 'а', 'м', 'с', 'ч', 'ы']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'В':
            kpyr = ['Ц', 'У', 'К', 'А', 'М', 'С', 'Ч', 'Ы']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'А':
            kpyr = ['В', 'У', 'К', 'Е', 'П', 'И', 'М', 'С']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'а':
            kpyr = ['в', 'у', 'к', 'е', 'п', 'и', 'м', 'с']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'f':
            kpyr = ['d', 'e', 'r', 't', 'g', 'b', 'v', 'c']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'F':
            kpyr = ['D', 'E', 'R', 'T', 'G', 'B', 'V', 'C']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'g':
            kpyr = ['v', 'f', 'r', 't', 'y', 'h', 'n', 'b']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'G':
            kpyr = ['V', 'F', 'R', 'T', 'Y', 'H', 'N', 'B']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'п':
            kpyr = ['м', 'а', 'к', 'е', 'н', 'р', 'т', 'и']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'П':
            kpyr = ['А', 'М', 'К', 'Е', 'Н', 'Р', 'Т', 'И']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'h':
            kpyr = ['g', 't', 'y', 'u', 'j', 'n', 'b', 'm']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'H':
            kpyr = ['B', 'G', 'T', 'Y', 'U', 'J', 'M', 'N']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'р':
            kpyr = ['и', 'п', 'е', 'н', 'г', 'о', 'ь', 'т']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'Р':
            kpyr = ['И', 'П', 'Е', 'Н', 'Г', 'О', 'Ь', 'Т']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'о':
            kpyr = ['т', 'р', 'н', 'г', 'ш', 'л', 'б', 'ь']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'О':
            kpyr = ['Т', 'Р', 'Н', 'Г', 'Ш', 'Л', 'Б', 'Ь']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'J':
            kpyr = ['N', 'H', 'Y', 'U', 'I', 'K', '<', 'M']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'j':
            kpyr = ['n', 'h', 'y', 'u', 'i', 'k', ',', 'm']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'k':
            kpyr = ['m', 'j', 'u', 'i', 'o', 'l', '.', ',']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'K':
            kpyr = ['m', 'j', 'u', 'i', 'o', 'l', '>', '<']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'л':
            kpyr = ['ь', 'о', 'г', 'ш', 'щ', 'д', 'ю', 'б']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'Л':
            kpyr = ['Ь', 'О', 'Г', 'Ш', 'Щ', 'Д', 'Ю', 'Б']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'Д':
            kpyr = ['Б', 'Л', 'Ш', 'Щ', 'З', 'Ж', ',', 'Ю']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'д':
            kpyr = ['б', 'л', 'ш', 'щ', 'з', 'ж', '.', 'ю']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'l':
            kpyr = [',', 'k', 'i', 'o', 'p', ';', '/', '.']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'L':
            kpyr = ['K', 'I', 'O', 'P', '<', '>', ':', '?']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'ж':
            kpyr = ['ю', 'д', 'щ', 'з', 'х', 'э', '.', '']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'Ж':
            kpyr = [',', 'Ю', 'Д', 'Щ', 'З', 'Х', 'Э', '']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'э':
            kpyr = ['.', 'ж', 'з', 'х', 'ъ', ' ', '', '']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'Э':
            kpyr = [',', 'Ж', 'З', 'Х', 'Ъ', ' ', ' ', '']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == "'":
            kpyr = ['/', ';', 'p', '[', ']', ' ', ' ', '']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'Z':
            kpyr = ['A', 'S', 'X', 'caps', ' ', '', '', '']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == "z":
            kpyr = ['a', 's', 'x', 'caps', ' ', '', '', '']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'Я':
            kpyr = ['Ф', 'Ы', 'Ч', 'caps', ' ', '', '', '']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'я':
            kpyr = ['ф', 'ы', 'ч', 'caps', ' ', '', '', '']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'x':
            kpyr = ['z', 'a', 's', 'd', 'c', ' ', ' ', '']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'X':
            kpyr = ['Z', 'A', 'S', 'D', 'C', ' ', ' ', '']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'ч':
            kpyr = ['я', 'ф', 'ы', 'в', 'с', ' ', ' ', '']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'Ч':
            kpyr = ['Я', 'Ф', 'Ы', 'В', 'С', ' ', ' ', '']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'С':
            kpyr = ['Ч', 'Ы', 'В', 'А', 'М', ' ', ' ', ' ']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'с':
            kpyr = ['с', 'в', 'а', 'м', 'ч', ' ', ' ', ' ']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'C':#eng
            kpyr = ['X', 'S', 'D', 'F', 'V', ' ', ' ', ' ']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'c':#eng
            kpyr = ['x', 's', 'd', 'f', 'v', ' ', ' ', ' ']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'V':
            kpyr = ['C', 'D', 'F', 'G', 'B', ' ', ' ', ' ']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'v':
            kpyr = ['c', 'd', 'f', 'g', 'b', ' ', ' ', ' ']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'м':
            kpyr = ['с', 'в', 'а', 'п', 'и', ' ', ' ', ' ']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'М':
            kpyr = ['С', 'В', 'А', 'П', 'И', ' ', ' ', ' ']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'и':
            kpyr = ['м', 'а', 'п', 'р', 'т', ' ', ' ', ' ']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'И':
            kpyr = ['М', 'А', 'П', 'Р', 'Т', ' ', ' ', ' ']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'B':
            kpyr = ['V', 'F', 'G', 'H', 'N', ' ', ' ', ' ']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'b':
            kpyr = ['v', 'f', 'g', 'h', 'n', ' ', ' ', ' ']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'т':
            kpyr = ['и', 'п', 'р', 'о', 'ь', ' ', ' ', ' ']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'Т':
            kpyr = ['И', 'П', 'Р', 'О', 'Ь', ' ', ' ', ' ']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'N':
            kpyr = ['B', 'G', 'H', 'J', 'M', ' ', ' ', ' ']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'n':
            kpyr = ['b', 'g', 'h', 'j', 'm', ' ', ' ', ' ']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'M':
            kpyr = ['N', 'H', 'J', 'K', '<', ' ', ' ', '']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'm':
            kpyr = ['n', 'h', 'j', 'k', ',', ' ', ' ', '']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'ь':
            kpyr = ['т', 'р', 'о', 'л', 'б', ' ', ' ', '']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'Ь':
            kpyr = ['Т', 'Р', 'О', 'Л', 'Б', ' ', ' ', '']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'б':
            kpyr = ['ь', 'о', 'л', 'д', 'ю', ' ', '', '']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'Б':
            kpyr = ['Ь', 'О', 'Л', 'Д', 'Ю', ' ', '', '']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == '<':
            kpyr = ['M', 'J', 'K', 'L', '>', ' ', '', '']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == ',':#eng
            kpyr = ['m', 'j', 'k', 'l', '.', ' ', '', '']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == '>':
            kpyr = ['<', 'K', 'L', ':', '?', ' ', '', '']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == '.':#eng
            kpyr = [',', 'k', 'l', ';', '/', ' ', '', '']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'ю':
            kpyr = ['б', 'л', 'д', 'ж', '.', '  ', '', '']
            key = kryg[random.randrange(0, len(kpyr))]
        elif key == 'Ю':
            kpyr = ['Б', 'Л', 'Д', 'Ж', ',', ' ', '', '']
            key = kryg[random.randrange(0, len(kpyr))]
        return key
''' Slova = dict()
    Slova['сложно'] = 'геморно'
    Slova['затратно'] = 'геморно'
    Slova['тяжело'] = 'потно'
    Slova['долго'] = 'потно'
    Slova['что'] = 'чо'
    Slova['что-то'] = 'чо-то'
    Slova['зачем'] = 'нафига'
    Slova['почему'] = 'какого фига'
    Slova['сообщил'] = 'высветил'
    Slova['программа'] = 'штука'
    Slova['отключился'] = 'лёг'
    Slova['компьютер'] = 'комп'
    Slova['мышь'] = 'мыша'
    Slova['плохо'] = 'фигово'
    Slova['тех. поддержка'] = 'саппорты'
    Slova['сейчас'] = 'щас'
    Slova['отказываюсь'] = 'пошёл ты'
    Slova['не буду'] = 'пошёл ты'
    Slova['не хочу'] = 'иди ты'
    Slova['ошибка'] = 'эрор'
    Slova['разработчик'] = 'разраб'
    Slova['разработчики'] = 'разрабы'
    Slova['хорошо'] = 'офигенно'
    Slova['работает'] = 'фурычит'
    Slova['ломается'] = 'сыпется'
    Slova['ломаться'] = 'сыпаться'
    Slova['сломалось'] = 'крякнулось'
    Slova['сломалась'] = 'крякнулась'
    Slova['сломался'] = 'крякнулся'
    Slova['утомило'] = 'задолбало'
    Slova['утомил'] = 'задолбал'
    Slova['утомила'] = 'задолбала'
    Slova['я устал от этого'] = 'задолбало'
    Slova['совсем'] = 'нифига'
    Slova['плохая'] = 'долбанная'
    Slova['не хорошая'] = 'дибильная'
    Slova['ужасная'] = 'грёбанная'
    Slova['точно'] = 'В точку!'
    Slova['верно'] = 'В яблочко!'
    Slova['правильно'] = 'В десяточку!'
    Slova['Нет'] = 'ну че, съел?'
    Slova['всегда'] = 'сегда'
    Slova['не знаю'] = 'хз'
    Slova['может быть'] = 'мб'
    Slova['настоящий'] = 'тру'    
    Slova['натсоящая'] = 'тру'
    Slova['настоящее'] = 'тру'
    Slova['истинный'] = 'тру'
    Slova['истинная'] = 'тру'
    Slova['истинное'] = 'тру'
    Slova['страшно'] = 'крипово'
    Slova['забыть'] = 'развидеть'
    Slova['группа'] = 'паблик'    
    for i in range(len(words)):
        boool = bool(0)
        if not str(words[i]).islower() and not str(words[i]).isalnum():
            slovo_i = str(words[i])
            slovo_i[0].swapcase()
            boool = 1
            words[i] = slovo_i
        if words[i] in Slova:
            words[i] = Slova[words[i]]
        if boool:
            slovo_i = str(words[i])
            slovo_i[0].swapcase()
            words[i] = slovo_i
    return words'''    
print(switch_keyboard_layout_particle(words[], 1), '#')
print(get_caps(words[], 'капс?')
print(is_letter(words[]), 'буква')
print(switch_tsya(words[], 1), 'тся')
print(switch_ei(words[], 1), 'еи')
print(switch_ao(words[], 1), 'ао')
print(switch_dt(words[], 1), 'дт')
print(switch_zs(words[], 1), 'зс')
print(switch_zh_sh(words[], 1), 'жш')
print(switch_vf(words[], 1), 'вф')
print(switch_bp(words[], 1), 'бп')
print(delete('spaces', words[], 1), 'убрать рпобелы')
print(delete('dot', words[], 1), 'убрать точки')
print(delete('comma', words[], 1), 'убрать запятые')
print(toe(words[], 1), 'ёе')
print(switch_keyboard_layout_particle(words[], 1),'раскладка партикл')
print(switch_to_neigh(words[], 1), 'сосед')
print(switch_to_neigh(words[], 1), 'сосед')
print(switch_to_neigh(words[], 1), 'сосед')
print(switch_to_neigh(words[], 1), 'сосед')
print(switch_to_neigh(words[], 1), 'сосед')
print(switch_to_neigh(words[], 1), 'сосед')
print(switch_to_neigh(words[], 1), 'сосед')
print(switch_to_neigh(words[], 1), 'сосед')
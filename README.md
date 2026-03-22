# Лабораторная работа №1
# Шифрование данных методами подстановки, перестановки и многоалфавитными шифрами

## Цель работы:
 
Приобретение навыков шифрования информации с использованием простейших методов шифрования.

## Краткая теория:
 
# Метод подстановки 
Шифр подстановки или замены - наиболее простой вид преобразований, 
заключающийся в замене символов исходного текста на другие символы того же, либо 
другого алфавита по определенному правилу. 

# Метод перестановки 
При шифровании этим методом переставляются не буквы алфавита, а буквы 
открытого текста в пределах группы, называемой таблицей перестановки. Например, 
сообщение разбито на группы знаков, включая пробелы, и в каждой группе буквы 
переставлены в соответствии с правилом.

# Многоалфавитные шифры 
Слабая криптостойкость моноалфавитных подстановок преодолевается с 
применением подстановок многоалфавитных. Для защиты от частотного анализа были 
разработаны многоалфавитные шифры, в которых для шифрования сообщения периодически 
используется несколько различных подстановочных алфавитов.

## Задание

1. Разработать алгоритм и составить программу, позволяющую закодировать любой
текст одним из методов (подстановки, перестановки и многоалфавитными шифрами) и выполнить обратное преобразование. Метод,
которым необходимо зашифровать исходную информацию, выбирается в соответствии с
вариантом.
2. Осуществить вывод на экран или принтер полученной криптограммы.
3. Провести дешифрование данной криптограммы, в результате должен быть
получен исходный текст.
4. Результаты работы оформить в виде отчёта.

## Ход работы

Вариант выбирается произвольно. Выбранный для реализации вариант - ВСЕ!.


### Описание программы

Программа реализована в Python коде и состои из следующих элементов:
 - главное меню;
 - пользовательский ввод;
 - криптографический алгоритм согласно заданию.


### Текст программы

# encoding: utf-8
import math

ALFABET00_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЬЫЭЮЯ '  # l=34
ALFABET00_EN = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ .,!:;?-'
ALFABET01_RU = 'БЮГЫЕЬЗШЙЦЛФНТПРСОУМХКЧИЩЖЪДЭВЯ ФЁ'
ALFABET01_EN = 'VWXYZ .,!:;?-KLMNOPQRSTUABCDEFGHIJ'
ALFABET02_RU = 'СОУМКХЧИЩЖЪДЭВЯАБЮГ ЕЬЗШЙЦЁФНТПРЫЛ'
ALFABET02_EN = 'CDABHIJEFGOPQRKLMNUVW:STZ XY;?-.,!'
ALFABET03_RU = 'ОПМНХЛИЙЖЗДЕВГАБЮЯЫЭЬ ШЩЦЧФКТУРСЪЁ'
ALFABET03_EN = 'Z .XY,!ST:;QR?-NOPLMUVWABCDEFGHIJK'
ALFABET04_RU = 'ЮЯЫЭЬЪШЩЦЧФХТУРСОПМНКЛ ЙЖЗДЕВГАБЁИ'
ALFABET04_EN = 'CDABHIJEFGOPQRKLMNUVW:STZ XY;?-.,!'
ALFABET05_RU = 'МНОПРСТУФХЦЧШЩЪЬЫЭЮЯ АБВГДЕЁЖЗИЙКЛ'
ALFABET05_EN = 'VWXYZ .,!:;?-KLMNOPQRSTUABCDEFGHIJ'

PERMUTATION_KEY01 = [[1, 2, 3, 4, 5, 6], [3, 5, 2, 6, 1, 4]]
PERMUTATION_KEY02 = [[1, 2, 3, 4, 5], [5, 4, 1, 2, 3]]
PERMUTATION_KEY03 = [[1, 2, 3, 4, 5, 6], [2, 5, 3, 4, 1, 6]]
PERMUTATION_KEY04 = [[1, 2, 3, 4, 5, 6], [2, 6, 3, 5, 1, 4]]
PERMUTATION_KEY05 = [[1, 2, 3, 4, 5], [2, 5, 4, 3, 1]]
PERMUTATION_KEY06 = [[1, 2, 3, 4, 5, 6], [3, 5, 2, 6, 1, 4]]

VARIANT01 = [1, 'SUBS', ALFABET00_EN, ALFABET03_EN, 'EN']
VARIANT02 = [2, 'PERMUT', PERMUTATION_KEY01, 'ASCII']
VARIANT03 = [3, 'MULTISUBS', ALFABET00_RU, [ALFABET01_RU, ALFABET02_RU, ALFABET05_RU], 'RU']
VARIANT04 = [4, 'PERMUT', PERMUTATION_KEY02, 'RU']
VARIANT05 = [5, 'SUBS', ALFABET00_EN, ALFABET04_EN, 'EN']
VARIANT06 = [6, 'MULTISUBS', ALFABET00_RU, [ALFABET01_RU, ALFABET03_RU], 'RU']
VARIANT07 = [7, 'SUBS', ALFABET00_EN, ALFABET01_EN, 'EN']
VARIANT08 = [8, 'MULTISUBS', ALFABET00_EN, [ALFABET02_EN, ALFABET05_EN], 'EN']
VARIANT09 = [9, 'PERMUT', PERMUTATION_KEY03, 'ASCII']
VARIANT10 = [10, 'SUBS', ALFABET00_RU, ALFABET02_RU, 'RU']
VARIANT11 = [11, 'PERMUT', PERMUTATION_KEY04, 'ASCII']
VARIANT12 = [12, 'MULTISUBS', ALFABET00_RU, [ALFABET01_RU, ALFABET03_RU, ALFABET04_RU], 'RU']

EXAMPLE_TEXT_RU = 'ОСНОВЫ ЗАЩИТЫ ИНФОРМАЦИИ АБЫРВАЛ'  # l=32
EXAMPLE_TEXT_EN = 'HELLO WORLD!'
EXAMPLE_TEXT_ASCII = '2*x^2 + 3*x + (A-B)/!C >= 4*y^2'  # l=31
ALFABET_ASCII_32_126 = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"


def substitution(text, alfabet0, alfabet1, mode):
    """ Шифр подстановки """
    result = ''
    for char in text:
        if mode == 'encrypt':
            char_index = alfabet0.find(char)
            subs_char = alfabet1[char_index]
        elif mode == 'decrypt':
            char_index = alfabet1.find(char)
            subs_char = alfabet0[char_index]
        else:
            return 'Error'
        result += subs_char

    return result


def multisubstitution(text, alfabet0, alfabets, mode):
    """ Шифр мультиперестановки """
    result = ''
    lenght = len(text)
    qnt = len(alfabets)
    for i, char in zip(range(lenght), text):
        if mode == 'encrypt':
            alfabet_c = alfabets[i % qnt]
            #print(alfabet0)
            char_index = alfabet0.find(char)
            subs_char = alfabet_c[char_index]
        elif mode == 'decrypt':
            alfabet_c = alfabets[i % qnt]
            char_index = alfabet_c.find(char)
            subs_char = alfabet0[char_index]
        else:
            return 'Error'
        result += subs_char

    return result


def permutation(text, key, mode):
    """ Шифр перестановки """
    result = ''
    lenght = len(text)
    step = len(key[1])
    if mode == 'encrypt':
        delta = (step - (lenght % step)) % step
        for start in range(0, lenght, step):
            if (start + step) > lenght:
                s = text[start:start + step] + ' ' * delta
            else:
                s = text[start:start + step]
            result += ''.join([s[i - 1] for i in key[1]])
    elif mode == 'decrypt':
        key_d = []
        for k in key[0]:
            key_d.append(key[1].index(k) + 1)
        for start in range(0, lenght, step):
            if (start + step) > lenght:
                s = text[start:start + step] + ' ' * delta
            else:
                s = text[start:start + step]
            result += ''.join([s[i - 1] for i in key_d])
        result = result.rstrip()
    else:
        print('Error')

    return result


def run_variant(text, variant):
    if variant[1] == 'SUBS':
        alfabet0 = variant[2]
        alfabet1 = variant[3]
        encrypted_subs = substitution(text, alfabet0, alfabet1, mode='encrypt')
        decrypted_subs = substitution(encrypted_subs, alfabet0, alfabet1, mode='decrypt')
        print(f"= Вариант {variant[0]} =")
        print('== ПОДСТАНОВКА ==')
        print('Исходный словарь:', f"'{alfabet0}'")
        print('Подстановочный словарь:', f"'{alfabet1}'")
        print('Текст для зашифрования:', f"'{text}'")
        print('Зашифрованный текст   :', f"'{encrypted_subs}'")
        print('Расшифрованный текст  :', f"'{decrypted_subs}'", '\n')

    if variant[1] == 'MULTISUBS':
        alfabet0 = variant[2]
        alfabets = variant[3]
        encrypted_multisubs = multisubstitution(text, alfabet0, alfabets, 'encrypt')
        decrypted_multisubs = multisubstitution(encrypted_multisubs, alfabet0, alfabets, 'decrypt')
        print(f"= Вариант {variant[0]} =")
        print('== МУЛЬТИПОДСТАНОВКА ==')
        print('Исходный словарь:', f"'{alfabet0}'")
        print('Подстановочные словари:', [f'{alfabet}' for alfabet in alfabets])
        print('Текст для зашифрования:', f"'{text}'")
        print('Зашифрованный текст   :', f"'{encrypted_multisubs}'")
        print('Расшифрованный текст  :', f"'{decrypted_multisubs}'", '\n')

    if variant[1] == 'PERMUT':
        key = variant[2]
        encrypted_permut = permutation(text, key, mode='encrypt')
        decrypted_permut = permutation(encrypted_permut, key, mode='decrypt')
        print(f"= Вариант {variant[0]} =")
        print('== ПЕРЕСТАНОВКА ==')
        print('Группа перестановки:', key)
        print('Текст для зашифрования:', f"'{text}'")
        print('Зашифрованный текст   :', f"'{encrypted_permut}'")
        print('Расшифрованный текст  :', f"'{decrypted_permut}'", '\n')

#----Алгоритмы------

algo_subs_graph = """
   НАЧАЛО
      |
      v
    text = '123'
    alfabet0 = '12345'
    alfabet1 = '23451'
    print('= ENCRYPT =')
    result = ''
      |
      v
  ┌──────────────────────┐
  | ДЛЯ char в text ЦИКЛ:|
  └──────────────────────┘
    char_index = alfabet0.find(char)
    subs_char = alfabet1[char_index]
    result = (result + subs_char)
    assert(result == '234')
      |
      v
    print('= DECRYPT =')
    result = ''
      |
      v
  ┌──────────────────────┐
  | ДЛЯ char в text ЦИКЛ:|
  └──────────────────────┘
    char_index = alfabet0.find(char)
    subs_char = alfabet1[char_index]
    result = (result + subs_char)
    assert(result == '123')
      |
      v
   КОНЕЦ
"""

algo_permut_graph = """
   НАЧАЛО  
      | 
      v
    text = 'АБВГД'
    key = [[1,2,3,4,5],[5,2,4,1,3]]
    lenght = len(text)
    step = len(key[1])
    delta = ((step - (lenght % step)) % step)
    print('= ENCRYPT =')
    delta = ((step - (lenght % step)) % step)
      |
      v
  ┌─────────────────────────────────────────┐
  | ДЛЯ start в range(0, lenght, step) ЦИКЛ:|
  └─────────────────────────────────────────┘
     ЕСЛИ (start + step) > lenght:
       s = (text[start:(start + step):] + (' ' * delta))
        |
     ИНАЧЕ:
       s = text[start:(start + step):]
     result += ''.join([s[i-1] for i in key_d])   
  assert(result == 'ГБДВА')
      |
      v
  print('= DECRYPT =')
  key_d = []
      |
      v
  ┌──────────────────────────┐
  | ДЛЯ k в key[Error2] ЦИКЛ:|
  └──────────────────────────┘
     key_d.append((key[1].index(k) + 1))
      |
      v
  ┌─────────────────────────────────────────┐
  | ДЛЯ start в range(0, lenght, step) ЦИКЛ:|
  └─────────────────────────────────────────┘
      |
      v
    ЕСЛИ (start + step) > lenght:
      s = (text[start:(start + step):] + (' ' * delta))
       |
    ИНАЧЕ:
      s = text[start:(start + step):]
    result += ''.join([s[i-1] for i in key_d])
  result = result.rstrip()
  assert(result == 'АБВГД')
      | 
      v 
   КОНЕЦ
"""

algo_multisubs_graph = """
   НАЧАЛО  
      | 
      v
    text = '1234'
    alfabet0 = '12345'
    alfabets = ['23451','34512']
    lenght = len(text)
    qnt = len(alfabets)
    print('= ENCRYPT =')
    result = ''
      |
      v
  ┌───────────────────────────────────────────────────┐
  | ДЛЯ i, char in zip(range(lenght), text) ЦИКЛ:     |
  └───────────────────────────────────────────────────┘
    alfabet_c = alfabets[i % qnt]
    char_index = alfabet0.find(char)
    subs_char = alfabet_c[char_index]
    result = (result + subs_char)
  assert(result == '2441')
      |
      v
    print('= DECRYPT =')
    result = ''
      |
      v
  ┌───────────────────────────────────────────────────┐
  | ДЛЯ i, char in zip(range(lenght), text) ЦИКЛ:     |
  └───────────────────────────────────────────────────┘
    alfabet_c = alfabets[i % qnt]
    char_index = alfabet_c.find(char)
    subs_char = alfabet_0[char_index]
    result = (result + subs_char)
    assert(result == '1234')
      | 
      v 
   КОНЕЦ
"""

#----Алгоритмы.Окончание------

def algo_graph(type):
    if type == 'subs':
        print('= АЛГОРИТМ ПОДСТАНОВКИ =', end='')
        print(algo_subs_graph)
    elif type == 'multisubs':
        print('= АЛГОРИТМ МУЛЬТИПОДСТАНОВКИ =', end='')
        print(algo_multisubs_graph)
    elif type == 'permut':
        print('= АЛГОРИТМ ПЕРЕСТАНОВКИ =', end='')
        print(algo_permut_graph)


# Меню -----

menu = """
== МЕТОДЫ ШИФРОВАНИЯ ==

 0. Прогон по всем вариантам
 1. Подстановка, алфавит 3 (en), английский язык
 2. Перестановка, ключ 1, ASCII символы
 3. Мультиподстановка, [алфавиты 1, 2, 5] (ru), русский язык
 4. Перестановка, ключ 2, русский язык
 5. Подстановка, алфавит 4 (en), английский язык
 6. Мультиподстановка, [алфавиты 1, 3] (ru), русский язык
 7. Подстановка, алфавит 1 (en), английский язык
 8. Мультиподстановка, [алфавиты 2, 5] (en), английский язык
 9. Перестановка, ключ 3, ASCII символы
10. Подстановка, алфавит 2 (ru), русский язык
11. Перестановка, ключ 4, ASCII символы
12. Мультиподстановка, [алфавиты 1, 3, 4] (ru), русский язык
"""

while True:
    print(menu)
    print('Выберите номер варианта (по умолчанию 0):')
    answer = input()

    if answer == '0':
        print('=== ПРОГОН ПО ВСЕМ ВАРИАНТАМ ШИФРОВАНИЯ!!! ===')
        print()
        run_variant(EXAMPLE_TEXT_EN, VARIANT01)
        run_variant(EXAMPLE_TEXT_ASCII, VARIANT02)
        run_variant(EXAMPLE_TEXT_RU, VARIANT03)
        run_variant(EXAMPLE_TEXT_RU, VARIANT04)
        run_variant(EXAMPLE_TEXT_EN, VARIANT05)
        run_variant(EXAMPLE_TEXT_RU, VARIANT06)
        run_variant(EXAMPLE_TEXT_EN, VARIANT07)
        run_variant(EXAMPLE_TEXT_EN, VARIANT08)
        run_variant(EXAMPLE_TEXT_ASCII, VARIANT09)
        run_variant(EXAMPLE_TEXT_RU, VARIANT10)
        run_variant(EXAMPLE_TEXT_ASCII, VARIANT11)
        run_variant(EXAMPLE_TEXT_RU, VARIANT12)
        algo_graph('subs')
        algo_graph('permut')
        algo_graph('multisubs')
    else:
        print(f"Введите текст, тип которого соответствует выбранному варианту:")
        text = ' '
        text = input()
        print(f"'{text}'", '\n')

    if answer == '1':
        run_variant(text, VARIANT01)
        algo_graph('subs')
    elif answer == '2':
        run_variant(text, VARIANT02)
        print(algo_graph('permut'))
    elif answer == '3':
        run_variant(text, VARIANT03)
        algo_graph('multisubs')
    elif answer == '4':
        run_variant(text, VARIANT04)
        algo_graph('permut')
    elif answer == '5':
        run_variant(text, VARIANT05)
        algo_graph('subs')
    elif answer == '6':
        run_variant(text, VARIANT06)
        algo_graph('multisubs')
    elif answer == '7':
        run_variant(text, VARIANT07)
        algo_graph('subs')
    elif answer == '8':
        run_variant(text, VARIANT08)
        algo_graph('multisubs')
    elif answer == '9':
        run_variant(text, VARIANT09)
        algo_graph('permut')
    elif answer == '10':
        run_variant(text, VARIANT10)
        algo_graph('subs')
    elif answer == '11':
        run_variant(text, VARIANT11)
        algo_graph('permut')
    elif answer == '12':
        run_variant(text, VARIANT12)
        algo_graph('multisubs')
    print('Продолжить (1 или 0)?')
    answer = input()
    if answer == '0':
        break

# Конец меню -----




### Демонстрация работы:

== МЕТОДЫ ШИФРОВАНИЯ ==

 0. Прогон по всем вариантам
 1. Подстановка, алфавит 3 (en), английский язык
 2. Перестановка, ключ 1, ASCII символы
 3. Мультиподстановка, [алфавиты 1, 2, 5] (ru), русский язык
 4. Перестановка, ключ 2, русский язык
 5. Подстановка, алфавит 4 (en), английский язык
 6. Мультиподстановка, [алфавиты 1, 3] (ru), русский язык
 7. Подстановка, алфавит 1 (en), английский язык
 8. Мультиподстановка, [алфавиты 2, 5] (en), английский язык
 9. Перестановка, ключ 3, ASCII символы
10. Подстановка, алфавит 2 (ru), русский язык
11. Перестановка, ключ 4, ASCII символы
12. Мультиподстановка, [алфавиты 1, 3, 4] (ru), русский язык

Выберите номер варианта (по умолчанию 0):
0
=== ПРОГОН ПО ВСЕМ ВАРИАНТАМ ШИФРОВАНИЯ!!! ===

= Вариант 1 =
== ПОДСТАНОВКА ==
Исходный словарь: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ .,!:;?-'
Подстановочный словарь: 'Z .XY,!ST:;QR?-NOPLMUVWABCDEFGHIJK'
Текст для зашифрования: 'HELLO WORLD!'
Зашифрованный текст   : 'SYQQ-DW-PQXG'
Расшифрованный текст  : 'HELLO WORLD!' 

= Вариант 2 =
== ПЕРЕСТАНОВКА ==
Группа перестановки: [[1, 2, 3, 4, 5, 6], [3, 5, 2, 6, 1, 4]]
Текст для зашифрования: '2*x^2 + 3*x + (A-B)/!C >= 4*y^2'
Зашифрованный текст   : 'x2* 2^3x  +*(- B+A! />)C4y ^=*    2 '
Расшифрованный текст  : '2*x^2 + 3*x + (A-B)/!C >= 4*y^2' 

= Вариант 3 =
== МУЛЬТИПОДСТАНОВКА ==
Исходный словарь: 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЬЫЭЮЯ '
Подстановочные словари: ['БЮГЫЕЬЗШЙЦЛФНТПРСОУМХКЧИЩЖЪДЭВЯ ФЁ', 'СОУМКХЧИЩЖЪДЭВЯАБЮГ ЕЬЗШЙЦЁФНТПРЫЛ', 'МНОПРСТУФХЦЧШЩЪЬЫЭЮЯ АБВГДЕЁЖЗИЙКЛ']
Текст для зашифрования: 'ОСНОВЫ ЗАЩИТЫ ИНФОРМАЦИИ АБЫРВАЛ'
Зашифрованный текст   : 'РГЪРУЗЁЩМЪЖЯВЛХПЬЬОВМИЖХЁСНВЮОБЭ'
Расшифрованный текст  : 'ОСНОВЫ ЗАЩИТЫ ИНФОРМАЦИИ АБЫРВАЛ' 

= Вариант 4 =
== ПЕРЕСТАНОВКА ==
Группа перестановки: [[1, 2, 3, 4, 5], [5, 4, 1, 2, 3]]
Текст для зашифрования: 'ОСНОВЫ ЗАЩИТЫ ИНФОРМАЦИИ АБЫРВАЛ'
Зашифрованный текст   : 'ВООСНЩАЫ ЗИ ИТЫМРНФО ИАЦИВРАБЫ  АЛ '
Расшифрованный текст  : 'ОСНОВЫ ЗАЩИТЫ ИНФОРМАЦИИ АБЫРВАЛ' 

= Вариант 5 =
== ПОДСТАНОВКА ==
Исходный словарь: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ .,!:;?-'
Подстановочный словарь: 'CDABHIJEFGOPQRKLMNUVW:STZ XY;?-.,!'
Текст для зашифрования: 'HELLO WORLD!'
Зашифрованный текст   : 'EHPPKXSKNPB?'
Расшифрованный текст  : 'HELLO WORLD!' 

= Вариант 6 =
== МУЛЬТИПОДСТАНОВКА ==
Исходный словарь: 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЬЫЭЮЯ '
Подстановочные словари: ['БЮГЫЕЬЗШЙЦЛФНТПРСОУМХКЧИЩЖЪДЭВЯ ФЁ', 'ОПМНХЛИЙЖЗДЕВГАБЮЯЫЭЬ ШЩЦЧФКТУРСЪЁ']
Текст для зашифрования: 'ОСНОВЫ ЗАЩИТЫ ИНФОРМАЦИИ АБЫРВАЛ'
Зашифрованный текст   : 'РЫПБГУЁЖБФЦЭВЁЦАКБОГБЩЦЗЁОЮУОМБВ'
Расшифрованный текст  : 'ОСНОВЫ ЗАЩИТЫ ИНФОРМАЦИИ АБЫРВАЛ' 

= Вариант 7 =
== ПОДСТАНОВКА ==
Исходный словарь: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ .,!:;?-'
Подстановочный словарь: 'VWXYZ .,!:;?-KLMNOPQRSTUABCDEFGHIJ'
Текст для зашифрования: 'HELLO WORLD!'
Зашифрованный текст   : ',Z??LCTLO?YF'
Расшифрованный текст  : 'HELLO WORLD!' 

= Вариант 8 =
== МУЛЬТИПОДСТАНОВКА ==
Исходный словарь: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ .,!:;?-'
Подстановочные словари: ['CDABHIJEFGOPQRKLMNUVW:STZ XY;?-.,!', 'VWXYZ .,!:;?-KLMNOPQRSTUABCDEFGHIJ']
Текст для зашифрования: 'HELLO WORLD!'
Зашифрованный текст   : 'EZP?KCSLN?BF'
Расшифрованный текст  : 'HELLO WORLD!' 

= Вариант 9 =
== ПЕРЕСТАНОВКА ==
Группа перестановки: [[1, 2, 3, 4, 5, 6], [2, 5, 3, 4, 1, 6]]
Текст для зашифрования: '2*x^2 + 3*x + (A-B)/!C >= 4*y^2'
Зашифрованный текст   : '*2x^2  x3*+  -(A+B/ !C)> y4*=^    2 '
Расшифрованный текст  : '2*x^2 + 3*x + (A-B)/!C >= 4*y^2' 

= Вариант 10 =
== ПОДСТАНОВКА ==
Исходный словарь: 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЬЫЭЮЯ '
Подстановочный словарь: 'СОУМКХЧИЩЖЪДЭВЯАБЮГ ЕЬЗШЙЦЁФНТПРЫЛ'
Текст для зашифрования: 'ОСНОВЫ ЗАЩИТЫ ИНФОРМАЦИИ АБЫРВАЛ'
Зашифрованный текст   : 'АГЯАУТЛЩСЁЖ ТЛЖЯЬАЮВСШЖЖЛСОТЮУСЭ'
Расшифрованный текст  : 'ОСНОВЫ ЗАЩИТЫ ИНФОРМАЦИИ АБЫРВАЛ' 

= Вариант 11 =
== ПЕРЕСТАНОВКА ==
Группа перестановки: [[1, 2, 3, 4, 5, 6], [2, 6, 3, 5, 1, 4]]
Текст для зашифрования: '2*x^2 + 3*x + (A-B)/!C >= 4*y^2'
Зашифрованный текст   : '* x22^  3x+* B(-+A/>! )C ^4y=*    2 '
Расшифрованный текст  : '2*x^2 + 3*x + (A-B)/!C >= 4*y^2' 

= Вариант 12 =
== МУЛЬТИПОДСТАНОВКА ==
Исходный словарь: 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЬЫЭЮЯ '
Подстановочные словари: ['БЮГЫЕЬЗШЙЦЛФНТПРСОУМХКЧИЩЖЪДЭВЯ ФЁ', 'ОПМНХЛИЙЖЗДЕВГАБЮЯЫЭЬ ШЩЦЧФКТУРСЪЁ', 'ЮЯЫЭЬЪШЩЦЧФХТУРСОПМНКЛ ЙЖЗДЕВГАБЁИ']
Текст для зашифрования: 'ОСНОВЫ ЗАЩИТЫ ИНФОРМАЦИИ АБЫРВАЛ'
Зашифрованный текст   : 'РЫРРМГЁЖЮЪЗНВЁЧП СОГЮИЗЧЁОЯВЯЫБВ'
Расшифрованный текст  : 'ОСНОВЫ ЗАЩИТЫ ИНФОРМАЦИИ АБЫРВАЛ' 

= АЛГОРИТМ ПОДСТАНОВКИ =
   НАЧАЛО
      |
      v
    text = '123'
    alfabet0 = '12345'
    alfabet1 = '23451'
    print('= ENCRYPT =')
    result = ''
      |
      v
  ┌──────────────────────┐
  | ДЛЯ char в text ЦИКЛ:|
  └──────────────────────┘
    char_index = alfabet0.find(char)
    subs_char = alfabet1[char_index]
    result = (result + subs_char)
    assert(result == '234')
      |
      v
    print('= DECRYPT =')
    result = ''
      |
      v
  ┌──────────────────────┐
  | ДЛЯ char в text ЦИКЛ:|
  └──────────────────────┘
    char_index = alfabet0.find(char)
    subs_char = alfabet1[char_index]
    result = (result + subs_char)
    assert(result == '123')
      |
      v
   КОНЕЦ

= АЛГОРИТМ ПЕРЕСТАНОВКИ =
   НАЧАЛО  
      | 
      v
    text = 'АБВГД'
    key = [[1,2,3,4,5],[5,2,4,1,3]]
    lenght = len(text)
    step = len(key[1])
    delta = ((step - (lenght % step)) % step)
    print('= ENCRYPT =')
    delta = ((step - (lenght % step)) % step)
      |
      v
  ┌─────────────────────────────────────────┐
  | ДЛЯ start в range(0, lenght, step) ЦИКЛ:|
  └─────────────────────────────────────────┘
     ЕСЛИ (start + step) > lenght:
       s = (text[start:(start + step):] + (' ' * delta))
        |
     ИНАЧЕ:
       s = text[start:(start + step):]
     result += ''.join([s[i-1] for i in key_d])   
  assert(result == 'ГБДВА')
      |
      v
  print('= DECRYPT =')
  key_d = []
      |
      v
  ┌──────────────────────────┐
  | ДЛЯ k в key[Error2] ЦИКЛ:|
  └──────────────────────────┘
     key_d.append((key[1].index(k) + 1))
      |
      v
  ┌─────────────────────────────────────────┐
  | ДЛЯ start в range(0, lenght, step) ЦИКЛ:|
  └─────────────────────────────────────────┘
      |
      v
    ЕСЛИ (start + step) > lenght:
      s = (text[start:(start + step):] + (' ' * delta))
       |
    ИНАЧЕ:
      s = text[start:(start + step):]
    result += ''.join([s[i-1] for i in key_d])
  result = result.rstrip()
  assert(result == 'АБВГД')
      | 
      v 
   КОНЕЦ

= АЛГОРИТМ МУЛЬТИПОДСТАНОВКИ =
   НАЧАЛО  
      | 
      v
    text = '1234'
    alfabet0 = '12345'
    alfabets = ['23451','34512']
    lenght = len(text)
    qnt = len(alfabets)
    print('= ENCRYPT =')
    result = ''
      |
      v
  ┌───────────────────────────────────────────────────┐
  | ДЛЯ i, char in zip(range(lenght), text) ЦИКЛ:     |
  └───────────────────────────────────────────────────┘
    alfabet_c = alfabets[i % qnt]
    char_index = alfabet0.find(char)
    subs_char = alfabet_c[char_index]
    result = (result + subs_char)
  assert(result == '2441')
      |
      v
    print('= DECRYPT =')
    result = ''
      |
      v
  ┌───────────────────────────────────────────────────┐
  | ДЛЯ i, char in zip(range(lenght), text) ЦИКЛ:     |
  └───────────────────────────────────────────────────┘
    alfabet_c = alfabets[i % qnt]
    char_index = alfabet_c.find(char)
    subs_char = alfabet_0[char_index]
    result = (result + subs_char)
    assert(result == '1234')
      | 
      v 
   КОНЕЦ

Продолжить (1 или 0)?

### Анализ результатов работы программы:

Программа корректно реализует требования лабораторной работы.

### Вывод:

В результате работы над заданием лабораторной работы корректно реализовано шифрование строки всеми заданными способами (подстановки, перестановки, мультиподстановки) во всех заданных вариантах. Это помогло лучше изучить предметную область шифрования.

## Контрольные вопросы:

1. В: Почему метод подстановки имеет слабую надёжность?

   О: Потому что он сохраняет статистические особенности языка открытого текста     
      и уязвим перед частотным анализом.

2. В: Что такое частотный анализ?

   О: это метод криптоанализа, используемый для взлома шифров, основанный на
      анализе частоты появления символов, буквосочетаний или слов в зашифрованном тексте.

3. В: Что является криптографическим ключом в методе перестановки?

   О: Криптографическим ключом является порядок перестановки.

4. В: Как связаны метод подстановки и многоалфавитные шифры?

   О: Они оба основаны на замене символов исходного текста на другие символы.

5. В: В чём отличие криптографии от криптоанализа?

   О: Криптография – наука создания криптографических систем с целью обеспечения конфиденциальноыти, и целостности, и доступности информации.
      Криптоанализ – наука раскрытия криптографических систем с целью нарушения конфиденциальности, и (или) целостности, и (или) доступности информации.

6. В: По какому признаку шифры делят на симметричные и асимметричные?

   О: По типу ключа. Симметричные шифры используют один и тот же ключ для
      зашифрования и расшифрования. Асимметричные используют пару ключей.
	  
	  
Замеченные аномалии в методичке:
1. В таблице 1.2 алфавит_2_ru символ 20: не написано слово "пробел"
2. В таблице 1.2 алфавит_3_en символы 16,17,18 и 21,22,23: дублируются. Заменил 21,22,23 NOP -> UVW
3. В таблице 1.2 алфавит_2_en и алфавит_4_en: одинаковые.
4. В таблице 1.2 алфавит_1_en и алфавит_5_en: одинаковые.
5. В таблице 1.3 группы перестановок 1 и 6: одинаковые.

Вопрос:
Анна Васильевны, Вы в первой лекции упоминали, что есть научные исследования каменных плит из Древнего Египта с информацией о Старших Арканах Таро. Можете дать ссылку на эти материалы?

# encoding: utf-8
import math

class Alphabet:
    """Класс для хранения алфавитов"""
    ALPHABET00_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЬЫЭЮЯ '
    ALPHABET00_EN = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ .,!:;?-'
    ALPHABET01_RU = 'БЮГЫЕЬЗШЙЦЛФНТПРСОУМХКЧИЩЖЪДЭВЯ ФЁ'
    ALPHABET01_EN = 'VWXYZ .,!:;?-KLMNOPQRSTUABCDEFGHIJ'
    ALPHABET02_RU = 'СОУМКХЧИЩЖЪДЭВЯАБЮГ ЕЬЗШЙЦЁФНТПРЫЛ'
    ALPHABET02_EN = 'CDABHIJEFGOPQRKLMNUVW:STZ XY;?-.,!'
    ALPHABET03_RU = 'ОПМНХЛИЙЖЗДЕВГАБЮЯЫЭЬ ШЩЦЧФКТУРСЪЁ'
    ALPHABET03_EN = 'Z .XY,!ST:;QR?-NOPLMUVWABCDEFGHIJK'
    ALPHABET04_RU = 'ЮЯЫЭЬЪШЩЦЧФХТУРСОПМНКЛ ЙЖЗДЕВГАБЁИ'
    ALPHABET04_EN = 'CDABHIJEFGOPQRKLMNUVW:STZ XY;?-.,!'
    ALPHABET05_RU = 'МНОПРСТУФХЦЧШЩЪЬЫЭЮЯ АБВГДЕЁЖЗИЙКЛ'
    ALPHABET05_EN = 'VWXYZ .,!:;?-KLMNOPQRSTUABCDEFGHIJ'
    ALPHABET06_ASCII_32_126 = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

    def print_alphabets(self, index=''):
        """Печать всего списка алфавитов или выбранного по индексу"""
        # Собираем все алфавиты в словарь для удобного доступа
        alphabets = {name: value for name, value in vars(Alphabet).items() 
                    if name.startswith('ALPHABET') and isinstance(value, str)}

        if index is not '':
            # Если указан индекс, ищем алфавит с таким индексом
            found = False
            
            for name, alphabet in alphabets.items():
                if name.startswith(f"ALPHABET{index}"):
                    print(f"{name}: {alphabet}")
                    found = True
            if not found:
                print(f"Алфавит с индексом {index} не найден")
        else:
            # Печатаем все алфавиты
            for name, alphabet in sorted(alphabets.items()):
                print(f"{name}: {alphabet}")

class PermutationKey:
    """Класс для хранения ключей перестановки"""
    KEY01 = [[1, 2, 3, 4, 5, 6], [3, 5, 2, 6, 1, 4]]
    KEY02 = [[1, 2, 3, 4, 5], [5, 4, 1, 2, 3]]
    KEY03 = [[1, 2, 3, 4, 5, 6], [2, 5, 3, 4, 1, 6]]
    KEY04 = [[1, 2, 3, 4, 5, 6], [2, 6, 3, 5, 1, 4]]
    KEY05 = [[1, 2, 3, 4, 5], [2, 5, 4, 3, 1]]
    KEY06 = [[1, 2, 3, 4, 5, 6], [3, 5, 2, 6, 1, 4]]


class Cipher:
    """Базовый класс для всех шифров"""
    def __init__(self, name):
        self.name = name
    
    def encrypt(self, text):
        raise NotImplementedError
    
    def decrypt(self, text):
        raise NotImplementedError
        
    def get_algo_graph(self):
        """Возвращает графическое представление алгоритма"""
        raise NotImplementedError


class SubstitutionCipher(Cipher):
    """Шифр подстановки"""
    def __init__(self, alphabet0, alphabet1, language):
        super().__init__("Подстановка")
        self.alphabet0 = alphabet0
        self.alphabet1 = alphabet1
        self.language = language
    
    
    def _process(self, text, source_alphabet, target_alphabet):
        result = ''
        for char in text:
            char_index = source_alphabet.find(char)
            if char_index == -1:
                raise ValueError(f"Символ '{char}' не найден в алфавите")
            result += target_alphabet[char_index]
        return result
    
    
    def encrypt(self, text):
        return self._process(text, self.alphabet0, self.alphabet1)
    
    
    def decrypt(self, text):
        return self._process(text, self.alphabet1, self.alphabet0)
    
    
    def get_algo_graph(self):
        return """
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
    char_index = alphabet0.find(char)
    subs_char = alphabet1[char_index]
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
    char_index = alphabet1.find(char)
    subs_char = alphabet0[char_index]
    result = (result + subs_char)
    assert(result == '123')
      |
      v
   КОНЕЦ
"""


class MultiSubstitutionCipher(Cipher):
    """Шифр мультиподстановки"""
    def __init__(self, alphabet0, alphabets, language):
        super().__init__("Мультиподстановка")
        self.alphabet0 = alphabet0
        self.alphabets = alphabets
        self.language = language
    
    
    def encrypt(self, text):
        result = ''
        for i, char in enumerate(text):
            alphabet_c = self.alphabets[i % len(self.alphabets)]
            char_index = self.alphabet0.find(char)
            if char_index == -1:
                raise ValueError(f"Символ '{char}' не найден в алфавите")
            result += alphabet_c[char_index]
        return result
    
    
    def decrypt(self, text):
        result = ''
        for i, char in enumerate(text):
            alphabet_c = self.alphabets[i % len(self.alphabets)]
            char_index = alphabet_c.find(char)
            if char_index == -1:
                raise ValueError(f"Символ '{char}' не найден в алфавите")
            result += self.alphabet0[char_index]
        return result
    
    
    def get_algo_graph(self):
        return """
   НАЧАЛО  
      | 
      v
    text = '1234'
    alphabet0 = '12345'
    alphabets = ['23451','34512']
    length = len(text)
    qnt = len(alphabets)
    print('= ENCRYPT =')
    result = ''
      |
      v
  ┌───────────────────────────────────────────────────┐
  | ДЛЯ i, char in zip(range(length), text) ЦИКЛ:     |
  └───────────────────────────────────────────────────┘
    alphabet_c = alphabets[i % qnt]
    char_index = alphabet0.find(char)
    subs_char = alphabet_c[char_index]
    result = (result + subs_char)
  assert(result == '2441')
      |
      v
    print('= DECRYPT =')
    result = ''
      |
      v
  ┌───────────────────────────────────────────────────┐
  | ДЛЯ i, char in zip(range(length), text) ЦИКЛ:     |
  └───────────────────────────────────────────────────┘
    alphabet_c = alphabets[i % qnt]
    char_index = alphabet_c.find(char)
    subs_char = alphabet0[char_index]
    result = (result + subs_char)
    assert(result == '1234')
      | 
      v 
   КОНЕЦ
"""


class PermutationCipher(Cipher):
    """Шифр перестановки"""
    def __init__(self, key):
        super().__init__("Перестановка")
        self.key = key
        self.step = len(key[1])
        self.length = 0
    
    
    def _get_decrypt_key(self):
        """Создает обратный ключ для дешифрования"""
        decrypt_key = []
        for k in self.key[0]:
            decrypt_key.append(self.key[1].index(k) + 1)
        return decrypt_key
    
    
    def encrypt(self, text):
        result = ''
        self.length = len(text)
        delta = (self.step - (self.length % self.step)) % self.step
        
        for start in range(0, self.length, self.step):
            if (start + self.step) > self.length:
                s = text[start:start + self.step] + ' ' * delta
            else:
                s = text[start:(start + self.step)]
            result += ''.join([s[i - 1] for i in self.key[1]])
        
        return result
    
    
    def decrypt(self, text):
        result = ''
        #length = len(text)
        delta = (self.step - (self.length % self.step)) % self.step
        decrypt_key = self._get_decrypt_key()
        
        for start in range(0, self.length, self.step):
            if (start + self.step) > self.length:
                s = text[start:start + self.step] + ' ' * delta
            else:
                s = text[start:start + self.step]
            result += ''.join([s[i - 1] for i in decrypt_key])
        
        return result[:self.length]
    
    
    def get_algo_graph(self):
        return """
   НАЧАЛО  
      | 
      v
    text = 'АБВГД'
    key = [[1,2,3,4,5],[5,2,4,1,3]]
    length = len(text)
    step = len(key[1])
    delta = ((step - (length % step)) % step)
    print('= ENCRYPT =')
    delta = ((step - (length % step)) % step)
      |
      v
  ┌─────────────────────────────────────────┐
  | ДЛЯ start в range(0, length, step) ЦИКЛ:|
  └─────────────────────────────────────────┘
     ЕСЛИ (start + step) > length:
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
  | ДЛЯ k в key[0] ЦИКЛ:     |
  └──────────────────────────┘
     key_d.append((key[1].index(k) + 1))
      |
      v
  ┌─────────────────────────────────────────┐
  | ДЛЯ start в range(0, length, step) ЦИКЛ:|
  └─────────────────────────────────────────┘
      |
      v
    ЕСЛИ (start + step) > length:
      s = (text[start:(start + step):] + (' ' * delta))
       |
    ИНАЧЕ:
      s = text[start:(start + step):]
    result += ''.join([s[i-1] for i in key_d])
  assert(result == 'АБВГД')
      | 
      v 
   КОНЕЦ
"""
# encoding: utf-8
import math

class Alphabet:
    """Класс для хранения алфавитов"""
    ALFABET00_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЬЫЭЮЯ '
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
    ALFABET_ASCII_32_126 = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"


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
    def __init__(self, alfabet0, alfabet1, language):
        super().__init__("Подстановка")
        self.alfabet0 = alfabet0
        self.alfabet1 = alfabet1
        self.language = language
    
    def _process(self, text, source_alfabet, target_alfabet):
        result = ''
        for char in text:
            char_index = source_alfabet.find(char)
            if char_index == -1:
                raise ValueError(f"Символ '{char}' не найден в алфавите")
            result += target_alfabet[char_index]
        return result
    
    def encrypt(self, text):
        return self._process(text, self.alfabet0, self.alfabet1)
    
    def decrypt(self, text):
        return self._process(text, self.alfabet1, self.alfabet0)
    
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


class MultiSubstitutionCipher(Cipher):
    """Шифр мультиподстановки"""
    def __init__(self, alfabet0, alfabets, language):
        super().__init__("Мультиподстановка")
        self.alfabet0 = alfabet0
        self.alfabets = alfabets
        self.language = language
    
    def encrypt(self, text):
        result = ''
        for i, char in enumerate(text):
            alfabet_c = self.alfabets[i % len(self.alfabets)]
            char_index = self.alfabet0.find(char)
            if char_index == -1:
                raise ValueError(f"Символ '{char}' не найден в алфавите")
            result += alfabet_c[char_index]
        return result
    
    def decrypt(self, text):
        result = ''
        for i, char in enumerate(text):
            alfabet_c = self.alfabets[i % len(self.alfabets)]
            char_index = alfabet_c.find(char)
            if char_index == -1:
                raise ValueError(f"Символ '{char}' не найден в алфавите")
            result += self.alfabet0[char_index]
        return result
    
    def get_algo_graph(self):
        return """
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


class PermutationCipher(Cipher):
    """Шифр перестановки"""
    def __init__(self, key):
        super().__init__("Перестановка")
        self.key = key
        self.step = len(key[1])
    
    def _get_decrypt_key(self):
        """Создает обратный ключ для дешифрования"""
        decrypt_key = []
        for k in self.key[0]:
            decrypt_key.append(self.key[1].index(k) + 1)
        return decrypt_key
    
    def encrypt(self, text):
        result = ''
        length = len(text)
        delta = (self.step - (length % self.step)) % self.step
        
        for start in range(0, length, self.step):
            if start + self.step > length:
                s = text[start:start + self.step] + ' ' * delta
            else:
                s = text[start:start + self.step]
            result += ''.join([s[i - 1] for i in self.key[1]])
        
        return result
    
    def decrypt(self, text):
        result = ''
        length = len(text)
        delta = (self.step - (length % self.step)) % self.step
        decrypt_key = self._get_decrypt_key()
        
        for start in range(0, length, self.step):
            if start + self.step > length:
                s = text[start:start + self.step] + ' ' * delta
            else:
                s = text[start:start + self.step]
            result += ''.join([s[i - 1] for i in decrypt_key])
        
        return result.rstrip()
    
    def get_algo_graph(self):
        return """
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


class Variant:
    """Класс для представления варианта шифрования"""
    def __init__(self, variant_id, cipher_type, *params):
        self.variant_id = variant_id
        self.cipher_type = cipher_type
        self.params = params
        self.cipher = self._create_cipher()
    
    def _create_cipher(self):
        if self.cipher_type == 'SUBS':
            alfabet0, alfabet1, language = self.params
            return SubstitutionCipher(alfabet0, alfabet1, language)
        elif self.cipher_type == 'MULTISUBS':
            alfabet0, alfabets, language = self.params
            return MultiSubstitutionCipher(alfabet0, alfabets, language)
        elif self.cipher_type == 'PERMUT':
            key = self.params[0]
            return PermutationCipher(key)
        else:
            raise ValueError(f"Неизвестный тип шифра: {self.cipher_type}")
    
    def process_text(self, text):
        """Обрабатывает текст: шифрует и расшифровывает"""
        encrypted = self.cipher.encrypt(text)
        decrypted = self.cipher.decrypt(encrypted)
        return encrypted, decrypted
    
    def display_result(self, text):
        """Выводит результат обработки"""
        encrypted, decrypted = self.process_text(text)
        
        print(f"\n{'='*60}")
        print(f"= Вариант {self.variant_id} =")
        print(f"{'='*60}")
        print(f"== {self.cipher.name.upper()} ==")
        print(f"{'-'*40}")
        
        if isinstance(self.cipher, SubstitutionCipher):
            print(f"Тип: Подстановка")
            print(f"Язык: {self.cipher.language}")
            print(f"Исходный словарь: '{self.cipher.alfabet0[:50]}...'")
            print(f"Подстановочный словарь: '{self.cipher.alfabet1[:50]}...'")
        elif isinstance(self.cipher, MultiSubstitutionCipher):
            print(f"Тип: Мультиподстановка")
            print(f"Язык: {self.cipher.language}")
            print(f"Исходный словарь: '{self.cipher.alfabet0[:50]}...'")
            print(f"Количество подстановочных словарей: {len(self.cipher.alfabets)}")
        elif isinstance(self.cipher, PermutationCipher):
            print(f"Тип: Перестановка")
            print(f"Размер группы: {self.cipher.step}")
            print(f"Ключ: {self.cipher.key}")
        
        print(f"{'-'*40}")
        print(f"Текст для зашифрования: '{text}'")
        print(f"Зашифрованный текст   : '{encrypted}'")
        print(f"Расшифрованный текст  : '{decrypted}'")
        print(f"{'='*60}\n")
        
        return encrypted, decrypted
    
    def show_algorithm(self):
        """Показывает алгоритм работы шифра"""
        print(f"\n{'='*60}")
        print(f"АЛГОРИТМ {self.cipher.name.upper()}")
        print(f"{'='*60}")
        print(self.cipher.get_algo_graph())
        print(f"{'='*60}\n")


class ExampleTexts:
    """Класс для хранения примеров текстов"""
    TEXT_RU = 'ОСНОВЫ ЗАЩИТЫ ИНФОРМАЦИИ АБЫРВАЛ'
    TEXT_EN = 'HELLO WORLD!'
    TEXT_ASCII = '2*x^2 + 3*x + (A-B)/!C >= 4*y^2'
    
    @staticmethod
    def get_example(language):
        if language == 'RU':
            return ExampleTexts.TEXT_RU
        elif language == 'EN':
            return ExampleTexts.TEXT_EN
        else:
            return ExampleTexts.TEXT_ASCII


class CipherMenu:
    """Класс для управления меню программы"""
    
    def __init__(self):
        self.variants = self._create_variants()
        self.running = True
    
    def _create_variants(self):
        """Создает все варианты шифрования"""
        return [
            Variant(1, 'SUBS', Alphabet.ALFABET00_EN, Alphabet.ALFABET03_EN, 'EN'),
            Variant(2, 'PERMUT', PermutationKey.KEY01),
            Variant(3, 'MULTISUBS', Alphabet.ALFABET00_RU, 
                    [Alphabet.ALFABET01_RU, Alphabet.ALFABET02_RU, Alphabet.ALFABET05_RU], 'RU'),
            Variant(4, 'PERMUT', PermutationKey.KEY02),
            Variant(5, 'SUBS', Alphabet.ALFABET00_EN, Alphabet.ALFABET04_EN, 'EN'),
            Variant(6, 'MULTISUBS', Alphabet.ALFABET00_RU, 
                    [Alphabet.ALFABET01_RU, Alphabet.ALFABET03_RU], 'RU'),
            Variant(7, 'SUBS', Alphabet.ALFABET00_EN, Alphabet.ALFABET01_EN, 'EN'),
            Variant(8, 'MULTISUBS', Alphabet.ALFABET00_EN, 
                    [Alphabet.ALFABET02_EN, Alphabet.ALFABET05_EN], 'EN'),
            Variant(9, 'PERMUT', PermutationKey.KEY03),
            Variant(10, 'SUBS', Alphabet.ALFABET00_RU, Alphabet.ALFABET02_RU, 'RU'),
            Variant(11, 'PERMUT', PermutationKey.KEY04),
            Variant(12, 'MULTISUBS', Alphabet.ALFABET00_RU, 
                    [Alphabet.ALFABET01_RU, Alphabet.ALFABET03_RU, Alphabet.ALFABET04_RU], 'RU')
        ]
    
    def display_menu(self):
        """Отображает главное меню"""
        print("\n" + "="*60)
        print("         МЕТОДЫ ШИФРОВАНИЯ")
        print("="*60)
        print(" 0. Прогон по всем вариантам")
        print("-"*40)
        print(" 1. Подстановка, алфавит 3 (en), английский язык")
        print(" 2. Перестановка, ключ 1, ASCII символы")
        print(" 3. Мультиподстановка, [алфавиты 1, 2, 5] (ru), русский язык")
        print(" 4. Перестановка, ключ 2, русский язык")
        print(" 5. Подстановка, алфавит 4 (en), английский язык")
        print(" 6. Мультиподстановка, [алфавиты 1, 3] (ru), русский язык")
        print(" 7. Подстановка, алфавит 1 (en), английский язык")
        print(" 8. Мультиподстановка, [алфавиты 2, 5] (en), английский язык")
        print(" 9. Перестановка, ключ 3, ASCII символы")
        print("10. Подстановка, алфавит 2 (ru), русский язык")
        print("11. Перестановка, ключ 4, ASCII символы")
        print("12. Мультиподстановка, [алфавиты 1, 3, 4] (ru), русский язык")
        print("="*60)
    
    def get_variant_by_id(self, variant_id):
        """Получает вариант по ID"""
        for variant in self.variants:
            if variant.variant_id == variant_id:
                return variant
        return None
    
    def run_all_variants(self):
        """Запускает все варианты с примерами текстов"""
        print("\n" + "="*60)
        print("      ПРОГОН ПО ВСЕМ ВАРИАНТАМ ШИФРОВАНИЯ")
        print("="*60)
        
        for variant in self.variants:
            if variant.cipher_type in ['SUBS', 'MULTISUBS']:
                if variant.params[-1] == 'RU':
                    text = ExampleTexts.TEXT_RU
                elif variant.params[-1] == 'EN':
                    text = ExampleTexts.TEXT_EN
                else:
                    text = ExampleTexts.TEXT_ASCII
            else:  # PERMUT
                text = ExampleTexts.TEXT_ASCII
            
            variant.display_result(text)
    
    def run_single_variant(self, variant_id, custom_text=None):
        """Запускает один вариант"""
        variant = self.get_variant_by_id(variant_id)
        if not variant:
            print(f"Ошибка: Вариант {variant_id} не найден!")
            return
        
        # Определяем текст для шифрования
        if custom_text:
            text = custom_text
        else:
            if variant.cipher_type in ['SUBS', 'MULTISUBS']:
                if variant.params[-1] == 'RU':
                    text = ExampleTexts.TEXT_RU
                elif variant.params[-1] == 'EN':
                    text = ExampleTexts.TEXT_EN
                else:
                    text = ExampleTexts.TEXT_ASCII
            else:  # PERMUT
                text = ExampleTexts.TEXT_ASCII
        
        variant.display_result(text)
        
        # Спрашиваем, хочет ли пользователь увидеть алгоритм
        print("Показать алгоритм работы? (y/n): ", end="")
        show_algo = input().lower()
        if show_algo in ['y', 'yes', 'да', 'д']:
            variant.show_algorithm()
    
    def get_user_input(self):
        """Получает ввод пользователя"""
        while True:
            try:
                choice = input("\nВыберите номер варианта (0-12): ").strip()
                if not choice:
                    return 0
                return int(choice)
            except ValueError:
                print("Ошибка: Введите число от 0 до 12")
    
    def get_custom_text(self, variant):
        """Запрашивает пользовательский текст"""
        print(f"\nВведите текст для шифрования (рекомендуемый тип: {self._get_text_type(variant)}):")
        print("(Нажмите Enter для использования примера):")
        text = input().strip()
        
        if not text:
            return None
        return text
    
    def _get_text_type(self, variant):
        """Определяет рекомендуемый тип текста для варианта"""
        if variant.cipher_type == 'PERMUT':
            return "ASCII символы"
        elif variant.params[-1] == 'RU':
            return "русский текст"
        elif variant.params[-1] == 'EN':
            return "английский текст"
        return "любой текст"
    
    def run(self):
        """Главный цикл программы"""
        while self.running:
            self.display_menu()
            choice = self.get_user_input()
            
            if choice == 0:
                self.run_all_variants()
            elif 1 <= choice <= 12:
                variant = self.get_variant_by_id(choice)
                if variant:
                    custom_text = self.get_custom_text(variant)
                    self.run_single_variant(choice, custom_text)
                else:
                    print(f"Вариант {choice} не найден!")
            else:
                print("Неверный выбор! Пожалуйста, выберите номер от 0 до 12.")
                continue
            
            # Спрашиваем о продолжении
            print("\nПродолжить работу?")
            print("1 - Да, показать меню")
            print("0 - Нет, выйти")
            answer = input("Ваш выбор: ").strip()
            
            if answer == '0':
                self.running = False
                print("\nДо свидания!")
            elif answer != '1':
                print("Неверный ввод. Программа завершается.")
                self.running = False


# Главная функция
def main():
    """Точка входа в программу"""
    print("\n" + "="*60)
    print("   ПРОГРАММА ДЛЯ ШИФРОВАНИЯ ТЕКСТА")
    print("   Поддержка подстановки, перестановки и мультиподстановки")
    print("="*60)
    
    menu = CipherMenu()
    menu.run()


if __name__ == "__main__":
    main()
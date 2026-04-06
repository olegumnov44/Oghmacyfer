import cyphers

class Variant:
    """Класс для представления варианта шифрования"""
    def __init__(self, variant_id, cipher_type, *params):
        self.variant_id = variant_id
        self.cipher_type = cipher_type
        self.params = params
        self.cipher = self._create_cipher()
    
    def _create_cipher(self):
        if self.cipher_type == 'SUBS':
            alphabet0, alphabet1, language = self.params
            return cyphers.SubstitutionCipher(alphabet0, alphabet1, language)
        elif self.cipher_type == 'MULTISUBS':
            alphabet0, alphabets, language = self.params
            return cyphers.MultiSubstitutionCipher(alphabet0, alphabets, language)
        elif self.cipher_type == 'PERMUT':
            key = self.params[0]
            return cyphers.PermutationCipher(key)
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
        
        if isinstance(self.cipher, cyphers.SubstitutionCipher):
            print(f"Тип: Подстановка")
            print(f"Язык: {self.cipher.language}")
            print(f"Исходный словарь: '{self.cipher.alphabet0}'")
            print(f"Подстановочный словарь: '{self.cipher.alphabet1}'")
        elif isinstance(self.cipher, cyphers.MultiSubstitutionCipher):
            print(f"Тип: Мультиподстановка")
            print(f"Язык: {self.cipher.language}")
            print(f"Исходный словарь: '{self.cipher.alphabet0}'")
            print(f"Количество подстановочных словарей: {len(self.cipher.alphabets)}")
        elif isinstance(self.cipher, cyphers.PermutationCipher):
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

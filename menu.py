import variants, cyphers, texts

class CipherMenu:
    """Класс для управления меню программы"""
    
    def __init__(self):
        self.variants = self._create_variants()
        self.running = True
    
    def _create_variants(self):
        """Создает все варианты шифрования"""
        return [
            variants.Variant(1, 'SUBS', cyphers.Alphabet.ALPHABET00_EN, cyphers.Alphabet.ALPHABET03_EN, 'EN'),
            variants.Variant(2, 'PERMUT', cyphers.PermutationKey.KEY01),
            variants.Variant(3, 'MULTISUBS', cyphers.Alphabet.ALPHABET00_RU, 
                    [cyphers.Alphabet.ALPHABET01_RU, cyphers.Alphabet.ALPHABET02_RU, cyphers.Alphabet.ALPHABET05_RU], 'RU'),
            variants.Variant(4, 'PERMUT', cyphers.PermutationKey.KEY02),
            variants.Variant(5, 'SUBS', cyphers.Alphabet.ALPHABET00_EN, cyphers.Alphabet.ALPHABET04_EN, 'EN'),
            variants.Variant(6, 'MULTISUBS', cyphers.Alphabet.ALPHABET00_RU, 
                    [cyphers.Alphabet.ALPHABET01_RU, cyphers.Alphabet.ALPHABET03_RU], 'RU'),
            variants.Variant(7, 'SUBS', cyphers.Alphabet.ALPHABET00_EN, cyphers.Alphabet.ALPHABET01_EN, 'EN'),
            variants.Variant(8, 'MULTISUBS', cyphers.Alphabet.ALPHABET00_EN, 
                    [cyphers.Alphabet.ALPHABET02_EN, cyphers.Alphabet.ALPHABET05_EN], 'EN'),
            variants.Variant(9, 'PERMUT', cyphers.PermutationKey.KEY03),
            variants.Variant(10, 'SUBS', cyphers.Alphabet.ALPHABET00_RU, cyphers.Alphabet.ALPHABET02_RU, 'RU'),
            variants.Variant(11, 'PERMUT', cyphers.PermutationKey.KEY04),
            variants.Variant(12, 'MULTISUBS', cyphers.Alphabet.ALPHABET00_RU, 
                    [cyphers.Alphabet.ALPHABET01_RU, cyphers.Alphabet.ALPHABET03_RU, cyphers.Alphabet.ALPHABET04_RU], 'RU')
        ]
    
    def display_menu(self):
        """Отображает главное меню"""
        print("\n" + "="*60)
        print("         МЕТОДЫ ШИФРОВАНИЯ")
        print(" 0. Прогон по всем вариантам")
        print("-"*40)
        print(" 1. Подстановка, алфавит 3 (en), английский язык")
        print(" 2. Перестановка, ключ 1")
        print(" 3. Мультиподстановка, [алфавиты 1, 2, 5] (ru), русский язык")
        print(" 4. Перестановка, ключ 2")
        print(" 5. Подстановка, алфавит 4 (en), английский язык")
        print(" 6. Мультиподстановка, [алфавиты 1, 3] (ru), русский язык")
        print(" 7. Подстановка, алфавит 1 (en), английский язык")
        print(" 8. Мультиподстановка, [алфавиты 2, 5] (en), английский язык")
        print(" 9. Перестановка, ключ 3")
        print("10. Подстановка, алфавит 2 (ru), русский язык")
        print("11. Перестановка, ключ 4")
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
                    text = texts.ExampleTexts.TEXT_RU
                elif variant.params[-1] == 'EN':
                    text = texts.ExampleTexts.TEXT_EN
                else:
                    text = texts.ExampleTexts.TEXT_ASCII
            else:  # PERMUT
                text = texts.ExampleTexts.TEXT_ASCII
            
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
                    text = texts.ExampleTexts.TEXT_RU
                elif variant.params[-1] == 'EN':
                    text = texts.ExampleTexts.TEXT_EN
                else:
                    text = texts.ExampleTexts.TEXT_ASCII
            else:  # PERMUT
                text = texts.ExampleTexts.TEXT_ASCII
        
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
        if variant.cipher_type in ['SUBS', 'MULTISUBS']:
            print(f"Исходный словарь: '{variant.cipher.alphabet0}'")
        elif variant.cipher_type in ['PERMUT']:
            print(f"Ключ: '{variant.cipher.key[1]}'")
        print(f"Введите текст для шифрования (нажмите Enter для использования примера):")
        text = input()
        
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
    # alpha = cyphers.Alphabet()
    # alpha.print_alphabets('00')
    """Точка входа в программу"""
    print("\n" + "="*60)
    print("   ПРОГРАММА ДЛЯ ШИФРОВАНИЯ ТЕКСТА")
    print("   Поддержка подстановки, перестановки и мультиподстановки")
    print("="*60)
    
    menu = CipherMenu()
    menu.run()


if __name__ == "__main__":
    main()
# menu.py
import argparse
import sys
import variants
import cyphers
import texts


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
    
    def get_variant_by_id(self, variant_id):
        """Получает вариант по ID"""
        for variant in self.variants:
            if variant.variant_id == variant_id:
                return variant
        return None
    
    def get_all_variants(self):
        """Возвращает список всех вариантов"""
        return self.variants
    
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
    
    def run_all_variants(self, show_algo=False):
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
            
            if show_algo:
                variant.show_algorithm()
    
    def run_single_variant(self, variant_id, custom_text=None, show_algo=False):
        """Запускает один вариант"""
        variant = self.get_variant_by_id(variant_id)
        if not variant:
            print(f"Ошибка: Вариант {variant_id} не найден!")
            return None
        
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
        
        encrypted, decrypted = variant.display_result(text)
        
        if show_algo:
            variant.show_algorithm()
        
        return {'text': text, 'encrypted': encrypted, 'decrypted': decrypted}
    
    def encrypt_text(self, variant_id, text):
        """Только шифрование текста (без вывода)"""
        variant = self.get_variant_by_id(variant_id)
        if not variant:
            raise ValueError(f"Вариант {variant_id} не найден")
        
        encrypted, _ = variant.process_text(text)
        return encrypted
    
    def decrypt_text(self, variant_id, text):
        """Только расшифрование текста (без вывода)"""
        variant = self.get_variant_by_id(variant_id)
        if not variant:
            raise ValueError(f"Вариант {variant_id} не найден")
        
        _, decrypted = variant.process_text(text)
        return decrypted
    
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
    
    def interactive_mode(self):
        """Интерактивный режим работы"""
        print("\n" + "="*60)
        print("   ПРОГРАММА ДЛЯ ШИФРОВАНИЯ ТЕКСТА")
        print("   Поддержка подстановки, перестановки и мультиподстановки")
        print("="*60)
        
        while self.running:
            self.display_menu()
            choice = self.get_user_input()
            
            if choice == 0:
                # Спрашиваем про показ алгоритмов
                show_algo = input("Показывать алгоритмы для каждого варианта? (y/n): ").lower() in ['y', 'yes', 'да', 'д']
                self.run_all_variants(show_algo)
            elif 1 <= choice <= 12:
                variant = self.get_variant_by_id(choice)
                if variant:
                    custom_text = self.get_custom_text(variant)
                    # Спрашиваем про показ алгоритма
                    show_algo = input("Показать алгоритм работы? (y/n): ").lower() in ['y', 'yes', 'да', 'д']
                    self.run_single_variant(choice, custom_text, show_algo)
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


def setup_cli_parser():
    """Настройка парсера командной строки"""
    parser = argparse.ArgumentParser(
        prog='cli',
        description='Инструмент для шифрования текста с использованием подстановки, перестановки и мультиподстановки',
        epilog="""
Примеры использования:
  %(prog)s --list
  %(prog)s --variant 1 --text "HELLO"
  %(prog)s --variant 1 --encrypt "HELLO"
  %(prog)s --variant 1 --decrypt "KHOOR"
  %(prog)s --variant 1 --file input.txt --output encrypted.txt
  %(prog)s --variant 2 --text "ABCDEF" --show-algo
  %(prog)s --run-all
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument('--list', '-l', action='store_true',
                       help='Показать список доступных вариантов шифрования')
    
    parser.add_argument('--variant', '-v', type=int, choices=range(1, 13), metavar='N',
                       help='Номер варианта (1-12)')
    
    parser.add_argument('--encrypt', '-e', action='store_true',
                       help='Режим шифрования (по умолчанию)')
    
    parser.add_argument('--decrypt', '-d', action='store_true',
                       help='Режим расшифрования')
    
    parser.add_argument('--text', '-t', type=str,
                       help='Текст для обработки')
    
    parser.add_argument('--file', '-f', type=str,
                       help='Входной файл с текстом')
    
    parser.add_argument('--output', '-o', type=str,
                       help='Выходной файл для сохранения результата')
    
    parser.add_argument('--show-algo', '-a', action='store_true',
                       help='Показать алгоритм работы шифра')
    
    parser.add_argument('--run-all', '-r', action='store_true',
                       help='Прогнать все варианты')
    
    parser.add_argument('--interactive', '-i', action='store_true',
                       help='Интерактивный режим с меню')
    
    return parser


def cli_mode():
    """CLI режим работы с аргументами командной строки"""
    parser = setup_cli_parser()
    args = parser.parse_args()
    
    menu = CipherMenu()
    
    # Интерактивный режим
    if args.interactive:
        menu.interactive_mode()
        return
    
    # Список вариантов
    if args.list:
        menu.display_menu()
        return
    
    # Прогон всех вариантов
    if args.run_all:
        menu.run_all_variants(show_algo=args.show_algo)
        return
    
    # Работа с конкретным вариантом
    if args.variant:
        # Получаем текст
        text = None
        if args.file:
            try:
                with open(args.file, 'r', encoding='utf-8') as f:
                    text = f.read()
                print(f"Текст прочитан из файла: {args.file}")
            except Exception as e:
                print(f"Ошибка чтения файла: {e}")
                sys.exit(1)
        elif args.text:
            text = args.text
        else:
            # Если не указан ни текст, ни файл, используем пример
            variant = menu.get_variant_by_id(args.variant)
            if variant:
                if variant.cipher_type in ['SUBS', 'MULTISUBS']:
                    if variant.params[-1] == 'RU':
                        text = texts.ExampleTexts.TEXT_RU
                    elif variant.params[-1] == 'EN':
                        text = texts.ExampleTexts.TEXT_EN
                    else:
                        text = texts.ExampleTexts.TEXT_ASCII
                else:
                    text = texts.ExampleTexts.TEXT_ASCII
                print(f"Использован пример текста: '{text}'")
        
        if not text:
            print("Ошибка: не указан текст для обработки")
            sys.exit(1)
        
        # Режим расшифрования или шифрования
        if args.decrypt:
            result = menu.decrypt_text(args.variant, text)
            operation = "Расшифрованный текст"
        else:
            result = menu.encrypt_text(args.variant, text)
            operation = "Зашифрованный текст"
        
        # Вывод результата
        if args.output:
            try:
                with open(args.output, 'w', encoding='utf-8') as f:
                    f.write(result)
                print(f"{operation} сохранен в файл: {args.output}")
            except Exception as e:
                print(f"Ошибка записи в файл: {e}")
                sys.exit(1)
        else:
            print(f"\n{operation}: '{result}'")
        
        # Показ алгоритма
        if args.show_algo:
            variant = menu.get_variant_by_id(args.variant)
            if variant:
                variant.show_algorithm()
    
    else:
        # Если не указаны аргументы, показываем справку
        parser.print_help()


# Главная функция
def main():
    """Точка входа в программу"""
    # Проверяем наличие аргументов командной строки
    if len(sys.argv) > 1:
        cli_mode()
    else:
        # Без аргументов запускаем интерактивный режим
        menu = CipherMenu()
        menu.interactive_mode()


if __name__ == "__main__":
    main()
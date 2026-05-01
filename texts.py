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
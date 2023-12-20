"""
У нас есть класс TextProcessor, который содержит в себе методы для работы с текстом.

Задания:
    1. Создайте класс AdvancedTextProcessor, который будет наследником TextProcessor.
    2. Переопределите метод summarize у класса AdvancedTextProcessor таким образом, чтобы он возвращал еще и количество слов в тексте.
       Например: Total text length: 67, total number of words in the text: 10
    3. Создайте экземпляры каждого из двух классов и у каждого экземпляра вызовите все возможные методы.
"""


class TextProcessor:
    def __init__(self, text: str) -> None:
        self.text = text

    def to_upper(self) -> str:
        return self.text.upper()

    def summarize(self) -> str:
        return f'Total text length: {len(self.text)}'
    

class AdvancedTextProcessor(TextProcessor):
    def summarize(self) -> str:
        summary=super().summarize()
        words_count=len(self.text.split())
        return f'{summary}, total number of words in the text: {words_count}'


if __name__ == '__main__':
    text = """Такие термины как "протокол итератора" или "протокол дескрипторов" уже привычны и используются давно.
Теперь можно описывать протоколы в виде кода и проверять их соответствие на этапе статического анализа.
"""
    text_processor = TextProcessor(text)
    print('\nTextProcessor\n')
    print(text_processor.to_upper())
    print(text_processor.summarize())
    adv_text_processor = AdvancedTextProcessor(text)
    print('\nAdvancedTextProcessor\n')
    print(adv_text_processor.to_upper())
    print(adv_text_processor.summarize())

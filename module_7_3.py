# Оператор "with"
# Задача  "Найдёт везде"

class WordsFinder:
    def __init__(self, *names):
        self.file_names = list(names)

# возвращает словарь, в котором ключ - название файла,
# а значение - все слова из этого файла
    def get_all_words(self):
        all_words = {}
        del_char = [',', '.', '=', '!', '?', ';', ':', ' -']
        for file_name in self.file_names:
            try:
                with open(file_name, encoding='utf-8') as file:
                    words = file.read().lstrip('\ufeff').lower()
                    for char in del_char:
                        words = words.replace(char, ' ')
                    all_words[file_name] = words.split()
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")
                all_words[file_name] = []
        return all_words

# Возвращает словарь, где ключ - название файла, значение -
# позиция первого такого слова в списке слов этого файла.
    def find(self, word):
        dict_words = {}
        word = word.lower()
        for name, words in self.get_all_words().items():  # извлекаем имя файла и список слов в нём
            if word in words:
                dict_words[name] = words.index(word) + 1
            else:
                print('Такого слова нет')
        return (dict_words)


# # Возвращает словарь, где ключ - название файла, значение -
# # количество слова word в списке слов этого файла.

    def count(self, word):
        dict_count = {}
        word = word.lower()
        for name, words in self.get_all_words().items():  # извлекаем имя файла и список слов в нём
            if word in words:
                dict_count[name] = words.count(word)
            else:
                print('Такого слова нет')
        return (dict_count)


finder2 = WordsFinder('test_file.txt')

print(finder2.get_all_words())  # Все слова

print(finder2.find('TEXT'))  # 3 слово по счёту

print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

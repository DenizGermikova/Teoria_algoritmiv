# Константа розміру таблиці
M = 13

# Список вхідних слів (варіант 25)
WORDS = ["НЕ", "ВСЕ", "ТЕ", "РОБОТА", "ЩО", "РУКИ", "РОБЛЯТЬ",
         "ГОЛОВА", "МАЄ", "ЗНАТИ", "ЩО", "РОБИТИ"]

# Словник позицій українських букв
LETTER_POSITIONS = {
    'А':1,'Б':2,'В':3,'Г':4,'Ґ':5,'Д':6,'Е':7,'Є':8,'Ж':9,'З':10,
    'И':11,'І':12,'Ї':13,'Й':14,'К':15,'Л':16,'М':17,'Н':18,'О':19,
    'П':20,'Р':21,'С':22,'Т':23,'У':24,'Ф':25,'Х':26,'Ц':27,'Ч':28,
    'Ш':29,'Щ':30,'Ь':31,'Ю':32,'Я':33
}


def primary_hash_division(key: str) -> int:
    """ h(k) = (сума позицій букв) mod M """
    total = 0
    for char in key:
        total += LETTER_POSITIONS.get(char, 0)
    return total % M


def build_closed_hash_table_div(words: list, m: int) -> list:
    """
    Будує хеш-таблицю з відкритою адресацією (метод ділення),
    використовуючи лінійне дослідження.
    """
    hash_table = [None] * m

    for word in words:
        start_address = primary_hash_division(word)

        # Лінійне дослідження
        for i in range(m):
            address = (start_address + i) % m
            if hash_table[address] is None:
                hash_table[address] = word
                break
        else:
            print(f"Помилка: Таблиця переповнена. Не вдалося вставити {word}")

    return hash_table


def display_hash_table(table: list):
    """Виводить хеш-таблицю у зручному форматі."""
    print("\n--- Хеш-таблиця (метод ділення) ---")
    print("Індекс | Слово")
    print("-------|----------------")
    for i, item in enumerate(table):
        value = item if item is not None else "(NULL)"
        print(f"{i:02d}    | {value}")


# Виконання
hash_table = build_closed_hash_table_div(WORDS, M)
display_hash_table(hash_table)

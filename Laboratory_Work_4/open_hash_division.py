# Відкрите хешування, варіант 25
M = 13
# Слова варіанта 25
WORDS = ["НЕ", "ВСЕ", "ТЕ", "РОБОТА", "ЩО", "РУКИ", "РОБЛЯТЬ",
         "ГОЛОВА", "МАЄ", "ЗНАТИ", "ЩО", "РОБИТИ"]

# Таблиця позицій
LETTER_POSITIONS = {
    'А':1,'Б':2,'В':3,'Г':4,'Ґ':5,'Д':6,'Е':7,'Є':8,'Ж':9,'З':10,
    'И':11,'І':12,'Ї':13,'Й':14,'К':15,'Л':16,'М':17,'Н':18,'О':19,'П':20,
    'Р':21,'С':22,'Т':23,'У':24,'Ф':25,'Х':26,'Ц':27,'Ч':28,'Ш':29,'Щ':30,
    'Ь':31,'Ю':32,'Я':33
}

def simple_hash_from_map(key: str) -> int:
    """
    Хеш-функція: h(k) = (сума позицій літер) mod M
    """
    total = 0
    for ch in key.upper():
        total += LETTER_POSITIONS.get(ch, 0)
    return total % M

def build_open_hash_table(words: list, m: int) -> list:
    """Створює хеш-таблицю з ланцюжками."""
    table = [[] for _ in range(m)]
    for w in words:
        h = simple_hash_from_map(w)
        table[h].append(w)
    return table

def display_hash_table(table: list):
    print("\n--- Хеш-таблиця (Відкрите хешування, M=13) ---")
    for i, chain in enumerate(table):
        print(f"Індекс {i:02d}: {chain}")

# Виконання
hash_table = build_open_hash_table(WORDS, M)
display_hash_table(hash_table)

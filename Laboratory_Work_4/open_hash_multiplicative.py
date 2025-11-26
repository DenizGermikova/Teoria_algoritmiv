# Хешування методом множення
# Варіант 25

M = 16

WORDS = ["НЕ", "ВСЕ", "ТЕ", "РОБОТА", "ЩО", "РУКИ", "РОБЛЯТЬ",
         "ГОЛОВА", "МАЄ", "ЗНАТИ", "ЩО", "РОБИТИ"]

LETTER_POSITIONS = {
    'А':1,'Б':2,'В':3,'Г':4,'Ґ':5,'Д':6,'Е':7,'Є':8,'Ж':9,'З':10,
    'И':11,'І':12,'Ї':13,'Й':14,'К':15,'Л':16,'М':17,'Н':18,'О':19,'П':20,
    'Р':21,'С':22,'Т':23,'У':24,'Ф':25,'Х':26,'Ц':27,'Ч':28,'Ш':29,'Щ':30,
    'Ь':31,'Ю':32,'Я':33
}

A = (5 ** 0.5 - 1) / 2    # константа золотого перетину

def numeric_value(word: str) -> int:
    total = 0
    for ch in word.upper():
        total += LETTER_POSITIONS.get(ch, 0)
    return total

def multiplicative_hash(word: str) -> int:
    S = numeric_value(word)
    frac = (A * S) % 1
    return int(M * frac)

def build_multiplicative_table(words, m):
    table = [[] for _ in range(m)]
    for w in words:
        index = multiplicative_hash(w)
        table[index].append(w)
    return table

def display_multiplicative_table(table):
    print("\n--- Хеш-таблиця (метод множення, M=16) ---")
    for i, bucket in enumerate(table):
        print(f"Індекс {i:02d}: {bucket}")

# Виконання
table = build_multiplicative_table(WORDS, M)
display_multiplicative_table(table)

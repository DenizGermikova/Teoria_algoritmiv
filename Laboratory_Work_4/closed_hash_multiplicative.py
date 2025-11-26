M = 16

WORDS = ["НЕ", "ВСЕ", "ТЕ", "РОБОТА", "ЩО", "РУКИ", "РОБЛЯТЬ",
         "ГОЛОВА", "МАЄ", "ЗНАТИ", "ЩО", "РОБИТИ"]

LETTER_POSITIONS = {
    'А':1,'Б':2,'В':3,'Г':4,'Ґ':5,'Д':6,'Е':7,'Є':8,'Ж':9,'З':10,
    'И':11,'І':12,'Ї':13,'Й':14,'К':15,'Л':16,'М':17,'Н':18,'О':19,
    'П':20,'Р':21,'С':22,'Т':23,'У':24,'Ф':25,'Х':26,'Ц':27,'Ч':28,
    'Ш':29,'Щ':30,'Ь':31,'Ю':32,'Я':33
}

A = 0.6180339887  # Константа Кнута

def primary_hash_mult(key: str) -> int:
    """h(k) = ⌊16 * (k*A mod 1)⌋"""
    total = sum(LETTER_POSITIONS.get(ch, 0) for ch in key)
    fractional = (total * A) % 1
    h = int(16 * fractional)   # 16 — бо M = 16
    return h % M

def build_closed_hash_table_mult(words, m):
    table = [None] * m
    for word in words:
        start = primary_hash_mult(word)
        for i in range(m):
            addr = (start + i) % m
            if table[addr] is None:
                table[addr] = word
                break
    return table

def display_table(table):
    print("\n--- Хеш-таблиця (метод множення, M=16) ---")
    print("Індекс | Слово")
    print("-------|----------------")
    for i, v in enumerate(table):
        print(f"{i:02d}    | {v if v else '(NULL)'}")

table_mult = build_closed_hash_table_mult(WORDS, M)
display_table(table_mult)

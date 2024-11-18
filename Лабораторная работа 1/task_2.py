# TODO Найдите количество книг, которое можно разместить на дискете

val = 1.44 * 1024 * 1024
pages = 100
strokes = 50
symbols = 25
one_symbol = 4

val_book = pages * strokes * symbols * one_symbol
count = val // val_book

print("Количество книг, помещающихся на дискету:", int(count))

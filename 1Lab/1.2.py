# TODO Найдите количество книг, которое можно разместить на дискете
v_disk = 1.44 * 1024 ** 2
lot_pages_in_book = 100
line_on_page = 50
symbols_on_line = 25
symbole_byte = 4

one_book = symbole_byte * symbols_on_line * line_on_page * lot_pages_in_book
res = v_disk // one_book

print("Количество книг, помещающихся на дискету:", int(res))

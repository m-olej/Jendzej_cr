# Zadanie-rekrutacyjne-AKAI

###  Treść zadania:
- Z podanego zbioru danych wyselekcjonuj 5 o największej wartości na jednostkę, znając kategorię obiektu
- Dane znajdują się w folderze "dane" w pliku "zbiór_wejściowy.json" oraz "kategorie.json"
- Wynik przedstaw w czytelnej formie na standardowym wyjściu

# Rozwiązanie
Całe rozwiązanie znajduje się w pliku [main.py](main.py).

Przy użyciu funkcji `open` oraz `json.load()` zamieniłem dane z podanych plików json na listę słowników (obiektów).
Następnie dla każdego minerału porównałem jego nazwę oraz czystość i ustaliłem końcową wartość. 

Stworzyłem również funkcję `to_ounces(n, unit)`, która przeliczała podane w karatach i gramach wartości na uncje.

Na końcu posortowałem listę i wypisałem 5 najdroższych minerałów.

# Uwagi

W pliku [kategorie.json](kategorie.json) nie znalazły się wszystkie minerały z pliku [zbiór_wejściowy.json](zbiór_wejściowy.json) (*np. złoto 535*).
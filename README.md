# Circular Areas - CA
Struktura danych, która szybko potrafi zwrócić listę powierzchni do jakich punkt należy

# Lokalna instalcja
W gownym katalogu gdzie znajduje się setup.py wykonać polecenie
```python
pip install -e .
```
# Flake8
Ustawienie do flake8 jest w pliku setup.cfg

# Ustawienia
Można ustawić prezycję (zakres od 1 do 12) z jaką CA ma wyznaczać powierzchnie i punkty. Ustawienie precyzji następuje podczas inicjalizowania, domyślnie 8
```python
CA = CircularAreas(precision=5)
```
# Dane wejściowe
Inicjacja strukry następuje po dodaniu listy powierzchni kolistych zdefiniowanych poprzez współrzędne geograficzne i promień w metrach.
```python
batch_create([(lat:float, long:flot, radius:int, id:int]),...)
```

# Sprawdzanie punktów
Aby dostać listę powierzchni do jakich należy punkt trzeba przekazać jego współrzędne geograficzne. W odpowidzi będzie lista id powierzchni, jeżeli lista jest pusta, oznacza to, że dany punkt nie należy do żadnej powierzchni.
```python
query(lat:float, long:flot)
```
# Dane powierzchni
Dane poweirzchni dostaje w postaci słownika po zapytaniu o odpowienie id.
```python
get_area(id:int)
```
# Uwagi
  - Maksymalny szybki zakres promienia to 1000m, powyżej dodawanie poweirzchni jest dłuższe ze względu na wyliczanie obszarów (przy 1000 czas na dodanie 2 powierchni to około 0.46s (około 0.20-0.23s na jedną), a przy 10000 to już 47.53s (około 20-25s na jedną))
  - Nie wiem na ile algorytm jest dokładny, ale wydaje mi się, że nawet bardzo
  - Można pomyśleć o dodaniu filtru blooma do szybszego wykluczania powierzchni
  - Można spróbować zwielowątkować dodawanie poweirzchni (obliczanie)
  - Samo sprawdzanie punktów jest dość szybkie
  - To rozwiązanie ma ograniczenie w pojemnosci listy, więc można przy dużej liczbie powierzchni lub wielkich obszarach zastować jakiś cache lub inną strukturę do przetrzymywania list
  - Ze względu na krótki czas realizacji zadania (do zadania mogłem siąść dopiero od poniedziałku wieczór i pracować nad nim tylko wieczorami), brakuje pewnych zabezpieczeń (typu sprawdzanie, czy dane wchodzące są prawidłwe), ale uznałem, że to jest prototyp i świadomie tego nie dokończyłem (brakło mi czasu)

# ASD_Lista4

Program napisany w jezyku Python w wersji 3.10.8 na systemie linux w dystrybucji arch



Opis załączonych plików:

main.py - program rozwiązujący główne zadanie.

person.binary - plik binarny z danymi do zadania.

convertToBinFromTxt.py - dodatkowy program mający na celu wygenerowanie pliku binarnego z danymi (person.binary) z pliku tekstowego (persons.txt) na wypadek gdyby ktoś usunął wszystkie dane z pliku binarnego. Wrzuciłem dodatkowo gdyby coś się zepsuło w trakcie prezentowania zadania.

test.py - dodatkowy program mający na celu testowanie poprawnej konwersji danych z string -> binary i binary -> string. Wrzuciłem dodatkowo w razie wypadku potwierdzenia prawidłowej konwersji danych.

person.txt - dane do programu zawarte w pliku tekstowym potrzebne do convertToBinFromTxt.py w razie awarii oraz do "podejrzenia" danych.



Treść zadania:

Ksiazka telefoniczna wariant B

1. Napisać program realizujący książkę telefoniczną w strukturze drzewa AVL.
Program ma umożliwiać wykonanie następujących operacji:
a) wstawienie nowego abonenta wraz z numerami telefonów tego abonenta. Porządek
symetryczny drzewa jest wyznaczony przez porządek leksykograficzny na danych
abonenta. Dane abonenta to: nazwisko i imię (albo nazwa firmy), adres abonenta. Jeżeli
dwóch abonentów nie rozróżnia nazwisko i imię, to o kolejności danych decyduje adres.
Zakładamy, że nie ma dwóch abonentów o tym samym imieniu i nazwisku oraz adresie,
b) usunięcie abonenta wraz z jego numerami telefonów,
c) wyszukanie numeru (numerów) telefonu po podaniu danych abonenta (nazwisko i imię
oraz adres), względnie wyświetlenie komunikatu : Brak abonenta .......
d) zapis aktualnej zawartości książki telefonicznej w pliku binarnym. Trzeba zapamiętać
dane wszystkich abonentów wraz z ich tłumaczeniami. Format danych w pliku proszę
ustalić samodzielnie.
e) odczyt książki telefonicznej z pliku binarnego i wstawienie wszystkich danych do
drzewa AVL (niekoniecznie pustego).
2. Przygotować plik wejściowy książki zawierający co najmniej 100 abonentów.
3. Przetestować poprawność działania operacji słownikowych na podstawie przygotowanego
pliku wejściowego.

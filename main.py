import math
import random

#### Zadanie 1
## Poniżej masz 3 zbiory genów, 3 różnych pacjentów chorych na różne choroby
## Odpowiedz na poniższe pytania:
## a) Które elementy/geny są wspólne dla wszystkich pacjentów?
## b) Jakie elementy/geny są wspólne dla 2 pacjentów?
## c) Jakie elementy/geny występują wyłącznie w przypadku 1 choroby?
#
# set_gene1 = set(['SLC19A2', 'ATP7B', 'ERBB3', 'FGFR4', 'ABCC3','GALNT14', 'ERCC1',
#                 'LJS19A2', 'AKM7B', 'ELLB34', 'FULR4', 'ANGC3', 'WELNT14', 'EOO1',
#                 'SAC19A22', 'AAAP7B', 'ERB3', 'FGR4', 'ACC3', 'GASNT14', 'ERSS4'])
# set_gene2 = set(['SLC19A3', 'ATP7B', 'ERBB3', 'FGFR4', 'ABCC3','GALNT14', 'ERCC1',
#                 'LJS19A2', 'AKM7B', 'ELLB32', 'FULR421', 'ANGC3', 'WELNT14', 'EOO11',
#                 'SAC19A2', 'AAAP7B', 'ERB3', 'FGR4', 'ACC3', 'GASNT14', 'ERSS4'])
# set_gene3 = set(['SLC19A3', 'ATP7B1', 'ERBB32', 'FGFR4', 'ABCC3','GALNT14', 'ERCC11',
#                 'LJS19A2', 'AKM7B', 'ELLB34', 'FULR4', 'ANGC3', 'WELNT15', 'EOO1',
#                 'SAC19A22', 'AAP7B', 'ERBB3', 'FGR4', 'ACC4', 'GASNT14', 'ERSS4'])
#
# # a:
# print("A: \n")
# x = set_gene1.intersection(set_gene2).intersection(set_gene3)
# print(x)
#
# # b:
# print("\n B: \n")
# p12 = (set_gene1.intersection(set_gene2))
# p23 = (set_gene2.intersection(set_gene3))
# p13 = (set_gene1.intersection(set_gene3))
#
# p = p12.union(p23).union(p13)
# print(p.difference(x))
#
# # c:
# print("\n C: \n")
# all = set_gene1.union(set_gene2).union(set_gene3)
# print(all.difference(p12).difference(p13).difference(p23))

# ##########Zadanie 2
# ### Sprawdź czy w poniższym zbiorze występuje gen 'FGFR4' oraz 'FGERA4', jeśli tak to wskaż index
# ### genu na liście
#
# lista_gene1 = ['SLC19A2', 'ATP7B', 'ERBB3', 'FGFR14', 'ABCC3','GALNT14', 'ERCC1',
#                 'LJS19A2', 'AKM7B', 'ELLB34', 'FULR4', 'ANGC3', 'WELNT14', 'EOO1',
#                 'SAC19A22', 'FGFR4', 'ERB3', 'FGR4', 'FGFR4', 'GASNT14', 'ERSS4']
#
# for i in lista_gene1:
#     if i == 'FGFR4' or  i == 'FGERA4':
#         print(lista_gene1.index(i))


#####Zadanie 3
## Przekopiuj dowolny ale długi fragment tekstu ze strony:
## http://www.national-geographic.pl/ludzie/dziennikarka-kontra-komputer-kto-napisze-lepszy-tekst
## sprawdź:
## a) ile razy w tekście występuje słowo Emma
## b) zamień całość tekstu na duże litery
## c) wstaw poszczególne wyrazy jako elementy listy
## d) ile zdań jest w analizowanym tekście?

# var_string_txt = 'Któregoś dnia w zeszłym tygodniu dokładnie o 9:29 pochyliłam się nerwowo nad klawiaturą komputera gotowa do walki ze sztucznym tworem o nazwie Emma. Emma i ja dostałyśmy instrukcje, by o 9:30 napisać o oficjalnych danych dotyczących zatrudnienia w Wielkiej Brytanii i wysłać nasze wersje do redaktora. Byłam przekonana, że Emma będzie ode mnie szybsza, ale miałam też szczerą nadzieję, że to ja będę lepsza. Twórca Emmy, start-up o nazwie Stealth, nazywa ją „niezależną sztuczną inteligencją” zaprojektowaną, by świadczyć profesjonalne usługi, takie jak badania i analiza. Odkąd w modzie są prognozy, że sztuczna inteligencja (ang. artificial intelligence, AI) zastąpi pracowników biurowych, w tym również dziennikarzy, chciałam to sprawdzić na własnej skórze. Emma rzeczywiście była szybka – dane wysłała w 12 minut. Mi zajęło to 35. Jej wersja była też lepsza, niż się spodziewałam. Fakty się zgadzały, zawarła nawet trafne treści, takie jak możliwość Brexitu (choć podzielała wątpliwą opinię, że wyjście z Unii Europejskiej byłoby niezwykle korzystne dla brytyjskiej gospodarki).'
#
# print(var_string_txt.count('Emma'))
# print(var_string_txt.upper())
# print(var_string_txt.split())
# print(var_string_txt.count('.') - 1)


########Zadanie 4
## Sprawdź czy dowolnie podana przez użytkownika liczba jest parzysta czy nieparzysta

# var_int_x = int(input("Podaj liczbe: "))
#
# if var_int_x % 2 == 0:
#     print("To liczba parzysta")
# else:
#     print("To nie liczba parzysta")


########Zadanie 5
## W zależności od procentu uzyskanych punktów z kolokwium z Python'a
## student uzyskuje określoną ocenę końcową z laboratorium
## np 50%-60% to 3.0, 61%-70% to 3.5, ...., 91%-100% to 5.0 - if
## np 50% to 3.0, 61% to 3.5, ...., 91% to 5.0 - match
## Korzystając z instrukcji match, napisz program który będzie wyznaczał ocenę studenta na podstawie uzyskanych punktów (max 15pkt)

# var_float_points = float(input("Podaj liczbe punktów: "))
#
# var_float_points = ((var_float_points/15) * 100)
#
# if var_float_points >= 50 and var_float_points <= 60:
#     print("3.0")
# elif var_float_points >= 61 and var_float_points <= 70:
#     print("3.5")
# elif var_float_points >= 71 and var_float_points <= 80:
#     print("4.0")
# elif var_float_points >= 81 and var_float_points <= 90:
#     print("4.5")
# elif var_float_points >= 91 and var_float_points <= 100:
#     print("5.0")
# elif var_float_points < 50:
#     print("2.0")
# else:
#     print("Error")
#
# match var_float_points:
#     case 50:
#         print("3.0")
#     case 61:
#         print("3.5")
#     case 71:
#         print("4.0")
#     case 81:
#         print("4.5")
#     case 91:
#         print("5.0")
#     case _:
#         print("Error")


# # #Zadanie 6
### Napisz skrypt, ktory obliczy sume ciagu: 1+1/2+1/3+...+1/n korzystając z pętli for
### Zmienna wejsciowa n jest dowolnia, n-parametr wprowadzany jako dane wejsciowe przez uzytkownika (użyj input)
### Write a program that calculates the sum of the sequence: 1+1/2+1/3+...+1/m using the for loop.
### The input variable m is arbitrary. The m-parameter is provided as input by the user (use input).

# var_int_x = int(input("Podaj liczbe: "))
# var_float_suma = 0.0
#
# for i in range (1,var_int_x+1):
#     var_float_suma = var_float_suma + (1 / i)
#
# print(var_float_suma)


###### Zadanie 7
###### Calculate the root of the numbers from 1 to 10 using the while loop
###### Oblicz pierwiastek liczb od 1 do 10 korzystając z pętli while

# var_int_x = 1
#
# while var_int_x <= 10:
#     print(math.sqrt(var_int_x))
#     var_int_x = var_int_x + 1


###### Task 8
###### Write a program which takes 3 digits: a, b, c as input and
###### calculate the roots of a quadratic equation ax^2 + bx + c = 0

# var_int_a = int(input("Podaj liczbe a: "))
# var_int_b = int(input("Podaj liczbe b: "))
# var_int_c = int(input("Podaj liczbe c: "))
#
# var_float_delta = (var_int_b**2) - 4*var_int_a*var_int_c
# if var_float_delta < 0:
#     print("Brak pierwiastków")
# elif var_float_delta == 0:
#     print((-var_int_b)/(2*var_int_a))
# elif var_float_delta > 0:
#     x1 = (((-var_int_b)-math.sqrt(var_float_delta))/(2*var_int_a))
#     x2 = (((-var_int_b) + math.sqrt(var_float_delta)) / (2 * var_int_a))
#     print("x1: " + str(x1))
#     print("x2: " + str(x2))

###### Task 9
##### Write a program, which will find all such numbers between 1 and 1000 (both included) such
##### that each digit of the number is an even number the numbers obtained should be printed
### in a comma-separated sequence on a single line.

# result = []
# for i in range(0, 1001):
#     even = True
#     for j in str(i):
#         if int(j) % 2 != 0:
#             even = False
#     if even == True:
#         result.append(str(i))
#
# print(", ".join(result))


# # ################################ Task 10
## Write a program using if statement, for loop, break(), continue() which takes 2 digits: x, y as input and
###### calculate multiplication x*y. The program stops working if x or y is equal to 0.
## Korzystając z instrukcji sterujących napisz program który będzie wczytywał kolejno z klawiatury 2 liczby,
## a następnie obliczał i wyświetlał na ekranie iloczyn wprowadzonych przez użytkownika liczb,
## program kończy działanie jeżeli uzytkownik wprowadzi cyfrę 0. Użytkownik może wykonać obliczenia tylko na
## liczbach całkowitych (wstaw odpowiedni warunek).


# for i in range(100000):
#     var_int_x = input("Podaj liczbe x:")
#     var_int_y = input("Podaj liczbe y:")
#
#     if not (var_int_x.lstrip('-').isdigit() and var_int_y.lstrip('-').isdigit()):
#         print("Error")
#         continue
#
#     var_int_x = int(var_int_x)
#     var_int_y = int(var_int_y)
#
#     if var_int_x == 0 or var_int_y == 0:
#         break
#     else:
#         print(var_int_x*var_int_y)

## # ################################ Task 11
## Napisz program, który wyświetli twoje imię i nazwisko jeżeli użytkownik poda
## właściwe hasło, jedno z 2 do wyboru, (hasła są przechowywane w krotce)
## Write a program that will display your name if the user enters the correct
## password (the password is stored in a variable)


# passwords = ('Hasło1' , 'Hasło2')
# x = input('Podaj hasło: ')
#
# if  x in passwords:
#     print("Mariusz Bienasz")


################################## Task 12
## Generate list with 100 random numbers (integer type)
## Ascending sort these odd numbers and print only odd numbers from list.

# all_numbers=[]
# for i in range(100):
#     all_numbers.append(random.randint(1,100))
#
# print(all_numbers)
#
# odd_numbers=[]
#
# for i in all_numbers:
#     if i%2 != 0:
#         odd_numbers.append(i)
#
# odd_numbers.sort()
#
# print(odd_numbers)

## Wygeneruj listę złożoną z 100 liczb całkowitych parzystych i nieparzystych
## wypisz wszystkie liczby parzyste z tablicy liczby, od najmniejszej do największej.
## Do losowania liczb wykorzystaj moduł random patrz przykład poniżej

# even_numbers = []
# for i in all_numbers:
#     if i%2 == 0:
#         even_numbers.append(i)
#
# even_numbers.sort()
#
# print(even_numbers)


############### Task 13
## Uprość kod z Zadania 11 korzystając w w/w struktur
## Simplify the code from Task 11 using a one line if/else statement


# passwords = ('Hasło1' , 'Hasło2')
# x = input('Podaj hasło: ')
#
# print(("Error","Mariusz Bienasz")[x in passwords])


#################### Task 14
## Write a function that calculates the quotient of 3 even numbers
## Utwórz funkcje która obliczy iloraz 3 parzystych liczb, użyj "one line statement"

# def calculate(a, b, c):
#     return (a / b) / c if b != 0 and c != 0 and a%2 == 0 and b%2 == 0 and c%2 == 0 else None
#
# print(calculate(4,2,2))
def from_to(start, end):
    for number in range(start, end):
        print(number)

#from_to(1, 101)

def div_by6():
    for number in range(1, 101):
        if number % 6 == 0: 
            print(number)

#div_by6()

def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("fizzbuzz")
        elif number % 5 == 0:
            print("buzz")
        elif number % 3 == 0: 
            print("fizz")
            
        else: print(number)
        


#fizzbuzz()

liste = [2, 4, 5, 7, 3, 5, 9, 27, 34, 26]

def summe(lst):
    summe = 0
    for num in lst:
        summe += num
    return summe 


ergebnis_summe = summe(liste)
print(ergebnis_summe)

def durchschnitt(lst):
    summe = 0
    for num in lst:
        summe += num
    return summe / len(lst)


durchschnitt = durchschnitt(liste)
print(durchschnitt)
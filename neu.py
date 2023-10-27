fruits = ["apple", "banana", "cherry", "date", "fig"]
print ("first fruit: ", fruits[0])
print("last fruit: ", fruits[-1])


numbers =[1, 2, 3, 4, 5]
print(max(numbers))
print(numbers[-2])

text = "Python"
print(text[2])

colors = ["red", "blue", "green", "yellow", "orange"]
print("colors", colors[1:3])

nested_list = [[1, 2, 3], ["apple", "banana", "cherry"]]
print("secind item from second list", nested_list[1][1])
simple_list = nested_list[0] + nested_list[1]
print("flatMap: ", simple_list)

numbers = [1, 2, 3, 4, 5]
numbers_sum = sum(numbers)
print("sum of numbers in the list", numbers_sum)

summe = 0
for element in numbers:
    summe += element

print(summe)



numbers = [10, 20, 30, 40, 50]
n_avg = (sum(numbers) / len(numbers))
print ("numbers average", n_avg)


words = ["apple", "banana", "cat", "dog", "elephant"]
new_words = [word for word in words]
print(new_words)

new_words2 =[]
for word in words:
    if len(word) > 3:
        new_words2.append(word)
print("a normal for logo", new_words2)

original_list = [1, 2, 3, 4, 5]
print("reversed_list", original_list[::-1])

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
even_numbers = [num for num in numbers if num % 2 == 0]
print("list comprhension: ", even_numbers)

even_numbers2 = []
for num in numbers:
    if num % 2 == 0:
        even_numbers2.append(num)

print("for loops. ", even_numbers2)
print(" hello world")

name = input("Dein name: ")

print("Hi", name+ " schön dich zu sehen!")
a = input("zahl eingeben: ")
if a > 0:
    print("a is positve")
    print("New line")
print("Ende")

def main():
    return "Jo Brudi"

print(
    main()
)
fruits = ["apple", "banana", "cherry"]

for x in fruits:
  print("this are my fruits: ", x)

class Person:
  # similar to javascript constructor
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36) # no need for a new keywords as in js
print(p1)
print(p1.name)
print(p1.age)

obj = {"name": "Dimi", "age": 35}

print(obj["name"])
print(obj["age"])
print(obj.get("name", "Pablo"))

"""
this is my multi-line comment
"""

'''
this is my multi-line comment
'''

mal = 5 * 5
geteilt = 5 / 5
res = (3 + 5) * 4

print(
   mal,
   geteilt,
   res
)

# parseInt von string zu number casten
# str() castet von number zu string

xs = [1, 2, 3, 4, 5] # .length

print(
    len( str(10) ),
    len( xs )
)

print(
   "\"Hallo Welt\". Ich bin hier und danke!",
   '\"Hallo Welt\". Ich hier und danke!'
   "'Hallo Welt'. Ich hier und danke!"
)

True and False # && and  || or

if True:
   print("it is true")

# if (false) {
#    console.log()
# } else {
#    console.log()
# }

if False:
    print("is false")
else: 
    print("this is from false")

#true or false

print(
   type([1,2,3,4]),
   type(5),
   type({"name":  "dimi"}), # dict in js obj
   type("string")
)

a = 5
a = 10
a = 15

print(a)

test = 1
Test = 5

# case-sensitive !!!
print(
   test,
   Test
)

ひらがな="Konichiva"
官话="mandarin"

print(
    ひらがな,
    官话
)


# fatherName
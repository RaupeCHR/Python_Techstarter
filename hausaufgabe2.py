def test(name, age):
    if age > 30 and name.startswith("A"):
        return True
    return False

names = ["Bartek", "Mathias", "Jonathan", "Evelyn", "Christoph", "Anna", "Andreas" ]
age = 32

for n in names:
    print(n)
    print(test(n, age))
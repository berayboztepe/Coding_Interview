#Verilen arrayde, aranan sayının kaçıncı indexte olduğunu bulma(eğer sayı arrayde yoksa 0 döndürülecek)
array = [10, 25, 46, 7, 8, 15]
element = int(input("Write a number:"))

for i in range(0, (len(array))):
    if (element == array[i]):
        break

if (array[i] == element):
    print(i)
else:
    print(0)

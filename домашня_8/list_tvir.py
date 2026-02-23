list1 = [1,2,3]
list2 = [4,5,6]

list_product = list(map(lambda x,y: x * y , list1,list2))
print(list_product)

#   перемножуємо спочатку     1 * 4 = 4,    2 * 5 = 10,    3 *6 = 18
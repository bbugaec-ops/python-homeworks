import pickle

numbers = input("Ввеіть цілі числа :")

test_data = pickle.dumps(numbers)
print(f"test_data :\n {test_data}")

detest_data = pickle.loads(test_data)
print(f"detest_data : {detest_data}")
print("========RESULT=========="

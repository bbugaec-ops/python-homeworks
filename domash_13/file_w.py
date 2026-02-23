data = input("Hobby:")
file = open('data_myfile.txt','a')
file.write(data + '\n')
file.close()
with open("test.txt",'w',encoding = 'utf-8') as f:
   f.write("my first file\n")
   f.write("This file\n\n")
   f.write("contains three lines\n")
   f.close()

with open("test.txt",'r') as f1:
    f1_list = f1.readlines()
    for  line in f1_list:
        print(line)

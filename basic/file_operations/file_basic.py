with open("test.txt",'w',encoding = 'utf-8') as f:
   f.write("my first file \n")
   f.write("This file \n")
   f.write("contains three lines \n")
   f.close()

with open("test.txt",'r') as f1:
    f1_list = f1.readlines()
    result = []
    for line in f1_list:
        result.append(line.split())
print(f"result:{result}")
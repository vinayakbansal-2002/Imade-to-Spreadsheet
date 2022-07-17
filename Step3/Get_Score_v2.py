count=0
with open("Colleges_dataset_V2",'r') as reader:
    line=reader.readline()
    print("hello1")
    while line != '':
        
        if line.startswith('Score'):
            count=count+1
            print(count,line)
            

        line=reader.readline()
    print('hello')


print("hello")

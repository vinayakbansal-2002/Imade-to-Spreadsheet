count=0
linecount=1
with open("Colleges_dataset_V4",'r') as reader:
    line=reader.readline()
    print("hello1")
    missinglines=[]
    
    while line != '':
        
        if line.startswith('Score'):
            count=count+1
            print(count,line)

        elif line.find('Score')>=0:
            
            missinglines.append(linecount)
        



            

        line=reader.readline()
        linecount=linecount+1
    print('hello')

print(missinglines)

print("hello")

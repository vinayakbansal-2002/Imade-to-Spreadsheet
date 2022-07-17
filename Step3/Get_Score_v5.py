count=0
linecount=1
ScoreLines=[]
with open("Colleges_dataset_V5",'r') as reader:
    line=reader.readline()
    print("hello1")
 
    while line != '':
        
        if line.startswith('Score'):
            count=count+1
            ScoreLines.append(line)


        line=reader.readline()
        linecount=linecount+1
    print('hello')

with open("College_csv.csv",'w') as writer:
    for line in ScoreLines:
        new_college=""
        x=-1 #to store the start and end of sub string
        for i in range(6,len(line)):# first characters in each line is Score We do not need that
            if line[i-1].isspace() and line[1].isalpha():
                x=i
        
            elif line[i].isspace():
                if x!=-1:
                    new_college=new_college+line[x:i]+','
                x=-1

        new_college=new_college[0:len(new_college)-1]#remove the last ','
        print(new_college)
        writer.write(new_college+"\n")



print("hello")




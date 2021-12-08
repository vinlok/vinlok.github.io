import sys
from collections import defaultdict
import json

def tokenize(line):
    tokens=[]
    #print(line)
    # print(line)
    words=line.split()
    for i in range(len(words)):
        if not words[i].isalnum():
            new_word = ""
            for c in words[i]:
                if c.isalnum() or c=="'":
                    new_word=new_word+c

            words[i]=new_word
    print(words)
    return words





def split_into_chunks(MAX_CHUNK_SIZE):
    num_of_char=MAX_CHUNK_SIZE
    # print(num_of_char)
    with open("words.txt",'r') as f:

        chunk_num=1
        chunk=f.read(num_of_char)

        # print(chunk)
        while chunk:
            count=0
            cur_pos=f.tell()
            for c in range(len(chunk)-1,-1,-1):
                 count += 1
                 # print(chunk[c])
                 if chunk[c] == " ":
                     break

            f1= open(str(chunk_num)+".txt","w")



            words=tokenize(chunk[:-count])
            for word in words:
                f1.write(word.lower()+" ")

            f1.close()
            chunk_num+=1
            f.seek(cur_pos-count,0)
            chunk=f.read(num_of_char)
            if len(chunk) < num_of_char:
                # print(chunk)
                break


        return(chunk_num)





chunk_num=split_into_chunks(1000)


for c in range(1,chunk_num):

    with open(str(c)+".txt") as f, open(str(c)+".result.json","w") as f1 :
        dd={}

        words=f.read().split()



        for word in words:
            wf=open(word+".count","a")
            wf.write("1 ")
            wf.close()
            if word in dd:
                dd[word] += 1
            else:
                dd[word] =1

        json.dump(dd,f1)







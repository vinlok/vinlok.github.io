'''
algo:
1. Reverse the entire string
2. Then on the reversed string, reverse the words in place.
'''

def in_place_reverse_string(string,s,e):

    while s < e:
        t=string[s]
        string[s]=string[e]
        string[e]=t

        s+=1
        e-=1

    return string

s=list("  my name is     vinayak")

s=in_place_reverse_string(s,0,len(s)-1)

i=j=0
while j < len(s):

    if s[i] != " ":
        while s[j] != " ":
        #walk j untill you see a space
            j += 1
            if j == len(s):
                break
        s=in_place_reverse_string(s,i,j-1)

        i=j
    else:
        i += 1
        j += 1


print("".join(s))

import time

string=input('enter the string: ')
substring=input('enter the sub string: ')

#intialization of prefix array
ls=[0]*len(substring)

def prefix_array(pattern):
    i=1
    j=0
    while(i<=(len(substring)-1)):
        #condition 1: if i == j
        if(i==j):
            ls[i]=j+1
            i+=1
            j+=1
        else:
        #condition 2: if j is at starting
            if(j==0):
                i+=1
        #condition 3: if j is not at the beginning
            else:
                j=ls[j-1]

def KMPsearch(text,pattern):
    i,j=0,0
    while(i<len(text) and j<len(pattern)):
        if(text[i]==pattern[j]):
            i+=1
            j+=1
        else:
            if(j==0):
                i+=1
            else:
                j=ls[j-1]
    if(j==len(pattern)):
        print('match found bro!')
    else:
        print('match not found bro')

start=time.time()
KMPsearch(string,substring)
end=time.time()
print('----time taken for exec is %f secs----'%(end-start))


import time
string=input('enter the string: ')
substring=input('enter the substring: ')
m=len(string)
n=len(substring)


def createHash(pattern,x):
    value=0
    for i in range(x):
        value=value+(ord(pattern[i])*pow(101,i))
    return value

def reCalculateHash(pattern,old_index,old_hash,x):
    value=(old_hash-ord(string[old_index]))/101
    value=value+(ord(pattern[-1])*pow(101,x-1))
    return value

start=time.time()


textHash=createHash(string,n)
patternHash=createHash(substring,n)

if(textHash==patternHash and string[0:n]==substring):
    print('match found at i = %d'%(0))

for i in range(1,m-n+1):
    window=string[i:i+n]
    textHash=int(reCalculateHash(window,i-1,textHash,n))

    if(textHash==patternHash and window==substring):
        print('match found at i = %d'%(i))

end=time.time()

print('---this program completed in %f secs---'%(end-start))






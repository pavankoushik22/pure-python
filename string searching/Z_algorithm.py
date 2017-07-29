import time

string=input('enter your string: ')
substring=input('enter your substring: ')

bigboy=substring+'$'+string


def z_algo(bigboss):
    z=[0]*len(bigboss)
    left, right = 0, 0
    for k in range(1, len(bigboss)):
        # while only single element matches at a time
        if k > right:
            left = k
            right = k
            while right < len(bigboss) and bigboss[right] == bigboss[right-left]:
                right += 1
            z[k] = right - left
            right -= 1
        # while more than one matches
        else:
            k1 = k - left
            if z[k1] < right - k + 1:
                z[right] = z[k1]
            else:
                left = k
                while right < len(bigboss) and bigboss[right] == bigboss[right-left]:
                    right += 1
                z[k] = right - left
                right -= 1
    return z

start = time.time()


z_list = z_algo(bigboy)
count = 0
for i in z_list:
    if i >= len(substring):
        count += 1
end = time.time()

print('number of matches found are %d ' % count)
print('---time taken for execution is %f secs' % (end-start))







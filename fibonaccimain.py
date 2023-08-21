














import random
N = int(input("Enter positive N: "))
for i in range(N):
    randomlist = random.randint(1,1000)
    randomlist.append(randomlist)

pancake = randomlist
print(pancake)
k = N
while(k>1):
    curr_list = pancake[0:k]
    max_val = max(curr_list);
    max_idx = curr_list.index(max(curr_list))
    if(max_idx == k-1):
        k = k-1
    elif(max_idx == 0):
        curr_list = curr_list[-1::-1]
        pancake[0:k] = curr_list
        k = k-1
    else:
        curr_list[0:max_idx+1] = curr_list[max_idx::-1]
        curr_list = curr_list[-1::-1]
        pancake[0:k] = curr_list
        k = k-1
print(pancake)


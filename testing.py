INPUT_ARRAY = [ 1, 29, 3, 'v', 78, 69, 'a', '8', 99, 't', '9']

result1 = [] # mang chua cac phan tu so nguyen cua mang INPUT_ARRAY, sap xep theo chieu tang dan

result2 = [] # mang chua cac phan tu ky tu trong mang INPUT_ARRAY


#s = 'v-a-8-t-9' # kieu chuoi (str), gom cac ky tu cua result2

#####################################
## YOUR CODE BEGIN
l = len(INPUT_ARRAY)
print("Do dai mang: {}".format(l))
#m = 0
# for c in INPUT_ARRAY
for i in range(l):
    if type(INPUT_ARRAY[i]) == int:
        result1.append(INPUT_ARRAY[i])
        m = len(result1)

    elif type(INPUT_ARRAY[i]) == str:
        result2.append(INPUT_ARRAY[i])

print("Length: {}".format(m))
for j in range(m):
    for n in range(j+1, 6):
        if result1[j] > result1[n]:
            tg = result1[j]
            result1[j] = result1[n]
            result1[n] = tg
#result1.sort()
print("result1 = {}".format(result1))
print("result2 = {}".format(result2))
s =  str(result2)[1: -1]
print("s = {}".format(s))


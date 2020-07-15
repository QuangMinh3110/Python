a= '+'
b= ' '
chieu_cao = input("nhập chiều cao mong muốn: ")
new_chieu_cao = int(chieu_cao) # python casting
for i in range (1, new_chieu_cao + 1):
    n = new_chieu_cao - i
    m = 2*i - 1
    x = (b * n) + (a * m)
    print(x)



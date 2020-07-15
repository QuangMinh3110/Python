canh_ben_1 = input("nhập giá trị canh bên 1: ")
x = float(canh_ben_1)
canh_ben_2 = input("nhập giá trị canh bên 2: ")
y = float(canh_ben_2)
def tam_giac_vuong(x, y):
    canh_huyen = (((x**2) + (y**2))**(.5))
    k = str(canh_huyen)
    z = 'giá trị canh huyền: '
    print(z + k)
tam_giac_vuong(x, y)


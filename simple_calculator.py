"""
Cho phép người dùng nhập vào một chuỗi tương ứng với 1 phép tính đơn (chỉ chứa 1 toán tử). In ra giá trị phép toán đó
Toán tử hỗ trợ: + - x / ^

Khó: Cho phép người dùng nhập ký tự space, ""

Ví dụ:
Nhập biểu thức: "10 ^ 2"
Kết quả: 100

Real Caculator: tính toán phép tính nhiều toán tử, ví dụ: 10 + 10 + 4 + 5 / 6 + 4
"""
j = (input("nhập giá trị của x: "))
x = int(j)
def f(x):
    z=10 * x / 7
    print(z)
f()

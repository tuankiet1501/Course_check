import sys
# in ra 1 kí tự hay gì đó
print("Hello World")
print("1")
print(0+1)
# nhập input
x = input()
print(x)
# gán giá trị cho 1 biến
y = "3000"
print(y)
# đo bộ nhớ của 1 biến
x = 3
y = '3'
print(type(x))
print(sys.getsizeof(x))
print(type(y))
print(sys.getsizeof(y))
# list
x = ["apple", "banana", "chill guy"]
y = ["a", "b", "c", "abc"]
z = 500000
# thao tác với list
print(x) # in hết tất cả phần tử trong list x
x.append(input()) # thêm vào cuối list phần tử trong ngoặc tròn
x.clear()
x.remove(0) # xóa phần tử trong ngoặc xuất hiện đầu tiên, nếu không có thì bị lỗi
y.sort() # sắp xếp các phần tử từ bé đến lớn
print("Các mặt hàng đã mua: ", x, y)
# sai tên
# hàm
# đã có giá trị của x, y nhưng chưa có giá trị của z
def john(x):
    print(x)

def max(x):
    x = x / 10
    return x
# hàm thủ tục
john(x)
john(y)
john(z)
print(john(z))
# print(john(x) + john(y)) # None
# hàm giá trị
z1=max(z)
print(max(z))
print(max(z) + max(z1)) # 1 số = 55000

# while
x1 = 9
while x1 > 8: # hàm while trước tiên so sánh biểu thức điều kiện, nếu biểu thức đk ok thì sẽ thực hiện khối lệnh ở dưới, SAU ĐẤY lặp lại các bước.
    print("x1 > 8")
    x1 = x1 - 1  # Nếu không thỏa mãn bth điều kiện -> out vòng lặp
# nếu như biểu thức điều kiện ok mãi -> vòng lặp vô tận
y = "abcd"
z = y[2:]
for i in y: # chỉ áp dụng với kiểu dữ liệu string (chuỗi); range(5) = [0,1,2,3,4]
    print(i)
print(z)
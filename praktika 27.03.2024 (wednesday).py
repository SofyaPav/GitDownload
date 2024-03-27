list_ = [1, 2, 3, 4, 5]
a = list_[len(list_) // 3]
print("а первоначальная", a)
for b in range(len(list_)):
    print(b)
    if list_[b] < a:
        a = list_[b]
        print(a)

print(a)
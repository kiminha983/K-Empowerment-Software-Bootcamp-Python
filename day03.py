# input 2 numbers

# start = int(input("start number : "))
# end = int(input("end number : "))
# print(start, end)

# start_end = input("start and end number : ").split()
# print(start_end)
# print(int(start_end[0]), int(start_end[1]))

start = int(input("start number : "))
end = int(input("end number : "))
print(start, end)
for k in range(start, end+1):
    print(k, end=' ')

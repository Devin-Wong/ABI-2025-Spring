numbers = [-1, -3, 0, 7, -6, 9]

# def positive(x):
#     return x>0
# rst = list(filter(positive, numbers))

rst = list(filter(lambda x: x>0, numbers))
print(rst)





# positive_numbers = []
# for i in numbers:
#     if i>0:
#         positive_numbers.append(i)

# print(positive_numbers)
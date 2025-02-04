numbers = [1,2,3,4,5]
# squares = [1,4,9,16,25]

## --- use map function
def square(x):
    return x**2
squares = list(map(square, numbers))
print(squares)

squares_2 = list(map(lambda x: x**2, numbers))
print(squares_2)




## --- tranditional method
# squares = []
# for i in numbers:
#     square = i**2
#     squares.append(square)

# print(squares)
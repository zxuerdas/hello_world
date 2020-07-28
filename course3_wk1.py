# n = input("Please enter your age: ")
# # user types in 18
# print(type(n))
# test commint


p_phrase = "was it a car or a cat I saw"

r_phrase = reversed(p_phrase)
r_phrase = "".join(list(r_phrase))
if r_phrase == p_phrase:
    print("It is palindrome")
else:
    print("It is not")

    print("////////////////////////////")
list1= [5, 2, 1, 4, 9, 10]
min_value = list1[0]
for item in list1:
   if item < min_value:
       min_value = item
print(min_value)
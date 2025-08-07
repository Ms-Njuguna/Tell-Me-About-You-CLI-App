# challenge 1

name = input("What's your name? ")
print(f"Hi {name}")

age = int(input("How old are you? "))
favorite_color = input("What's your favorite color? ")
hobby = input("Anny hobby? ")

print(f"Hello {name}! You are {age} years old, you love {hobby} and your favorite color is {favorite_color}.")


# challenge 2

num1 = int(input("Give me a random number: "))
num2 = int(input("And one more: "))

def calculations(num1, num2):
    total = num1 + num2
    product = num1 * num2
    average = total / 2

    print(f"The sum of the numbers is {total}, product is {product} and the average of the two is {average}.")

calculations(num1, num2)

### function definition ###
def multiples_2_and_3(number):
    if number % 2 == 0:
        print(number, "is a multiple of 2")
    if number % 3 == 0:
        print(number, "is a multiple of 3")
    if number % 2 != 0 and number % 3 != 0:
        print(number, "is neither")

    
### main program ###
multiples_2_and_3(4)
multiples_2_and_3(9)
multiples_2_and_3(12)
multiples_2_and_3(7)
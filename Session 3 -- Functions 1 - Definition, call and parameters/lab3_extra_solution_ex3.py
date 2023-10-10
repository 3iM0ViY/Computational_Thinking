### function definition ###
def layer_triangle(l, opt):
    if opt == "a":
        print("x"*l)
    elif opt == "b":
        nr_of_spaces = 5 - l # note that knowing the total number of layers (5) is relevant here!
        spaces = " "*nr_of_spaces
        crosses = "x"*l
        print(spaces+crosses)
    elif opt == "c":
        nr_of_spaces = (5 - l) # note that knowing the total number of layers (5) is relevant here!
        spaces = " "*nr_of_spaces
        print( spaces + "x "*l)
    else:
        print("error - please enter a valid option")

    
### main program ###
layer_triangle(4, "a")
layer_triangle(4, "b")
print()
layer_triangle(1, "c")
layer_triangle(2, "c")
layer_triangle(3, "c")
layer_triangle(4, "c")
layer_triangle(5, "c")
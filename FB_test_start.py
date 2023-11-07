### PART 1 - TASK 1 ###
def nearest_multiple_of_3(my_number):
    return round(my_number/3) * 3


### PART 1 - TASK 2 ###
def check_value(my_value):
    if my_value < 10:
        return "small"
    elif 10 <= my_value < 50:
        return "medium"
    else:
        return "large"
    

### PART 1 - TASK 3 ###
def count_character_case_insensitive(my_word, capital_char, small_char):
    c = 0
    for i in my_word:
        if i == capital_char or i == small_char:
            c += 1

    return c


### PART 1 - TASK 4 ###
def sum_first_squares(number):
    if number < 0:
        return -1
    i = 0
    res = 0
    while i <= number:
        res += i ** 2
        i += 1

    return res


### PART 1 - TASK 5 ###
def check_double_char(string):
    for i in range(len(string) - 1):
        if string[i] == string[i+1]:
            return True
    else:
        return False


### PART 1 - TASK 6 ###
def return_values_below(my_list, threshold):
    res = []
    for i in my_list:
        if i < threshold:
            res.append(i)

    return res




# TEST CODE : DO NOT CHANGE ANYTHING BELOW THIS LINE

def test():
    
    score = 0
    age_list = [ 34, 23, 26, 26, 27, 18, 60, 35, 59, 26 ]
    
    #test nearest_multiple_of_3
    t1_1 = nearest_multiple_of_3(36)
    t1_2 = nearest_multiple_of_3(4)
    t1_3 = nearest_multiple_of_3(3002)
    print( t1_1 )
    print( t1_2 )
    print( t1_3 )
    
    if t1_1 == 36 and t1_2 == 3 and t1_3 == 3003:
        score += 1
        print( "TEST 1 SUCCEEDED" )
    else:
        print( "TEST 1 FAILED" )

    #test check_value
    t2_1 = check_value( 8 )
    t2_2 = check_value( 73 )
    t2_3 = check_value( 24 )
    t2_4 = check_value( 50 )
    print( t2_1 )
    print( t2_2 )
    print( t2_3 )
    print( t2_4 )
    
    if t2_1 == "small" and t2_2 == "large" and t2_3 == "medium" and t2_4 == "large":
        score += 1
        print( "TEST 2 SUCCEEDED" )
    else:
        print( "TEST 2 FAILED" )
        
    #test count_characters_case_insensitive
    t3_1 = count_character_case_insensitive("Abracadabra", "a", "A")
    t3_2 = count_character_case_insensitive("", "x", "X")
    t3_3 = count_character_case_insensitive("QQQQqqqq0qQqqQQQqqqq", "q", "Q")
    print( t3_1 )
    print( t3_2 )
    print( t3_3 )
    
    if t3_1 == 5 and t3_2 == 0 and t3_3 == 19:
        score += 1
        print( "TEST 3 SUCCEEDED" )
    else:
        print( "TEST 3 FAILED" )

    #test sum_first_squares
    t4_1 = sum_first_squares( 8 )
    t4_2 = sum_first_squares( 0 )
    t4_3 = sum_first_squares( -6 )
    print( t4_1 )
    print( t4_2 )
    print( t4_3 )
    
    if t4_1 == 204 and t4_2 == 0 and t4_3 == -1:
        score += 1
        print( "TEST 4 SUCCEEDED" )
    else:
        print( "TEST 4 FAILED" )
        
        
    #test check_double_char
    t5_1 = check_double_char("bjuehdosleiopm")
    t5_2 = check_double_char("bkillompl")
    t5_3 = check_double_char("qq")
    t5_4 = check_double_char("bkiompAA")
    t5_5 = check_double_char("bkiAAompAA")
    print( t5_1 )
    print( t5_2 )
    print( t5_3 )
    print( t5_4 )
    print( t5_5 )
    
    if t5_1 == False and t5_2 == True and t5_3 == True and t5_4 == True and t5_5 == True:
        score += 1
        print( "TEST 5 SUCCEEDED" )
    else:
        print( "TEST 5 FAILED" )
        
    #test return_values_below
    t6_1 = return_values_below( age_list, 30 )
    t6_2 = return_values_below( age_list, 20 )
    t6_3 = return_values_below( age_list, 10 )
    print( t6_1 )
    print( t6_2 )
    print( t6_3 )
    
    if t6_1 == [ 23, 26, 26, 27, 18, 26 ] and t6_2 == [ 18 ] and t6_3 == []:
        score += 1
        print( "TEST 6 SUCCEEDED" )
    else:
        print( "TEST 6 FAILED" )
        
   #final score 
    print( "\nFinal score =", score, "/ 6" )
    
if __name__ == "__main__":    
    test()
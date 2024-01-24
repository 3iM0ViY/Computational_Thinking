# TASK 1 #

def get_minors(year, minors):
    new_students = []
    new_years = []
    students = minors[0]
    years = minors[1]
    for i in range( 0, len( students ) ):
        print( year - years[i] )
        if year - years[i] < 18:
            print( "minor" )
            new_students += [students[i]]
            new_years += [years[i]]
    return [new_students, new_years]

# TASK 2 #

def read_from_file(filename):
    file = open( filename )
    line_nr = 1
    students = []
    years = []
    cur_year = 0
    for line in file:
        if line_nr % 2 == 1:
            cur_year = int(line[4:8])
        else:
            if 2022 - cur_year < 18:
                years += [cur_year]
                students += [line.rstrip()]
        line_nr += 1
    return [ students, years ]
    

### DON'T CHANGE ANYTHING BELOW THIS LINE ###

def test():
    
    score = 0
    
    # TEST 1 #
    print("# TEST 1 : get_minors() #")
    t1_1 = get_minors(2023, [['Sarah', 'James', 'Ashley'], [2019, 2019, 2005]])
    t1_2 = get_minors(2020, [['Sarah', 'James', 'Ashley'], [2019, 2019, 2005]])
    print(t1_1)
    print(t1_2)
    if t1_1 == [['Sarah', 'James'], [2019, 2019]] and t1_2 == [['Sarah', 'James', 'Ashley'], [2019, 2019, 2005]]:
        score += 2
        print( "TEST 1 SUCCESS" )
    else:
        print( "TEST 1 FAILED" )
    print("--------------------")
        
    # TEST 2 #
    print("# TEST 2 : read_from_file() #")
    t2_1 = read_from_file("minors.txt")
    t2_2 = read_from_file("adults.txt")
    print(t2_1)
    print(t2_2)
    if t2_1 == [['Sarah', 'James', 'Ashley'], [2019, 2019, 2005]] and t2_2 == [[],[]]:
        score += 4
        print( "TEST 2 SUCCESS" )
    else:
        print( "TEST 2 FAILED" )
    print("--------------------")
    

    
    print("Final score:", score)
    
if __name__ == "__main__":
    test()
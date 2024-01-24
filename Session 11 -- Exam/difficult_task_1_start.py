# TASK 1 #
# [['Sarah', 'James', 'Ashley'], [2019, 2019, 2005]]
def get_minors(year, minors):
    res = [[], []]
    for i, y in enumerate(minors[1]):
        if 0 <= year - y < 18 :
            res[0].append(minors[0][i])
            res[1].append(minors[1][i])
    return res

# TASK 2 #

def read_from_file(filename):
    all = [[], []]
    c = 0
    with open(filename) as f:
        for l in f:
            c += 1
            if c % 2 == 0:
                all[0].append(l.replace("\n", ""))
            else:
                all[1].append(int(l.replace("\n", "")[4:]))
    res = get_minors(2022, all)
    return res

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
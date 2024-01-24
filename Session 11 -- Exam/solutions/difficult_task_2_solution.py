# TASK 1 #

def is_valid(queen_positions):
    for i in range( 0, len(queen_positions) ):
        if queen_positions[i][0] not in "abcdefgh" or queen_positions[i][1] not in "12345678":
            return False
        for j in range( 0, len(queen_positions) ):
            if queen_positions[i] == queen_positions[j] and i != j:
                return False     
    return True


# TASK 2 #

def squares_covered(queen_position):
    ranks = "87654321"
    files = "abcdefgh"
    qf = queen_position[0]
    qr = queen_position[1]
    board = []
    
    for rank in ranks:
        cur_row = []
        for file in files:
            
            #queen pos
            if rank == qr and file == qf:
                cur_row += [-1]
                
            #same rank or file as queen
            elif rank == qr or file == qf:
                cur_row += [1]
                
            else:
                
                #same diagonal as queen
                diagonal = False
                qr_index = ranks.index( qr )
                qf_index = files.index( qf )
                r_index = ranks.index( rank )
                f_index = files.index( file )
                vertical_diff = qr_index - r_index
                horizontal_diff = qf_index - f_index
                if vertical_diff == horizontal_diff or vertical_diff == -horizontal_diff:
                    cur_row += [1]
                    
                #not covered by queen
                else:
                    cur_row += [0]
                    
        board += [cur_row]         
        
    return board


            
### DON'T CHANGE ANYTHING BELOW THIS LINE ###

def test():
    
    score = 0
    
    # TEST 1 #
    t1_1 = is_valid([])
    t1_2 = is_valid(["b4", "c6"])
    t1_3 = is_valid(["b4", "c6", "b4"])
    t1_4 = is_valid(["4b", "c6"])
    t1_5 = is_valid(["4b", "j9"])
    print("# TEST 1 #")
    print(t1_1)
    print(t1_2)
    print(t1_3)
    print(t1_4)
    print(t1_5)
    if t1_1 and t1_2 and not t1_3 and not t1_4 and not t1_5:
        score += 3
        print( "Test 1 success" )
    print("--------------------")
    
    
    # TEST 2 #
    t2_1 = squares_covered("d3")
    t2_2 = squares_covered("a1")
    print("# TEST 2 #")
    print(t2_1)
    print(t2_2)
    
    answer2_1 = [[0, 0, 0, 1, 0, 0, 0, 0], #rank 8
                 [0, 0, 0, 1, 0, 0, 0, 1], #rank 7
                 [1, 0, 0, 1, 0, 0, 1, 0], #rank 6
                 [0, 1, 0, 1, 0, 1, 0, 0], #rank 5
                 [0, 0, 1, 1, 1, 0, 0, 0], #rank 4
                 [1, 1, 1,-1, 1, 1, 1, 1], #rank 3
                 [0, 0, 1, 1, 1, 0, 0, 0], #rank 2
                 [0, 1, 0, 1, 0, 1, 0, 0]] #rank 1
            #file A  B  C  D  E  F  G  H
    
    answer2_2 = [[1, 0, 0, 0, 0, 0, 0, 1], #rank 8
                 [1, 0, 0, 0, 0, 0, 1, 0], #rank 7
                 [1, 0, 0, 0, 0, 1, 0, 0], #rank 6
                 [1, 0, 0, 0, 1, 0, 0, 0], #rank 5
                 [1, 0, 0, 1, 0, 0, 0, 0], #rank 4
                 [1, 0, 1, 0, 0, 0, 0, 0], #rank 3
                 [1, 1, 0, 0, 0, 0, 0, 0], #rank 2
                [-1, 1, 1, 1, 1, 1, 1, 1]] #rank 1
            #file A  B  C  D  E  F  G  H
    
    if t2_1 == answer2_1 and t2_2 == answer2_2:
        score += 3
        print( "Test 2 success" )
    print("--------------------")
        
    print("Final score:", score)    
    
if __name__ == "__main__":
    test() 
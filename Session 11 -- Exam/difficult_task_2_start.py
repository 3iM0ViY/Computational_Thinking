# TASK 1 #

def is_valid(queen_positions):
    if queen_positions != []:
        for p in queen_positions:
            test = queen_positions
            test.remove(p)
            if p not in test: # check repetition
                if p[0] in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] and 0 < int(p[1]) <= 8:
                    return True
            return False # instead of two else statements
    else:
        return True


# TASK 2 #

def squares_covered(queen_position):
    alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    board = []
    r = 0
    # precreate the board for further usage by coordinates
    while r < 8:
        l = []
        c = 0
        while c < 8:
            l.append(0)
            c += 1
        board.append(l)
        r += 1
    # print(board)

    # print(queen_position)

    col = 0 # get column number from letter
    for letter in alph:
        if letter == queen_position[0]:
            break
        col += 1

    for i, r in enumerate(board): # 2d coordinates
        if i == int(queen_position[1]) - 1: # the line on which the queen lies
            t = 0
            for c in r:
                if t == col: # queen's line
                    board[7-i][col] = -1 # queen position

                    # diagonals - going away to a distance d from position
                    # this whole part is quite gibberish and blasphemous, but works - don't fix it
                    d = 1
                    while d < 8**2: # squared to cover every box
                        # here try\except protect in debugging from IndexOutOfBounds 
                        if col - d >= 0:
                            board[7-i - d][col - d] = 1 # top left
                        if col + d < 8:
                            board[7-i - d][col + d] = 1 # top right
                        if i - d >= 0: 
                            board[7-i + d][col + d] = 1 # bottom right
                        if i - d >= 0:
                            board[7-i + d][col - d] = 1 # bottom left
                        d += 1
                else: # every other place on queen's line
                    board[7-i][t] = 1 # horizontal
                t += 1
        else:
            t = 0
            for c in r:
                if t == col:
                    board[7-i][col] = 1 # vertical
                t += 1

    # for l in board:
    #     print(l)
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
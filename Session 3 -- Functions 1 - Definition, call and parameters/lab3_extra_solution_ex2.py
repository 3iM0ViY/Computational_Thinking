### function definition ###
def time_conv(h, m):
    if h >= 12:
        h_am = h - 12
        indication = "pm"
    else:
        h_am = h
        indication = "am"
    message = str(h_am) + ":" + str(m) + indication
    #note: str(*integer*) means: interpret this integer as a string
    print(message)

    
### main program ###
hour = 19
minutes = 20
time_conv(hour, minutes)

hour = 7
minutes = 15
time_conv(hour, minutes)
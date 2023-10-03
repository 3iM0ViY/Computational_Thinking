park_open = True
day = "Thursday"
age = 22

if park_open:
    if age <= 6:
        print( "Free admission" )
    elif age >= 60:
        print( "Ticket price = €20" )
    else:
        if day == "Saturday" or day == "Sunday":
            print( "Ticket price = €45" )
        else:
            print( "Ticket price = €35" )
else:
    print( "Park is closed, come back some other time" )
    
    
timeTable = ["Physics", "English", "Computer Science", "Helicoptor Maintenance"]


for i in range(0, 26):
    
    currentCourse = timeTable[ i % 4 ]
    
    print( "i = " + str(i) + "\t" + "i % 4 = " + str(i%4) + "\t" + currentCourse )

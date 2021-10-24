from sys import exit

WELCOME = "                         WELCOME"          
LINE = "---------------------------------------------------------"
L1_HEADER = "                        Lesson # 1"
L2_HEADER = "                        Lesson # 2"  
L3_HEADER = "                        Lesson # 3"  
L4_HEADER = "                        Lesson # 4"  
L5_HEADER = "                        Lesson # 5"  
L6_HEADER = "                        Lesson # 6"  
L7_HEADER = "                        Lesson # 7"
L8_HEADER = "                        Lesson # 8" 
L9_HEADER = "                        Lesson # 9" 
L10_HEADER = "                        Lesson # 10" 
UNDEFINED_HEADER = "             This lesson is not yet published"        

def displayLessonIntroMessage(num):

    ERROR = False

    print(LINE)

    if num == 1:
        print(L1_HEADER)
    elif num == 2:
        print(L2_HEADER)
    elif num == 3:
        print(L3_HEADER)
    elif num == 4:
        print(L4_HEADER)
    elif num == 5:
        print(L5_HEADER)
    elif num == 6:
        print(L6_HEADER)
    elif num == 7:
        print(L7_HEADER)
    elif num == 8:
        print(L8_HEADER)
    elif num == 9:
        print(L9_HEADER)
    elif num == 10:
        print(L10_HEADER)
    else:
        ERROR = True
        print(UNDEFINED_HEADER)

    print(LINE)

    if ERROR:
        exit()

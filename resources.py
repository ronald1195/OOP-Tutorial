from sys import exit, path
import os

WELCOME = "WELCOME"          
LINE = "-"
L1_HEADER = "Lesson # 1"  
L2_HEADER = "Lesson # 2"  
L3_HEADER = "Lesson # 3"  
L4_HEADER = "Lesson # 4"  
L5_HEADER = "Lesson # 5"  
L6_HEADER = "Lesson # 6"  
L7_HEADER = "Lesson # 7"
L8_HEADER = "Lesson # 8" 
L9_HEADER = "Lesson # 9" 
L10_HEADER = "Lesson # 10" 
UNDEFINED_HEADER = "This lesson is not yet published"        


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    OUTPUTGREY = '\033[90m'


def displayLessonIntroMessage(num):

    ERROR = False
    # window_size, height= pyautogui.size()
    window_size = os.get_terminal_size().columns

    print(LINE * window_size)

    if num == 1:
        # print(L1_HEADER)
        print( " " * ((window_size//2) - len(L1_HEADER)) + L1_HEADER)
    elif num == 2:
        print( " " * ((window_size//2) - len(L2_HEADER)) + L2_HEADER)
    elif num == 3:
        # print(L3_HEADER)
        print( " " * ((window_size//2) - len(L3_HEADER)) + L3_HEADER)
    elif num == 4:
        # print(L4_HEADER)
        print( " " * ((window_size//2) - len(L4_HEADER)) + L4_HEADER)
    elif num == 5:
        # print(L5_HEADER)
        print( " " * ((window_size//2) - len(L5_HEADER)) + L5_HEADER)
    elif num == 6:
        # print(L6_HEADER)
        print( " " * ((window_size//2) - len(L6_HEADER)) + L6_HEADER)
    elif num == 7:
        # print(L7_HEADER)
        print( " " * ((window_size//2) - len(L7_HEADER)) + L7_HEADER)
    elif num == 8:
        # print(L8_HEADER)
        print( " " * ((window_size//2) - len(L8_HEADER)) + L8_HEADER)
    elif num == 9:
        # print(L9_HEADER)
        print( " " * ((window_size//2) - len(L9_HEADER)) + L9_HEADER)
    elif num == 10:
        # print(L10_HEADER)
        print( " " * ((window_size//2) - len(L10_HEADER)) + L10_HEADER)
    else:
        ERROR = True
        # print(UNDEFINED_HEADER)
        print( " " * ((window_size//2) - len(UNDEFINED_HEADER)) + UNDEFINED_HEADER)

    print(LINE * window_size)

    if ERROR: 
        exit()


class TestBed:

    # class variables
    total = 0

    succeded_tests = 0

    # Constructor
    def __init__(self) -> None:
        pass

    def verifySolution(self, student_output, desired_output):
        # Increment the amount of tests created for the  test
        self.total += 1

        print(f"{bcolors.OUTPUTGREY}Your output: {student_output}{bcolors.ENDC}")
        print(f"{bcolors.OUTPUTGREY}Desired output: {desired_output}{bcolors.ENDC}")
        if student_output == desired_output:
            self.succeded_tests += 1
            self.printSuccessMessage()
        else:
            self.printFailMessage()



    def printSuccessMessage(self):
        print(f"{bcolors.OKGREEN}Testbed PASSED!{bcolors.ENDC}")
        print(" ")

    def printFailMessage(self):
        print(f"{bcolors.FAIL}Testbed FAILED.{bcolors.ENDC}")
        print(" ")


    def printTestBedSummary(self):
        color = bcolors.OKGREEN if self.total == self.succeded_tests else bcolors.FAIL
        print(f"{color}------------------- TESTBED COMPLETED -------------------{bcolors.ENDC}")
        print(f"{color}Summary: [{self.succeded_tests}] of [{self.total}] passed{bcolors.ENDC}")



if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   pass

# for i in range(0, 16):
#     for j in range(0, 16):
#         code = str(i * 16 + j)
#         print("\033[" + code + "m " + code.ljust(4))
#     print("\033[0m")
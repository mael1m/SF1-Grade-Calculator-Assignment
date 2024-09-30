LPP = int(input("Enter the number of labs completed: "))
#LPP = Lab Programming Problems, LPPG = Lab Programming Grade
if (LPP) >= 6:
    LPPG = 100
else:
    LPPG = (LPP / 6) * 100

Q = int(input("Enter the number of quizzes completed: "))
# Q = Quizzes, QG = Quiz Grades
if (Q) >= 6:
    QG = 100
else:
    QG = (Q / 6) * 100

A1 = int(input("Enter grade for Assignment 1: "))
A1G = A1 * 0.04
# A1 = Assignment 1, A1G = Assignemnt 1 Grade

A2 = int(input("Enter grade for Assignment 2: "))
A2G = A2 * 0.04

A3 = int(input("Enter grade for Assignment 3: "))
A3G = A3 * 0.04

A4 = int(input("Enter grade for Assignment 4: "))
A4G = A4 * 0.04

M1 = int(input("Enter grade for Midterm 1: "))
M1G = M1 * 0.125
#M1 = Midterm 1, M1G = Midterm 1 Grade

M2 = int(input("Enter grade for Midterm 2: "))
M2G = M2 * 0.125

FE = int(input("Enter grade for Final Exam: "))
FEG = FE * 0.18
# FE = Final Exam, FEG = Final Exam Grade

MFP = int(input("Enter grade for Midterms and Final Preparation: "))
MFPG = MFP * 0.06
# MFP = Midterm and Final Preparation, MFPG = Midterm and Final Preparation Grade

FG = float((LPPG * 0.2) + (QG * 0.15) + A1G + A2G + A3G + A4G + M1G + M2G + FEG + MFPG)
#FG = Final Grade

print("your grade is: ", float(FG))

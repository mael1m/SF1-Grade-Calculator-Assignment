A4 = int(input("Enter grade for Assignment 4: "))
A4G = A4 * 0.04
M1 = int(input("Enter grade for Midterm 1: "))
M1G = M1 * 0.125
# M1 = Midterm 1, M1G = Midterm 1 Grade
M2 = int(input("Enter grade for Midterm 2: "))
M2G = M2 * 0.125
FE = int(input("Enter grade for FInal Exam: "))
FEG = FE * 0.18
# FE = Final Exam, FEG = Final Exam Grade
MFP = int(input("Enter grade for Midterms and Final Preparation: "))
MFPG = MFP * 0.06
# MFP = Midterm and Final Preparation, MFPG = Midterm and Final Preparation Grade
FG = float((LPPG * 0.2) + (QG * 0.15) + A1G + A2G + A3G + A4G + M1G + M2G + FEG + MFPG)
#FG = Final Grade
print("your grade is: ", float(FG))

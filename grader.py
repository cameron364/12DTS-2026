gpa = 0

ASSESSMENT_CREDITS = [6, 6, 4, 3]
credit_excellence = []
credit_merit = []

# error detection for score
def score_cal():
    while True:
        try:
            assessment = int(input("Score from assessment 1 (0-100): "))
            if assessment > 100:
                print("Score is not bigger than 100")
            elif assessment < 0:
                print("Score is bigger than 0")
            else:
                return assessment
                break
        except ValueError:
            print("Not a integer")

# checks score and gets the grade
def grade_checker(score):
    if score > 85:
        return "Excellence"
    elif score > 65:
        return "Merit"
    elif score > 50:
        return "Achieved"
    else:
        return "Not Achieved"

print("Excellent is greater than 85")
print("Merit is greater than 65")
print("Achieved is greater than 50")
print("Not Achieved is 50 and below")
print()

for i in range(1,5):
    if i == 1:
        assessment_1_score = score_cal()
        assessment_1_grade = grade_checker(assessment_1_score)
        curr_assessment_score = assessment_1_score
        curr_assessment_grade = assessment_1_grade
    elif i == 2:
        assessment_2_score = score_cal()
        assessment_2_grade = grade_checker(assessment_2_score)
        curr_assessment_score = assessment_2_score
        curr_assessment_grade = assessment_2_grade
    elif i == 3:
        assessment_3_score = score_cal()
        assessment_3_grade = grade_checker(assessment_3_score)
        curr_assessment_score = assessment_3_score
        curr_assessment_grade = assessment_3_grade
    elif i == 4:
        assessment_4_score = score_cal()
        assessment_4_grade = grade_checker(assessment_4_score)
        curr_assessment_score = assessment_4_score
        curr_assessment_grade = assessment_4_grade

    if curr_assessment_grade == "Excellence":
        credit_excellence.append(ASSESSMENT_CREDITS[i-1])
        credit_merit.append(ASSESSMENT_CREDITS[i-1])
    if curr_assessment_grade == "Merit":
        credit_merit.append(ASSESSMENT_CREDITS[i - 1])

    if curr_assessment_grade == "Not Achieved":
        print("Assessment", i, "score is", curr_assessment_score, "and grade is", curr_assessment_grade, "got no credits")
    else:
        print("Assessment", i, "score is", curr_assessment_score, " and grade is", curr_assessment_grade, "got",  ASSESSMENT_CREDITS[i-1],"credits at", curr_assessment_grade)
    gpa += curr_assessment_score * ASSESSMENT_CREDITS[i-1]

gpa = gpa / (sum(ASSESSMENT_CREDITS))

print("GPA is",gpa)

if sum(credit_excellence) >= 14:
    print("Excellence course endorsement")
elif sum(credit_merit) >= 14:
    print("Merit course endorsement")

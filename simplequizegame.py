print("******************")
print("Welcome to My Quiz Game!!!")
question_bank=[{
    "text":"The ability of one class to aquire methods and attributes from another class is called------","answer":"A"
},
               {"text":"which of the following is a type of inheritance?","answer":"D"},
               {"text":"What type of inheritance has multiple subclasses to a single superclass?","answer":"C"},
               {"text":"What is the depth of multilevel inheritance in Python?","answer":"C"},
               {"text":"What does MRO stand for?","answer":"B"}]

options=[
    ["A.Inheritance","B.Abstraction","C.Polymorphism","D.Objects"],
    ["A.Single","B.Double","C.Multiple","D.both A and C"],
    ["A.Multiple Inheritance","B.Multilevel Inheritance","C.hieraechical Inheritance","D.None of these"],
    ["A.Two level","B.Any level","C.Any level","D.None of these"],
    ["A.Method Recursive Object","B.Method Resolution Order","C.Main Resolution Order","D.Method Resolution Object"]
]

score=0
def check_answer(user_guess,correct_answer):
    if user_guess==correct_answer:
        return True
    else:
        return False
    
for question_num in range(len(question_bank)):
    print("*********************" )
    print(question_bank[question_num]["text"])
    for i in options[question_num]:
        print(i)
    check = True
    while check:
        guess=input("Enter your answer(A/B/C/D): ").upper()
        is_correct=check_answer(guess,question_bank[question_num]["answer"])
        if is_correct:
            print("Correct Answer")
            score += 1
            break
            
        else:
            print("Incorrect Answer")
            break
    continue1 = input("You want to continue if you want then press y and if not then press n : ")
    if continue1 == 'y':
        continue
    else:
        print("******************-- THANK FOR USING QUIZ GAME --*****************")
        break
    
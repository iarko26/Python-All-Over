questions = [
    [
        "Which language is used for web development?",
        "A. Python",
        "B. Java",
        "C. HTML",
        "D. C#",
        "C"  # Correct answer
    ],
    [
        "Which of the following is a JavaScript framework?",
        "A. Laravel",
        "B. Django",
        "C. React",
        "D. Flask",
        "C"  # Correct answer
    ],
    [
        "Which of these is a front-end development language?",
        "A. PHP",
        "B. SQL",
        "C. CSS",
        "D. Python",
        "C"  # Correct answer
    ],
    [
        "Which language is primarily used for Android app development?",
        "A. Swift",
        "B. Kotlin",
        "C. Objective-C",
        "D. Ruby",
        "B"  # Correct answer
    ]
]

levels = [1000, 2000, 3000, 5000]

def instructions():
    print("Ei Khelai Tumake shagotom! Khela shuru korar age ei instructions gulo poro")
    print("ami tumake kichu prashno korbo, tumi prashno gulo uttor dao")
    print("Tumi joto taka jette chao totota uttor dao")
    print("Tumi jodi uttor dao tahole tumi jabe next level e")
    print("Prothom proshoner jnno kono sahhaayyok nei")
    print("Ditiyo proshoner jnno ekta sahhaayyok thakbe")
    print("Tritiyo proshoner jnno duita sahhaayyok thakbe")
    print("Choturtho proshoner jnno tin ta sahhaayyok thakbe")
    print("Tumi jodi kono proshoner jnno sahhaayyok na nite chao tahole 'skip' likho")
    print("Tumi jodi game theke ber hote chao tahole 'quit' likho")
    print("Tumi jodi prothom dui proshner uttor bhul dao tahole tumar khela sesh ")
    print("Tumi jodi prothom proshner uttor thik dao kintu porer dui proshner uttor bhul dao tahole tumar jeta taka ordhek hobe")

def game():
    instructions()
    n = len(questions)
    prizes = 0
    consecutive_wrong = 0
    first_question_answered = False
    for i in range(n):
        question = questions[i]
        select_level = int(input("Tumi koto taka niye khelte chao? 1000,2000,3000,5000: "))
        print("Tumi koto taka niye khelte chao?", select_level)
        print(question[0])
        print(question[1])
        print(question[2])
        print(question[3])
        print(question[4])
        answer = input("Tumi kono uttar dao: ")
        if answer.lower() == "q":
            print("Tumar khela sesh")
            return
        elif answer == question[5]:
            if i == 0:
                first_question_answered = True
            prizes = select_level
            consecutive_wrong = 0
            print(f"Tumi jeet gale {prizes} taka")

        else:
            if consecutive_wrong==0 and not first_question_answered:
                print("Tumar prothom proshner uttor bhul")
                return
            elif consecutive_wrong==1 and not first_question_answered:
                prizes=prizes//2
                print(f"Tumar jeta {prizes} taka ordhek hoye gelo")
                return
      
   
          
            

    return prizes

final_prize = game()
if final_prize:
    print(f"Tumar jeta {final_prize} taka")
else:
    print("Tumar kono taka nai")
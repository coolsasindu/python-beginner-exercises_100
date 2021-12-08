from question import Question

question_prompts = [
    "what color are Apple ? \n (a) Red,Green\n (b) blue\n (c) pink \n\n",
    "what color are Banana ? \n (a) Red\n (b) yellow\n (c) pink \n\n",
    "what color are Strawberries ? \n (a) black\n (b) Gray\n (c) Red \n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c")

]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("you got " + str(score) + "/" + str(len(questions)) + " Correct")


run_test(questions)

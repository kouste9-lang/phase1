from quest import Question

question_prompts = [
    "What is the capital of France?\n(a) Berlin\n(b) London\n(c) Paris\n(d) Madrid\n\n",
    "What is 2 + 2?\n(a) 3\n(b) 4\n(c) 5\n(d) 6\n\n",
    "What is the largest ocean on Earth?\n(a) Atlantic Ocean\n(b) Indian Ocean\n(c) Arctic Ocean\n(d) Pacific Ocean\n\n"
]

questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "d")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer.lower() == question.answer:
            score += 1
    print(f"You got {score}/{len(questions)} correct.")

run_test(questions)
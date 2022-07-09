import random
from string import ascii_lowercase
NUM_QUESTIONS = 5
QUESTIONS = {
    "Who is the richest person on the Earth?":[
        "Bhargav",
        "Elon Musk",
        "Jeff Bazoes",
        "Bill Gates",
    ],
    "Who is the best actor on the planet Earth?":[
        "Bhargav",
        "Prabhas",
        "Leonardo",
        "Jonny Depp",
    ],
    "What is the capital city of USA?":[
        "Washington DC",
        "Newyork",
        "California",
        "Atlanta",
    ]
}
def prepare_questions(questions,num_questions):
    num_questions = min(num_questions,len(questions))
    return random.sample(list(questions.items()),k=num_questions)


def get_answer(question,alternatives):
    print(f"{question}")
    labeled_alternatives = dict(zip(ascii_lowercase,alternatives))
    for label,alternative in labeled_alternatives.items():
        print(f'  {label})  {alternative}')
    while (answer_labeled := input("Choice?")) not in labeled_alternatives:
        print(f'Please choose the mentioned one {", ".join(labeled_alternatives)}')
    return labeled_alternatives[answer_labeled]


def ask_question(question,alternatives):
    correct_answer = alternatives[0]
    ordered_alternatives = random.sample(alternatives,k=len(alternatives))
    answer = get_answer(question,ordered_alternatives)
    if answer == correct_answer:
        print("Correct!")
        return 1
    else:
        print(f"The correct answer is {correct_answer!r}, not {answer!r}")
        return 0


def run_quiz():
    questions = prepare_questions(QUESTIONS,num_questions=NUM_QUESTIONS)
    num_correct = 0
    for num,(question,alternatives) in enumerate(questions,start=1):
        print(f"QUESTION {num}:")
        num_correct += ask_question(question,alternatives)
    print(f"You got {num_correct} corrected out of {len(QUESTIONS)} questions")


if __name__ == '__main__':
    run_quiz()

import time
import random

quiz = {
    "Solar system": [
        {"question": "Which planet is known as the Red Planet?", "options": ["A. Mars", "B. Earth", "C. Saturn", "D. Uranus"], "answer": "A"},
        {"question": "Which planet is known for its prominent ring system?", "options": ["A. Mars", "B. Earth", "C. Saturn", "D. Uranus"], "answer": "C"},
        {"question": "What is the largest planet in our solar system?", "options": ["A. Mars", "B. Jupiter", "C. Saturn", "D. Uranus"], "answer": "B"},
        {"question": "Which planet is closest to the Sun?", "options": ["A. Venus", "B. Earth", "C. Mercury", "D. Mars"], "answer": "C"},
        {"question": "Which planet is farthest from the Sun?", "options": ["A. Neptune", "B. Uranus", "C. Jupiter", "D. Saturn"], "answer": "A"}
    ],
    "Python": [
        {"question": "Which keyword is used to define a function in Python?", "options": ["A. func", "B. def", "C. function", "D. define"], "answer": "B"},
        {"question": "Which data type is immutable?", "options": ["A. set", "B. dictionary", "C. list", "D. tuple"], "answer": "D"},
        {"question": "Who developed Python Programming Language?", "options": ["A. Dennis Ritchie", "B. James Gosling", "C. Guido van Rossum", "D. Bjarne Stroustrup"], "answer": "C"},
        {"question": "Which symbol is used for comments in Python?", "options": ["A. //", "B. <!--", "C. #", "D. /*"], "answer": "C"},
        {"question": "Which method is used to add an element to a list?", "options": ["A. push()", "B. insert()", "C. add()", "D. append()"], "answer": "D"}
    ],
    "Mathematics": [
        {"question": "What is the value of π (pi) rounded to two decimal places?", "options": ["A. 3.12", "B. 3.14", "C. 3.16", "D. 3.18"], "answer": "B"},
        {"question": "What is 7 × 8?", "options": ["A. 56", "B. 58", "C. 48", "D. 64"], "answer": "A"},
        {"question": "What is the square root of 81?", "options": ["A. 7", "B. 8", "C. 9", "D. 10"], "answer": "C"},
        {"question": "What is 12% of 200?", "options": ["A. 24", "B. 20", "C. 28", "D. 22"], "answer": "A"},
        {"question": "What is the next prime number after 7?", "options": ["A. 9", "B. 10", "C. 11", "D. 13"], "answer": "C"}
    ]
}

def choose_category():
    print("Available categories are:")
    for cat in quiz:
        print(f"- {cat}")
    while True:
        category = input("Choose a category: ").strip().title()
        if category in quiz:
            return category
        print("Invalid category! Try again.")

def run_quiz(questions):
    score = 0
    selected_questions = random.sample(questions, 3)
    for index, qu in enumerate(selected_questions):
        print(f"\nQuestion {index + 1}/3: {qu['question']}")
        for option in qu['options']:
            print(option)
        start_time = time.time()
        answer = input("You have 10 seconds. Your Answer (A/B/C/D): ").strip().upper()
        elapsed_time = time.time() - start_time

        if elapsed_time > 10:
            print("⏰ Time's up! You missed the question.")
        elif answer == qu['answer']:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong answer! Correct answer was {qu['answer']}.")

    print(f"\nFinal Score: {score}/3")
    if score == 3:
        print("🎉 Great job!")
    elif score == 2:
        print("👍 Good effort!")
    elif score == 1:
        print("😬 Fail. Better luck next time.")
    else:
        print("🥴 Ouch. 0/3 hurts.")

def main():
    print("====== Welcome to Quiz Game ======")
    print("✨ Have Fun ✨")
    category = choose_category()
    print(f"\nYou selected: {category}")
    run_quiz(quiz[category])

if __name__ == "__main__":
    main()

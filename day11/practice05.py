questions = [
    {
        "question": "Python kis type ki language hai?",
        "options": ["A. Compiled", "B. Interpreted", "C. Machine", "D. Assembly"],
        "answer": "B"
    },
    {
        "question": "Python ka creator kaun hai?",
        "options": ["A. James Gosling", "B. Dennis Ritchie", "C. Guido van Rossum", "D. Elon Musk"],
        "answer": "C"
    },
    {
        "question": "Python me function define karne ke liye kaunsa keyword use hota hai?",
        "options": ["A. function", "B. define", "C. func", "D. def"],
        "answer": "D"
    },
    {
        "question": "List ko kaunse brackets me likhte hain?",
        "options": ["A. {}", "B. ()", "C. []", "D. <>"],
        "answer": "C"
    },
    {
        "question": "Python file ka extension kya hota hai?",
        "options": ["A. .java", "B. .py", "C. .js", "D. .html"],
        "answer": "B"
    }
]

prize_money = [1000, 5000, 10000, 50000, 100000]

print("Welcome to Kaun Banega Crorepati")

money_won = 0

for i in range(len(questions)):
    q = questions[i]
    print(f"Question {i+1} for ₹{prize_money[i]}")
    print(q["question"])

    for option in q["options"]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D) or Q to Quit: ").upper()

    if user_answer == "Q":
        print(f"App game chodd rahe hai. Aapne jeete hain ₹{money_won}")
        break

    if user_answer == q["answer"]:
        money_won = prize_money[i]
        print("Sahi jawab \n")
    else:
        print("Galat jawab\n")
        print(f"sahi jawab tha: {q['answer']}")
        print(f"Aap ₹{money_won} ke sath game se bahar ho gaye")
        break
else:
    print(f"Mubarak ho! Appne jeete hai total ₹{money_won}")

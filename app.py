from Test import Test

question_prompts = [
    "1). When I do well in school or I pass an exam it is because it was easy.",
    "2). If I fail in an exam that doesn't motivate me to learn for other exams.",
    "3). 'The right man at the right place' is the recipe for success.",
    "4). Participating in political meetings is usually ineffective, no one takes them into account.",
    "5). Intelligence is given to you at birth and there is nothing you can do to change things.",
    "6). Success is due to luck, not our abilities.",
    "7). The impression people form about you depends on them and them alone and you can't do anything to change it.",
    "8). If you're going to sick, you're going to get sick anyway and there's not much you can do about it.",
    "9). You can't escape destiny.",
    "10). If there is a soulmate somewhere in the world he/she will find you, it was written in the stars."
]

TheQuestions = [
    Test(question_prompts[0], "1", "2", "3", "4"),
    Test(question_prompts[1], "1", "2", "3", "4"),
    Test(question_prompts[2], "1", "2", "3", "4"),
    Test(question_prompts[3], "1", "2", "3", "4"),
    Test(question_prompts[4], "1", "2", "3", "4"),
    Test(question_prompts[5], "1", "2", "3", "4"),
    Test(question_prompts[6], "1", "2", "3", "4"),
    Test(question_prompts[7], "1", "2", "3", "4"),
    Test(question_prompts[8], "1", "2", "3", "4"),
    Test(question_prompts[9], "1", "2", "3", "4")
]

def run_test(questions):
    score = 0
    for question in questions:
        test = 0
        while test == 0:
            answer = input(question.prompt + "\n(1)Strongly disagree (2)Disagree (3)Agree (4)Strongly agree)\n\n")
            if answer == "1" or answer == "2" or answer == "3" or answer == "4":
                test = 1
            else:
                test = 0
                print("Enter a valid answer (Example: 1 / 2 / 3 / 4)")

        if answer == question.answer1:
            score += 1
        elif answer == question.answer2:
            score += 2
        elif answer == question.answer3:
            score += 3
        elif answer == question.answer4:
            score += 4

    if score <= 15:
        print("Your style is intern")
    elif score > 15 and score <= 20:
        print("Your style is  mixt to intern")
    elif score > 20 and score < 25:
        print("Your style is  mixt to extern")
    else:
        print("Your style is extern")

run_test(TheQuestions)
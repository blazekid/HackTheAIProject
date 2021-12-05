class Question0:
    question = "Would you like to play a game for the next clue?"
    answer = ["yes", "no"]
    prompts = ["Let's start!!!", "You seriously think this will work?"]

class Question1:
    question = "Thirty white horses on a red hill: first they champ, then they stamp, then they stand still. What am I?"
    answer = ["tooth", "teeth"]
    prompts = ["Almost There", "Not that Far", "Try better"]

class Question2:
    question = "What's round, but not always around?\n "\
               "It's light sometimes; it's dark sometimes," \
               "\nEveryone wants to walk all over me.\nWhat am I?"
    answer = ["moon"]
    prompts = ["Almost There", "Not that Far", "Try better"]

class Question3:
    question = "Tear one off and scratch my head\n What once was red is black instead"
    answer = ["match"]
    prompts = ["Almost There", "Not that Far", "Try better"]

class Question4:
    question = "As I was going to St. Ives,\n I met a man with seven wives,\n Every wife had seven sacks,\n Every sack had seven cats,"\
                "Every cat has seven kits.\n Kits, cats, sacks, and wives,\n How many were going to St. Ives?"
    answer = ["one","1"]
    prompts = ["Almost There", "Not that Far", "Try better"]

def print_next_clue():
    print ("Loading..............")
    print ("This is the next clue")
    raw_input("Press Enter to exit!!!")
    exit()

total_questions = 5
f = open("C:\\Users\\1000256474\\Desktop\\Quiz\\Hunt\\art.txt", "r")
print(f.read())

input = raw_input("Enter your response: ").strip(" ")

if input == "yes":
    print ("Let's start the fun then!!!!")
else:
    print ("You seriously think it will work???")
    input = raw_input("Enter your response")
    if input == "yes":
        print ("Haha don't be serious? I am asking you last time you sure about this? you don't want to play?")
        input = raw_input("Enter your response")
        if input == "yes":
            print ("OK..... you cracked it!!!?")
            print_next_clue()
        if input == "no":
            print ("Let's start the fun then!!!!")
    else:
        print ("Let's start the fun then!!!!")


q1 = Question1()
print (q1.question)
while True:
    input = raw_input("Enter your answer: ")
    if input in q1.answer:
        print ("Right Answer, Good Job...")
        break
    else:
        print (q1.prompts[1])

q2 = Question2()
print (q2.question)
while True:
    input = raw_input("Enter your answer: ")
    if input in q2.answer:
        print ("Right Answer, Good Job...")
        break
    else:
        print (q2.prompts[1])

q3 = Question3()
print (q3.question)
while True:
    input = raw_input("Enter your answer: ")
    if input in q3.answer:
        print ("Right Answer, Good Job...")
        break
    else:
        print (q3.prompts[1])

q4 = Question4()
print (q4.question)
while True:
    input = raw_input("Enter your answer: ")
    if input in q4.answer:
        print ("Right Answer, Good Job...")
        break
    else:
        print (q4.prompts[1])

print_next_clue()




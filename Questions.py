class QuestionPre:
    question = "Hello... I am Katie Weirs, the most advanced AI ever built!!! 10101 \n" \
               "In order to get the next clue, you need to answer my splendid six puzzles... \n" \
               "Beware no one has been able to solve all. Should we start? [yes/no]"
    answer = ["yes", "no"]
    hint = None
    prompts = ["Let's start the fun and see what have you got!!!", "As if you have some other option, 10101."]

class Question1:
    question = "I am a fruit, a bird, a person and also an iNAND project. What am I?"
    answer = ["kiwi"]
    hint = ["Seriously, you need hint for this as well???"]
    prompts = ["Almost There", "Not that Far", "Try better"]

class Question2:
    question = "If Alice had ten litres milk, and bob gives her ten litres more, and her ox gives 15 litres more. \n" \
               "How many litres of milk does Alice have now?"
    answer = ["10", "ten"]
    hint = ["Alice has a milk giving Ox, do you trust her???", "I had few chances, now I have none!!!"]
    prompts = ["you guys will become very bad accountants!!!"]

class Question3:
    question = "Find the missing Number... \n" \
               "2,5,6,28 \n" \
               "4,9,9,77 \n" \
               "3,7,6,? \n"
    answer = ["39", "thirty nine"]
    hint = ["Multiply some, subtract some!!!"]
    prompts = ["Basic maths it is...."]

class Question4:
    question = "Old Grandfather Adams left half his money to his granddaughter and half that amount to his grandson.\n"\
               "He left a sixth to his brother, and the remainder, $1000, to the dogs' home. \n" \
               "How much did Grandfather Adams leave altogether? \n"
    answer = ["12000"]
    hint = ["it's simple maths, come on!"]
    prompts = ["Old Grandfather should have hired a lawyer instead...", "Basic maths it is...."]

class Question5:
    question = "7 scientists - Anny, Bobby, Cathy, Danny, Effy, Fanny and Garry were working in a chemistry lab. \n" \
               "Next day, Garry was found dead with numbers 10 and 26 written on his hands. \n" \
               "Pol ice concluded it was a job of 2 Murderers.\n" \
               "Who are they??? (input names separated by space)??? \n"
    answer = ["anny", "effy"]
    hint = ["May be you need to refer to your chemistry notes", "Garry loved periodic tables"]
    prompts = ["Garry trusted you guys... :(", "Garry believed in you guys, looks like he was wrong..."]

class Question6:
    question = "Four friends need to cross a street to attend a wedding on a rainy day. Unfortunately, they have only one umbrella with them. \n" \
               "The width of the street is such that only two people can cross the street at a time. \n" \
               "Each person walks with different pace, and takes different timees to cross the street. \n" \
               "Times for each person: 5 min, 10 mins, 20 mins and 25 mins. What's the minimum time required to cross the street.\n "
    answer = ["60", "sixty"]
    hint = ["Maybe one of the friends needs to wait at the other side? Think hard!!!"]
    prompts = ["it looks like they are going to miss the marriage... hurry up!", "Maybe they should have brought 4 umbrellas, you guys are not that helpful"]

class Question7:
    question = "I come from a world of unix, and I was entrusted with a few Easter Eggs \n" \
               "One of these eggs can be yours but only if you can force me to give it you....................\n"
    answer = ["sudo"]
    hint = ["Maybe you should continue the hunt, and come back to me when you have conquered the treasure..."]
    prompts = ["it looks like they are going to miss the marriage... hurry up!",
               "Maybe they should have brought 4 umbrellas, you guys are not that helpful"]


class CommonPrompts:
    basic_prompts = [" Try again...", " Think Hard.", " I expected you to be better hackers.... :)"]
    classic_prompts = ["You sure you are an engineer???", "Someone call 100, it seems monkeys have entered the lab"]
    brute_force = ["Seriously Brute Force?????", "Rise above brute force!!!"," Your Brute Force won't work"]
    right_answer = ["yup, you got it right.", "Ok, you got this one", "Right Answer"]
    wrong_answer = ["Nahh, ", "Nops, ", "Naaa, ", "Incorrect Answer, ", "Wrong Answer, "]
    hint_precursor = ["you seem lost human, here is a hint to help you out!", "Hahaha, and you thought you will defeat AI, here ia a hint for you weakling."]
    cont_text = [" Press Enter to continue" ,  " | Press Enter to continue"]
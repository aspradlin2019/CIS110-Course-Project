import time

play_again = 'yes'
while play_again.lower() == 'yes':

    #Function for animated text
    def print_with_delay(text, delay=0.01):
            for char in text:
                print(char, end='', flush=True)
                time.sleep(delay)
            print()

    #Greet the user and provide instructions
    print("""
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
             The Enchanted Journey
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """)
    print_with_delay(f"Welcome to the Choose-Your-Own-Adventure application!")
    print_with_delay(f"Follow the prompts and make decisions to navigate through the story.")
    print_with_delay(f"Enter 'yes' or 'no' to answer the questions.")
    print_with_delay(f"Each 'yes' or 'no' question will say 'Enter 'yes' or 'no' at the end of the question.")
    print_with_delay(f"For all other questions, you may enter any answer you would like.")
    input(f"\nPress the enter key to start.")

    #Backstory
    print_with_delay(r"""
                                              /\
                                             /  \
                                            |    |
                                         __--------__
                                          :  0  0  :
                                          |   <    |
                                           \ \__/ /
                                            \----/
                     *                     _/:'':\_
                  *     *                ,'   ::    ' ,
              *     *           ________'              \
           *    *    ======<<(=)__________/|______|:__:/
           *   *    *                      (------)(::)
               *    *                      /       \\\
         ,(         ),                    /         \
        (             )                  /           \
      _-     ,00,      -_               /             \
     (      '  _ )       )             /               \
    (      ()_,\,\,       )           /_________________\
    """)


    #Ask the user five questions and store the answer in variables
    enchantedCreature = input("What kind of magical creature does Oliver encounter in the Enchanted Forest?")
    parallelRealm = input("What name should be given to the parallel realm behind the Enchanted Forest?")
    ultimateQuest = input("What does Oliver hope to achieve on his journey?")
    legendaryItem = input("What is one item you couldn't live without?")
    wiseMentor = input("Who is the wise mentor that guides Oliver through his journey?")

    #Start the story output
    print("\nIn the magical city of Arcania, there lived a young wizard named Oliver.")
    print(f"Oliver was known around the city for his mischievious nature.")
    print(f"One day, Oliver is daydreaming while in class at the Academy of Arcane Arts when he notices something behind a bookshelf on the other side of the classroom")

    #Ask the user to make their first decision
    decision1 = input("Does Oliver find a way to check out what is behind the bookshelf? Enter 'yes' or 'no': ")
    while decision1.lower() not in ['yes', 'no']:
        print("Please enter a valid response.")
        decision1 = input("Does Oliver find a way to check out what is behind the bookshelf? Enter 'yes', or 'no': ")

    #If-Else statement based on user choice
    if decision1.lower() == 'yes':
        print(f"Naturally curious, at the end of the day, Oliver decides to hide in the bathroom until everyone at school goes home.")
        print(f"With everyone gone, Oliver sneaks back into the classroom to find out what was behind the bookshelf.")
        print(f"Behind the bookshelf, was a hidden passage. He was unsure what lay ahead, but he couldn't resist the temptation to find out.")
        print(f"When Oliver got a peek behind the bookshelf, he couldn't believe his eyes. There were {enchantedCreature}s everywhere!")
    else:
        print(f"For the first time in his life, Oliver resisted the temptation, and to avoid the urge to look, Oliver left right away when school was over that day.")
        print(f"However, the next day at school, Oliver notices bright lights emanating from under the bookshelf. He let his curiosity get the best of him.")
        print(f"After school, Oliver decided to check out behind the bookshelf, despite being overwhelmed with cautionary fear.")
        print(f"Behind the bookshelf, was a hidden passage. He was unsure what lay ahead, but he couldn't resist the temptation to find out.")
        print(f"When Oliver got a peek behind the bookshelf, he couldn't believe his eyes. There were {enchantedCreature}s everywhere.")

    #Ask the user to make second choice
    decision2 = input("Should Oliver venture into the Enchanted Forest? Enter 'yes' or 'no': ")
    while decision2.lower() not in ['yes', 'no']:
        print("Please enter a valid response.")
        decision2 = input("Should Oliver venture into the Enchanted Forest? Enter 'yes' or 'no': ")

        #If-else statement based on user input
        if decision2.lower() == 'yes':
            print(f"Embracing his curiosity, Oliver decides to keep going into the Enchanted Forest.")
            print(f"The minute Oliver stepped through the door behind the bookshelf, he was swarmed by {enchantedCreature}s. The were curious about him.")
            print(f"The {enchantedCreature}s offered him a thrilling opportunity. They asked Oliver to find {legendaryItem}.")
            print(f"During his journey to complete {ultimateQuest} Oliver was approached by {wiseMentor}, who offered to guide him on his journey. He tells Oliver he knows just where to find {legendaryItem} and he will show him the way.")
        else:
            print(f"overwhelmed by caution, after seeing {enchantedCreature}s when walking by the bookshelf, Oliver decides to skip out on this adventure.")
            print(f"Oliver continues to live his mundane life at the academy, unaware of the magical creatures and the adventures hes missed out on.")
            print(f"Along his journey home one day, Oliver comes across a strange path. This path in the middle of no where has a locked door at the entrance!")
            print(f"Oliver decides to go through the door, instantly being transported to {parallelRealm}.")
            print(f"In this realm, Oliver faces numerous challenges and has to rely on the teachings of his {wiseMentor}.")

    #If-Elif-Else statement for alternative endings
    if decision1.lower() == 'yes' and decision2.lower() == 'yes':
        print("Oliver successfully completed the quest, becoming a legendary wizard in the Enchanted forest.")
        print("He is revered as a hero.")
    elif decision1.lower() == 'no' and decision2.lower() == 'no':
        print("Oliver eventually went on to become a renowned professor at the Academy of Arcane Art, sharing his ever expanding magic knowledge with other young wiizards.")
    else:
        print("A twist of fate took Oliver on a path of both adventure and academia.")
        print("Oliver became a dual-threat wizard, excelling in both magicalm and adventurous quests, and scholarly pursuits.")
        print("Oliver eventually became a professor at the Academy of Arcane Arts, mainly so that he could have access to the Enchanted Forest, as he was now the king of the magical forest's creatures.")

    #Loop to allow the user to start over and play again
    while True:
        play_again = input("Would you like to play again? Enter 'yes' or 'no'.: ")
        if play_again.lower() != 'yes':
              print("\n"*112) #clear the screen
        else:
            break
quit = False 
while not quit:

    #lists to draw from 
    sports = ["football", "badminton", "rugby", "basketball", "judo", "volleyball"]
    societies = ["hacking","kpop", "anime", "medicine", "dnd"]
    questions = [
        "where are my classes held", 
        "what is parking like",
        "where can i find financial help",
        "how do i access the library",
    ]
    answer = [
        "your classes will be held in the main building! just follow the map at the main doors",
        "parking costs £4 for a day but is free after 5pm",
        "you can email or talk to a SU representative",
        "the libabry is just behind the large statue in the center of campus",

    ]
    #intro asks for age 
    print("Hey!")
    print("At any time you want to quit just say 'bye' :)")
    name = input("What's your name? ").lower()
    print(f"Nice to meet you {name} :), I'm UniBuddy, you can call me buddy!")

    # asks for age 
    age = input(f"By the way, how old are you {name}?").lower()

    # checks for quit 
    if name == "bye" or age == "bye":
        quit = True 
        print ("bye!")
    age = int(age)
    #reply to age     
    if age > 30: 
        print("It's not too late to learn! You're going a great job")
        print("...")
        ans0 = input("Sorry I just realised that sounded ageist, sorry about that.")
    elif age < 18: 
        ans_young = input("Aren't you a little too young to be in uni?").lower()
        if ans_young == "yes":
            print("you'll do fine! Just don't forget to have fun!")
        elif ans_young == "no":
            print("Power to you.")
        else:
            print("hmm, alright!")
    else:
        print("HAha, welcome to the college experience!")
    
    #asks for hobby
    hobby = input("So, out of curiousity, what are you into?").lower()
 

    #ans if hobby is in lists     
    if (hobby in sports):
        print(f"Make sure to join the {hobby} society! We could use some more players!")
        print("Membership is a bit pricy tho so save up for it!")
    elif (hobby in societies):
        print(f"we have a {hobby} society! Do check it out!")
    elif hobby == "bye":
        quit = True
        print ("bye!")
    else: 
        print(f"Wow look at you! I personally am not very knowledgabel on {hobby} but if you look at our SU website we might have a society to your liking!")

    # opens questions to user, loops it too 
    ques = input("I am here if you need anything, do you have any questions for me?").lower()
    while ques != "bye":
        ques = ques.strip("?")
        ques = ques.strip()
        if (ques in questions):
            ques_num = questions.index(ques)
            print(answer[ques_num])
        else: 
            print("Sorry I don't know the answer to that, please try again")

        ques = input("I am here if you need anything, do you have any questions for me?").lower()

    #quit if ques = bye
    if (ques == "bye"):
        quit = True 
        print ("bye!")


#to improve this, i'd log any questions and train the chatbot to recognise the general meaning rather than specific words
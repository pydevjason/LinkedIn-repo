def love_calc():
    print("Welcome to the Love Calculator!")
    name1 = input("What is your first and last name? ").lower()
    name2 = input("What is their first and last name? ").lower()

    count1 = 0
    for letter in "true":
        count1 += name1.count(letter) + name2.count(letter)
            
    count2 = 0
    for letter in "love":
        count2 += name1.count(letter) + name2.count(letter) 

    combined_count = int(str(count1) + str(count2))

    if combined_count < 10 or combined_count > 90:
        print(f"your score is {combined_count}, you go together like coke and mentos.")
    elif combined_count >= 40 and combined_count <= 50:
        print(f"your score is {combined_count}, you are alright together.")
    else:
        print(f"your score is {combined_count}.")

love_calc()

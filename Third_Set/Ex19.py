def chees_and_cracker(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print(f"Man that's enough for a party!")
    print("Get a blanket. \n")


print("We can just give the function numbers directly:")
chees_and_cracker(20, 30)


print("OR, we  can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

chees_and_cracker(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
chees_and_cracker(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
chees_and_cracker(amount_of_cheese + 100, amount_of_crackers + 1000)

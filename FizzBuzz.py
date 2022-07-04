max_number = input("Enter a maximum number")
print("For the following rule implementations please enter either y or n")
rules = {'3': input("Implement the rule for 3?"), '5': input("Implement the rule for 5?"), '7': input("Implement the "
                                                                                                      "rule for 7?"),
         '11': input("Implement the rule for 11?"), '13': input("Implement the rule for 13?"), '17': input("Implement "
                                                                                                           "the rule "
                                                                                                           "for 17?")}

for item in rules:
    if rules[item] == "y":
        rules[item] = True
    else:
        rules[item] = False

try:
    for index in range(1, int(max_number) + 1):
        word_list = []
        if index % 3 == 0 and rules['3']:
            word_list.append("Fizz")
        if index % 5 == 0 and rules['5']:
            word_list.append("Buzz")
        if index % 7 == 0 and rules['7']:
            word_list.append("Bang")
        if index % 11 == 0 and rules['11']:
            word_list.append("Bong")
            del word_list[1:]
        if index % 13 == 0 and rules['13']:
            if "Fizz" in word_list:
                word_list.insert(1, "Fezz")
            else:
                word_list.insert(0, "Fezz")
        if index % 17 == 0 and rules['17']:
            word_list.reverse()

        if len(word_list) == 0:
            word_list.append(index)
        value = ""
        for word in word_list:
            value = value + str(word)

        print(value)

except ValueError:
    print("You didn't enter a valid number")

import question_a
print("This program will ask you to create a string and substring.")
print("Then it will compare the two to find the starting position of when your substring occurs within your string.")
print("Your string must be at least between 8 and 16 characters long.")
print("Your substring must be 4 characters long.\n")
option = str(input("Enter Y to create a string and substring: ")).lower()
while True:
    if option in ('y', 'yes'):
        while True:
            string1 = str(input("Enter your string between 8 and 16 characters: ")).upper()
            if question_a.validate_string_length(string1) == "Invalid":
                print("String not within 8-16 characters")
            else:
                break
        while True:
            string2 = str(input("Enter your 4 character substring: ")).upper()
            if question_a.validate_substring_length(string2) == "Invalid":
                print("Substring not 4 characters")
            else:
                break
        result = question_a.get_most_likely_ancestor_consensus(string1, string2)
        print("Your result(s) is: ",end="")
        for i in range(len(result)):
            if i == (len(result)-1):
                print(result[i])
            else:
                print(result[i], end=',')
        print("")
        option = str(input("Enter Y to create a another string and substring: ")).lower()
    else:
        print("Exiting Program")
        break
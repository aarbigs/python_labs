'''
Using f-strings, print out the name, last name, and quote of each person in the given dictionary,
formatted like so:

"The inspiring quote" - Lastname, Firstname

'''

famous_quotes = [
    {"full_name": "Isaac Asimov", "quote": "I do not fear computers. I fear lack of them."},
    {"full_name": "Emo Philips", "quote": "A computer once beat me at chess, but it was no match for me at "
                                          "kick boxing."},
    {"full_name": "Edsger W. Dijkstra", "quote": "Computer Science is no more about computers than astronomy "
                                                 "is about telescopes."},
    {"full_name": "Bill Gates", "quote": "The computer was born to solve problems that did not exist before."},
    {"full_name": "Norman Augustine", "quote": "Software is like entropy: It is difficult to grasp, weighs nothing, "
                                               "and obeys the Second Law of Thermodynamics; i.e., it always increases."},
    {"full_name": "Nathan Myhrvold", "quote": "Software is a gas; it expands to fill its container."},
    {"full_name": "Alan Bennett", "quote": "Standards are always out of date.  That’s what makes them standards."}
]

'''for dic in famous_quotes:
    for key, value in dic.items():
        print(key, value)
        '''

#"The inspiring quote" - Lastname, Firstname
quote_dict = {}
for i in famous_quotes:
    for key, value in i.items():
            print(value)
# name_dic = {}
# for i in famous_quotes:
#     name_dic[i] = ['full_name'].split()
#     print(name_dic[i])

# for dictionary in famous_quotes:
#     print(f"{dictionary['quote']} - {dictionary['full_name'].split()} ")





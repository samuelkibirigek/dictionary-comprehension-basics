
#I am coming from a list here to create a new dictionary
#I import the random module as I will need it to generate scores


import random
names = ["Sam", "David", "Elli", "Sasha", "Barack", "Isaac"]


# dict_from_list = {new_key, new_value for item in list}
new_dict_from_list = {student: random.randint(1, 100) for student in names}
print(new_dict_from_list)


#new_dict = {new_key : new_value for (key, value) in dict.items() if test}
passed_students_dict = {student : score for (student, score) in new_dict_from_list.items() if score > 60}

print(passed_students_dict)



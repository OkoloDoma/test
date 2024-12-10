# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, splt=","):
    lst1 = set(group1.split(splt))
    lst2 = set(group2.split(splt))
    lst = list(lst1.intersection(lst2))
    return lst

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, splt="|"))

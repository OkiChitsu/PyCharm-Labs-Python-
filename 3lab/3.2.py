def find_common_participants(group1, group2, separator=","):
    common = set(group1.split(separator)) & set(group2.split(separator))
    return sorted(common)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group, separator="|")
print(common_participants)
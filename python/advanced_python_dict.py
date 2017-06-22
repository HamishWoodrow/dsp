
fhand = open('faculty.csv')
full_lst =list()
lst_name = dict()
names_dict=dict()
names_dict_sort=dict()

for line in fhand:
    entry = line.rstrip().split(',')
    full_lst.append(entry)

for person in full_lst[1:]:
    last_name=person[0].split()[-1]
    names=tuple(person[0].split())
    names_dict[names]=person[1:]
    names_dict_sort[names[::-1]]=person[1:]
    if last_name in lst_name:
        lst_name[last_name].append(person[1:])
    else:
        lst_name[last_name]=[person[1:]]

print (lst_name)
print (names_dict)
print (names_dict_sort)

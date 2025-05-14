# Problem 1: Эки тизмени бириктирүү
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list1.extend(list2)
 
# Problem 2: "Jack" атын саноо

names = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon', 'Jimmy',
         'Jackson', 'Jhon', 'Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon']
jack_count = names.count('Jack')
 
# Problem 3: "Oskar" атын өчүрүү
names_to_modify = ['Jhon', 'Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon']
if 'Oskar' in names_to_modify:
    names_to_modify.remove('Oskar')
 
# Problem 4: Жеке маалыматтарды кошуу
info = []
info.append("Атыңыз: Пари")
info.append("Туулган күнүңүз: 11.04.2009")
info.append("Жаккан программалоо тили: Python")
 
# Problem 5: "loop" объектин өчүрүү
python_list = ["int", "str", "bool", "if", "else", "elif", "loop", "tuple", 
               "list", "None", True, False]
if "loop" in python_list:
    index = python_list.index("loop")
    python_list.pop(index)
 
# Бардык натыйжаларды чыгаруу
print("Problem 1: Бириктирилген тизме:", list1)
print("Problem 2: 'Jack' атынын саны:", jack_count)
print("Problem 3: 'Oskar' атын өчүргөндөн кийин:", names_to_modify)
print("Problem 4: Жеке маалыматтар:", info)
print("Problem 5: 'loop' объектин өчүргөндөн кийин:", python_list)

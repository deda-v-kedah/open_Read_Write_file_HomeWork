import pprint

def print_recipe(document):
    cook_book = {}
    with open(document, 'r', encoding='utf-8') as file:
        for line in file:
            dish = line.strip('\n')
            cook_book[dish] = []
            count = file.readline()
            for i in range(int(count)):
                str = file.readline()
                ingredient, amt, unit = str.split(' | ')

                ingredient_dict = {'ingredient_name': ingredient, 'quantity': amt, 'measure': unit.strip('\n')}

                cook_book[dish].append(ingredient_dict)
           
            file.readline()
    pprint.pprint(cook_book, width=120, sort_dicts=False)


print_recipe("recipes.txt")
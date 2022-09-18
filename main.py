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




def get_shop_list_by_dishes(dishes, person_count):
    shop_dict = {}
    with open('recipes.txt', 'rt', encoding='utf-8') as file:
        for line in file:
            if line.strip('\n') in dishes:
                dish = line
                count = file.readline()
                for i in range(int(count)):
                    row = file.readline()
                    ing, quantity, measure = row.split(' | ')
                    quantity = int(quantity) * person_count
                    if ing in shop_dict.keys():
                        value = shop_dict[ing]
                        num = int(value['quantity']) + int(quantity)
                        
                        shop_dict[ing] = {'measure': measure.strip('\n'), 'quantity': str(num)}
                    else:
                        shop_dict[ing] = {'measure': measure.strip('\n'), 'quantity': str(quantity)}
    pprint.pprint(shop_dict, sort_dicts=False)

get_shop_list_by_dishes(['Омлет', 'Фахитос'], 3)
#print_recipe("recipes.txt")


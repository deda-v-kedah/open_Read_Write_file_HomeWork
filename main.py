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

        

def collect_into_one():
    text_list = []
    with open('1.txt', 'rt', encoding='utf-8') as file1, open('2.txt', 'rt', encoding='utf-8') as file2, open('3.txt', 'rt', encoding='utf-8') as file3, open('result.txt', 'wt', encoding='utf-8') as write_file:
        text_list.append( (len(file1.readlines()), '1.txt') )
        text_list.append( (len(file2.readlines()), '2.txt') )
        text_list.append( (len(file3.readlines()), '3.txt') )

        sorted_tuple = sorted(text_list)
        
        for line in sorted_tuple:
            write_file.write(line[1]+'\n')
            write_file.write(str(line[0])+'\n')
            for i in range(int(line[0])):
                write_file.write(f'Строка номер {i+1} из файла номер {line[1].strip(".txt")}\n')


collect_into_one()
#get_shop_list_by_dishes(['Омлет', 'Фахитос'], 3)
#print_recipe("recipes.txt")
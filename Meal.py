import random
import time

def get_user_input(prompt, input_type=int):
    while True:
        try:
            user_input = input_type(input(prompt))
            if user_input > 0:
                return user_input
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid value.")

def get_random_selection(items, selection_count, unique=True):
    if unique:
        return random.sample(items, k=selection_count)
    else:
        return random.choices(items, k=selection_count)

def print_meal_details(protein_menu, fat_menu, vegetables_menu):
    protein_grams = sum([100 for _ in protein_menu])
    fat_grams = sum([100 for _ in fat_menu])
    vegetables_grams = sum([100 for _ in vegetables_menu])

    print(f'\nThe meal I created for you will be prepared with:\n\n'
      f'Proteins: {protein_grams}g of {", ".join(protein_menu[:-1])}' +
      (f' and {protein_menu[-1]}.' if len(protein_menu) > 1 else f'{protein_menu[-1]}.') + '\n'
      f'Fats: {fat_grams}g of {", ".join(fat_menu[:-1])}' +
      (f' and {fat_menu[-1]}.' if len(fat_menu) > 1 else f'{fat_menu[-1]}.') + '\n'
      f'Vegetables: {vegetables_grams}g of {", ".join(vegetables_menu[:-1])}' +
      (f' and {vegetables_menu[-1]}.' if len(vegetables_menu) > 1 else f'{vegetables_menu[-1]}.'))

def create_meal():
    protein = ['Chicken breast', 'Chicken thighs', 'Chicken wings', 'Steak', 'Pork ribs', 'Lamb chops', 'Shrimp', 'Lobster', 'Eggs', 'Egg whites', 'Octopus', 'Salmon', 'Tuna', 'Duck', 'Cod', 'Crab legs', 'Turkey breast']
    fat = ['Avocado', 'Macadamia', 'Olives', 'Pistachio', 'Almonds', 'Swiss cheese', 'Provolone cheese', 'Burrata', 'Blue cheese', 'Brie', 'Mozzarella cheese', 'Gouda cheese', 'Gruyere cheese', 'Parmesan cheese']
    vegetables = ['White onions', 'Red onions', 'Caramelized onions', 'Green onions', 'Red pepper', 'Green pepper', 'Yellow pepper', 'Mushrooms', 'Broccoli', 'Cauliflower', 'Tomatoes', 'Brussels sprouts', 'Spinach', 'Arugula', 'Celery', 'Cucumber', 'Pickles']

    while True:
        # Proteins
        protein_input = get_user_input("Enter the number of proteins you would like in the meal: ")
        protein_menu = get_random_selection(protein, protein_input)
        print(f'\nProteins: {", ".join(protein_menu)}.')

        # Fats
        fat_input = get_user_input("\nEnter the number of fats you would like in the meal: ")
        fat_menu = get_random_selection(fat, fat_input)
        print(f'\nFats: {", ".join(fat_menu)}.')

        # Vegetables
        vegetables_input = get_user_input("\nEnter the number of vegetables you would like in the meal: ")
        vegetables_menu = get_random_selection(vegetables, vegetables_input)
        print(f'\nVegetables: {", ".join(vegetables_menu)}.\n')

        print_meal_details(protein_menu, fat_menu, vegetables_menu)
        
        satisfied = input("\nDo you like this meal? (yes/no): ").strip().lower()
        if satisfied == 'yes':
            print("\nGreat! Enjoy your meal prep!")
            break
        else:
            print("\nLet's try again!\n")
            time.sleep(1)
    
print('Hi there!\n')
time.sleep(1)
print('This program was created with the intent of helping you meal prep easily.\n')
time.sleep(2)
print('All you need to do is tell me how many proteins, fats and vegetables you would like to include and I will select a custom menu with the ingredients for you!\n')
time.sleep(2)
print('Let\'s get right into it, shall we?\n')
time.sleep(2)
create_meal()


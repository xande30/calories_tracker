from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt
from colorama import Fore, Back

CALORIES_GOAL_LIMIT = 2500
PROTEIN_GOAL = 160
FAT_GOAL = 70
CARBS_GOAL = 25

today = []


@dataclass
class Food:
    name: str
    calories: int
    protein: int
    fat: int
    carbs: int


done = False

while not done:
    print(Fore.LIGHTGREEN_EX, """
        (1) Add New Food
        (2) Visualize Progress
        (q) Quit""")
    choice = input('Chose An Option: ')

    if choice == '1':
        print(Fore.LIGHTMAGENTA_EX, 'Adding A New Food!')
        name = input('Name: ')
        calories = int(input('Calories:'))
        proteins = int(input('Proteins: '))
        fats = int(input('Fats: '))
        carbs = int(input('Carbs: '))
        food = Food(name, calories, proteins, fats, carbs)
        today.append(food)
        print(Fore.RED, "Successfully Added")
    elif choice == '2':
        calorie_sum = sum(food.calories for food in today)
        protein_sum = sum(food.protein for food in today)
        fats_sum = sum(food.fat for food in today)
        carbs_sum = sum(food.carbs for food in today)
        fig, axs = plt.subplots(2,2)
        axs[0, 0].pie([protein_sum, fats_sum, carbs_sum], labels=["Proteins", "Carbs", "Fats"], autopct="%1.1f%%")
        axs[0, 0].set_title("Nutrition Distribution")
        axs[0, 1].bar([0, 1, 2], [protein_sum, fats_sum, carbs_sum], width=0.4)
        axs[0, 1].bar([0.5, 1.5, 2.5], [PROTEIN_GOAL, FAT_GOAL, CARBS_GOAL], width=0.4)
        axs[0, 1].set_title("Nutrition Distribution")
        axs[1, 0].pie([calorie_sum, CALORIES_GOAL_LIMIT - calorie_sum], labels=["Calories", "Remaining"], autopct="%1.1f%%")
        axs[1, 0].set_title("Nutrition Distribution")
        axs[1, 1].plot(list(range(len(today))), np.cumsum([food.calories for food in today]), label="Calories Eaten")
        axs[1, 1].plot(list(range(len(today))), [CALORIES_GOAL_LIMIT] * len(today), label="Calorie Goal")
        axs[1, 0].set_title("Calories Goal Over Time")
        axs[1, 1].get_legend()
        plt.show()
    elif choice == "q":
        done = True
    else:
        print(Fore.BLACK + Back.RED, "Invalid Choice")
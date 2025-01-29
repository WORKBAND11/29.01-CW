import pandas as pd

def main_menu()
user_input = int(input("Что вы хочете вывести(если весь дата сэт напишите 1, если конкретную строчку, то напишите индекс, если столбец, то напишите индекс, если конкретную ячейку, тоже напишите индекс)?" ))
df = pd.read_excel('marks.xlsx')

if user_input == 1:
    print(df)
while True:
 print("Введите индекс строчки" )

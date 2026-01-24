#Программа, которая записывает настроение
filename = "mood.txt"
try:
    with open(filename, "r", encoding="utf-8") as file:
        history = file.read()
    if history.strip():  
        print("Твоя история настроений:")
        print(history)
    else:
        print("История пока пуста.")
except FileNotFoundError:
    print("История пока пуста.")
mood = input("\nКак твоё настроение сегодня? ")
with open(filename, "a", encoding="utf-8") as file:
    file.write(mood + "\n")
print("Запись сохранена!")
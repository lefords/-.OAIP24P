import json
import os

FILENAME = "mood_diary.json"

def load_entries():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_entries(entries):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(entries, f, ensure_ascii=False, indent=2)

def add_entry(mood, **kwargs):
    entries = load_entries()
    entry = {"id": len(entries) + 1, "mood": mood, **kwargs}
    entries.append(entry)
    save_entries(entries)
    print("Запись добавлена!")

def show_entries():
    entries = load_entries()
    if not entries:
        print("Дневник пуст.")
        return
    for e in entries:
        print(e)


print("1 - Добавить запись")
print("2 - Показать дневник")

choice = input("Выберите действие (1 или 2): ")

if choice == "1":
    mood = input("Ваше настроение: ")
    note = input("Заметка (можно оставить пустым): ").strip()
    extra = {}
    if note:
        extra["note"] = note

    add_entry(mood, **extra)

elif choice == "2":
    show_entries()

else:
    print("Неверный выбор.")
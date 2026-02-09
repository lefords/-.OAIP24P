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
        json.dump(entries, f, ensure_ascii=False, indent=4)

def add_entry(mood, **kwargs):
    entries = load_entries()
    entry_id = len(entries) + 1
    new_entry = {
        "_id": entry_id,
        "mood": mood.strip(),
        **kwargs  
    }
    entries.append(new_entry)
    save_entries(entries)
    print(f"Запись #{entry_id} сохранена!")

def show_diary():
    entries = load_entries()
    if not entries:
        print("Дневник пуст.")
        return
    print("\n--- Твой дневник настроения ---")
    for entry in entries:
        print(json.dumps(entry, ensure_ascii=False, indent=2))
        print("-" * 30)

if __name__ == "__main__":
    add_entry("Отличное", note="Сдал экзамен", energy=9)
    add_entry("Грустное", sleep_hours=5, weather="дождь")
    add_entry("Спокойное", meditation=True, caffeine_cups=1)

    show_diary()
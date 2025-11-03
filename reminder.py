
---

### ⏰ **reminder.py**
```python
tasks = [
    "Drink water 💧",
    "Take a short walk 🚶‍♂️",
    "Stretch your back 🧘",
    "Check your to-do list ✅",
    "Call someone you care about ☎️"
]

def show_reminders():
    print("Today's reminders:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

if __name__ == "__main__":
    show_reminders()

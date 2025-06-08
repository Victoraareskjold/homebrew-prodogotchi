#!/usr/bin/env python3

import yaml
import os
from datetime import datetime

DATA_FILE = "data.yaml"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return yaml.safe_load(f) or {}
    else:
        return {"tasks": []}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        yaml.dump(data, f)

def think():
    data = load_data()
    print("""
          
🤔 What do you want to do?""")
    title = input("📝 Task (leave empty to cancel): ").strip()

    if not title:
        print("""
                            
🚫 Think mode cancelled.""")
        return

    estimate_input = input("⏱️ Estimate in minutes (optional): ").strip()

    try:
        estimate = int(estimate_input)
    except ValueError:
        estimate = None

    task = {
        "title": title,
        "status": "todo",
        "created_at": datetime.now().isoformat(),
    }

    if estimate:
        task["estimate"] = estimate

    data["tasks"].append(task)
    save_data(data)

    print(f"✅ Created task: {title}")
    if estimate:
        print(f"⏳ Estimated time: {estimate} min")


def start():
    data = load_data()
    todos = [t for t in data["tasks"] if t["status"] == "todo"]

    if not todos:
        print("🎉 No tasks to start!.")
        return

    print("🚀 Tasks to choose from:")
    for i, task in enumerate(todos):
        print(f"{i + 1}. {task['title']} ({task.get('estimate', '?')} min)")

    choice = input("Choose a task (number): ").strip()
    try:
        index = int(choice) - 1
        task = todos[index]
    except (ValueError, IndexError):
        print("⚠️ Invalid choice.")
        return

    for t in data["tasks"]:
        if t == task:
            t["status"] = "in_progress"
            t["started_at"] = datetime.now().isoformat()

    save_data(data)
    print(f"🐾 Startet: {task['title']}")

def check():
    data = load_data()
    tasks = data.get("tasks", [])

    current = None
    for t in tasks:
        if t.get("status") == "in_progress":
            current = t
            break

    if not current:
        print("🐶 You have no ongoing tasks at the moment!")
        return

    title = current.get("title")
    started = datetime.fromisoformat(current.get("started_at"))
    estimate_min = current.get("estimate", 30)
    elapsed = (datetime.now() - started).total_seconds() / 60
    emoji = "🐢" if elapsed > estimate_min * 1.5 else "🦴"

    print(f"\n🔎 Task: {title}")
    print(f"⏱️  Time spent: {elapsed:.1f} min")
    print(f"📌 Estimate: {estimate_min} min")

    if elapsed > estimate_min * 2:
        print(f"{emoji} This is starting to take some time... maybe some scope-creep?")
    elif elapsed > estimate_min * 1.2:
        print(f"{emoji} A little behind, but you're still okay.")
    else:
        print(f"{emoji} Keep up the great tempo!")

    print()

def help():
    print("""
Prodogotchi 🐶 - Productivity with attitude!

Available commands:

  start     → Start new task
  think     → Write down projectidea
  check     → Check progress and time spent on task
  commit    → Create commit and end task
  help      → Show help commands
""")


def main():
    import sys
    cmd = sys.argv[1] if len(sys.argv) > 1 else "help"

    if cmd == "think":
        think()
    elif cmd == "start":
        start()
    elif cmd == "check":
        check()
    elif cmd == "help":
        help()
    else:
        print("Unknown command. Try: think, start, check, help")

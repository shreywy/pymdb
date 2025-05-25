import json
import os
from tmdbv3api import TMDb, TV

# --- Config ---
KEY_FILE = "key.txt"
STORAGE_FILE = "storage.json"

# --- Initialize TMDb ---
def load_api_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "r") as f:
            return f.read().strip()
    else:
        key = input("Enter your TMDb API key: ").strip()
        with open(KEY_FILE, "w") as f:
            f.write(key)
        return key

def init_tmdb():
    tmdb = TMDb()
    tmdb.api_key = load_api_key()
    tmdb.language = "en"
    return TV()

# --- Storage ---
def load_storage():
    if os.path.exists(STORAGE_FILE):
        with open(STORAGE_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                print("Warning: storage.json was empty or invalid. Resetting...")
                return []
    return []


def save_storage(data):
    with open(STORAGE_FILE, "w") as f:
        json.dump(data, f, indent=2)


# --- Initial Features ---
def search_shows(tv, query):
    results = tv.search(query)
    return [
        {
            "id": show.id,
            "name": show.name,
            "overview": show.overview,
            "poster_path": show.poster_path,
        }
        for show in results
    ]

def add_show_to_storage(show_data):
    storage = load_storage()
    storage.append(show_data)
    save_storage(storage)

def list_saved_shows():
    storage = load_storage()
    if not storage:
        print("No shows saved.")
    for i, show in enumerate(storage, 1):
        print(f"{i}. {show['name']}")


# --- CLI Testing ---
if __name__ == "__main__":
    tv = init_tmdb()
    
    while True:
        print("\n--------------------------------------------------------------\nOptions: 1) Search Show  2) List Saved Shows  3) Quit")
        choice = input("Select option: ").strip()

        if choice == "1":
            query = input("Enter show name: ")
            results = search_shows(tv, query)
            if not results:
                print("No results found.")
                continue

            for i, show in enumerate(results, 1):
                print(f"{i}. {show['name']}\n   {show['overview'][:100]}...")

            sel = input("Select a show to save (number, letter to cancel): ")
            if sel.isdigit() and 1 <= int(sel) <= len(results):
                add_show_to_storage(results[int(sel) - 1])
                print("Show saved.")

        elif choice == "2":
            list_saved_shows()

        elif choice == "3":
            break

        else:
            print("Invalid choice.")

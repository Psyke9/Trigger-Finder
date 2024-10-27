import os
import time
import platform
import easygui

def clear_screen():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def find_triggers(folder_path, trigger_keywords):
    triggers = []
    file_extensions = ('.lua', '.txt', '.cfg', '.sql', '.json', '.xml')
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(file_extensions):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        for line_number, line in enumerate(f, start=1):
                            for keyword in trigger_keywords:
                                if keyword in line:
                                    triggers.append((keyword, line.strip(), file_path, line_number))
                                    break
                except Exception as e:
                    print(f"Oops! Couldn't open {file_path}: {e}")
    return triggers

def save_trigger_file(folder_name, triggers):
    data_folder = "data"
    os.makedirs(data_folder, exist_ok=True)

    filename = os.path.join(data_folder, f'trigger_{folder_name}.txt')
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for keyword, line, file_path, line_number in triggers:
                f.write(f"Trigger: {keyword}\nLine: {line}\nFile: {file_path}, Line Number: {line_number}\n\n")
        print(f"\nTriggers saved successfully in '{filename}'")
    except Exception as e:
        print(f"Couldn't save file: {e}")

def loading_message(message):
    print(message, end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="")
    print()

def print_header(title):
    print("=" * 50)
    print(f"{title:^50}")
    print("=" * 50)

def print_credits():
    clear_screen()
    print_header("Credits")
    print("\nDeveloped by Psyke\n")
    print("Connect with:")
    print(" - Forum: cracked.io/Psyke")
    print(" - Telegram: t.me/Psyke9")
    print(" - GitHub: github.io/Psyke9\n")
    print("\nTrigger Finder!")
    time.sleep(5)
    clear_screen()

def show_welcome():
    clear_screen()
    print_header("Welcome to Trigger Finder!")

def main():
    show_welcome()
    
    trigger_keywords = [
        'TriggerServerEvent',
        'TriggerEvent',
        'AddEventHandler',
        'RegisterNetEvent',
        'TriggerClientEvent'
    ]
    
    while True:
        show_welcome()
        print("\nChoose an option:")
        print("1. Finder")
        print("2. Credits")
        print("3. Exit")

        choice = input("\nEnter your choice [1, 2, or 3]: ")
        
        if choice == '1':
            folder_path = easygui.diropenbox("Selectionne ton dump fdp")
            if folder_path and os.path.isdir(folder_path):
                clear_screen()
                loading_message("Recherche de triggers...")
                triggers = find_triggers(folder_path, trigger_keywords)
                clear_screen()

                if triggers:
                    print_header("Search Results")
                    for keyword, line, file_path, line_number in triggers:
                        print(f"Trigger: {keyword}")
                        print(f"    Line: {line}")
                        print(f"    File: {file_path}, Line Number: {line_number}\n")
                    
                    print(f"\n{'=' * 90}\nTotal triggers found: {len(triggers)}")
                    save_choice = input(f"Save results to 'data/trigger_{os.path.basename(folder_path)}.txt'? (y/n): ")
                    if save_choice.lower() == 'y':
                        save_trigger_file(os.path.basename(folder_path), triggers)
                    clear_screen()
                else:
                    print("No triggers found in this folder.")
                    time.sleep(2)
            else:
                print("Error: Invalid folder selected.")
                time.sleep(2)
        
        elif choice == '2':
            print_credits()
        
        elif choice == '3':
            print("Merci d'utiliser la merde (Trigger Finder).")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            time.sleep(2)

if __name__ == "__main__":
    main()

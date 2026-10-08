
"""Main entry point for the diary application.
 
Run it from the project root directory with:
    python3 src/main.py
"""
 
from datetime import date
 
import diary_functions
 
 
def show_menu(diary_file):
    """Print the menu and the diary file currently in use."""
    print(f'\n\t\tDiary Menu ({diary_file})\n')
    print('\t1. Add an entry')
    print('\t2. Print all entries')
    print('\t3. Print entries for one date')
    print('\t4. Load a different diary file')
    print('\t5. Exit')
 
 
def print_entries(entries):
    """Print a list of entries, one per line."""
    if len(entries) == 0:
        print('No entries found.')
    for entry in entries:
        print(entry)
 
 
def choose_diary_file():
    """Ask for a diary file name until we get one that works."""
    while True:
        file_name = input('Diary file name (Enter for diary.txt): ').strip()
        if file_name == '':
            file_name = 'diary.txt'
        try:
            diary_functions.load_diary_file(file_name)
            return file_name
        except Exception as e:
            print(f'Could not open that file: {e}')
 
 
def main():
    """Run the diary application."""
    print('Welcome to your diary!')
    diary_file = choose_diary_file()
 
    while True:
        show_menu(diary_file)
        menu_choice = input('\n\tEnter menu number: ').strip()
 
        match menu_choice:
            case '1':
                entry_date = input('Date (YYYY-MM-DD) or Enter for today: ')
                entry_date = entry_date.strip()
                if entry_date == '':
                    entry_date = str(date.today())
                entry_text = input('Entry: ')
 
                if not diary_functions.is_valid_date(entry_date):
                    print('Invalid date. Entry not saved.')
                elif entry_text.strip() == '':
                    print('Empty entry. Entry not saved.')
                else:
                    diary_functions.add_entry(diary_file, entry_date, entry_text)
                    print('Entry saved.')
            case '2':
                print_entries(diary_functions.read_entries(diary_file))
            case '3':
                entry_date = input('Date (YYYY-MM-DD): ').strip()
                if diary_functions.is_valid_date(entry_date):
                    print_entries(
                        diary_functions.filter_entries(diary_file, entry_date))
                else:
                    print('Invalid date.')
            case '4':
                diary_file = choose_diary_file()
            case '5':
                print('Goodbye!')
                break
            case _:
                print('Please enter a number from 1 to 5.')
 
 
# Call main() if this is the main execution module
if __name__ == '__main__':
    main()
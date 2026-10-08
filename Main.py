from datetime import date
 
import diary_functions
 
 
def show_menu(diary_file):
#Print the menu.
    print()
    print(f'Diary file: {diary_file}')
    print('1. Add an entry')
    print('2. Print all entries')
    print('3. Print entries for one date')
    print('4. Load a different diary file')
    print('5. Exit')
 
 
def print_entries(entries):
#Print a list of entries, one per line.
    if len(entries) == 0:
        print('No entries found.')
    for entry in entries:
        print(entry)
 
 
def ask_for_file():
#Ask for a diary file name. Create the file if it does not exist.
    file_name = input('Diary file name (Enter for diary.txt): ').strip()
    if file_name == '':
        file_name = 'diary.txt'
    diary_functions.load_diary_file(file_name)
    return file_name
 
 
def main():
#Run the diary application.
    print('Diaries!')
    diary_file = ask_for_file()
 
    while True:
        show_menu(diary_file)
        choice = input('Enter menu number: ').strip()
 
        if choice == '1':
            entry_date = input('Date (YYYY-MM-DD) or Enter for today: ')
            entry_date = entry_date.strip()
            if entry_date == '':
                entry_date = str(date.today())
            entry_text = input('Entry: ').strip()
 
            if not diary_functions.is_valid_date(entry_date):
                print('Invalid date. Entry not saved.')
            elif entry_text == '':
                print('Empty entry. Entry not saved.')
            else:
                diary_functions.add_entry(diary_file, entry_date, entry_text)
                print('Entry saved.')
 
        elif choice == '2':
            entries = diary_functions.read_entries(diary_file)
            print_entries(entries)
 
        elif choice == '3':
            entry_date = input('Date (YYYY-MM-DD): ').strip()
            if diary_functions.is_valid_date(entry_date):
                entries = diary_functions.filter_entries(diary_file, entry_date)
                print_entries(entries)
            else:
                print('Invalid date.')
 
        elif choice == '4':
            diary_file = ask_for_file()
 
        elif choice == '5':
            print('Bye!')
            break
 
        else:
            print('Please enter a number from 1 to 5.')
 
 

if __name__ == '__main__':
    main()
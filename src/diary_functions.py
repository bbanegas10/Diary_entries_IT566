
"""Functions for reading and writing the diary file.
 
Each entry is ONE line in a text file, like this:
 
    2026-10-02 Today I started my diary project.
"""
 
from datetime import datetime
 
 
def is_valid_date(date_text):
    """Return True if date_text is a real date written as YYYY-MM-DD."""
    if len(date_text) != 10:
        return False
    try:
        datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except Exception:
        return False
 
 
def load_diary_file(file_path):
    """Make sure the diary file exists. Create it if it does not."""
    # Mode 'a' (append) creates a missing file and never erases anything.
    diary_file = open(file_path, 'a', encoding='utf-8')
    diary_file.close()
 
 
def add_entry(file_path, entry_date, entry_text):
    """Add one entry, on its own line, to the end of the diary file."""
    with open(file_path, 'a', encoding='utf-8') as diary_file:
        diary_file.write(f'{entry_date} {entry_text.strip()}\n')
 
 
def read_entries(file_path):
    """Return a list of every entry (line) in the diary file."""
    entries = []
    with open(file_path, 'r', encoding='utf-8') as diary_file:
        for line in diary_file:
            if line.strip() != '':
                entries.append(line.strip())
    return entries
 
 
def filter_entries(file_path, entry_date):
    """Return a list of the entries that have the given date."""
    matching_entries = []
    for line in read_entries(file_path):
        if line[:10] == entry_date:  # first 10 characters are the date
            matching_entries.append(line)
    return matching_entries
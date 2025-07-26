from stats import count_words, count_chars, sort_chars, pretty_print  
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents
def argv_check():
    try:
        file_path = sys.argv[1]
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return file_path

def main():
    file_path = argv_check()
    word_count = count_words(get_book_text(file_path))
    char_count = count_chars(get_book_text(file_path))
    sorted_list = sort_chars(char_count)
    pretty = pretty_print(sorted_list,word_count,file_path)
main()

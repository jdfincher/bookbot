def count_words(string):
    words = string.replace("\n"," ").replace("\\"," ").split()
    num_words = 0
    for word in words:
        num_words += 1
    return f"{num_words}"

def count_chars(string):
    chars = string.lower()
    num_chars = {}
    for char in chars:
        if char not in num_chars.keys():
            key = char
            count = 1
            num_chars[key] = count
        elif char in num_chars.keys():
            key = char
            count = 1
            num_chars[key] += count
    return num_chars

def sort_on(items):
    return items['num']

def sort_chars(dict):
    sorted_list = []
    for char, count in dict.items():
        if char.isalpha():
            sorted_list.append({'char':char,'num':count})
        else:
            pass 
        sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def pretty_print(list_of_dictionaries, count,file_path):
    
    start = """
============ BOOKBOT ============
Analyzing book found at {0}...
----------- Word Count ----------
Found {1} total words
--------- Character Count -------""".format(file_path,count)
    end = "============= END ==============="
    print(start)
    
    for i in range(0,len(list_of_dictionaries)):
        char = list_of_dictionaries[i]['char']
        count = list_of_dictionaries[i]['num']
        print(char+":",count)
    print(end) 

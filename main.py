from stats import get_num_words, count_words, sort_list
import sys 

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]

    total_words = get_num_words(filepath)
    list_sorted = sort_list(count_words(filepath))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for item in list_sorted:
        print(f"{item['char']}: {item['num']}")

main()






def get_num_words(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        words = file_contents.split()
        total_words = len(words)
        return total_words

def count_words(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        file_contents_letters = list(file_contents.lower())
        char_dic = {}
        for char in file_contents_letters:
            if char not in char_dic:
                char_dic[char] = 1
            else:
                char_dic[char] += 1
        return char_dic


def sort_on(d):
    return d["num"]

def sort_list(char_dic):
    letter_list = []
    for ch, count in char_dic.items():
        if ch.isalpha():
            letter_list.append({"char": ch, "num": count })
    letter_list.sort(key=sort_on, reverse=True)
    return letter_list







        
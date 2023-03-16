import re
char_path = r'C:\Users\Clsm\Desktop\Test files (epm)\number_char.txt'
txt_file = open(char_path, 'r', encoding='utf-8')
char_list = txt_file.read().split('\n')  
char_array = []
#punctuation = ['\\.','．','、','：','）']
def get_numbering_patterns():     
    for char in char_list:
        dummy_list = char.split('=')
        char_array.append(dummy_list[1])
    return char_array

def remove_specialchar_in_title(text_list):
    """
    get the re pattern of the numbering
    clean the numbering in the subtiles
    return: the clean subtiltes
    """
    #numbering = '^【[0-9]】|^[0-9].|^[0-9]、|^（[0-9]）|^[0-9]：|^[0-9]．|^[0-9]）|^[\u24FF-\u277E]|^[\uFF10-\uFF19]）|^[\uFF10-\uFF19]：|^[\uFF10-\uFF19]．'
    result = []
    char_re = get_numbering_patterns()
    for line in text_list:
        for i in char_re:
            # Cleaning the whitespaces in num_char text file
            i = re.sub(r'\s+', ' ', i).strip()
            line = re.sub(i, '', line, count=1)
        result.append(line)
    return result

text = ["1-1）リモコンの操作が効かない", "1-1）リモコンの操作が効かない"]
result = remove_specialchar_in_title(text)
print(result)
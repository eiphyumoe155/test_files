import re
char_path = r'C:\Users\Clsm\Desktop\Test files\number_char.txt'
txt_file = open(char_path, 'r', encoding='utf-8')
char_list = txt_file.read().split('\n')  
        #char_list = char_list.replace(\"'\\\\'\",\"\"\\\"\")\n",
#print(char_list)
char_array = []
punctuation = ['\\.','．','、','：','）']
def get_numbering_patterns():     
    for char in char_list:
        dummy_list = char.split(':')
        char_array.append('^【['+dummy_list[1]+']】')
        char_array.append('^（['+dummy_list[1]+']）')
        char_array.append('^['+dummy_list[1]+']-['+dummy_list[1]+']）')
        for pun in punctuation:
            
            numbering_pattern = '^['+dummy_list[1]+']'+pun
            char_array.append(numbering_pattern)
        if char != '0-9:0-9':
                    #print(\"aa\",char)\n",
            char_array.append('^['+dummy_list[1]+']')
    #print(char_array)
    return char_array

def remove_specialchar_in_title(text):
    """
    get the re pattern of the numbering
    clean the numbering in the subtiles
    return: the clean subtiltes
    """
    #numbering = '^【[0-9]】|^[0-9].|^[0-9]、|^（[0-9]）|^[0-9]：|^[0-9]．|^[0-9]）|^[\u24FF-\u277E]|^[\uFF10-\uFF19]）|^[\uFF10-\uFF19]：|^[\uFF10-\uFF19]．'
    char_re = get_numbering_patterns()
    #print(char_re)
    for i in char_re:
        print(i)
        text = re.sub(i, '', text, count=1)
        #text = text.replace(i,'')

    # Cleaning the whitespaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text

text = '【 1 】おみやげ'
result = remove_specialchar_in_title(text)
print(result)
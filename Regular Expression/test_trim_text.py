import re
test_str = ["ブリーチな : しでも理想のヘアカラーにできるの？",
"ブリーチなしで理想のヘ : アカラーを叶えるオーダーポイント",
"初めてカラーさんに試して : ほしい、おすすめ8大ヘアカラーサンプル",
"ブリーチな :しカラーをチェックして、理想的な髪色に！"]
result = []
punc = r'^[^:-]*[^\s+]*'
#punc = r'^[^:-]*'
def remove_duplicate(test_str):
    for line in test_str:
        i = re.sub(punc, '', line)
        result.append(i)
    return result

str_list = [re.sub(punc, '', i) for i in test_str]

print(remove_duplicate(test_str))

#print(str_list)

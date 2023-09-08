import json
from pypinyin import lazy_pinyin, Style
import re

name_list = ["马云", "李彦宏"]
pinyin_list = [lazy_pinyin(name, style=Style.TONE) for name in name_list]
file_path = "./idiom.json"

out = ""

# 1、【a】ā á ǎ à
# 2、【o】ō ó ǒ ò
# 3、【e】ē é ě è
# 4、【i】ī í ǐ ì
# 5、【u】ū ú ǔ ù
# 6、【ü】ǖ ǘ ǚ ǜ

def load_idiom(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        idiom_json = json.load(f)
    return idiom_json


def get_idiom_result(pinyin_list, idiom_json):
    result = ""
    for i in idiom_json:
        idiom_pinyin = re.split("[， ]", i["pinyin"])
        word_in_idiom_list = [[find_index(idiom_pinyin, word) for word in pinyin] for pinyin in pinyin_list]
        if all([any(index >= 0 for index in word_in_idiom) for word_in_idiom in word_in_idiom_list]):
            comma_index = i["word"].index("，") if "，" in i["word"] else None
            idiom_word = i["word"].replace("，", "")
            for idx, word_in_idiom in enumerate(word_in_idiom_list):
                for index, item in enumerate(word_in_idiom):
                    if item >=0:
                        idiom_word = idiom_word[:item] + name_list[idx][index] + idiom_word[item + 1 :]
            idiom_word = (
                idiom_word[:comma_index] + "，" + idiom_word[comma_index:]
                if comma_index
                else idiom_word
            )
            result += idiom_word + "\n"
    return result

def find_index(list, element):
    try:
        index = list.index(element)
    except ValueError:
        index = -1
    return index

def write_to_file(result):
    with open("out.txt", "w", encoding="utf-8") as f:
        f.write(result)

if __name__ == "__main__":
    idiom_json = load_idiom(file_path)
    result = get_idiom_result(pinyin_list, idiom_json)
    write_to_file(result)
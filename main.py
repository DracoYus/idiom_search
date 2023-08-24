import json
from pypinyin import lazy_pinyin, Style
import re

name_first = "马云"
name_second = "李彦宏"
pinyin_first = lazy_pinyin(name_first, style=Style.TONE)
pinyin_second = lazy_pinyin(name_second, style=Style.TONE)
file_path = "./idiom.json"

out = ""

# 1、【a】ā á ǎ à
# 2、【o】ō ó ǒ ò
# 3、【e】ē é ě è
# 4、【i】ī í ǐ ì
# 5、【u】ū ú ǔ ù
# 6、【ü】ǖ ǘ ǚ ǜ

with open(file_path, "r", encoding="utf-8") as f:
    idiom_json = json.load(f)


for i in idiom_json:
    idiom_pinyin = re.split("[， ]", i["pinyin"])
    pinyin_first_in_idiom = [pinyin in idiom_pinyin for pinyin in pinyin_first]
    pinyin_second_in_idiom = [pinyin in idiom_pinyin for pinyin in pinyin_second]
    if any(pinyin_first_in_idiom) and any(pinyin_second_in_idiom):
        comma_index = i["word"].index("，") if "，" in i["word"] else None
        idiom_word = i["word"].replace("，", "")
        pinyin_first_index = pinyin_first_in_idiom.index(True)
        pinyin_second_index = pinyin_second_in_idiom.index(True)
        idiom_word_index_first = idiom_pinyin.index(pinyin_first[pinyin_first_index])
        idiom_word_index_second = idiom_pinyin.index(pinyin_second[pinyin_second_index])
        idiom_word = (
            idiom_word[:idiom_word_index_first]
            + name_first[pinyin_first_index]
            + idiom_word[idiom_word_index_first + 1 :]
        )
        idiom_word = (
            idiom_word[:idiom_word_index_second]
            + name_second[pinyin_second_index]
            + idiom_word[idiom_word_index_second + 1 :]
        )
        idiom_word = (
            idiom_word[:comma_index] + "，" + idiom_word[comma_index:]
            if comma_index
            else idiom_word
        )
        out += idiom_word + "\n"


with open("out.txt", "w", encoding="utf-8") as f:
    f.write(out)

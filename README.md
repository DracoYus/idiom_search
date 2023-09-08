## 起因

有段时间，同事群兴起一个起名热潮：将成语中的某个同音字替换成自己姓名中的字。例如有个人姓俞，并且是个很佛系的人，因此可以叫“俞世无争”；或者最近很伤心，可以叫“哀莫大俞心死”；又或者想表现地很聪明，坐山观虎斗，可以叫“鹬蚌相争，俞翁得利”。还有类似“放长线钓大俞”、“心有俞而力不足”这种很有趣的名字。

在此基础上，还可以和关系好的群友组CP，将两个人的名字中的字都替换。例如有个同事姓谢，另一个姓刘，他们组合的名字可以叫“谢刘成河”，给人一种凶狠狡诈的感觉。

名字替换不局限于姓氏，名当中比较有代表性、特点的字都可以进行替换。

奈何本人文学素养不高，在起名大赛上灵感远不如其他同事。

但社恐程序员也想体验为别人赐名的感受，因此写了这个看似不明所以的小程序。

## 设计思路

程序根据输入的人名，计算名字中的拼音，遍历成语数据库，如果拼音和成语库中某个成语的字同音，则进行替换。

直接输入人名计算拼音，比直接输入拼音要更便于使用。因为匹配时需要同声调，常规输入法难以输入带声调的字符，如ā á ǎ à。

计算拼音使用了[pypinyin](https://github.com/mozillazg/python-pinyin)。

成语库来自[中华新华字典数据库](https://github.com/pwxcoo/chinese-xinhua)。如果数据库进行了更新，可以将新的`idiom.json`拷贝替换掉项目根目录中的文件。

## 使用方法

1.在项目根目录执行安装依赖

```shell
pip install -r requirements.txt
```

2.修改main.py文件中定义的全局变量

3.在项目根目录执行，输出结果默认保存为out.txt

```shell
python main.py
```

## 存在的问题

名字中存在多音字的情况下，拼音计算不一定准确

如果两个人名字中包含相同读音的字，产生的结果可能只会替换掉一个字

## 可能的改进

支持命令行交互

支持输入拼音和声调

支持拼音的模糊匹配，例如`z`和`zh`
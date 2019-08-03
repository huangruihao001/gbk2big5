from langconv import Converter


class Gbk2Big5():
    """
    :param text: 要转换的文本
    :param flag: 0-简转繁，1-繁转简
    :return:
    """
    def __init__(self, text, flag=0):
        self.text = text
        self.flag = flag

    def __str__(self):
        return self.convert()

    def convert(self):
        rule = 'zh-hans' if self.flag else 'zh-hant'
        return Converter(rule).convert(self.text)


if __name__ == '__main__':
    text = Gbk2Big5("忧郁的台湾乌龟")
    print(text.convert())
    print(text)
    print(Gbk2Big5("忧郁的台湾乌龟"))

    text2 = Gbk2Big5("憂郁的臺灣烏龜", flag=1)
    print(text2.convert())
    print(text2)
    print(Gbk2Big5("憂郁的臺灣烏龜", flag=1))

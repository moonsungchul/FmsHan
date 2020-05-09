
from konlpy.tag import Kkma, Komoran, Hannanum, Mecab, Twitter
from konlpy.utils import pprint


class KonlParser:


    def __init__(self):
        self.komoran = Komoran()
        self.kkma = Kkma()
        self.hann = Hannanum()
        self.mecab = Mecab()
        self.twitter = Twitter()

    def parserKomoran(self, intext):
        ch = self.komoran.nouns(intext)
        print("komoran : ", ch)
        return ch


    def parserKkma(self, intext):
        ch = self.kkma.nouns(intext)
        print("kkma : ", ch)
        return ch

    def parserHannanum(self, intext):
        ch = self.hann.nouns(intext)
        print("hannanum : ", ch)
        return ch

    def parserMecab(self, intext):
        ch = self.mecab.nouns(intext)
        print("mecab : ", ch)
        return ch

    def parserTwitter(self, intext):
        ch = self.twitter.nouns(intext)
        print("twitter : ", ch)
        return ch

    def parserNouns(self, intext):
        buf = []
        buf.append(rr.parserKomoran(intext))
        buf.append(rr.parserKkma(intext))
        buf.append(rr.parserHannanum(intext))
        buf.append(rr.parserTwitter(intext))
        buf.append(rr.parserMecab(intext))

        print("test .....")

        dic = {}
        for ar in buf:
            for nn in ar:
                if nn in dic:
                    dic[nn] +=1
                else:
                    dic[nn] = 0
        print(dic)
        ret = []
        for key, val in dic.items():
            print(key, val)
            if val >= 3:
                ret.append(key)
        print(ret)
        return ret



if __name__ == '__main__':
    rr = KonlParser()
    intext = u'질문이나 전의 사항은 갓협 이슈 트래커에 남겨주세요'
    #rr.parserKomoran(intext)
    #rr.parserKkma(intext)
    #rr.parserHannanum(intext)
    #rr.parserTwitter(intext)
    #rr.parserMecab(intext)
    ret = rr.parserNouns(intext)
    print("final : ", ret)



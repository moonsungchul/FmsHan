
from konlpy.tag import Kkma, Komoran, Hannanum, Mecab, Twitter, Okt
from konlpy.utils import pprint


class KonlParser:


    def __init__(self):
        self.komoran = Komoran()
        self.kkma = Kkma()
        self.hann = Hannanum()
        self.mecab = Mecab()
        self.twitter = Twitter()
        self.okt = Okt()

    def parserKomoran(self, intext):
        ch = self.komoran.nouns(intext)
        return ch

    def posKomoran(self, intext):
        ch = self.komoran.pos(intext)
        return ch


    def parserKkma(self, intext):
        ch = self.kkma.nouns(intext)
        return ch

    def posKkma(self, intext):
        ch = self.kkma.pos(intext)
        return ch

    def parserHannanum(self, intext):
        ch = self.hann.nouns(intext)
        return ch

    def posHannanum(self, intext):
        ch = self.hann.pos(intext)
        return ch

    def parserMecab(self, intext):
        ch = self.mecab.nouns(intext)
        return ch

    def posMecab(self, intext):
        ch = self.mecab.pos(intext)
        return ch

    def parserTwitter(self, intext):
        ch = self.twitter.nouns(intext)
        return ch

    def posTwitter(self, intext):
        ch = self.twitter.pos(intext)
        return ch

    def parserOkt(self, intext):
        ch = self.okt.nouns(intext)
        return ch

    def posOkt(self, intext):
        ch = self.okt.pos(intext)
        return ch


    def parserNouns(self, intext):
        buf = []
        buf.append(rr.parserKomoran(intext))
        buf.append(rr.parserKkma(intext))
        buf.append(rr.parserHannanum(intext))
        buf.append(rr.parserTwitter(intext))
        buf.append(rr.parserMecab(intext))
        buf.append(rr.parserOkt(intext))


        dic = {}
        for ar in buf:
            for nn in ar:
                if nn in dic:
                    dic[nn] +=1
                else:
                    dic[nn] = 0
        ret = []
        for key, val in dic.items():
            if val >= 3:
                ret.append(key)
        return ret


    def parserPos(self, intext):
        buf = []
        buf.append(rr.posKomoran(intext))
        buf.append(rr.posKkma(intext))
        buf.append(rr.posHannanum(intext))
        buf.append(rr.posTwitter(intext))
        buf.append(rr.posMecab(intext))
        buf.append(rr.posOkt(intext))
        dic = {}
        for ar in buf:
            for vv in ar:
                #if vv[0] in dic:
                if vv[0] not in dic:
                    dic[vv[0]] = [vv[1]]
                else:
                    dic[vv[0]].append(vv[1])
        return dic


if __name__ == '__main__':
    rr = KonlParser()
    intext = u'질문이나 전의 사항은 갓협 이슈 트래커에 남겨주세요'
    #rr.posKomoran(intext)
    #rr.poskkma(intext)
    #rr.posHannanum(intext)
    #rr.posMecab(intext)
    #rr.posTwitter(intext)
    #rr.posOkt(intext)
    rr.parserPos(intext)
    
    #rr.parserKkma(intext)
    #rr.parserHannanum(intext)
    #rr.parserTwitter(intext)
    #rr.parserMecab(intext)
    #ret = rr.parserNouns(intext)
    #print("final : ", ret)


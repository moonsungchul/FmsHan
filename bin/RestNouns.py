from flask_restful import Resource, request

class RestNouns(Resource):
    """
    {
        "type": "all|hananum|kkma|komoran|mecab|okt", 
        "source": "영등포구청역에 있는 맛집 좀 알려주세요", 
        "result" : [] 
    }
    """

    def __init__(self, **kwargs):
        self.konl = kwargs['Parser'] 


    def put(self):
        print("put test ...")
        jj = request.get_json()
        print(jj)

        stype = jj['type']

        if stype == "hananum":
            print("hananum ...")
            result = self.konl.parserHannanum(jj['source'])
            jj['result'] = result
            return jj
        elif stype == "kkma":
            print("kkma ...")
            result = self.konl.parserKkma(jj['source'])
            jj['result'] = result
            return jj
        elif stype == "komoran":
            print("komoran ...")
            result = self.konl.parserKomoran(jj['source'])
            jj['result'] = result
            return jj
        elif stype == "mecab":
            print("mecab ...")
            result = self.konl.parserMecab(jj['source'])
            jj['result'] = result
            return jj
        elif stype == "okt":
            print("okt ...")
            result = self.konl.parserOkt(jj['source'])
            jj['result'] = result
            return jj
            
        elif stype == "all":
            print("all ...")
            result = self.konl.parserNouns(jj['source'])
            jj['result'] = result
            return jj

        else:
            print("error")
            jj['result'] = ["error type"]
            return jj
            


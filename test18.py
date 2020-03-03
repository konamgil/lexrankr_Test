from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_restful import reqparse
from lexrankr import LexRank
from time import time


app = Flask(__name__)
api = Api(app)
lexrank = LexRank()  # can init with various settings


@app.route('/summary', methods=['POST'])
def post():
    try:
        start = time()
        parser = reqparse.RequestParser()
        parser.add_argument('contents', type=str)
        args = parser.parse_args()

        contents = args['contents']
        print("==== contents ==== : ", contents)

        print(contents)

        # lexrank.summarize(contents)
        # originalText = "이 업체 물건 절대 사지마세요. 형편없습니다. 직원들이 고객은 안중에도 없습니다. 열 받게 만드는 데 선수입니다. 박지원 직원인지 대표인지 몰라도 열받게 하는 제주가 보통이 넘습니다. 다시 한 번 강조하지만 절대 네버네버 스위트피 사지 마세요. 절대 비추입니다."
        lex = LexRank()
        lex.summarize(contents)

        sum = lex.probe(2)

        print(lex.probe(2))

        strd = sum[1] + " " + sum[0]

        resp = {"sum": strd}


        return jsonify(resp)
    except Exception as e:
        return {'error': str(e)}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=51039)


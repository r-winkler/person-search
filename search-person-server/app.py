from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import unidecode
import sys

from service.person_service import PersonService
from service.algo_compare_service import AlgoCompareService
from service.person_similarity_service import PersonSimilarityService

person_service = PersonService()
algo_compare_service = AlgoCompareService()
person_similarity_service = PersonSimilarityService()

app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/test')
def test():
    str1 = request.args.get('str1')
    str2 = request.args.get('str2')
    ignore_case = request.args.get('ignoreCase')
    ignore_accent = request.args.get('ignoreAccent')

    if ignore_case == 'true':
        str1 = str1.lower()
        str2 = str2.lower()

    if ignore_accent == 'true':
        str1 = unidecode.unidecode(str1)
        str2 = unidecode.unidecode(str2)

    result = algo_compare_service.compare(str1, str2)

    return jsonify(result.__dict__)


@app.route('/persons')
def persons():
    return person_service.find_all().to_json(orient='records', force_ascii=False)


# http://localhost:5000/search?name=Winkler&firstname=René
@app.route('/search')
def search():
    name = request.args.get('name')
    firstname = request.args.get('firstname')
    algo_type = request.args.get('algoType') or 'jaro-winkler'
    name_threshold = float(request.args.get('nameThreshold')) if request.args.get('nameThreshold') else 0.9
    firstname_threshold = float(request.args.get('firstnameThreshold')) if request.args.get('firstnameThreshold') else 0.85
    word_similarity = request.args.get('wordSimilarity') == 'true' if request.args.get('wordSimilarity') else False
    word_similarity_name_threshold = float(request.args.get('wordSimilarityNameThreshold')) if request.args.get('wordSimilarityNameThreshold') else 0.3
    word_similarity_firstname_threshold = float(request.args.get('wordSimilarityFirstnameThreshold')) if request.args.get('wordSimilarityFirstnameThreshold') else 0.3

    print(name_threshold, file=sys.stderr)
    return person_similarity_service.find_similar(name, firstname, algo_type, name_threshold, firstname_threshold, word_similarity, word_similarity_name_threshold, word_similarity_firstname_threshold)[['name', 'firstname']].to_json(orient='records', force_ascii=False)

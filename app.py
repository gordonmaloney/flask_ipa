from flask import *
import json, time
import requests
from bs4 import BeautifulSoup
import lxml
import asyncio
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/', methods=['GET'])
def home_page():
    data_set = {'Msg': 'API running'}
    json_dump = json.dumps(data_set)

    return json_dump


@app.route('/ipa/', methods=['GET'])
async def request_page():
    # /ipa/?word=duine&lang=scottish_gaelic
    word_query = str(request.args.get('word'))
    lang_query = str(request.args.get('lang'))


    def CheckIpa(word):
        ipa_url = f'https://en.wiktionary.org/wiki/{word}'

        r_ipa = requests.get(ipa_url)

        soup_ipa = BeautifulSoup(r_ipa.content, 'lxml')

        return soup_ipa.find("span", id='Scottish_Gaelic').findNext('span', class_='IPA').string

    ipa = CheckIpa(word_query)






    data_set = {'word': word_query, 'ipa': ipa}
    json_dump = json.dumps(data_set)

    return json_dump

if __name__ == '__main__':
    app.run(port=7777)

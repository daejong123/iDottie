import requests

class Translate(object):

    def hello(self):
        print('hello')

    def translate(self, text):
        result = requests.get('http://fanyi.youdao.com/translate', {'type': 'AUTO', 'doctype': 'json','i': str(text)})
        print(result.json()['translateResult'])
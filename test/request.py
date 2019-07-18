import requests

result = requests.get('http://fanyi.youdao.com/translate', {'type': 'AUTO', 'doctype': 'json','i': '你好'})
print(result.json()['translateResult'])
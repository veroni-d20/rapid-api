import json

f = open("data.json", "r")
news_data = f.read()
json_object = json.loads(news_data)
print(json_object['articles'][0]['summary'])

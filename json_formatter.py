import json

bad = open('bad.json', 'r', encoding="utf8")
bad_json = bad.read()
bad.close()

bad_content = json.loads(bad_json)
good_content = json.dumps(bad_content, indent=4)

good = open('good.json', 'w', encoding="utf8")
good.write(good_content)
good.close()
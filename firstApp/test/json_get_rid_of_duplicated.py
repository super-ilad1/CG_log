import json
with open("term_json",'r',encoding='utf-8', errors='ignore') as f:
    json_data=set(json.loads(f.read()))
    print(len(json_data))
    print(len(json.loads(f.read())))

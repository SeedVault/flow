import jsonschema
import simplejson as json

with open('flow-schema.json', 'r') as f:
    schemaData = f.read()

schema = json.loads(schemaData)

with open('flow-json-eg-1.json', 'r') as f:
    jsonData = f.read()

jsonObj = json.loads(jsonData)

jsonschema.validate(jsonObj, schema)
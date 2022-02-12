import json


def get_schema_by_ref(data, ref):
    parts = ref.split("/")
    schema = data["components"]["schemas"][parts[-1]]['properties']
    return schema

def get_attrs_from_schema(schema):
    attrs = schema.keys()
    # print(attrs)
    for attr in attrs:
        print(attr, schema[attr]['type'])


with open('../swagger.json', 'r') as f:
  data = json.load(f)
  paths = data['paths'].keys()
  for path in paths:
      methods = data['paths'][path].keys()
      for method in methods:
          # print(path)
          success_body_json = None
          try:
              success_body_json =\
                  data['paths'][path][method]["responses"]["200"]['content']["application/json"]["schema"]["items"]["$ref"]
              attrs = get_attrs_from_schema(get_schema_by_ref(data, success_body_json))
              # print(attrs)
          except KeyError:
              pass

# "$ref": "#/components/schemas/AcademicQtrDto"



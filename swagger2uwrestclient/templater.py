from jinja2 import Environment, FileSystemLoader
import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

def print_templ():
    j2_env = Environment(loader=FileSystemLoader(THIS_DIR),
                         trim_blocks=True)

    data  = {"model_classes": [{"class": "FooBarClass",
                                "model_attrs": [{"name": "user",
                                                 "type": "models.CharField(max_length=32)"},
                                                {"name": "title",
                                                 "type": "models.CharField(max_length=32)"},
                                                {"name": "description",
                                                 "type": "models.CharField(max_length=32)"}
                                                ]}
                               ]}
    out = j2_env.get_template('templates/models.py').render(data)
    print(out)

if __name__ == '__main__':
    print_templ()
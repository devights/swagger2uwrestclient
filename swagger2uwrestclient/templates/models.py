from restclients_core import models


{%+ for line in model_classes %}
class {{line.class}}(models.Model):
    {%+ for attr in line.model_attrs %}
    {{attr.name}} = {{attr.type}}
    {% endfor %}

{% endfor %}
{{ objname | escape | underline}}
{{ fullname | escape}}

{% block modules %}
{% if modules %}
.. rubric:: Modules

.. autosummary::
   :toctree:
   :template: custom-module-template.rst
   :recursive:
{% for item in modules %}
   {{ item }}
{%- endfor %}
{% endif %}
{% endblock %}

.. automodule:: {{ fullname }}

   {% block classes %}
   {% if classes %}
   .. rubric:: {{ _('Classes') }}

   .. autosummary::
      :toctree:
      :template: custom-class-template.rst
   {% for item in classes %}
      {{ item }}
   {%- endfor %}
   {% endif %}
   {% endblock %}

   {% block attributes %}
   {% if attributes %}
   .. rubric:: Module Attributes

   .. autosummary::

   {% for item in attributes %}
      {{ item }}
   {%- endfor %}
   {% endif %}
   {% endblock %}

   {% block functions %}
   {% if functions %}
   .. rubric:: {{ _('Functions') }}

   .. the null templates have autosummary make the table, but not the entries

   .. autosummary::
      :template: custom-null-function-template.rst

   {% for item in functions %}
      {{ item }}
   {%- endfor %}
   {% endif %}
   {% endblock %}

   {% block exceptions %}
   {% if exceptions %}

   .. rubric:: {{ _('Exceptions') }}

   .. autosummary::
      :template: custom-null-function-template.rst

   {% for item in exceptions %}
      {{ item }}
   {%- endfor %}
   {% endif %}
   {% endblock %}

   {% for item in attributes %}
   .. autoattribute:: {{ item }}

   {%- endfor %}
 
   {% for item in functions %}
   .. autofunction:: {{ item }}
 
   {%- endfor %}
 
   {% for item in exceptions %}
   .. autoexception:: {{ item }}

   {%- endfor %}

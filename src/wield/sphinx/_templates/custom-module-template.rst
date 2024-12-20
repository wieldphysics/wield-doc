{{ name | escape | underline}}
{{ fullname | escape}}

.. currentmodule:: {{ fullname }}


{% block aliases %}
{% if classes_imported or functions_imported or exceptions_imported %}
.. rubric:: {{ _('Aliases') }}

Items from sub-modules exposed to import from this module

.. list-table::
   :class: longtable
   :width: 100%
{% for item, val in classes_imported.items() if val.startswith(fullname) %}
   * - :class:`{{ item }}<{{ val }}>`
{%- endfor %}{%- for item, val in functions_imported.items() if val.startswith(fullname) %}
   * - :func:`{{ item }}<{{ val }}>`
{%- endfor %}{%- for item, val in exceptions_imported.items() if val.startswith(fullname) %}
   * - :exc:`{{ item }}<{{ val }}>`
{%- endfor %}
 
{% endif %}
{% endblock %}

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



   .. rubric:: {{ _('Details') }}

   {% for item in attributes -%}
   .. autoattribute:: {{ item }}

   {% endfor %}
 
   {% for item in functions -%}
   .. autofunction:: {{ item }}
 
   {% endfor %}
 
   {% for item in exceptions -%}
   .. autoexception:: {{ item }}

   {% endfor %}



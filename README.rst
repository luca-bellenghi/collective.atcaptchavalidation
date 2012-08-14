Introduction
============

This product provides a dummy field that allow to request captcha validation 
(through collective.recaptcha) when a new object it's created.

How to use it
=============

Just install the product; then in the plone_control_panel you will find the new
entry "Select type to validate with captcha". Here you can select types you want
to relate to captcha validation.

.. image:: http://imagebin.org/index.php?mode=image&id=224536
   :alt: Types configuration

Remembar to configure collective.recaptcha here:[[BR]]
/path/to/your/site/@@recaptcha-settings

Then, creating a new AT configured to deal with captcha validation, you'll be able
to see captcha field at the form bottom

.. image:: http://imagebin.org/index.php?mode=image&id=224538
   :alt: Captcha in the AT edit form

Dependencies
============

 * Plone 4.2 (Not tested on older versions)
 * `collective.recaptcha`__
 * `archetypes.schemaextender`__ (to extends AT dinamically)
 * `plone.app.registry`__ (to store settings)

__ http://pypi.python.org/pypi/collective.recaptcha/
__ http://pypi.python.org/pypi/archetypes.schemaextender/
__ http://pypi.python.org/pypi/plone.app.registry

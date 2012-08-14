from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='collective.atcaptchavalidation',
      version=version,
      description="Captcha validation for Archetypes",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='archetypes catpcha field validation',
      author='lucabel',
      author_email='lucabel@gmail.com',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'collective.recaptcha',
          'archetypes.schemaextender'
      ],
      entry_points=""" """,
      )

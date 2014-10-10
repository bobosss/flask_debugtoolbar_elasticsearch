from setuptools import setup, find_packages

setup(
    name='Flask_debugtoolbar_elasticsearch',
    version="0.1",
    description='Elasticsearch panel for flask debug toolbar',
    long_description=open('README.rst').read(),
    author='Boboss',
    author_email='bobos.papa@gmail.com',
    include_package_data=True,
    zip_safe=False,
    py_modules=['elastics'],
    setup_requires=[
        'Flask>=0.8',
        'elasticsearch',
        'Flask-DebugToolbar',
    ],
	classifiers=[
	'Development Status :: 3 - Alpha',
	'Environment :: Web Environment',
	'Intended Audience :: Developers',
	'License :: OSI Approved :: MIT License',
	'Operating System :: OS Independent',
	'Programming Language :: Python',
	'Topic :: Database',
	'Topic :: Software Development :: Libraries :: Python Modules',
	],
  
)

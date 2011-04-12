# Good list of classifiers at:
# http://pypi.python.org/pypi?%3Aaction=list_classifiers

from setuptools import setup
setup(
	name = 'dnsmon',
	version = "0.1",
	packages = ['dnsmon'],
	author = 'Jim Wyllie',
	author_email = 'jwyllie83@gmail.com',
	description = 'A package to monitor DNS resolution values and report on differences from expected values',
	url = 'http://github.com/jwyllie83/dnsmon',
	install_requires = ['python-daemon>=1.5.5', 'pydns>=2.3.4'],
	include_package_data = True,
	classifiers = [
		"Environment :: No Input/Output (Daemon)",
		"Intended Audience :: Developers",
		"License :: OSI Approved :: GNU General Public License (GPL)",
		"Natural Language :: English",

	]
)

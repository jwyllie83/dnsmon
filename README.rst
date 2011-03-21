======
dnsmon
======

What is it?
===========

``dnsmon`` is a way to test and verify DNS resolution from a given location.  I find it useful in the following situations:

Firewall Rules
~~~~~~~~~~~~~~

Say you have a firewall rule like the following, which sets traffic to ``example.com`` to a given class::

 iptables -t mangle -A POSTROUTING -o eth0 -d 192.0.32.0/255.255.255.0 -p tcp -j CLASSIFY --set-class 1:10

However, you're not sure how long ``192.0.32.0/24`` will point to ``example.com`` and you'd like to be notified when it doesn't so you can update your traffic rule.  To do so, you can use ``dnsmon`` to monitor and e-mail you when the mapping changes.  You can then update your firewall rule with the new value.

DNS Server Configuration Tests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Though there are other ways to do this, you can use this to make sure your DNS server resolves a given host to a target network.

DNS Server Uptime Tests
~~~~~~~~~~~~~~~~~~~~~~~

Though there are other ways to do this, you can use this to make sure your DNS server is responsive to queries.

How does it work?
=================

``dnsmon`` uses the default machine resolver to look up a set of DNS addresses with a configurable frequency.  It'll compare the results against the config file you provide and send an email to the configured address if it doesn't match.

OS Compatibility
================

I've only tested this on Linux, so I'm only sure it works there.

Installation
============

Easiest installation is with PyPI via pip::

 sudo apt-get install pip; sudo pip install dnsmon

If you don't have pip, you can install it with the older setuptools::

 sudo apt-get install python-setuptools; sudo easy_install dnsmon

Once installed, create a base template for settings::

 cp dnsmon/settings_local.py.example dnsmon/settings_local.py

... and try it out::

 dnsmon.py --foreground

If all goes well, run it as a daemon::

 dnsmon.py

.. _PyPI:  http://pypi.python.org/

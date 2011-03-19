#!/usr/bin/env python

__doc__ = """Daemon to check whether hostname resolutions have changed for a
configured set of hostnames.  If so, it should notify the user about the
discrepancy."""

import sys
import settings
import socket
import time

from settings import dns_settings, message
from mailer import Mailer
from resolver import lookup

try:
	import daemon
except ImportError, e:
	sys.stderr.write('Unable to import daemon; you can get it with: sudo apt-get install python-setuptools; sudo easy_install daemon\n')
	sys.exit(1)

try:
	import argparse
except ImportError, e:
	sys.stderr.write('Unable to import argparse.  You can get it with: sudo apt-get install python-setuptools; sudo easy_install argparse\n')
	sys.exit(1)


def ip_in_network(ip, network):
	"""Returns True if ip is contained in network.  Network is 1.2.3.0/24 format"""
	network, subnet = network.split('/')
	network = network.split('.')
	ip = ip.split('.')
	network = int("%02x%02x%02x%02x" % tuple([int(x) for x in network]), 16)
	ip = int("%02x%02x%02x%02x" % tuple([int(x) for x in ip]), 16)

	return ip & network == network
	

def run():

	# This is some pretty ridiculous indenting, but it's pretty
	# straightforward... look up the address and make sure they're all in
	# the network
	while True:
		for test in dns_settings:
			hostname = test['hostname']
			target_network = test['network']
			actual_ips = lookup(hostname)
			for ip in actual_ips:
				if not ip_in_network(ip, target_network):
					notify(hostname, ip, target_network)
					break

		time.sleep(settings.delay)

def notify(hostname, ip, target_network):
	message_body = message % {'hostname' : hostname, 'resolved_ip' : ip, 'expected_network' : target_network}
	subject = 'Mismatched IP detected for hostname %s' % hostname
	Mailer(settings.mail_to, settings.mail_from, subject, message_body)

def main():

	the_parser = argparse.ArgumentParser(description=__doc__)
	the_parser.add_argument('-f', '--foreground', action='store_true', default=False, help='If set, runs in the foreground.  Defaults to %(default)s')
	options = the_parser.parse_args()

	if not options.foreground:
		with daemon.DaemonContext():
			run()
	else:
		run()


if __name__ == '__main__':
	main()

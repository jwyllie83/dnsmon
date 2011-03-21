# Mailer Settings.  Replace any of these with None if they don't apply
mail_host = None
mail_port = None
mail_username = None
mail_password = None
mail_use_TLS = None

mail_from = None	# Should be a string
mail_to = None		# Should be a list

delay = 14400		# Seconds to wait between runs

# Sample DNS settings.  You can add your own in the local settings.
dns_settings = [
	{
		'hostname' : 'www.google.com',
		'network'  : '74.125.226.0/24',
	},
]

# Message will be tokenized appropriately before sending
message = """
dnsmon discovered a mismatched host resolution.

Hostname         : %(hostname)s
Resolved IP      : %(resolved_ip)s
Expected Network : %(expected_network)s
"""

# Store things you don't want committed in thr repository (say, mail passwords...)
from settings_local import *

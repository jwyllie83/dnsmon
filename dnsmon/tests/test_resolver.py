from dnsmon import resolver

def test_resolver():
	"""Makes sure that the resolver is giving any and all IP addresses"""
		
	# Don't really want to do a huge number of lookups; a sanity check will work...
	assert resolver.lookup('example.com') == ['192.0.32.10']

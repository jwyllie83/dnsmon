__doc__ = """Wrapper to pyDNS to retrieve all DNS results for a given hostname"""

import DNS
DNS.ParseResolvConf()
resolver = DNS.DnsRequest(qtype='A')

def lookup(hostname):
	global resolver
	res = resolver.req(hostname)
	if len(res.answers) == 0:
		return []
	return [x['data'] for x in res.answers]

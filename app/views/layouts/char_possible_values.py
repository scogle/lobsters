import csv
from util import *
from namespaces import *
from graph import getGraph

NAN = 5000
def getNAN():
	global NAN
	NAN += 1
	return NAN

# To findOrMake new nodes
directory = {}


lookup = {}

with open ('characteristics_possible_values.ttl', 'wb') as output:
	output.write(NAMESPACE_PREFIXES)
	with open('characteristics_possible_values.csv', 'rU') as csvfile:
		csvreader = csv.reader(csvfile)
		for csvrow in csvreader:
			if csvrow[1] in lookup:
				# might need to change this to csvrow[5]
				lookup[csvrow[1]].append(csvrow[6])
			else:
				lookup[csvrow[1]] = [csvrow[6]]

		for char,vals in lookup.iteritems:
			print char
			print vals






# 			res = getGraph().executeTupleQuery("""
# SELECT ?uri WHERE {
# 	?uri rdf:type spo:Characteristic .
# 	?uri spo:fieldName "%s" .
# }
# 			""" % csvrow[1])
# 			print csvrow[1]
# 			if res:
# 				try:
# 					uri = str([row for row in res][0]['uri'])
# 					print uri
# 					for val in csvrow[]
# 					ttl = "\n%s rdfs:label '%s' .\n" % (uri, csvrow[1])
# 					print ttl
# 					output.write(ttl.encode('utf-8'))
# 				except:
# 					print "exception in result"
# 					ttl = """
# spo:_char_%s
# 	rdf:type spo:Characteristic ;
# 	spo:fieldName "%s" ;
# 	rdfs:description '%s' .
# 					""" % (getNAN(), csvrow[0], csvrow[1])
# 				print ttl
# 				output.write(ttl)
# 			else:
# 				ttl = """
# spo:_char_%s
# 	rdf:type spo:Characteristic ;
# 	spo:fieldName "%s" ;
# 	rdfs:description "%s" .
# 				""" % (getNAN(), csvrow[0], csvrow[1])
# 				print ttl
# 				output.write(ttl)









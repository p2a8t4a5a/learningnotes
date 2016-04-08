#! /usr/bin/python
import fileinput,re
pat=re.compile('From: (.*) <.*?>$')
for line in fileinput.input():
	m=pat.match(line)
#	if m:print m.group(1)

fileinput.close()

pat=re.compile(r'[a-z\-\.]+@[a-z\-\.]+',re.IGNORECASE)
addresses=set()
for line in fileinput.input():
	for address in pat.findall(line):
		addresses.add(address)
for address in sorted(addresses):
	print address


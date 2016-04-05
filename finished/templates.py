#! /usr/bin/env python
#do things like unpack[1+5]
#[name="yaoge"]he is [name]

import re,fileinput
lines=[]
for line in fileinput.input():
	lines.append(line)

text=''.join(lines)

pat=re.compile(r'\[(.*?)\]')
scope={}
def solve(match):
	m=match.group(1)
	try:
		return str(eval(m,scope))
	except SyntaxError:
		exec(m,scope)
		return ''

text=pat.sub(solve,text)
f=open('data.out','w')
f.write(text)

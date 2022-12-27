#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  wspace.py
#  
#  Copyright 2022 mike <mike@pop-os>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

def bbshub_gen(s0 = 14025256):
	# Blum Blum Shub Generator
	return (s0*s0) % 20300713
	
def int_list(n):
	l = [int(c) for c in str(n)]
	return(l)
	
def wspaces(n_words):
	# generate n_words using bbshub and convert to list
	s0 = 14025256
	sn = bbshub_gen(s0)
	infstr = int_list(s0)
	infstr += (int_list(sn))
	n_words -= 2
	while n_words:
		sn = bbshub_gen(sn)
		infstr += (int_list(sn))
		n_words -= 1
	n_ints = len(infstr)
	
	P = dict()
	for posn in range(32):
		wspace = [infstr[posn]]
		for c in range(posn+1,n_ints//2):
			wspace.append(wspace[-1]+infstr[c])
		print();print(f"Posn:{posn}\n {wspace}")
		
		for t in wspace:
			if t not in P:
				P[t] = posn
				
		print(P)
		print(len(P))
		foo =[k for k in P.keys()]
		foo = sorted(foo)
		S=0
		for k in foo:
			S += P[k]
		print(S)
		
def infstr(n_words):
	# generate n_words using bbshub and convert to list
	s0 = 14025256
	sn = bbshub_gen(s0)
	infstr = int_list(s0)
	infstr += (int_list(sn))
	n_words -= 2
	while n_words:
		sn = bbshub_gen(sn)
		infstr += (int_list(sn))
		n_words -= 1
	n_ints = len(infstr)
	# infstr[] has len() single digit integers
	
	width = 24
	nxt = width	# index to additional integer from inf string
	# ??advance the workspace until the first sum is not in dictionary??
	# Initialise the workspace length 32
	wspace = [infstr[0]]
	for c in range(1,width+1):
		wspace.append(wspace[-1]+infstr[c])
		
	# Loop start
	p = dict()
	p[0] = 0
	posn = 1
	print(wspace)		
	while True:
		# Process workspace
		for i in wspace:
			if i not in p:	# check for key
				p[i] = posn
		# update workspace
		delta = wspace.pop(0) * -1
		if nxt >= len(infstr):
			break
		wspace.append(wspace[-1]+infstr[nxt])
		nxt += 1
		wspace = list(map(lambda x : x + delta, wspace))
		print(wspace)
	
#-----------------------------------------------------------------------
		
def main(args):
	infstr(80)
	return 0
	
	
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

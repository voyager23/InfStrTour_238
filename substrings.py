#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  substrings.py
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
	
#-----------------------------------------------------------------------
	
def main(args):
	
	max_ss = 32	# max sub string length
	wlen = max_ss * 4	# length of 'infinite' string
	
	s0 = 14025256
	ss = int_list(s0)
	while len(ss) < wlen:
		sn = bbshub_gen(s0)
		#print(s0, sn, int_list(sn))
		ss += int_list(sn)
		s0 = sn
	#print(ss)
	
	# workspace is a list of substring sums
	# generate successive wspaces by simple addition
	for posn in range(8):
		wspace = [ss[posn]]
		for c in range(posn+1,max_ss+1):
			wspace.append(wspace[-1]+ss[c])
		print();print(wspace)
	
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

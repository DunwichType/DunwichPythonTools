#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Dunwich Type Cooker
#Based on Erik van Blokand's Typecooker.com without the Noordzijian logic
#Version 2.0

#import random
from random import choice
from random import randint

characters = ['Uppercase', 'Lowercase', 'Mixed Case', 'Figures']

figures = ['Old Style', 'Lining', 'Hybrid']

weight = ['Hairline', 'Thin', 'Light', 'Medium', 'Semibold', 'Bold', 'Black', 'Ultra',]

width = ['XCondensed', 'Condensed', 'Regular', 'Wide', 'Xwide']

tool = ['Wide Nib Pen', 'Pointed Pen', 'Pointed Brush', 'Flat Brush', 'Speedball']

style = [ 'Blackletter', 'Glyphic', 'Script', 'Uncial', 'Humanist', 'Modern']

contrast = ['None', 'Slight', 'Some', 'Lots', 'Extreme']

serifs = ['None', 'Slab', 'Wedge']

xheight = ['XSmall', 'Small', 'Medium', 'Large', 'Huge', 'Unicase']

slant = ['Roman/Upright', 'Roman/Upright', 'Slight', 'Exaggerated']

special = ['Round Corners', 'Concave Stems', 'No Curves', 'Tuscan', 'Stencil', 'No Descender', 'Inline', 'Multiple Lines', 'Shaded', 'Inverse Stress', 'Square Interior', 'Dots']

paramWeight = 'Weight: ' +  choice(weight)
paramWidth = 'Width: ' +  choice(width)
paramTool = 'Tool: ' +  choice(tool)
paramStyle = 'Style: ' +  choice(style)
paramContrast = 'Contrast: ' + choice(contrast)
paramSerifs = 'Serifs: ' +  choice(serifs)
paramXheight = 'x-Height: ' +  choice(xheight)
paramSlant = 'Slant: ' +  choice(slant)
paramSpecial1 = 'Special: ' +  choice(special)

print ''
print 'Design A Typeface With These Parameters'
print ''
print paramWeight
print paramWidth
print paramTool
print paramStyle
# Serifs
if paramStyle != 'Style: Script':
	print paramSerifs
	if paramSerifs != 'Serifs: None':
		roll = randint(4,100)
		if roll%4==0:
			print 'No Bracketing on Serifs'
			
print paramXheight
print paramSlant
#Character Set
charChoice = choice(characters)
if  charChoice == 'Figures':
	figChoice = choice(figures)
	paramCharacters = 'Characters: ' +  figChoice + ' Figures'
else :
	paramCharacters = 'Characters: ' +  charChoice
print paramCharacters

# Special design considerations
print paramSpecial1
roll = randint(3,99)
if roll%3==0:
	paramSpecial2 = 'Special: ' +  choice(special)
	while paramSpecial2 == paramSpecial1:
		paramSpecial2 = 'Special: ' +  choice(special)
	print paramSpecial2
	roll = randint(3,99)
	if roll%3==0:
		paramSpecial3 = 'Special: ' +  choice(special)
		while paramSpecial3 == paramSpecial1 or paramSpecial3 == paramSpecial2:
			paramSpecial3 = 'Special: ' +  choice(special)
		print paramSpecial3
	
print ''

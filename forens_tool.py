import os
import binascii
import Image
import sys
def stats(pixels):
	elements={}
	var=list()
	ave=list()
	length=len(pixels[0])
	c=0
	a=pixels
	while c<length:
		average=0
		variations=0
		nums=list()
		d=0
		while d<len(a):
			temp=a[d][c]
			average+=temp
			try:
				nums.index(temp)
			except ValueError:
				nums.append(temp)
				variations+=1
			
			d+=1
		average/=len(a)
		ave.append(average)
		var.append(variations)
		c+=1		
	elements["R"]=(var[0],ave[0])
	elements["G"]=(var[1],ave[1])
	elements["B"]=(var[2],ave[2])
	if length==4:
		elements["A"]=(var[3],ave[3])
	else:
		elements["A"]="n/a"	
	return elements
def analyze(statistics):
	r=statistics["R"]
	print "There are", r[0], "different shades represented in R"
	print "These shades are centered around", r[1],"\n"
	g=statistics["G"]
	print "There are", g[0], "different shades represented in G"
	print "These shades are centered around", g[1], "\n"
	b=statistics["B"]
	print "There are", b[0], "different shades represented in B"
	print "These shades are centered around", b[1]	, "\n"	
	try:
		a=statistics["A"]
		int(a[0])
		print "There are", a[0], "different shades represented in A"
		print "These shades are centered around", a[1]	
	except ValueError:
		pass
def main():
	input_file=""
	if len(sys.argv)!=2:
		print "Correct input: python forens_tool.py input_file"	
	try:
		input_file=sys.argv[1]
		im=Image.open(input_file)
		pix=im.load()
		pixels=list()
		width=im.size[0]
		height=im.size[1]
		x=0
		y=0
		while y<height:
			while x<width:
				pixels.append(pix[x,y])
				x+=1
			x=0
			y+=1
		statistics=stats(pixels)
		analyze(statistics)
			
	except IndexError:
		pass 	
	except IOError:
		print "File", input_file, "Does Not Exist with Current Specifications"
main()

import re
from pprint import pprint

heChars = [
		u'\u05d0',u'\u05d1',u'\u05d2',u'\u05d3',u'\u05d4',u'\u05d5',u'\u05d6',u'\u05d7',u'\u05d8',u'\u05d9',\
		#//u'\u05da',\
		u'\u05db',u'\u05dc',\
		#//u'\u05dd',\
		u'\u05de',\
		#//u'\u05df',\
		u'\u05e0',u'\u05e1',u'\u05e2',\
		#//u'\u05e3',\
		u'\u05e4',\
		#//u'\u05e5',\
		u'\u05e6',u'\u05e7',u'\u05e8',u'\u05e9',\
		u'\u05ea']

def main():
	filename = '25-26.original.txt'
	add1 = 6
	add2 = 0
	addAmounts(filename,add1,add2)

def addAmounts(filename,add1,add2):
	file = open(filename,'r')
	lines = file.readlines()
	symbol = '!'
	for line in lines:
		if line[0] == symbol:
			print(symbol + ' ' + int2heb(heb2int(line[1:]) + add1))
		else:
			if add2 == 0:
				print(line,end='')
			else:
				abc = re.finditer(r"\{{4}(.*?)\}{4}", line)
				newStr = ''
				last = 0
				for match in abc:
					newStr += line[last:match.start(1)] +  int2heb(heb2int(match.group(1)) + add2)
					last = match.end(1)
				newStr += line[last:-1]
				#print(line,end='')
				print(newStr)
			

	

def heb2int(num):
	num = re.sub(u'[^\u05d0-\u05ea]', "", num)
	gematria = 0
	for letter in num:
		alef = u'\u05d0'
		relativeVal = int.from_bytes(letter.encode('utf-8'),byteorder='big') - int.from_bytes(alef.encode('utf-8'),byteorder='big') + 1
		if relativeVal >= 12 and relativeVal <= 13:
			relativeVal -= 1
		if relativeVal == 15:
			relativeVal -= 2
		if relativeVal >= 17 and relativeVal <= 19:
			relativeVal -= 3
		if relativeVal == 21:
			relativeVal -= 4
		if relativeVal >= 23:
			relativeVal -= 5
		if relativeVal > 10 and relativeVal < 20:
			relativeVal = (int(str(relativeVal)[1]) + 1) * 10
		elif relativeVal >= 20 and relativeVal < 26:
			relativeVal = (int(str(relativeVal)[1]) + 2) * 100
		gematria += relativeVal
	
	return gematria


	

def	int2heb(num):
	origNum = num
	heb = ""
	place = 0
	while (num >= 1):
		digit = int(num%10)
		num /= 10
		num = int(num)
		baseHebChar = 0 #this is the position of a char in hebChars
		hebChar = ''
		if (digit == 0):
			hebChar = '\0'; #//no char when exactly multiple of ten
		
		else:
			if (place == 0): 
				baseHebChar = 0;# //alef
				hebChar = heChars[(baseHebChar + digit-1)];
				heb = hebChar + heb;
			elif (place == 1):
				baseHebChar = 9; #//yud
				hebChar = heChars[(baseHebChar + digit-1)];
				heb = hebChar + heb
			elif (place >= 2):
				baseHebChar = 18 #//kuf
				if (digit == 9): #//can't be greater than tuf
					hChar1 = heChars[(baseHebChar + digit-9)]
					hChar2 = heChars[(baseHebChar + 3)] #//tuf, need two of these
					heb = "" + hChar2 + hChar2 + hChar1 + heb
				elif (digit > 4):
					hChar1 = heChars[(baseHebChar + digit-5)]
					hChar2 = heChars[(baseHebChar + 3)] #//tuf
					heb = "" + hChar2 + hChar1 + heb
				else:
					hChar1 = heChars[(baseHebChar + digit-1)]
					heb = "" + hChar1 + heb;
				
			
		
		place += 1
		
		#//now search for 15 & 16 to replace
		ka = u'\u05D9\u05D4'; #//careful...don't join these strings
		ku = u'\u05D9\u05D5';
		kaPatt = ("(" + ka + ")+");
		kuPatt = ("(" + ku + ")+");
		heb = re.sub(kaPatt,u'\u05D8\u05D5', heb)
		heb = re.sub(kuPatt,u'\u05D8\u05D6', heb)
		
	return heb
		
if __name__ == '__main__':
	main()
﻿from postFile2 import *

def postBook(title, filename):
	index = {
	"title": title,
	#NO INDEX UPLOAD
	"heTitleVariants" : [],
	"sectionNames": ["Siman" , "Se'if"], 
	"categories": ["Halakhah", "Shulchan Arukh"],
	}
	textIndex = {
		"versionTitle": "Torat Emet 363",
		"versionSource":  "http://www.toratemetfreeware.com/index.html?downloads",
		"language": "he",	
	}
	actuallyPost = False; # False=> outputting file; True=> post to site
	useRealSite = False; # False=> dev site; True=> real site
	postBookIndex = False; #do False for old book in their DB, and do True for new book.
	symbolAtLevel = ['~', '!'] #put symbols where 'NL' means that NL is the lowest level. COMMON symbols: [ '~','^', '@', '$', '!', '#'] that start a new Chapter/Paragraph/etc in ToratEmet
	displayHeaderSymbols = []	# Put symbols (but not NL) that you want to display header into displayHeaderSymbol with bigger first. ex. displayHeaderSymbol = [ '@', '~']	
	createHeader = ['~'] #these are the headers for which you want to create a headers.csv with
	headerAttr = [[1,1]] # put in the attributes for the headers in the format: [displayNum , displayLevelType (ex. daf)] . ex. if using 2 header syms = [[1,0], [0,0]]
	useAsNumberForLocation = [] #typically used for commentary (usually ['!']), where not every line is there but there is only a commentary on some lines.
	postSifKatans = False # if you want to post Sif Katans (which are contained within a line of TE)
	commentary = False #if this is a commentary on something make it true. <book title> on <thing it's a comment on> is assumed to be the title of this book
	postFile2(filename, index, textIndex,symbolAtLevel, actuallyPost, useRealSite,postBookIndex, displayHeaderSymbols, createHeader, headerAttr, useAsNumberForLocation, postSifKatans, commentary)
	

	

title = "Shulchan Arukh, Choshen Mishpat";
filename = "043_חשן משפט מנוקד.txt";
postBook(title, filename)

"""
Comments/Changes/Problems:
manually have to overright 181 b/c of the weird non-n2mber (*) that it begins with. line 5986

there's a weird thing called: קיצור כללי דיני תפיסה מלקט מפסקים ראשונים ואחרונים וקצת מחודשים after 25 and b/f 26.
this has to be renumbered.

got rid of סליק. on last line

"""
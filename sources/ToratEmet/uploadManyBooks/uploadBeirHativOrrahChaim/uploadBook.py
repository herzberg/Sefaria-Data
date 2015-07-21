from postFile2 import *

def postBook(title, filename):
	index = {
	"title": title,
	"titleVariants": ["Beer Hetev on Shulchan Arukh, Orach Chayyim", "Be'ir Hetev on Shulchan Arukh, Orach Chayyim", "Ba'er Hetev on Shulchan Arukh, Orach Chayyim","Beir Hetev on Shulchan Arukh, Orach Chayyim", "Baer Hetev on Shulchan Arukh, Orach Chayyim" ],
	"heTitle" : "באר היטב אורח חיים",
	"heTitleVariants" : [],
	"sectionNames": ["Siman" ,  "Se'if Katan"], 
	"categories": ["Halakhah",  "Shulchan Arukh"],
	}
	textIndex = {
		"versionTitle": "Torat Emet 357",
		"versionSource":  "http://www.toratemetfreeware.com/index.html?downloads",
		"language": "he",	
	}
	actuallyPost = True; # False=> outputting file; True=> post to site
	useRealSite = False; # False=> dev site; True=> real site
	postBookIndex = True; #do False for old book in their DB, and do True for new book.
	symbolAtLevel = ['~', '!'] #put symbols where 'NL' means that NL is the lowest level. COMMON symbols: [ '~','^', '@', '$', '!', '#'] that start a new Chapter/Paragraph/etc in ToratEmet
	displayHeaderSymbols = []	# Put symbols (but not NL) that you want to display header into displayHeaderSymbol with bigger first. ex. displayHeaderSymbol = [ '@', '~']	
	createHeader = ['~'] #these are the headers for which you want to create a headers.csv with
	headerAttr = [[1,1]] # put in the attributes for the headers in the format: [displayNum , displayLevelType (ex. daf)] . ex. if using 2 header syms = [[1,0], [0,0]]
	useAsNumberForLocation = ['!'] #typically used for commentary (usually ['!']), where not every line is there but there is only a commentary on some lines.
	postSifKatans = True # if you want to post Sif Katans (which are contained within a line of TE)
	commentary = True #if this is a commentary on something make it true. <book title> on <thing it's a comment on> is assumed to be the title of this book
	postFile2(filename, index, textIndex,symbolAtLevel, actuallyPost, useRealSite,postBookIndex, displayHeaderSymbols, createHeader, headerAttr, useAsNumberForLocation, postSifKatans, commentary)
	

	

title = "Be'er Hetev on Shulchan Arukh, Orach Chayyim";
filename = "050_באר_היטב_אורח_חיים.txt";
postBook(title, filename)

"""
Comments/Changes/Problems:
added line the following after 2223 into the input file b/c it was weirdly missing:

 ~ סימן קלה - סדר קריאת התורה ביום ב' וה', {{ובו י''ד סעיפים }} 

"""

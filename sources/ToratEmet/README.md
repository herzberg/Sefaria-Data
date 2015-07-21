#Toret Emet Uploader

0. In local_settings, put in yourapikey.
1. Copy the blankBook folder to make a new folder for a different book.
2. Copy the book into the folder from Books_363.
3. Then in uploadBook, write the info about the book (and change the booleans to test/post-to-dev/post-to-www). Start with actuallyPost = False; and useRealSite = False; for testing. Then move to dev site.
4. To run: python uploadBook.py
5. If structure isn't right, then add some symbols (like '~', '#') into the copied book to make it make some sense (when it becomes possible to have hakdamas this might be different); you'll see what you need from a quick skim of the file and of the formatting in the ToratEmet program (windows) or on http://www.toratemetfreeware.com/online/a_root.html.
6. You might need to make small changes in the postFile2 (while parsing),  there's a line there in order to display the symbol line as a header (change displayHeaderSymbol to the symbol). (Try to make the needed changes in the book file instead).
7. Write any changes you make as a comment in the uploadBook, so that you could later come back make changes if the database changes, or we want to use different html tags formatting, etc.
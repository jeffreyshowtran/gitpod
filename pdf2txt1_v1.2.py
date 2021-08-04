#this short program will take a pdf file, convert it to text using
#pdfplumber, modify the output to add new lines where there should be ones,
#and print to a .txt file

import pdfplumber

#set working directory path/file names
pname = input("where is your raw report (path name)?")
fname = input("what is your raw report named (file name)?")

#specify the results directory
r_pname = input("where do you want your results file (path name)?")
r_fname = input("name the results of your output file (file name):")

#create an empty list "txtfile", which will contain all the
#characters of the pdf
txtfile = list()

#create a pdfplumber object - pdfplumber returns each character with positioning
#and other font information. Unfortunately new lines and text blocks are not
#separated by anything, resulting in some odd parsing
pdf = pdfplumber.open(pname + fname)

#get the number of pages in the pdfplumber object
#this is the number of pages in the pdf
pdf_length = len(pdf.pages)

for p in list(range(0, pdf_length)):
    page = pdf.pages[p]
    #how many characters in pdf?
    char_count = len(page.objects['char'])
    #create a list "coord1" of the coordinates of all x0 and y0 coordinates
    coord1 = list()
    for i in list(range(0,char_count)):
        x0 = page.chars[i]['x0']
        y0 = page.chars[i]['y0']
        coord1.append((x0,y0))
    #create a list of the (x,y) distances between two characters
    coord2 = coord1[1:]
    coord1 = coord1[:-1]
    newLine = [(b[0] - a[0], b[1] - a[1]) for a, b in zip(coord1, coord2)]
    #create a list of the indices of all characters that should make the end
    #of a line based on a change in the y-distance or a space between
    #characters > 10units
    newLineIndex = [i for i in range(len(newLine))
                    if newLine[i][1]< -0.5 or newLine[i][0]>=10]
    #create a list of all the characters contained in the pdfplumber object
    line = list()
    for i in list(range(0,char_count)):
        line.append(page.chars[i]['text'])
    #go through the list "line" and edit elements to add a the new line
    #character "/n" based on indexes specified by the newLineIndex list
    for e in newLineIndex:
        line[e] = line[e] + '\n'
    #add on a new line for the last character of the page
    line[-1] = line[-1] + '\n'
    #append this to the list "txtfile", which contains the contents of
    #the entire pdf
    txtfile.extend(line)

#create a string from the list "line"
sep = ''
txt = sep.join(txtfile)

#open a new text file and write the list to the txt file as a string
with open(r_pname + r_fname, 'w') as f:
    f.write(txt)

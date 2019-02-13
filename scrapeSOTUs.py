import urllib.request, re, time
from bs4 import BeautifulSoup
from datetime import datetime
stem = 'http://stateoftheunion.onetwothree.net/texts/'
#connect to a URL
website = urllib.request.urlopen(stem+'index.html')

#read html code
html = website.read()

#use re.findall to get all the links
fullLinks = re.findall('"?\d\d\d\d\d\d\d\d.html', str(html)) ## ['alice@google.com', 'bob@abc.com']

#loop over links
for iLink in range(0, len(fullLinks)):
    # create actual link to scrape
    iFullLink = stem+fullLinks[iLink].lstrip('"')
    fullLinks[iLink]=iFullLink

    # use soup to get them speeches
    soup = BeautifulSoup(urllib.request.urlopen(iFullLink), 'html.parser')
    pres = soup.title.string.split(' | ')[1].replace(' ','-')
    rawdate = datetime.strptime(soup.title.string.split(' | ')[2], '%B %d, %Y')
    date = str(rawdate.year)+"-"+str(rawdate.month)+"-"+str(rawdate.day)
    outfile = open(("raw/"+date+"_"+pres+".txt"), 'w')

    print (soup.title.string, "raw/"+date+"_"+pres+".txt")

    for p in soup.select('p'):
        #print (p.text,'\n')
        outfile.write(p.text+'\n')
        
    #print (len(soup.select('p')))
    
    time.sleep(1)

#iFullLink = stem+fullLinks[0].lstrip('"')
#print (iFullLink)
#soup = BeautifulSoup(urllib.request.urlopen(iFullLink), 'html.parser')
#print (soup.title.string)
#print (len(soup.select('p')))

#pres = soup.title.string.split(' | ')[1].replace(' ','-')
#rawdate = datetime.strptime(soup.title.string.split(' | ')[2], '%B %d, %Y')
#date = str(rawdate.year)+"-"+str(rawdate.month)+"-"+str(rawdate.day)
#print(date+"_"+pres+".txt")

#outfile = open((date+"_"+pres+".txt"), 'w')
#for p in soup.select('p'):
#    outfile.write(p.text+'\n')

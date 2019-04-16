import requests
from bs4 import BeautifulSoup
import re


""" Example of use:
    This will look into "A Study in Scarlet" for the 3rd paragraph, 1st line, 2nd word

    ```
    from sherlock import find_word


    find_word("asis", 3, 1, 2)
    ```

"""




BASE_URL = "https://sherlock-holm.es"

data = {}
data["A Study In Scarlet"] = "/stories/html/stud.html"
data["The Sign of the Four"] = "/stories/html/sign.html"
data["The Hound of the Baskervilles"] = "/stories/html/houn.html"
data["The Valley of Fear"] = "/stories/html/vall.html"
data["A Scandal in Bohemia"] = "/stories/html/scan.html"
data["The Red-Headed League"] = "/stories/html/redh.html"
data["A Case of Identity"] = "/stories/html/iden.html"
data["The Boscombe Valley Mystery"] = "/stories/html/bosc.html"
data["The Five Orange Pips"] = "/stories/html/five.html"
data["The Man with the Twisted Lip"] = "/stories/html/twis.html"
data["The Adventure of the Blue Carbuncle"] = "/stories/html/blue.html"
data["The Adventure of the Speckled Band"] = "/stories/html/spec.html"
data["The Adventure of the Engineer's Thumb"] = "/stories/html/engr.html"
data["The Adventure of the Noble Bachelor"] = "/stories/html/nobl.html"
data["The Adventure of the Beryl Coronet"] = "/stories/html/bery.html"
data["The Adventure of the Copper Beeches"] = "/stories/html/copp.html"
data["Silver Blaze"] = "/stories/html/silv.html"
data["Yellow Face"] = "/stories/html/yell.html"
data["The Stockbroker's Clerk"] = "/stories/html/stoc.html"
data["The Gloria Scott"] = "/stories/html/glor.html"
data["The Musgrave Ritual"] = "/stories/html/musg.html"
data["The Reigate Puzzle"] = "/stories/html/reig.html"
data["The Crooked Man"] = "/stories/html/croo.html"
data["The Resident Patient"] = "/stories/html/resi.html"
data["The Greek Interpreter"] = "/stories/html/gree.html"
data["The Naval Treaty"] = "/stories/html/nava.html"
data["The Final Problem"] = "/stories/html/fina.html"
data["The Adventure of the Empty House"] = "/stories/html/empt.html"
data["The Adventure of the Norwood Builder"] = "/stories/html/norw.html"
data["The Adventure of the Dancing Men"] = "/stories/html/danc.html"
data["The Adventure of the Solitary Cyclist"] = "/stories/html/soli.html"
data["The Adventure of the Priory School"] = "/stories/html/prio.html"
data["The Adventure of Black Peter"] = "/stories/html/blac.html"
data["The Adventure of Charles Augustus Milverton"] = "/stories/html/chas.html"
data["The Adventure of the The Six Napoleons"] = "/stories/html/sixn.html"
data["The Adventure of the The Three Students"] = "/stories/html/3stu.html"
data["The Adventure of the The Golden Pince-Nez"] = "/stories/html/gold.html"
data["The Adventure of the The Missing Three-Quarter"] = "/stories/html/miss.html"
data["The Adventure of the The Abbey Grange"] = "/stories/html/abbe.html"
data["The Adventure of the The Second Stain"] = "/stories/html/seco.html"
data["Wisteria Lodge"] = "/stories/html/wist.html"
data["The Cardboard Box"] = "/stories/html/card.html"
data["The Red Circle"] = "/stories/html/redc.html"
data["The Bruce-Partington Plans"] = "/stories/html/bruc.html"
data["The Dying Detective"] = "/stories/html/dyin.html"
data["Lady Frances Carfax"] = "/stories/html/lady.html"
data["The Devil's Foot"] = "/stories/html/devi.html"
data["His Last Bow"] = "/stories/html/last.html"


def initials(story):
    str = ""
    for w in story.split(' '):
        str += w[0].lower();

    return str

def fetch_word(link, p, l, w):
    p -= 1
    l -= 1
    w -= 1

    r = requests.get(BASE_URL + link)
    soup = BeautifulSoup(r.text, 'html.parser')

    # If there is a table of contents is a novel, otherwise its a short story
    # and in the novels, there is an extra paragraf
    if link == '/stories/html/stud.html' or link == '/stories/html/vall.html':
        p += 1


    if len(soup.find_all('p')) < p:
        return '[out of range]'
    paragraph = soup.find_all('p')[p].text

    if len(re.split('[.!?]', paragraph)) < l:
        return '[out of range]'
    line = re.split('[.!?]', paragraph)[l].strip()

    if len(line.split(' ')) < w:
        return '[out of range]'
    word = line.split(' ')[w]

    regex = re.compile('[^a-zA-Z]')

    return regex.sub('', word)


def find_word(story, par, line, word):
    found = False
    for story_name, link in data.items():
        if story.lower() == initials(story_name):
            print(story_name, '=>', fetch_word(link, par, line, word))
            found = True

    if not found:
        print('('+story+','+str(par)+','+str(line)+','+str(word)+') => NOT FOUND')

def find_words(words):
    for (story, par, line, word) in words:
        find_word(story, par, line, word)

find_words([('asis', 1,1,7)
           ,('tgs', 18,1,26)
           ,('acoi', 21,1,10)
           ,('tgs', 1,2,15)
           ,('tmwttl', 7,3,3)
           ,('taobp',3,6,13)
           ,('asis', 1,1,5)
           ,('tbvm', 6,2,4)
           ,('taotnb', 7,1,2)
           ,('asib', 1,1,1)
           ,('tmwttl',3,3,2)
           ,('trl', 61,6,12)
           ,('asib',5,1,3)
           ,('tmwttl', 1,4,15)
           ,('acoi',11,5,2)
           ,('tmwttl', 1,3,24)
           ,('tsotf', 2,1,13)
           ,('asis', 1,1,5)
           ,('tbvm', 1,2,2)
           ,('sb', 1,1,3)
           ,('acoi',1,1,14)
           ,('thotb', 17,2,24)
           ,('tmwttl', 13,6,9)
           ,('tmwttl',33,1,19)
           ,('asib',5,1,3)
           ,('acoi',1,3,10)
           ,('tgs',21,4,14)
           ])

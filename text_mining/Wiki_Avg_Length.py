from pattern.web import Wikipedia
from pattern.web import URL, extension
import string
import numpy as np
import matplotlib.pyplot as plt

'''
article = Wikipedia(language = 'fr').search('cat')
text = article.sections[0].content.split('\n')[0]
print text
'''

#url  = URL('http://translate.google.com/translate_tts?ie=UTF-8&tl=en&q=test')
f = open('OUTPUT.txt','w')
def Avg( s ):
    length = 0
    numb = 0
    article = Wikipedia().search(s)
    for i in xrange(len(article.sections)):
        if article.sections[i].title == "See also":
            break
        text = article.sections[i].content.replace('\n',' ')
        lengthtmp = 0
        numbtmp = 0
        for words in text.split(' '):
            length += len(words)
            lengthtmp += len(words)
            numb += 1
            numbtmp += 1
        #print article.sections[i].title + ' : ', float(lengthtmp)/float(numbtmp)

    return s , float(length)/float(numb)

ANIMALS = ['Cat', 'Dog', 'Duck', 'Rat', 'Ferret']
SCHOOLS = ['Olin College', 'MIT', 'Bunker Hill Community College', 'Harvard University', 'Princeton']
TESTS = ANIMALS + SCHOOLS
print TESTS
avg = []
for an in TESTS:
    tmp = Avg( an )
    avg.append(tmp[1])
    print tmp
print avg
Sep = np.arange(len(TESTS))
width = 0.1
fig, ax = plt.subplots()
rects = ax.bar(Sep, avg, width, color='r')
ax.set_xticks(Sep+width)
ax.set_xticklabels(TESTS)
def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                ha='center', va='bottom')

#autolabel(rects)

plt.show()

''' Compare collegs '''
#print Avg('Olin_College')
#print Avg('Bunker_hill_community_college')
#print Avg('Harvard_university')
#print Avg('MIT')

#print Avg('stephen hawking')
#print Avg('Einstein')
#print Avg('honey boo boo')

#print Avg('kanye west')
#print Avg('jesus')

#print Avg('Obama')
#print Avg('Putin')

#print Avg('llama')
#print Avg('poutine')

#print Avg('hollywood')
#print Avg('moon landing')

#print Avg('Kenya')
#print Avg('USA')
#print Avg('Mexico')

#print Avg('North')
#print Avg('South')

#print Avg('chicken')
#print Avg('egg')

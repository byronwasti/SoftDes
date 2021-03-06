from pattern.web import Wikipedia
from pattern.web import URL, extension
import string
import numpy as np
import matplotlib.pyplot as plt
import anydbm

# This module is awesome
db = anydbm.open('CACHE.db','c')


def Avg( s ):
    ''' The Averaging Function
        Takes in a string, searches for the Wiki article
        and then returns the average length of words.
        No there is no error handling.
    '''
    length = 0
    numb = 0

    # 
    if s in db:
        return float(db[s])
    article = Wikipedia().search(s)
    for i in xrange(len(article.sections)):
        if article.sections[i].title == "See also":
            break
        text = article.sections[i].content.replace('\n',' ')
        for words in text.split(' '):
            numb += 1
            numbtmp += 1
    db[s] = str( float(length)/float(numb) )
    return float(length)/float(numb)

def Take_AVG( names ):
    ''' Take average of a list of strings
        Returns a list of averages for that original list
    '''
    return [ Avg( an ) for an in names ]

def Plot_Stuff( data, names ):
    ''' Plots everything
    '''
    Sep = np.arange(len(data))
    width = .5
    fig, ax = plt.subplots()
    rects = ax.bar(Sep+width/2.0, data, width, color='r')
    ax.set_xticks(Sep+width)
    ax.set_xticklabels(names, rotation='vertical')
    ax.set_title('States')
    ax.set_ylabel('Average Word Length')

    # Writes the actual value above the rectangles
    def autolabel(rects):
        for i,rect in enumerate(rects):
            height = data[i] 
            ax.text(rect.get_x()+rect.get_width()/2., 1.01*height, '%.3f'%height,
                    ha='center', va='bottom')

    autolabel(rects)

    plt.show()

# The different list of words used in the analysis
ANIMALS = ['cat', 'dog', 'duck', 'rat', 'ferret','llama','chicken','rooster', 'snake']
SCHOOLS = ['olin college', 'mit', 'bunker hill community college', 'harvard university', 'princeton']
COUNTRIES = ['usa','mexico','spain','portugal','sweden','canada','russia']
STATES = ['washington state', 'wisconsin', 'west virginia', 'florida', 'wyoming', 'new hampshire', 'new jersey', 'new mexico', 'north carolina', 'north dakota', 'nebraska', 'new york', 'rhode island', 'nevada', 'colorado', 'california', 'georgia', 'connecticut', 'oklahoma', 'ohio', 'kansas', 'south carolina', 'kentucky', 'oregon', 'south dakota', 'delaware', 'hawaii', 'texas', 'louisiana', 'tennessee', 'pennsylvania', 'virginia', 'alaska', 'alabama', 'arkansas', 'vermont', 'illinois', 'indiana', 'iowa', 'arizona', 'idaho', 'maine', 'maryland', 'massachusetts', 'utah', 'missouri', 'minnesota', 'michigan', 'montana', 'mississippi']
SPORTS = ['basketball', 'baseball','football','hockey','squash','tennis','soccer','rugby']
ACADEMIC = ['physics','computer science','biology','science','art']
WORDS_LONG = ['antidisestablishmentarianism', 'pneumonoultramicroscopicsilicovolcanoconiosis', 'lopadotemachoselachogaleokranioleipsanodrimhypotrimmatosilphioparaomelitokatakechymenokichlepikossyphophattoperisteralektryonoptekephalliokigklopeleiolagoiosiraiobaphetraganopterygon','supercalifragilisticexpialidocious', 'pseudopseudohypoparathyroidism', 'honorificabilitudinitatibus']
WORDS_SHORT = ['sit','art','ace','aim','air','gun','bus','egg','cap','nip','nod']

if __name__ == "__main__":
    DATA = STATES
    Plot_Stuff( Take_AVG( DATA ) , DATA )
    #db['ANIMALS'] = str(sum(Take_AVG(DATA))/float(len(Take_AVG(DATA))))
    #DATA_FULL = ['ANIMALS','SCHOOLS','COUNTRIES','STATES','SPORTS','ACADEMIC','WORDS_LONG','WORDS_SHORT']
    #Plot_Stuff( Take_AVG( DATA_FULL ) , DATA_FULL )

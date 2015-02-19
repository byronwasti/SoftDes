def histogram(s):
    d = {}
    for i in s:
        if d.get(i,0) == 0:
            d[i] = 1
        else: d[i] += 1
    return d

#print histogram('asdfasdfgasdg')
            
def has_dupl(l):
    d = {}
    for i in l:
        if d.get(i,0) == 0:
            d[i] = 1
        else: return True

#print has_dupl([1,2,3,4,5,6,1])

def suffixer( w ):
    n = len(w)
    d = {}
    suf = {}
    pref = []
    f = open('/usr/share/dict/words','r')
    
    new = True
    current = 'A'
    d['A'] = []
    for word in f:
        word = word.strip('\n')
        if current in word:
            d[current] = d[current] + [word]
        elif len(word) > n-1:
            current = word
            d[current] = []
    return d[w]

print suffixer('test')

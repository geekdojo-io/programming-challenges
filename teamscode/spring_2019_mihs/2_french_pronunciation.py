def solve(s):
    ar = list(' ' + s + '  ')
    i = 1
    while i < len(ar) - 2:
        prev, cur, next = ar[i-1], ar[i], ar[i+1]
        if cur == ' ':
            i += 1
            continue
        if prev in ' .' and ''.join(ar[i:i+3]) == 'hh ': # two letter words with h
            i += 2
            continue
        elif prev in ' .' and cur == 'h':
            ar[i] = '.' # mark delete
        elif next in ' .' and cur not in 'clfr' : #  end of word
            ar[i] = '.' # mark delete
        i += 1            
    res = ''
    for i in range(1, len(ar)-2):
        if ar[i] != '.': # Construct string with items that are not marked as delete ('.')
            res += ar[i]
    return res

def test_simple():
    assert solve('Je me appelle Chris') == 'J m appell Chri'
    assert solve('Je espere que tu as du bon temps') == 'J esper qu t a d bo temp'
    assert solve('The question writers do not actually know French') == 'Th questio writer d no actuall kno Frenc'
    assert solve('But we try my best with the help of French Speakers') == 'Bu w tr m bes wit th el of Frenc Speaker'
    assert solve('Clfr rclf frcl lfrc hhhh') == 'Clfr rclf frcl lfrc hh'

if __name__ == '__main__':
    test_simple()

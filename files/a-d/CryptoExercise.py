code = """lrvmnir bpr sumvbwvr jx bpr lmiwv yjeryrkbi jx qmbm wi bpr xjvni mkd ymibrut jx irhx wi bpr riirkvr
jx ymbinlmtmipw utn qmumbr dj w ipmhh but bj rhnvwdmbr bpr yjeryrkbi jx bpr qmbm mvvjudwko bj yt wkbrusurbmbwjk
lmird jk xjubt trmui jx ibndt

wb wi kjb mk rmit bmiq bj rashmwk rmvp yjeryrkb mkd wbi iwokwxwvmkvr mkd ijyr ynib urymwk nkrashmwkrd bj
ower m vjyshrbr rashmkmbwjk jkr cjnhd prner bj lr fnmhwxwrd mkd wkiswurd bj invp mk rabrkb bpmb pr vjnhd
urmvp bpr ibmbr jx rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii ijnkd mkd ipmsrhrii ipmsr w dj kjb drry
ytirhx bpr xwkmh mnbpjuwbt lnb yt rasruwrkvr cwbp qmbm pmi hrxb kj djnlb bpmb bpr xjhhjcwko wi bpr sujsru
msshwvmbwjk mkd wkbrusurbmbwjk w jxxru yt bprjuwri wk bpr pjsr bpmb bpr riir-kvr jx jqwkmcmk qmurnbr cwhh
urymwk wkbmvb"""

#code = 'xultpaajcxitltlxaarpjhtiwtgxktghidhipxciwtvgtpilpitghlxiwiwtxggadds'
freq = {}
for letter in code:
    if letter not in {' ','\n','-'}:
        if letter not in freq:
            freq[letter] = 1
        else:
            freq[letter]+=1

letterFreq = list(freq.items())
letterFreq.sort(key = lambda x: x[1], reverse = True)

def attack(mess):
    decoder ={'r':'E','b':'T','p':'H','m':'A'}
    new = ''
    for c in mess:
        if c in decoder:
            new += decoder[c]
        
        else:
            new += c
    return new
#print(attack(code))

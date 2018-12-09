from collections import defaultdict
from collections import namedtuple
from collections import Counter

MetaData = namedtuple('MetaData', 'txt, chars, counts')

def getInputs(fileloc = 'test_input.txt'):
    '''
        rtype: list of MetaData
    '''
    inputs = []
    with open(fileloc, 'r') as f:
        for l in f.readlines():
            inputs.append(getmetadata(l.rstrip('\n')))

    inputs = sorted(inputs, key = lambda x : len(x.chars))
    return inputs

def findalmostsimilartext(inputs):
    for i in range(len(inputs)-1):
        j = 1
        while i+j < len(inputs) and len(inputs[i].chars - inputs[i+j].chars) < 2:
            # print('\n',inputs[i].txt,'\n',inputs[i+j].txt)

            diff = 0
            for idx in range(len(inputs[i].txt)):
                diff += [1,0][inputs[i].txt[idx] == inputs[i+j].txt[idx]]

            if diff == 1:
                print('\n', inputs[i], \
                '\n', inputs[i+j], \
                '\n', inputs[i].chars - inputs[i+j].chars, \
                '\n', inputs[i].counts - inputs[i+j].counts)
                print("hallelujah!!!!!")
                print(len(inputs[i].chars - inputs[i+j].chars) < 2)
                return [inputs[i].txt, inputs[i+j].txt]            
            j = j+1
    print('Done')
    return []

def getmetadata(txt):
    c = Counter(txt)
    return MetaData(txt, set(c), c)



if __name__ == '__main__':
    # assert findchecksumtxt('nkucgflathzwsicxrevtmbtpoq') ==(1,1), "Yo watch out."
    # print('Check sum is:', findchecksum('input.txt'))
    # findalmostsimilartext(getInputs('input.txt'))
    assert len(findalmostsimilartext([
        getmetadata('nkucgflathzwlijxrqvambdpoq'), \
        getmetadata('mkwcdflathzwsvjxrevymbdpoq'), \
        getmetadata('mkucdflathzwsvjxrevymbdpoq'), \
        ])) == 2, "Didn't run as expected."
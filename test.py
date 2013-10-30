#!/usr/bin/python
# FileName: test
import cPickle
class Persion():
    '''This class "Persion" have "name" "info"'''
    def __init__(self, pname):
        self.pname = pname
        self.pinfo = { }
    def __str__(self):
        print 'Name:', self.pname,
        for ikind, iinfo in self.pinfo.items():
            print ('%s: %s') % (ikind, iinfo)
        return '\n'



f = file('data', 'r')
dict = cPickle.load(f)
for name, info in dict.items():
    print name, '  ',info

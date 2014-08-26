#!/usr/bin/python
import sys
if len(sys.argv) == 3:
    a = sys.argv[1]
    b = sys.argv[2]
else:
    a = raw_input("replace string:\n> ")
    b = raw_input("replace %s with:\n> " % a)
a,b = [x.replace("/", "\/") for x in [a,b]]
if "\'" in a or "\'" in b:
    print 'sed "s/%s/%s/g"' % (a,b)
else:
    print "sed 's/%s/%s/g'" % (a,b)

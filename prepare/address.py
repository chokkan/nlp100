# -*- coding: utf-8 -*-
import sys
import csv

D = set()
for row in csv.reader(sys.stdin):
    s1 = unicode(''.join((row[6], row[7])))
    s2 = unicode(row[8])
    if s2 == u'以下に掲載がない場合':
        continue
    s2s = s2.split(u'、')
    for s in s2s:
        p = s.find(u'（')
        if p != -1:
            s = s[:p]
        D.add((s1, s))

for s1, s2 in D:
    print '\t'.join((s1, s2))

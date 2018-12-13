#!/usr/bin/env python

for l in xrange(1,400):
    for l1 in xrange(1,400):
        l2 = ((1000-l1)-l)
        if (l**2)+(l1**2) == (l2**2):
            print l*l1*l2
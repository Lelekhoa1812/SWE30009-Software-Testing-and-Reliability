import pytest
import numpy as np
import copy
from mutants import m1,m2,m3
from sut import p

# test cases
tc1 = [3, 5, 4]
tc2 = [0, 10, 3]
tc3 = [2, 2]
tc4 = [1, 2, 3]
testcases = [tc1,tc2,tc3,tc4]

# number to be added in follow-up test cases
followup = [1,0,3,4]

# original program (oracle)
p = p.compute_sum  # a1+a2+...+an 

# mutants
m1 = m1.compute_sum # a1*a2*...*an
m2 = m2.compute_sum # a2+a3+...+an
m3 = m3.compute_sum # 3+a1+...+an
mutants = [m1, m2, m3]
labels = ['m1','m2','m3']


# ............. TESTING WITH CONVENTIONAL TESTING .............


# testing with conventional testing with test oracle
def test_withoracle():
    for mutant,label in zip(mutants,labels):
        for testcase in testcases:
            oracle = p(testcase)
            actual = mutant(testcase)
            if actual==oracle:
                result = '-'
            else:
                result = 'killed'
            print('Testing {} with test case {}: {} ({} vs {})'.format(label,testcase,result,oracle,actual))


# ............. TESTING WITH MT .............


# testing with MT using MR1
def test_withmt():
    for mutant,label in zip(mutants,labels):
        for testcase,fvalue in zip(testcases,followup):
            si = testcase
            fi = copy.copy(testcase)
            fi.append(fvalue)
            so = mutant(si)+fvalue
            fo = mutant(fi)
            if so==fo:
                result = '-'
            else:
                result = 'killed'
            print('Testing {} with test case {} using {}: {} ({} vs {})'.format(label,testcase,fvalue,result,so,fo))


# test with conventional method
# test_withoracle()

# test with MT
test_withmt()

## * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
##* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
##=======================================================================
##Copyright (C) 2018-2019 Leonardo BAUTISTA GOMEZ
##This program is free software; you can redistribute it and/or modify
##it under the terms of the GNU General Public License (GPL) as published
##of the License, or (at your option) any later version.
##
##This program is distributed in the hope that it will be useful,
##but WITHOUT ANY WARRANTY; without even the implied warranty of
##MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##GNU General Public License for more details.
##
##To read the license please visit http://www.gnu.org/copyleft/gpl.html
##=======================================================================
##
## File          : swarmSec.py
## Created on    : 19 Feb 2018
## Author        : Leonardo BAUTISTA Gomez <leobago@gmail.com>
##
## Last modified : 19 Feb 2018 (12:59:44 PM)
## Author        : Leonardo BAUTISTA Gomez <leobago@gmail.com>
## Description   : .
##
#!/bin/python

import numpy as np
import scipy.stats as sp

def getProbabilityLostBlob(CRS):
    probLostBlob = [0.0]
    for p in range(1,9):
        Pp = sp.binom.pmf(CRS["k"]+1, CRS["n"], p/100.0)
        probLostBlob.append(Pp)
    return probLostBlob

def getProbabilityFileLost(probLostBlob, fileSize, CRS):
    nbBlobs = fileSize / (CRS["m"]*CRS["cs"])
    probFileLost = []
    for p in probLostBlob:
        probNoErasure = pow(1.0-p, nbBlobs)
        probErasure = 1.0 - probNoErasure
        probFileLost.append(probErasure)
    return probFileLost

def swarmSecurityAnalysis(CRS):
    print "CRS configuration : " + str(CRS) + "\n"
    probLostBlob = getProbabilityLostBlob(CRS)
    print "Probability of having one blob lost for different block loses(%):\n"
    for p in range(len(probLostBlob)):
        print "%01.7f," % p,
    print ""
    for p in probLostBlob:
        print "%01.7f," % p,
    print "\n"
    print "Probability of having a file lost for different file sizes(GB) and block loses(%):\n"
    for p in range(len(probLostBlob)):
        print "%01.7f," % p,
    print ""
    for fs in (1, 5, 10, 50):
        fileSize = fs * 1000000000
        probLostFile = getProbabilityFileLost(probLostBlob, fileSize, CRS)
        for p in probLostFile:
            print "%01.7f," % p,
        print "|"+str(fileSize/1000000000)+"GB"



CRS = {"n" : 128, "m" : 112, "k" : 16, "cs" : 4096}
swarmSecurityAnalysis(CRS)
print "\n=============================================\n"
CRS = {"n" : 128, "m" : 96, "k" : 32, "cs" : 4096}
swarmSecurityAnalysis(CRS)




"""
-*-Pyth-*-
###################################################################
 PFM - Python-based phase field solver

 FILE: "equation.py"
                                   created: 11/10/03 {2:45:34 PM} 
                               last update: 12/10/03 {11:16:37 AM} 
 Author: Jonathan Guyer
 E-mail: guyer@nist.gov
 Author: Daniel Wheeler
 E-mail: daniel.wheeler@nist.gov
   mail: NIST
    www: http://ctcms.nist.gov
 
========================================================================
This software was developed at the National Institute of Standards
and Technology by employees of the Federal Government in the course
of their official duties.  Pursuant to title 17 Section 105 of the
United States Code this software is not subject to copyright
protection and is in the public domain.  PFM is an experimental
system.  NIST assumes no responsibility whatsoever for its use by
other parties, and makes no guarantees, expressed or implied, about
its quality, reliability, or any other characteristic.  We would
appreciate acknowledgement if the software is used.

This software can be redistributed and/or modified freely
provided that any derivative works bear some notice that they are
derived from it, and any modified versions bear some notice that
they have been modified.
========================================================================
 
 Description: 

 History

 modified   by  rev reason
 ---------- --- --- -----------
 2003-11-10 JEG 1.0 original
###################################################################
"""

class Equation:
    def __init__(
        self,
        var,
        terms,
        solver,
	solutionTolerance = 1e-4):

	self.var = var
        self.terms = terms
	self.solver = solver
	
	self.solutionTolerance = solutionTolerance
	self.converged = 1

    def getVar(self):
        return self.var 

    def updateVar(self):
	pass
	
    def preSolve(self):
	pass
	
    def postSolve(self):
	pass
	
    def solve(self,dt):
	pass
    
    def isConverged(self):
	return self.converged

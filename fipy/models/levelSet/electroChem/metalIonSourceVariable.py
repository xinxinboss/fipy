#!/usr/bin/env python

## -*-Pyth-*-
 # ###################################################################
 #  FiPy - Python-based finite volume PDE solver
 # 
 #  FILE: "metalIonSourceVariable.py"
 #                                    created: 8/18/04 {10:39:23 AM} 
 #                                last update: 8/18/04 {4:00:40 PM} 
 #  Author: Jonathan Guyer
 #  E-mail: guyer@nist.gov
 #  Author: Daniel Wheeler
 #  E-mail: daniel.wheeler@nist.gov
 #    mail: NIST
 #     www: http://ctcms.nist.gov
 #  
 # ========================================================================
 # This software was developed at the National Institute of Standards
 # and Technology by employees of the Federal Government in the course
 # of their official duties.  Pursuant to title 17 Section 105 of the
 # United States Code this software is not subject to copyright
 # protection and is in the public domain.  PFM is an experimental
 # system.  NIST assumes no responsibility whatsoever for its use by
 # other parties, and makes no guarantees, expressed or implied, about
 # its quality, reliability, or any other characteristic.  We would
 # appreciate acknowledgement if the software is used.
 # 
 # This software can be redistributed and/or modified freely
 # provided that any derivative works bear some notice that they are
 # derived from it, and any modified versions bear some notice that
 # they have been modified.
 # ========================================================================
 #  
 #  Description: 
 # 
 #  History
 # 
 #  modified   by  rev reason
 #  ---------- --- --- -----------
 #  2003-11-12 JEG 1.0 original
 # ###################################################################
 ##

"""

The `MetalIonSourceVariable` object evaluates the source coefficient
for the `MetalIonEquation`. The source only exists on the cells in
front of the interface and simulates the loss of material from bulk
diffusion as the interface advances. The source is given by,

.. raw:: latex

    $$ D \\hat{n} \\cdot \\nabla c = \\frac{v(c)}{\\Omega} \;\; \\text{at} \;\; \\phi = 0$$ 

Here is a test,

   >>> from fipy.meshes.grid2D import Grid2D
   >>> mesh = Grid2D(dx = 1, dy = 1, nx = 2, ny = 2)
   >>> from fipy.models.levelSet.distanceFunction.distanceVariable import DistanceVariable
   >>> distance = DistanceVariable(mesh = mesh, value = (-.5, .5, .5, 1.5))
   >>> ionVar = CellVariable(mesh = mesh, value = (1, 1, 1, 1))
   >>> arr = Numeric.array(MetalIonSourceVariable(ionVar, distance, (1, 1, 1, 1), 1))
   >>> sqrt = Numeric.sqrt(2)
   >>> Numeric.allclose(arr, (0, 1 / sqrt, 1 / sqrt, 0))
   1

"""

__docformat__ = 'restructuredtext'

import Numeric

from fipy.variables.cellVariable import CellVariable

class MetalIonSourceVariable(CellVariable):

    def __init__(self, ionVar = None, distanceVariable = None, depositionRate = None, metalIonAtomicVolume = None):
        """

        The following arguments are required to instatiate a
        `MetalIonSourceVariable`,

        `ionVar` - A `CellVariable`.

        `distanceVariable` - A `DistanceVariable` object.

        `depositionRate` - Either a `CellVariable` or a float.

        `metalIonAtomicVolume` - Atomic volume of the metal ions.
       
        """
        
        CellVariable.__init__(self, distanceVariable.getMesh(), hasOld = 0)
        self.ionVar = self.requires(ionVar)
        self.distanceVariable = self.requires(distanceVariable)
        self.depositionRate = self.requires(depositionRate)
        self.metalIonAtomicVolume = metalIonAtomicVolume
        
    def _calcValue(self):
        ionVar = Numeric.where(self.ionVar > 1e-20, self.ionVar, 1e-20)
        self.value = Numeric.array(self.depositionRate) * self.distanceVariable.getCellInterfaceAreas() / (self.mesh .getCellVolumes() * self.metalIonAtomicVolume) / ionVar
        
def _test(): 
    import doctest
    return doctest.testmod()
    
if __name__ == "__main__": 
    _test() 

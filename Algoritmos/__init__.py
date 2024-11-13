# Algoritmos/__init__.py
import StrassenNaiv
import WinogradOriginal
import IV3SequentialBlock
import NaivLoopUnrollingFour
import NaivLoopUnrollingTwo
import NaivOnArrays
import StrassenWinograd
import V3SequentialBloc
import V4ParallelBlock
import WinogradScaled

"""
__all__ = ["StrassenNaiv","WinogradOriginal","IV3SequentialBlock",
           "NaivLoopUnrollingFour", "NaivLoopUnrollingTwo","NaivOnArrays","StrassenWinograd",
           "V3SequentialBloc", "V4ParallelBlock", "WinogradScaled"]
"""

from .StrassenNaiv import StrassenNaiv
from .WinogradOriginal import WinogradOriginal
from .IV3SequentialBlock import IV3SequentialBlock
from .NaivLoopUnrollingFour import NaivLoopUnrollingFour
from .NaivLoopUnrollingTwo import NaivLoopUnrollingTwo
from .NaivOnArrays import NaivOnArray
from .StrassenWinograd import StrassenWinograd
from .V3SequentialBloc import v3SequentialBlock
from .V4ParallelBlock import v4ParallelBlock
from .WinogradScaled import WinogradScaled

from .IMatrixMultiplication import IMatrixMultiplication

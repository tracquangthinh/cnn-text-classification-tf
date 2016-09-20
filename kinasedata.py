import numpy as np
import pandas as pd
import collections
from vector import ELMVector

class KinaseData:
  def __init__(self, vectorFile="elmvector", pathELM="", window=3, sizeVector=300,
    kinase="PKA_group", biggerNegative=3, newVector=True, windowSplit=1,
    nAround=3, filePos="kinase.pos", fileNeg="kinase.neg"):
    self.file = vectorFile
    self.window = window
    self.sizeVector = sizeVector
    self.pathELM = pathELM
    self.kinase = kinase
    self.biggerNegative = biggerNegative
    self.newVector = newVector
    self.windowSplit = windowSplit
    self.nAround = nAround
    self.filePos = filePos
    self.fileNeg = fileNeg
    
  def csvToArray(self):
    if self.newVector == True:
      elmVector = ELMVector(pathELM=self.pathELM, windowWordToVec=self.window,
        sizeVector=self.sizeVector, windowSplit=self.windowSplit,
        nAround=self.nAround, biggerNegative=3,
        filePos=self.filePos, fileNeg=self.fileNeg)

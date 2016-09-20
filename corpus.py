from random import randint
class ELMCorpus:
  def __init__(self, path):
    self.path = path

  def splitNotSignAll(self, sentences, index, windownSplit, nAround=10):
    windownSplit = int(windownSplit)
    length_word = windownSplit * nAround
    index = index - 1

    if index >= length_word:
      leftStr =  sentences[index - length_word:index]
    else:
      leftStr = sentences[0:index]

    namePhospho = sentences[index]

    leftResult = [leftStr[i:i+windownSplit] for i in range(len(leftStr) % windownSplit, len(leftStr), windownSplit)]
    leftRest = leftStr[0:len(leftStr) % windownSplit]
    rightStr = sentences[index + 1 : index + length_word +1]
    rightResult = [rightStr[i:i+windownSplit] for i in range(0, len(rightStr), windownSplit)]

    if len(leftResult) == 0:
      leftResultStr = ""
    else:
      leftResultStr = (" ".join(leftResult)) + " "
    if len(rightResult) == 0:
      rightResultStr = ""
    else:
      rightResultStr = " " + (" ".join(rightResult))

    resultSentence = leftRest + " " + leftResultStr + namePhospho + rightResultStr
    
    return resultSentence.strip(" ").strip("\n")
	
  def toCorpus(self, output, window, kinase, biggerNegative=3,
    filePos="kinase.pos", fileNeg="kinase.neg"):
    f = open(output, "w")
    results = self.toArray(window=window, kinase=kinase,
      biggerNegative=biggerNegative, filePos=filePos, fileNeg=fileNeg)
    for result in results:
      f.write(result + "\n")
    f.close()

  def toArray(self, window, kinase="PKA_group", nAround=10, biggerNegative=3,
    filePos="kinase.pos", fileNeg="kinase.neg"):
    result = []
    nPositive = 0
    filePositive = open(filePos, "w")
    negative = []
    with open(self.path) as ELM:
      for line in ELM:
        if len(line) > 1:
          objLine = line.split("|")
          index = int(objLine[0].split("_")[-1])
          sentence = objLine[2].strip(" ").strip("\n")
          sentence = self.splitNotSignAll(sentences=sentence, index=index,
            windownSplit=window, nAround=nAround)
          result.append(sentence)
          
          if kinase in objLine[1]:
            nPositive += 1
            filePositive.write(sentence + "\n")
          else:
            negative.append(sentence)
          
    filePositive.close()
    fileNegative = open(fileNeg, "w")
    i = 0
    indexArr = []
    while i < biggerNegative * nPositive:
      tmpIndex = randint(0, len(negative) - 1)
      if tmpIndex not in indexArr:
        indexArr.append(tmpIndex)
        fileNegative.write(negative[i] + "\n")
        i += 1
        print("%d samples in negative", i)
    fileNegative.close()
    return result

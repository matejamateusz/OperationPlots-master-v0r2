__author__ = 'mmateja'

from LoadLPC import LoadLPC
from LoadCondition import LoadCondition
class LoadFiles():

    def __init__(self, name, fillNumbers, basic_path, nameFileEnd):
         self.basic_path = basic_path
         self.nameFileEnd = nameFileEnd

         # Select which file decoder
         if 'LPC' in name:
            self.files=LoadLPC(fillNumbers, self.basic_path, self.nameFileEnd)
            self.files.load()
         elif 'Condition' in name:
            self.files=LoadCondition(fillNumbers, self.basic_path, self.nameFileEnd)
            self.files.load()
         else:
             raise IOError("WRONG PATH")

    def getLoadedFiles(self):
        return  self.files

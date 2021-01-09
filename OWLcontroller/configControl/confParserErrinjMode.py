from configparser import ConfigParser
from configControl.confFile import * # TODO: need ot change this to regualr import because we want to use the name of the class and than the name of the operation , for example : controlPC.function , that way we can see it very natural the functiom and who does them
from collections import namedtuple
from collections import OrderedDict
from pathlib import Path
import json
import os

# Errinj Mode
ERRINJ_CONFIG_FILE_SUFFIX = ".cts"
TEST_PARAM = "="
# DEFAULT_CONF_FILE = '..\defaultConfiguration.json' When running directly from this file
DEFAULT_CONF_FILE = 'defaultConfiguration.json' #when running from the controlPc


def cleanUpErrinjModeConfFile(line):
    return line.rstrip("\n").replace(";", "").replace('"', "").strip().split("=")

def convertToString(line):
    return str(line)

def getFilePath(legacyModeConfigFilesDirectory, filename):
    return os.path.join(legacyModeConfigFilesDirectory, filename)

def getRootDirectory(relativePath):
    return r'..\\' + relativePath


def findFile(fileNameFromUser ="../"):
    path = "../" + fileNameFromUser
    return path if os.path.isfile(path) else ''

# def searchFromRoot(dirNameFromUser):
#     start = "../"
#     for dirpath, dirnames, filenames in os.walk(start):
#         for filename in filenames:
#             if filename == dirNameFromUser:
#                 filename = os.path.join(dirpath, filename)
#                 # print(filename)
#                 # print(dirpath)
#                 # print(dirnames)
#                 #print(dirpath)
#                 return filename


def findDir(dirNameFromUser):
    path = "../" + dirNameFromUser
    return path if os.path.isdir(path) else ''



# Parser
class confParserErrinjMode():
    def __init__(self):

        # Legacy Mode configs paths
        defaultConfContent = self.parseDefaultConf()
        # Errinj mode configs paths
        self.errinjConfFilesPath = findDir(defaultConfContent['errinjModePath'])
        self.errinjConfFile = ConfigParser()
        self.errinjConfFile.read(self.errinjConfFilesPath)

        # Errinj Mode

    def getFilesNames(self, path):
        return os.listdir(path)

    def addParamAndValueToErrinjConfFile(self, testConf, Param, ParamValue):
        setattr(testConf, Param, ParamValue)
        return testConf

    def storeTestConfurationIntoDicts(self, testConf, testsByGroupErrinj, ):
        if testConf.testgroup not in testsByGroupErrinj:
            testsByGroupErrinj[testConf.testgroup] = []
        else:
            testsByGroupErrinj[testConf.testgroup].append(testConf)
        return (testsByGroupErrinj)

    def parseErrinjConfFiles(self):
        ''' Returns namedTuple which contains testsByGroupErrinj and testStatusErrinj '''
        testsByGroupErrinj = OrderedDict()
        #testStatusErrinj = OrderedDict()
        parsingResults = namedtuple('parsingResult', ['testsByGroupErrinj'])
        allConfFilesPaths = Path(self.errinjConfFilesPath).rglob('*.cts')
        for pathOFConfigFile in allConfFilesPaths:
            confFilePAth = convertToString(pathOFConfigFile)  # because pathOFConfigFile is object not string
            with open(confFilePAth) as config:
                testConf = testConfErrinj()
                for line in config.readlines():
                    if TEST_PARAM in line:
                        paramName, paramValue = cleanUpErrinjModeConfFile(line)
                        testConf = self.addParamAndValueToErrinjConfFile(testConf, paramName,
                                                                                  paramValue)
            testsByGroupErrinj = self.storeTestConfurationIntoDicts(testConf, testsByGroupErrinj)
        return parsingResults(testsByGroupErrinj)  # return the namedTuple contains both results dicts


    def parseDefaultConf(self, defaultConfig='..\defaultConfiguration.json'):
        # Opening JSON file

        defaultConf = open(DEFAULT_CONF_FILE, encoding="utf8")
        defaultConfContent = json.load(defaultConf)
        defaultConf.close()
        return defaultConfContent

if __name__ == '__main__':

    # Tester for parsing errinj config
    print ('dirnames')
    dirnames = confParserErrinjMode().parseErrinjConfFiles()
    for item in dirnames.testsByGroupErrinj.values():
        print(item)



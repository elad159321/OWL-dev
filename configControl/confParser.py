from configControl.confParserErrinjMode import confParserErrinjMode
from configControl.confParserLM import confParserLM
from collections import namedtuple

# Parser



class confParser():
    def __init__(self):
        pass

    def parseAll(self):
        parseResults = namedtuple('parsingResult', ['legacyMode', 'ErrinjMode'])
        lMparsingResults = confParserLM().parseLMConf() # Parsing the legacy mode config files (Flow operations and trainer scripts)
        errinjModeParsingResults = confParserErrinjMode().parseErrinjConfFiles() # Parsing the Errinj Mode config files
        return parseResults(lMparsingResults, errinjModeParsingResults)


if __name__ == '__main__':
    # # Tester for all the parsing being done
    controlPc = (confParser().parseAll())
    print(controlPc.legacyMode.legacyTestsByGroup)
    print(controlPc.legacyMode.legacyFlowOperationsTestsByGroups)
    print(controlPc.ErrinjMode.testsByGroupErrinj)
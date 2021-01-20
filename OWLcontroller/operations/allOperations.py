from operations.operation import operation
from operations.operationsTypes.powerOnWithClicker import powerOnWithClicker
from operations.operationsTypes.runDm import runDM
from operations.operationsTypes.turnOnWithLan import turnOnWithLan
from operations.operationsTypes.wait import wait
from operations.operationsTypes.hibernate import hibernate
from operations.operationsTypes.sleep import sleep
from operations.operationsTypes.shutdown import shutdown
from operations.operationsTypes.runCommandViaCmd import runCommandViaCmd


class allOperations():
    operationsImplement = {str : operation}
    operationsImplement['runCommandViaCmd'] = runCommandViaCmd
    operationsImplement['shutdown'] = shutdown
    operationsImplement['sleep'] = sleep
    operationsImplement['hibernate'] = hibernate
    operationsImplement['wait'] = wait
    operationsImplement['powerOnWithClicker'] = powerOnWithClicker
    operationsImplement['turnOnWithLan'] = turnOnWithLan
    # operationsImplement['runDM'] = runDM

#
# print (allOperations.operationsImplement)
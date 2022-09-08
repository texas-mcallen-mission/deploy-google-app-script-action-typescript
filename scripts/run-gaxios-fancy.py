import subprocess

# custom exception type
class killAction(Exception):
    pass

# the thing that runs clasp pushing
result = subprocess.run(["clasp","push","-f"],stdout=subprocess.PIPE)

# wrote this as a function so that I could write tests for it
def wasSuccessful(data):
    
    returnVal = True

    gaxios = "GaxiosError:"
    pushFailure = "Push failed. Errors:"

    gaxiosFail = (gaxios in data) # true if GaxiosError: is in the log
    pushFail = (pushFailure in data) # true if Push Failure is in the log
    # print(gaxiosFail,pushFail)
    if gaxiosFail or pushFail:
        returnVal = False
    return returnVal


claspRun = wasSuccessful(result.stdout)

if claspRun == False:
    print("throwing an error")
    raise killAction("Clasp had an internal error!")
    # and then throw an error.
else:
    print(result.stdout)
    print("Push succeeded.")

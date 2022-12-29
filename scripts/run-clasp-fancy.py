import subprocess

#  The new-and-improved CLASP runner!
#   This bad boi checks the output of CLASP and makes sure that it doesn't throw an error.
#   Previously, if clasp didn't succeed, it'd just continue on without any indication of problems.
#   Now, it'll throw an error and spit out the logs if it breaks.  *WAY* better.  :)
#
print("JUMPSTRING 4")
# custom exception type
class killAction(Exception):
    pass

# the thing that runs clasp pushing itself
result = subprocess.run(["clasp","push","-f"],stdout=subprocess.PIPE)

# the rest of this parses the output from CLASP.

# wrote this as a function so that I could write tests for it
def wasSuccessful(data):
    
    returnVal = True

    gaxios = "GaxiosError:"
    pushFailure = "Push failed. Errors:"
    gaxiosFail = (gaxios in data) # true if GaxiosError: is in the log
    pushFail = (pushFailure in data) # true if Push Failure is in the log
    if gaxiosFail or pushFail:
        returnVal = False
    return returnVal

encoding = 'utf-8'
parsedResult = str(result.stdout,encoding)
claspRun = wasSuccessful(parsedResult)

# *might* add some extra parsing here to make the result easier to read?

print(parsedResult)
if claspRun == False:
    # and then throw an error.
    raise killAction("""
    Clasp had an internal error!""")
else:
    print("""
    Push succeeded.""")


print(""" THIS IS A TEST OF THE EMERGENCY BREAKDANCE SYSTEM""")
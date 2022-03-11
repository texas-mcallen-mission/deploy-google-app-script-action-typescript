import sys

nameOfScript = sys.argv[0]
commandLineArgs = sys.argv[1]
commandLineArgsAsStr = str(sys.argv)

argumentString = str(commandLineArgs).replace('\\n', '\n').replace('\\t', '\t')

numArgs = len(sys.argv)

print(nameOfScript)
print("")
print(commandLineArgs)
# print(commandLineArgsAsStr)
# print(numArgs)

print("Hello, CLI!")

file_in = open("git-info.js","rt")

file_out = open("git-info-modified.js","wt")

# configString = '''
#     reportCreator: {
#         docIDs: {

#             zoneTemplate: "ZONE_TEMPLATE_ID",
#             distTemplate: "DISTRICT_TEMPLATE_ID",
#             areaTemplate: "AREA_TEMPLATE_ID",
#         },
#         outputDataSheetName: "Data",
#         configPageSheetName: "config",
#         kicDataStoreSheetName: "Data",
#     }
# '''

for line in file_in:
    # print(line)
    line_out = line.replace('PYTHON_STICKS_CONFIG_DATA_HERE', argumentString)
    # print(line_out)
    file_out.write(line_out)

file_in.close()
file_out.close()
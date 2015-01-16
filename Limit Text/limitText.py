inputString = "Two thousand verses is a great many - very, very great many."
outputString = ""
if len(inputString) > 55:
    outputString = inputString[0:40]
    if outputString[39] is " ":
        outputString = outputString[:-1]

    outputString = outputString + "... <Read More>"
else:
    outputString = inputString

print(outputString)

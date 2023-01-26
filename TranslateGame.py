from googletrans import Translator
import time

translator = Translator()

sourceFile = open('Scenario.txt','r+', encoding="utf8")
outputFile = open('Scenario2.txt', 'a', encoding="utf8")


for line in sourceFile:
        
        if '"' in line:
            
            outputFile.writelines(
            line[:line.find('"')] + translator.translate(
            line[line.find('"'):line.rfind('"')+1],
            dest='uk', src='auto').text)

            print(line[:line.find('"')] + translator.translate(
            line[line.find('"'):line.rfind('"')+1],
            dest='uk', src='auto').text)

            sourceFile.writelines("")
        else:
            print(line)
            outputFile.writelines(line)

            sourceFile.writelines("")

outputFile.close()
sourceFile.close()
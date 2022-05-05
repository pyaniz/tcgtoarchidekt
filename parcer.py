import csv 
import json
from pickle import TRUE
import requests
import argparse

parser = argparse.ArgumentParser(description='Transform your TCG scanner output into an Archidekt compatible format')

parser.add_argument("-f", "--filename", help="CSV from TCGapp", default="TCGplayer.csv")
parser.add_argument("-w", "--write", help="Name of the file ro write", default="archidekt.csv")
parser.add_argument("-l", "--logs", help="Turn on log of cards scanned", action="store_true")

args = parser.parse_args()

filefrom = args.filename

ffilename = args.write
effilename = 'error_'+ffilename

debugflag = args.logs
print(debugflag)

BASE_URL = "https://api.scryfall.com/cards"

def getcard(tcgid):
    try:

        response = requests.get(BASE_URL+"/tcgplayer/"+str(tcgid))
        jsoncard = json.loads(response.content)
        return jsoncard["id"]
    except KeyboardInterrupt:
        raise
    except:
        return 'error'


def parser(csvFilePath,tfilename):
    try:
        jsonArray = []
    #   csv
        fields = ['Quantity', 'Name', 'Scryfall ID']
        rows = []
        
        ercount = 0
        lcount = 0
        errows = []
        #read csv file
        print("Processing, please wait...")
        with open(csvFilePath, encoding='utf-8') as csvf: 
            #load csv file data using csv library's dictionary reader
            csvReader = csv.DictReader(csvf) 

            #convert each csv row into python dict
            for row in csvReader: 
                #add this python dict to json array
                jsonArray.append(row)
            for item in jsonArray:
                for line in item:
                    if line == 'Product ID':
                        getcardcall = getcard(item["Product ID"])
                        if getcardcall == 'error':
                            ex = item["Quantity"], item["Name"], item["Simple Name"], item["Set"]
                            errows.append(ex)
                            ercount = ercount+1
                            if debugflag is True: 
                                print("Error: " + item["Name"])
                        else:
                            lcount = lcount+1
                            nline = item["Quantity"], item["Simple Name"], getcardcall
                            if debugflag is True:
                                print(nline)
                            rows.append(nline)
            # writing to csv file 
            with open(ffilename, 'w') as csvfile: 
                # creating a csv writer object 
                csvwriter = csv.writer(csvfile) 
                    
                # writing the fields 
                csvwriter.writerow(fields) 
                    
                # writing the data rows 
                csvwriter.writerows(rows)
            if ercount > 1:
                with open(effilename, 'w') as ercsvfile: 
                    # creating a csv writer object 
                    ercsvwriter = csv.writer(ercsvfile) 
                        
                    # writing the data rows 
                    ercsvwriter.writerows(errows)

        #csvFilePath = r'TCGplayer-capenna.csv'
        #filename = "vergahermanos.csv"
                message = str(lcount) + " lines succesfully processed and written to " + ffilename + " " + \
                    str(ercount) + " lines could not be processed, check " + effilename
            
                return message
    except:
        return "Canceled by user"

        
            


if __name__ == '__main__':
    print(parser(filefrom,ffilename))
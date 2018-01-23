'''
This script takes a huge text file generated from the same PDF file, finds a few fields and produces a csv file for import into Excel. I put comments throughout in response to client concern about a need for future changes
'''


# every line with a # is ignored by the computer

import csv
import re
# IMPORT the functions (mini programs)re and csv
textfile = raw_input("Input File ").strip()
inputfile = open(textfile,"r")

n=0 #counter for page counts at end of script


outputfile = open("output.txt","w")
output = csv.writer(outputfile)
for line in inputfile: #remove multiple spaces in a line
    while line != line.replace("  "," "):
          line = line.replace("  "," ")
    line = line.strip()
#look for various fields
    if "Vendor ID" in line:
        found = re.search('Vendor ID: \d+',line) #\d+ is a 'regular expression' Google if necessary 
        VendorID = found.group()[10:]
        #print VendorID #used print lines to help debug script
        continue
    if "To: " in line:
        To = line[4:].strip()
        #print To
        continue
    if "Royalty ID:" in line:
        found = re.search('Royalty ID: .+ProdCode',line)
        RoyaltyID = found.group()[11:-8].strip()
        #print RoyaltyID
    if "ProdCode:" in line:
        found = re.search('ProdCode: .+Title',line)
        ProdCodeID = found.group()[10:-5]
        #print ProdCodeID

    if "Title:" in line:
        found = re.search('Title: .+Author',line)
        Title = found.group()[7:-6].strip()
        #print Title
    

    if  "Author: " in line:
        found = re.search('Author: .+',line)
        Author = found.group()[8:].strip()
        #print Author
        
    if "Balance as of" in line:
        #found = re.search('Balance as of 12/31/91: +\(*[0-9]{1,3}(,[0-9]{3})*\.[0-9]+\)*',line)
        try: Balance = line[24:]
        except: Balance = "ERROR"
        #print "Balance", Balance
    if "Total Earned:" in line:
        #found = re.search('Total Earned: +\(*[0-9]{1,3}(,[0-9]{3})*\.[0-9]+\)*',line)
        try: Earned = line[14:]
        except: Earned = "ERROR"
        #print "T Earned", Earned
    if "Net Earned:" in line:
        #found = re.search('Net Earned: +\(*[0-9]{1,3}(,[0-9]{3})*\.[0-9]+\)*',line)
        try: Earned = line[12:]
        except: Earned = "ERROR"
        #print "N Earned", Earned
    if "Total Payments:" in line:
        #found = re.search('Total Payments: +\(*[0-9]{1,3}(,[0-9]{3})*\.[0-9]+\)*',line)
        try: Payments = line[16:]
        except: Payments = "ERROR"
        #print "Payments", Payments
    if "Amount Due:" in line:
        #found = re.search('Amount Due: +\(*[0-9]{1,3}(,[0-9]{3})*\.[0-9]+\)*',line)
        try: AmountDue = line[12:]
        except: AmountDue = "ERROR"
        #print "AmountDue", AmountDue
    if "Reserve Against Returns" in line:
        #found = re.search('Reserve Against Returns: *\(*[0-9]{1,3}(,[0-9]{3})*\.[0-9]+\)*',line)
        try: Reserve = line[24:].strip()
        except: Reserve = "ERROR"
        #print "Reserve", Reserve
    if "Totals" in line:
        #found = re.search('Totals +\(*[0-9]{1,3}(,[0-9]{3})*\.[0-9]+\)*',line)
        try: Totals = line[7:]
        except: Totals = "ERROR"
        #print "Totals", Totals
    if "Payment Due:" in line:
        #found = re.match('Payment Due: +\(*[0-9]{1,3}(,[0-9]{3})*\.[0-9]+\)*',line)
        #PaymentDue = line[14:]
        try: PaymentDue = line[13:].strip()
        except: PaymentDue = "ERROR"
        #print "PaymentDue", PaymentDue
        output.writerow([RoyaltyID,ProdCodeID,Title,Author,To,VendorID,Totals,Balance,Earned,Payments,AmountDue,Reserve,PaymentDue])
        n=n+1
        print "Row ", n, "done"
inputfile.close()
outputfile.close()
print "Done"    



from django.shortcuts import render
import csv
import json

def make_json(csvFilePath, jsonFilePath):
 # create a dictionary
 data = {}
 # Open a csv reader called DictReader
 with open(csvFilePath, encoding='utf-8') as csvf:
  csvReader = csv.DictReader(csvf) 
  for rows in csvReader:
   # Addes SN as a primary key
   key = rows['SN']
   data[key] = rows
   # Open a json writer, and use the json.dumps()
   with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
    jsonf.write(json.dumps(data, indent=4))      

csvFilePath = r"./static/NIFTY_F1_Xm8mAtb.csv"
jsonFilePath = r'./static/NIFTY_F1_Xm8mAtb.json'
  




# function to build JSON
def BuildJson(request):
 # Call the make_json function
 make_json(csvFilePath, jsonFilePath)
 pass
  


 
 
def Data(request):
 data={}
 with open("./static/NIFTY_F1_Xm8mAtb.csv", 'r') as file:
  csvreader = csv.reader(file, delimiter=':')
  for row in csvreader:
    print(row)
 return render(request,"index.html")
import xmltodict   # xml code to dict
import json        # used for dump() which takes dict and makes json output
import os          # operating system functionality 
import errno       # error check
import shutil      # used for deleting directories
 

def make_sure_path_exists(path):                                        # function makes sure we have folder avaiable for putting output files in
    try:
        os.makedirs(path)                                                   # makes a folder with name output if the folder does not exist
    except OSError as exception:
        shutil.rmtree("/home/ubuntu/workspace/research/xmltojson/output")  # removes previous output folder and makes new one
        os.makedirs(path)
        if exception.errno != errno.EEXIST:
            raise

def convert(xml_file, xml_attribs=True):
    with open(os.path.join('input', xml_file), "rb") as f:        # "rb: mode "
        d = xmltodict.parse(f, xml_attribs=xml_attribs)           # put xml into dict
        return json.dumps(d, indent=4)                            # dict to json code 
        
        
def Write_to_File(filename,sourcefile):                            # takes in filename and json code 
    output = open(filename ,'w')                                   # open file for writing
    output.write(sourcefile)                                       # write json output code
       

       
# start of main    
path = "/home/ubuntu/workspace/research/xmltojson/output"         # path on where to make new output folder
make_sure_path_exists(path)                                       # make output folder if it doesn't already exist

filelist = []                                                     #list to hold names of all xml files we need to convert
for file in os.listdir("input"):                                  # go through list and get all xml file names
    if file.endswith(".xml"):                                     # check if file is xml type
        filelist.append(os.path.join("", file))                   # add xml file to list

tracker = 0                                         #iteration counter
for i in range(0, len(filelist)):                   # iterate through list of xml file names
    fileoutput = convert(filelist[tracker])         # get json code from xml file passed in saved in fileoutput
    filein = filelist[tracker]                      # get name of file
    fileout = ""  
    counter = 0
    for i in range(0,len(filein)):                  # loop to get everything up to '.' for file output name
        if filein[i] != '.' and counter == 0:
            fileout = fileout + filein[i] 
        else:
            counter = 1
    fileout = fileout + ".json"                     # add .json to make json file 
    completeName = os.path.join(path, fileout)      # makes sure we print out new file in output folder
    Write_to_File(completeName,fileoutput)          # write json code in output file passing in proper name of output file
    tracker = tracker + 1                           #increment counter to continue looping through other xml files
        

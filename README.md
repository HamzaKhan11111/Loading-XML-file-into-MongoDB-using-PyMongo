# Loading-XML-file-into-MongoDB-using-PyMongo
This python code parses DBLP.xml file and loads the data into MongoDB (a non-realational Database)

Steps:
1) Specify the .xml file you want to parse at : tree=ET.parse('file.xml')
2) Specify the connection string or URI (Uniform Resource Identifier) that specifies the location and details of the MongoDB server to which you want to connect at: client = pymongo.MongoClient("URI")
3) Execute the code.

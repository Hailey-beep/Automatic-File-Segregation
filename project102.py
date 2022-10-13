import os
import shutil

from_dir = "C:\Users\haiha\Downloads"
to_dir = "C:\Users\haiha\OneDrive\Documents"
list_of_files = os.listdir(from_dir)

#print(list_of_files)
for file in list_of_files:
    fime_name,file_extension = os.path.splitext(file)

    if file_extension == "":
        #this will continue the loop
        continue

    if file_extension in [".txt'", ".doc", ".docx", ".pdf"]:
        path1 = from_dir+"/"+file
        path2 = to_dir+"/"+"Dcoument_files"
        path3 = to_dir+"/"+"Dcoument_files"+"/"+file

        #Checks to make sure the file exist on the computer
        if os.path.exists(path2):
            print(file + "has been moved to Document Files in Documents")
            #Moves file to a different one that exist
            shutil.move(path1, path3)
        else:
            #create a file called Document_files
            os.makedirs(path2)
            print("Folder Called document_files has been created in documents")
            print(file + "has been moved to Document Files in Documents")
            shutil.move(path1, path3)
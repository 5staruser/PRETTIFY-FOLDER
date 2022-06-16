import os
def soldier(path,file,format):
    files = os.listdir(path)
    f = open(file)
    filelist = f.read().split("\n")
    f.close()
    os.chdir(path)
    i=1
    for file in files:
        if file not in filelist:
            os.rename(file,file.capitalize())
        if os.path.splitext(file)[1]==format:
            os.rename(file,f'{i}{format}')
            i=i+1
soldier(r"C:\Users\HP\OneDrive\Desktop\testing",r"C:\Users\HP\PycharmProjects\firstprog\soldier.txt",".jpg")
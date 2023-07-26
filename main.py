import os
import shutil
source="C:/Users/hp/Downloads/C102_assets-main/C102_assets-main/myfolder"
destination="C:/Users/hp/Downloads/C102_assets-main/C102_assets-main/mydestinationfolder"
listoffiles=os.listdir(source)
print(listoffiles)
for filename in listoffiles:
    name,extension=os.path.splitext(filename)
    print(name)
    print(extension)
    if extension=='':
        continue
    if extension in['.gif','.png','.jpg','.jpeg','.jfif']:
        path1=source+'/'+filename
        path2=destination+'/'+'imagefiles'
        path3=destination+'/'+'imagefiles'+'/'+ filename
        print("path1",path1)
        print("path3",path3)
        if os.path.exists(path2):
            print("moving")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving")
            shutil.move(path1,path3)



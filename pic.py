import shutil

fromDir = 'C:/Users/livcr/OneDrive/Pictures/projects/PRO-104-Project-Image-main/PRO-104-Project-Image-main/solar-system.jpg'
toDir = 'c:/Users/livcr/OneDrive/Pictures/projects/104'

shutil.copy(fromDir,toDir)
print('file copied succesfully')
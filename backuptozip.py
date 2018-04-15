# backuptozip.py - Copies an entire folder and its contents into a ZIP file whose filename increments.
# inputs - folder location, comma separated extensions[optional]
# output - foldername_1.zip, foldername_2.zip,...

import os, zipfile

# fw = open('temp1.txt', 'w')
# fw.close()
# fw = open('temp2.jpg', 'w')
# fw.close()


def backupToZip(folder, *extn):
    # Backup the entire contents of "folder" into a ZIP file.
    # Add only selected extension type files

    folder = os.path.abspath(folder)    # make sure folder is absolute

    # Figure out the filename this code should use based on what files already exist.
    number = 1
    while True:
        zipFilename = folder + '\\' + os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number += 1

    # Create ZIP file
    print("Creating %s..." %(zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Walk through the directory and add to ZIP file
    for foldername, subfolders, filenames in os.walk(folder):

        print("Adding files in folder %s..." %(foldername))
        # Add current folder to the ZIP file
        backupZip.write(foldername)

        # Add all the files in current folder to the ZIP file
        for filename in filenames:

            # skip old backup zip files
            newBase = os.path.basename(folder)+'_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue

            # if any extn provided then select only those files
            if len(extn) != 0:
                ind = filename.rfind('.')
                if ind != -1 and (filename[ind+1:] in extn):
                    backupZip.write(os.path.join(foldername, filename))
            else:
                backupZip.write(os.path.join(foldername, filename))

    backupZip.close()
    print('Done.')


# backupToZip('C:\\Users\Hariom\\PycharmProjects\\firstpyproject', 'txt', 'py')
# backupToZip('D:\\Docs\\Hariom Docs\\Studies\\Python\\docs')


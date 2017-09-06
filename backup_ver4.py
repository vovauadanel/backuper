import os
import time
import zipfile

# files wich need copy
source1 = '/home/volodymyr/python'
source = '/home/volodymyr/projects'

#directory for backup files
target_dir = '/home/volodymyr/backup'

# current date is the name of subdirectory in main directory
today = target_dir + os.sep + time.strftime('%Y%m%d')

# current time is the name of zip archive
now = time.strftime('%H%M%S')

#create directory if it is not created
if not os.path.exists(today):
	os.mkdir(today)
	print('directory successfully created', today)

comment = str(input('Input comment -->'))

# name of zip-file
if len(comment) == 0:
	target = today + os.sep + now + '.zip'
else:
	target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'

# run the backup
my_zip = zipfile.ZipFile(target, mode='w') #create archive
for root, dirs, files in os.walk(source):
	for file in files:
		my_zip.write(os.path.join(root, file))
my_zip.close()




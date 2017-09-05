import os
import time

# files wich need copy
source = ['/home/volodymyr/python', '/home/volodymyr/vizitka']

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

# use command zip for put files to archive
zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

# run the backup
print(zip_command)
if os.system(zip_command) == 0:
	print('The backup was successfully created in', target)
else:
	print('Backup failed')



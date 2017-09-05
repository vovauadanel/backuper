import os
import time

# files wich need copy
source = ['/home/volodymyr/python', '/home/volodymyr/vizitka']

#directory for backup files
target_dir = '/home/volodymyr/backup'

today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

if not os.path.exists(today):
	os.mkdir(today)
	print('directory successfully created', today)

# name of zip-file
target = today + os.sep + now + '.zip'

# use command zip for put files to archive
zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

# run the backup
print(zip_command)
if os.system(zip_command) == 0:
	print('The backup was successfully created in', target)
else:
	print('Backup failed')



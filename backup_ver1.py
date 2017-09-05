import os
import time

# files wich need copy
source = ['/home/volodymyr/python', '/home/volodymyr/vizitka']

#directory for backup files
target_dir = '/home/volodymyr/backup'

# name of zip-file
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

# use command zip for put files to archive
zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

# run the backup
print(zip_command)
if os.system(zip_command) == 0:
	print('The backup was successfully created in', target)
else:
	print('Backup failed')



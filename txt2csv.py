# courtesy of http://stackoverflow.com/questions/10220412/convert-tab-delimited-txt-file-into-a-csv-file-using-python

import csv

#without file extension
file_name = "[NAME OF FILE]"

txt_file = r + '"' + file_name + '.txt"'
csv_file = r + '"' + file_name + '.csv"'

# use 'with' if the program isn't going to immediately terminate
# so you don't leave files open
# the 'b' is necessary on Windows
# it prevents \x1a, Ctrl-z, from ending the stream prematurely
# and also stops Python converting to / from different line terminators
# On other platforms, it has no effect
in_txt = csv.reader(open(txt_file, "rb"), delimiter = '\t')
out_csv = csv.writer(open(csv_file, 'wb'))

out_csv.writerows(in_txt)

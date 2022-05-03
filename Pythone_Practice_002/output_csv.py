import csv

with open('/Users/nagatatooru/Code/git/Python_Practice/Pythone_Practice_002/sample_writer_row.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow([0, 1, 2])
	writer.writerow(['a', 'b', 'c'])


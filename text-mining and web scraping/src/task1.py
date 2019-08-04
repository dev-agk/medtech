import slate3k as slate
import csv
with open('/home/aishu/Minimal Access Surgery Need Specification Documents.pdf','rb') as f:
     extracted_text = slate.PDF(f)
#print(extracted_text)
with open('file2.csv', mode='w') as employee_file:
     employee_writer = csv.writer(employee_file)
     employee_writer.writerow(extracted_text)

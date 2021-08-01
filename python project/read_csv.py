import csv 
with open('training_data.csv') as myfile:
    csv_read = csv.reader(myfile, delimiter=':')
    line_count = 0
    my_list =[]
    #for row in csv_read:
     #   if line_count == 0:
        #    print(f'Column names are {", ".join(row)}')
         #   line_count += 1
        #else:
         #   print(f'\t{row[0]} {row[1]}  {row[2]}.')
          #  line_count += 1
            
           # if line_count == 10:
            #    break
    print(f'Processed {line_count} lines.')

    for row in csv_read:
        my_list.append(row)
        line_count += 1
        if line_count == 2:
            break
    print(my_list)

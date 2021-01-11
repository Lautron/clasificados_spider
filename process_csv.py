import csv

present_links = { 
        data[1] for data in csv.reader(
            open('miguel.csv', 'r')
            ) 
        }
with open('final_result.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    with open('results.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] in present_links:
                print(row[0] + ' was already present')
                continue
            if 'avisos' in row[0]:
                writer.writerow(row)
                print('Found something')



#!/usr/bin/python -tt

# MB 02.10.2016
# Read the contents of a VCF file
# ...write some to a tobii-contacts file.

#import sys

def main():
    vcf = open('00001.vcf', 'rU')
    record = []

    #Loop over the file, put individual vcards into separate
    #     lists within the master list, record[]
    contact = -1
    for line in vcf:
        #print(line)
        if line.startswith('BEGIN:VCARD'):
            contact += 1
            record.append([])
        if line.startswith('FN:'):
            #record[contact].append(line[3:].strip())
            record[contact].append(line)
        if line.startswith('EMAIL'):
            record[contact].append(line)
        if line.startswith('TEL;'):
            record[contact].append(line)
    vcf.close()
    
    #Now format the lists correctly:
    #   Name, telephone, email address (only one of each!)
    names = 0
    for person in record:
        print('Record', person)
        if any(entry.startswith('FN:') for entry in person):
            print('Has a name')
            names += 1
        else:
            print('No name!')
        #input() #wait for enter
    print('\n', contact + 1, 'Contacts.')
    print(names, 'have names.')

if __name__ == '__main__':
  main()

#!/usr/bin/python -tt

# MB 02.10.2016
# Read the contents of a VCF file
# ...write some to a tobii-contacts file.

#import sys

def main():
    vcf = open('00001.vcf', 'rU')
    record = []
    contact = -1
    for line in vcf:
        print(line)
        if line.startswith('BEGIN:VCARD'):
            contact += 1
            record.append([])
        if line.startswith('FN:'):
            record[contact].append(line[3:].strip())
        if line.startswith('EMAIL'):
            record[contact].append(line.strip())
        if line.startswith('TEL;'):
            record[contact].append(line.strip())
            
    vcf.close()
    
    for i in record:
        print('Record', i,)
        input() #wait for enter
    print('\n', contact + 1, 'Contacts.')


if __name__ == '__main__':
  main()

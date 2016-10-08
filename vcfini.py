#!/usr/bin/python -tt

# MB 02.10.2016
# Read the contents of a VCF file
# ...write some to a tobii-contacts file.

def main():
    vcf = open('00001.vcf', 'r')
    record = []
    contact = -1
    for line in vcf:
        if line.startswith('BEGIN:VCARD'):
            contact = contact + 1
            #print('Contact', contact)
            record.append([])
        if line.startswith('FN:'):
            #record[contact].append(line[3:-1])
            record[contact].append(line[3:].strip())
        if line.startswith('EMAIL'):
            #record[contact].append(line[11:-1])
            record[contact].append(line.strip())
        if line.startswith('TEL;'):
            record[contact].append(line.strip())
            
            
    vcf.close()
    
    for i in record:
        print('\nRecord', i)
    print('\n', contact, 'Contacts.')


if __name__ == '__main__':
  main()

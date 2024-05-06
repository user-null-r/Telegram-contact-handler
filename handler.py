import csv

file_input = open('telegram.csv', encoding='utf-8')
rare_input = csv.reader(file_input, delimiter=',')
rare_contacts = [[str(element) for element in person[:3]] for person in rare][1:]
contacts = []
alphanet = [chr(s) for s in range(1072, 1105)]
numbers = '0123456789'
k = 1

for rare_contact in rare_contacts:
    contact = [' '.join(rare_contact[:2]), rare_contact[2]]
    name = ''.join([s for s in contact[0] if s.lower() in alphanet]).lstrip('0')
    if not name:
        name = f'Неизвестный {k}'
        k += 1
    mobile = ''.join([n for n in contact[1] if n in numbers]).lstrip('0')
    if len(mobile) != 7:
        mobile = '+' + mobile
        if mobile[1] == '8':
            mobile = mobile.replace('8', '7')
    contacts.append([name, mobile])

file_output = open('google.csv', mode='w', encoding='utf-8')
res = csv.writer(file_output, delimiter='\t')
res.writerow(['Name', 'Mobile'])
for contact in contacts:
    res.writerow(contact)

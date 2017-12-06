import re
from collections import Counter
from math import ceil

f = open('scorelib.txt', 'r')

composers = Counter()
centuries = Counter()
c_minor_count = 0

for line in f:
    r_composer = re.compile(r"Composer: ([\w, ]+)")
    m_composer = r_composer.match(line)

    r_century = re.compile(r"Composition Year: .*(\d{4})")
    m_century = r_century.match(line)

    # how many in the key of c minor?
    if 'c minor' in line:
        c_minor_count += 1

    # how many pieces by each composer?
    if m_composer:
        composer_name = m_composer.group(1).replace(',', '').strip()
        composers[composer_name] += 1

    # how many pieces composed in a given century?
    if m_century:
        century = ceil(int(m_century.group(1).strip())/100)
        centuries[century] += 1

print('How many pieces by each composer?')
for key, value in composers.items():
    print('{0}: {1}'.format(key, value))

print('How many pieces composed in a given century?')
for key, value in centuries.items():
    print('{0}th century: {1}'.format(key, value))

print('How many in the key of c minor?\n{}'.format(c_minor_count))

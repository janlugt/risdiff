from sets import Set

path_old = 'databases2015.ris'
path_new = 'databases2017.ris'

overlap_entries = 0
new_entries = []

delimiter = 'ER  - \n'

old_file = open(path_old, 'r').read()
new_file = open(path_new, 'r').read()

entries_old = Set(old_file.split(delimiter)[:-1])
entries_new = new_file.split(delimiter)[:-1]

print('Entries in old file: %d' % len(entries_old))
print('Entries in new file: %d' % len(entries_new))

for entry in entries_new:
  if entry in entries_old:
    overlap_entries = overlap_entries + 1
  else:
    new_entries.append(entry)


print('Overlapping entries: %d' % overlap_entries)
print('New entries: %d' % len(new_entries))

with open('new_entries.ris', 'w') as out:
  for entry in new_entries:
    out.write('%s%s' % (entry, delimiter))

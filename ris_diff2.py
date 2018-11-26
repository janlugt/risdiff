from RISparser import readris, config
from sets import Set

path_old = 'databases2015.ris'
path_new = 'databases2017.ris'

overlap_entries = 0
new_entries = []

class hashabledict(dict):
  def __hash__(self):
    return hash(frozenset(self))

with open(path_old, 'r') as bibfile_old, open(path_new, 'r') as bibfile_new:
  entries_old = Set([ hashabledict(x) for x in readris(bibfile_old) ])
  entries_new = [ hashabledict(x) for x in list(readris(bibfile_new)) ]

  print('Entries in old file: %d' % len(entries_old))
  print('Entries in new file: %d' % len(entries_new))

  for entry in entries_new:
    if entry in entries_old:
      overlap_entries = overlap_entries + 1
    else:
      new_entries.append(entry)


print('Overlapping entries: %d' % overlap_entries)
print('New entries: %d' % len(new_entries))

tag_key_mapping = dict(zip(config.TAG_KEY_MAPPING.values(),
                           config.TAG_KEY_MAPPING.keys()))

with open('new_entries.ris', 'w') as out:
  for entry in new_entries:
    for key, value in entry.iteritems():
      if key in tag_key_mapping:
        tag = tag_key_mapping[key]
        if tag in config.LIST_TYPE_TAGS:
          for item in value:
            out.write('%s\t- %s\n' % (tag, item))
        else:
          out.write('%s\t- %s\n' % (tag, value))
    out.write('ER\t- \n')

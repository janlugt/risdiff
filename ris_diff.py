from RISparser import readris, config

path_old = 'databases2015.ris'
path_new = 'databases2017.ris'

overlap_entries = 0
new_entries = []

with open(path_old, 'r') as bibfile_old, open(path_new, 'r') as bibfile_new:
  entries_old = list(readris(bibfile_old))
  entries_new = list(readris(bibfile_new))

  print('Entries in old file: %d' % len(entries_old))
  print('Entries in new file: %d' % len(entries_new))

  for entry in entries_new:
    if len([ x for x in entries_old if x == entry ]):
      overlap_entries = overlap_entries + 1
    else:
      new_entries.append(entry)


print('Overlapping entries: %d' % overlap_entries)
print('New entries: %d' % len(new_entries))

tag_key_mapping = dict(zip(config.TAG_KEY_MAPPING.values(),
                           config.TAG_KEY_MAPPING.keys()))

with open('new_entries.ris', 'w') as out:
  for entry in new_entries[1:5]:
    for key, value in entry.iteritems():
      if key in tag_key_mapping:
        tag = tag_key_mapping[key]
        if tag in config.LIST_TYPE_TAGS:
          for item in value:
            out.write('%s\t- %s\n' % (tag, item))
        else:
          out.write('%s\t- %s\n' % (tag, value))
    out.write('ER\t- \n')

#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re


"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
    names = []
    row = 0
    column = 0
    f = open(filename, 'rU')
    text = f.read()
    year_match = re.search(r'Popularity\sin\s(\d\d\d\d)', text)
    if not year_match:
        print('Couldn\'t find the year!\n')
        sys.exit(1)
    year = year_match.group(1)
    names.append(year)
    tuples = re.findall(r'<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>', text)
    names_to_rank =  {}
    for i in tuples:
            names.append([i[1],i[0]])
            names.append([i[2],i[0]])
    return sorted(names,key=lambda l:l[0])

def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print ('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  text = []
  for filename in args:
    names = extract_names(filename)
    size = len(names)
    i = 1
    while(i < size):
        if names[i][0]==names[i-1][0]:
            if names[i][1] < names[i-1][1]:
                del names[i-1]
            else:
                del names[i]
            # i -= 1
            size = len(names)
        i += 1
    for i in names:
        print(i)

    if summary:
        file = open("outputfile.txt",'w')
        file.write(str(names))
        file.close()

if __name__ == '__main__':
  main()

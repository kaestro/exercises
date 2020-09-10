#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os

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

def extract_names(filename, isSummary: bool):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  
  year_pattern = re.compile("<h3 align=\"center\">Popularity in (\d{4})</h3>")
  name_rank_pattern = re.compile("<tr align=\"right\"><td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>")
  # +++your code here+++
  answer = []
  f = open(filename, 'r')
  for line in f:
    year = re.search(year_pattern, line)
    if year:
      year = year.group(1)
      break
  f.close()
  answer.append(year)

  name_ranks = []
  f = open(filename, 'r')
  for line in f:
    name_rank = re.search(name_rank_pattern, line)
    if name_rank:
      name_ranks.append(name_rank.group(2) + " " + name_rank.group(1))
      name_ranks.append(name_rank.group(3) + " " + name_rank.group(1))
  name_ranks.sort()
  answer.extend(name_ranks)

  return answer


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

  FILENAME = "summary.txt"
  
  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  if summary:
    f = open(FILENAME, 'w')
    f.close()
    for filename in args:
      names = extract_names(filename, True)
      f = open(FILENAME, 'a')
      f.write('\n'.join(names[:]))
      f.close()
  else:
    names = extract_names(args[1], False)
    f = open(FILENAME, "w")
    f.write('\n'.join(names[:]))



if __name__ == '__main__':
  main()
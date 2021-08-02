import re
import sys
import data

rules = data.rules

class Token:
  def __init__(self, line, column, value, category):
    self.line = line
    self.column = column
    self.value = value
    self.category = category

  def __str__(self):
    return ( "              [%04d, %04d] (TODO, %20s) {%s}" % 
    (self.line, self.column, self.category, self.value) )


class Tokenize:

  def __init__(self, file, rules):
    self.line = 0
    self.file = file
    self.regex = re.compile('|'.join(['(?P<%sA%d>%s)' % (type, idx, regex)
                             for idx, (type, regex) in enumerate(rules)]))
    self.token = self.tokenGenerator()

  def tokenGenerator(self):
    
    for linecontent in self.file:

      position = 0

      while position < len(linecontent):
        if linecontent[position] == ' ' or linecontent[position] == '\n':
            position = position + 1
            continue
        temp_match = self.regex.match(linecontent, position)
        if temp_match is None:
            print("erro lexico")
            break

        group_name = temp_match.lastgroup
        token = Token(self.line, position, temp_match.group(group_name), group_name.split('A')[0])
        position = temp_match.end()
        yield token

      self.line = self.line + 1

  def nextToken(self):
    return self.token.__next__()

print(sys.argv)

file = open('input.txt', 'r')

instance = Tokenize(file, rules)

print(instance.nextToken())
print(instance.nextToken())

file.close()

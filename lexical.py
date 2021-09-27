from token import Token, regexes, TokenCategory
import re

class Tokenizer:
  def __init__(self, file_name):
    self.line = 0
    self.file = open(file_name, 'r')
    self.regex = re.compile('|'.join(['(?P<%s>%s)' % (type, regex) for (type, regex) in regexes]))
    self.token = self.tokenGenerator()

  def tokenGenerator(self):
    
    for linecontent in self.file:

      column = 0

      print("%4d  %s" % (self.line, linecontent.rstrip()))

      while column < len(linecontent):
        if linecontent[column] == ' ' or linecontent[column] == '\n':
          column = column + 1
          continue

        temp_match = self.regex.match(linecontent, column)

        if temp_match is None:
          yield Token(self.line, column, linecontent[column], 'UNDEFINED')
          column = column + 1
          continue

        group_name = temp_match.lastgroup
        token = Token(self.line, column, temp_match.group(group_name), group_name)
        column = temp_match.end()
        
        yield token

      self.line = self.line + 1

    yield Token(self.line, column, 'EOF', 'EOF')
    self.file.close()

  def nextToken(self):
    return self.token.__next__()


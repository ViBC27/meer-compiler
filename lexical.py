import re
from token import Token, regexes, TokenCategory

class Tokenizer:

  def __init__(self, file_name):
    self.line = 0
    self.file = open(file_name, 'r')
    self.regex = re.compile('|'.join(['(?P<%s>%s)' % (type, regex)
                             for (type, regex) in regexes]))
    self.token = self.tokenGenerator()

  def tokenGenerator(self):
    
    for linecontent in self.file:

      position = 0

      print("%4d  %s" % (self.line, linecontent.strip()))

      while position < len(linecontent):
        if linecontent[position] == ' ' or linecontent[position] == '\n':
          position = position + 1
          continue

        temp_match = self.regex.match(linecontent, position)

        if temp_match is None:
          yield Token(self.line, position, linecontent[position], 'UNDEFINED')
          position = position + 1
          continue

        group_name = temp_match.lastgroup
        token = Token(self.line, position, temp_match.group(group_name), group_name)
        position = temp_match.end()
        
        yield token

      self.line = self.line + 1

    yield Token(self.line, position, 'EOF', 'EOF')
    self.file.close()

  def nextToken(self):
    return self.token.__next__()


from enum import Enum, auto

class TokenCategory(Enum):
  ID = auto()
  TYPEBOOL = auto()
  TYPECHAR = auto()
  TYPESTRING = auto()
  TYPEINT = auto()
  TYPEFLOAT = auto()
  OPASUM = auto()
  OPAMINUS = auto()
  OPADIV = auto()
  OPAMULT = auto()
  OPRLESS = auto()
  OPRGREAT = auto()
  OPREQL = auto()
  OPRLESSEQL = auto()
  OPRGREATEQL = auto()
  OPRNOTEQL = auto()
  ARRAYBEGIN = auto()
  ARRAYEND = auto()
  PARAMSBEGIN = auto()
  PARAMSEND = auto()
  BLOCKBEGIN = auto()
  BLOCKEND = auto()
  FCDEF = auto()
  FCRETURN = auto()
  LINEEND = auto()
  SEPARATOR = auto()
  ASSIGN = auto()
  TYPEASSIGN = auto()
  FCTYPEVOID = auto()
  CONSTLINT = auto()
  CONSTLSTRING = auto()
  CONSTLBOOL = auto()
  CONSTLFLOAT = auto()
  CONSTLCHAR = auto()
  PRINT = auto()
  INPUT = auto()
  CONDIF = auto()
  CONDELSEIF = auto()
  CONDELSE = auto()
  CASTINGINT = auto()
  CASTINGFLOAT = auto()
  CASTINGSTRING = auto()
  CASTINGBOOLEAN = auto()
  CASTINGCHAR = auto()
  LOOPFOR = auto()
  LOOPWHILE = auto()
  VAR = auto()
  OPLAND = auto()
  OPLOR = auto()
  OPLNOT = auto()
  EOF = auto()
  UNDEFINED = auto()


regexes = [
  ('VAR', 'var'),
  ('TYPEBOOL', 'boolean'),
  ('TYPECHAR', 'char'),
  ('TYPEINT', 'int'),
  ('TYPEFLOAT', 'float'),
  ('TYPESTRING', 'string'),
  ('OPLAND', 'and'),
  ('OPLOR', 'or'),
  ('OPLNOT', 'not'),
  ('OPASUM', '\+'),
  ('OPAMINUS', '\-'),
  ('OPADIV', '\/'),
  ('OPAMULT', '\*'),
  ('OPRLESS', '<'),
  ('OPRGREAT', '>'),
  ('OPREQL', '=='),
  ('OPRLESSEQL', '<='),
  ('OPRGREATEQL', '>='),
  ('OPRNOTEQL', '!='),
  ('SEPARATOR', '\,'),
  ('ASSIGN', '='),
  ('PRINT', 'print'),
  ('INPUT', 'input'),
  ('CONDIF', 'if'),
  ('CONDELSEIF', 'elseif'),
  ('CONDELSE', 'else'),
  ('CASTINGINT', 'Int'),
  ('CASTINGFLOAT', 'Float'),
  ('CASTINGSTRING', 'String'),
  ('CASTINGBOOLEAN', 'Boolean'),
  ('CASTINGCHAR', 'Char'),
  ('LOOPFOR', 'for'),
  ('LOOPWHILE', 'while'),
  ('FCRETURN', 'return'),
  ('FCDEF', 'def'),
  ('FCTYPEVOID', 'void'),
  ('BLOCKBEGIN', 'begin'),
  ('BLOCKEND', 'end'),
  ('PARAMSBEGIN', '\('),
  ('PARAMSEND', '\)'),
  ('TYPEASSIGN', '\:'),
  ('ARRAYBEGIN', '\['),
  ('ARRAYEND', '\]'),
  ('LINEEND', '\;'),
  ('CONSTLSTRING', '"([\w\W]*)"'),
  ('CONSTLBOOL', 'true|false'),
  ('CONSTLFLOAT', '([0-9]+)\.([0-9]+)'),
  ('CONSTLINT', '[0-9]+'),
  ('CONSTLCHAR', '\'([\w\W])\''),
  ('ID', '[a-zA-Z][a-zA-Z0-9\_]*'),
]

class Token:
  def __init__(self, line, column, value, category):
    self.line = line
    self.value = value
    self.column = column
    self.category = category

  def __str__(self):
    return ("              [%04d, %04d] (%04d, %20s) {%s}" % 
    (self.line, self.column, TokenCategory[self.category].value, self.category, self.value) )

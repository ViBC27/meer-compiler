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
  FCBEGIN = auto()
  FCEND = auto()
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
  FCINIT = auto()
  EOF = auto()
  UNDEFINED = auto()


regexes = [
  ('FCDEF', 'def'),
  ('FCINIT', 'init'),
  ('FCTYPEVOID', 'void'),
  ('PRINT', 'print'),
  ('FCBEGIN', 'begin'),
  ('FCEND', 'end'),
  ('TYPESTRING', 'string'),
  ('PARAMSBEGIN', '\('),
  ('PARAMSEND', '\)'),
  ('TYPEASSIGN', '\:'),
  ('ARRAYBEGIN', '\['),
  ('ARRAYEND', '\]'),
  ('LINEEND', '\;'),
  ('ID', '[a-zA-Z][a-zA-Z0-9\_]*'),
  ('CONSTLSTRING', '"([\w\W]*)"'),
]

class Token:
  def __init__(self, line, column, value, category):
    self.line = line
    self.column = column
    self.value = value
    self.category = category

  def __str__(self):
    return ("              [%04d, %04d] (%04d, %20s) {%s}" % 
    (self.line, self.column, TokenCategory[self.category].value, self.category, self.value) )

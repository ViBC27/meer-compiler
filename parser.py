import sys
from lexical import Tokenizer

def main():
  if len(sys.argv) > 1:
    lexical = Tokenizer(sys.argv[1])

    while True:
      token = lexical.nextToken()
      print(token)

      if token.category == 'EOF':
        break

  else:
    print("file path was not given")

if __name__ == '__main__':
  main()

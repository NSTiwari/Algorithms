import itertools


def get_value(word, substitution):
    s = 0
    factor = 1
    for letter in reversed(word):
        s += factor * substitution[letter]
        factor *= 10
    return s


def cryptarithmetic(equation):
    # split equation in left and right
    left, right = equation.lower().replace(' ', '').split('=')
    # split words in left part
    left = left.split('+')
    # create list of used letters
    letters = set(right)
    for word in left:
        for letter in word:
            letters.add(letter)
    letters = list(letters)

    digits = range(10)
    for perm in itertools.permutations(digits, len(letters)):
        sol = dict(zip(letters, perm))

        if sum(get_value(word, sol) for word in left) == get_value(right, sol):
            print(' + '.join(str(get_value(word, sol)) for word in left) + " = {} (mapping: {})".format(get_value(right, sol), sol))


def main():
  words=[]
  n=int(input("Enter the no. of words: "))
  print()
  for i in range(n):
    word=input("Enter word"+str(i+1)+": ")
    words.append(word)
  
  result_word=input("Enter result word: ")
  equation=' + '.join(map(str, words))+" = "+result_word 
  print()
  print("The equation is: ",equation)
  print()
  print("Solving the cryptarithmetic equation ...")
  print()
  print("Following are the possible solutions for given cryptarithmetic equation")
  print()
  cryptarithmetic(equation)


if __name__ == '__main__':
  main()

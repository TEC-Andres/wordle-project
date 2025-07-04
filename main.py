from nltk.corpus import words

class WordleCalc:
    def __init__(self):
        self.lenWord = 11
        self.forbiden_letters= []
        self.letters_that_must_be_in_word = []
        self.word_list = [word.lower() for word in words.words() if len(word) == self.lenWord]

    """
    Letters we know they arent in the word
    """
    def add_forbiden_letter(self) -> None:
        letters = input("Enter letter(s) that are not in the word (no spaces): ").lower()
        for letter in letters:
            if letter.isalpha() and letter not in self.forbiden_letters:
                self.forbiden_letters.append(letter)

    """
    Letters we know they are in the word just not in the correct position
    """
    def add_letters_that_must_be_in_word(self) -> None:
        letters = input("Enter letter(s) that must be in the word (no spaces): ").lower()
        for letter in letters:
            if letter.isalpha():
                self.letters_that_must_be_in_word.append(letter)

    """
    Letters we know they are in the word and in the correct position (for spaces, leave "*" in the position)
    """
    def add_letters_in_correct_position(self) -> None:
        letters = input("Enter letters in the correct position (use * for spaces): ").lower()
        if len(letters) != self.lenWord:
            print(f"Please enter exactly {self.lenWord} characters.")
            return
        for i, letter in enumerate(letters):
            if letter.isalpha() or letter == '*':
                if i < len(self.word_list[0]):
                    self.word_list = [word for word in self.word_list if word[i] == letter or letter == '*']
            else:
                print("Invalid character. Please use only letters or '*' for spaces.")
                return
            
    def filter_words(self) -> None:
        for letter in self.forbiden_letters:
            self.word_list = [word for word in self.word_list if letter not in word]
        for letter in self.letters_that_must_be_in_word:
            self.word_list = [word for word in self.word_list if letter in word]

        print("Possible words:", self.word_list)

def main() -> None:
    calc: WordleCalc = WordleCalc()
    while True:
        try:
            calc.add_forbiden_letter()
            calc.add_letters_that_must_be_in_word()
            calc.add_letters_in_correct_position()
            calc.filter_words()
            if not calc.word_list:
                print("No possible words found. Please check your inputs.")
                break
            else:
                print(f"Remaining possible words: {len(calc.word_list)}")

        except KeyboardInterrupt:
            print("\nExiting...")
            break

if __name__ == "__main__":
    main()
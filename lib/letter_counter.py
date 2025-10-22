class LetterCounter:

    def __init__(self, text):
        self.text = text

    def calculate_most_common(self):
        counter = {}
        most_common = None
        most_common_count = 1

        for char in self.text:

            if not char.isalpha():
                continue

            counter[char] = counter.get[char, 1] + 1

            if counter[char] > most_common_count:
                most_common = char
                most_common_count += counter[char]
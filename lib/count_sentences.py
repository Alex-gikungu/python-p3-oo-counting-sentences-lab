class MyString:
    def __init__(self, value=''):
        self._value = ''
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.")

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self._value.endswith('.')

    def is_question(self):
        return self._value.endswith('?')

    def is_exclamation(self):
        return self._value.endswith('!')

    def count_sentences(self):
        sentences = self._value.split('.')
        sentences = [s.strip() for s in sentences if s]
        return len(sentences)

# Test the MyString class
if __name__ == "__main__":
    my_string = MyString("Hello World.")
    print(my_string.value)  # Output: Hello World.
    print(my_string.is_sentence())  # Output: True
    print(my_string.is_question())  # Output: False
    print(my_string.is_exclamation())  # Output: False
    print(my_string.count_sentences())  # Output: 1

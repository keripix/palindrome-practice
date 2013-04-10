from pyvows import Vows, expect
from palindrome import reverse, cleanse, isPalindrome


@Vows.batch
class Palindrome(Vows.Context):
    class Cleanse(Vows.Context):
        def topic(self):
            return cleanse("a.b,c d 'e#f $ gh i-jklm n o p-q")

        def should_cleanse_input_from_non_alfa_chars(self, topic):
            expect(topic).to_equal("abcdefghijklmnopq")

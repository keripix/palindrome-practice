from pyvows import Vows, expect
from palindrome import reverse, cleanse, isPalindrome


@Vows.batch
class Palindrome(Vows.Context):
    class Cleanse(Vows.Context):
        def topic(self):
            return cleanse("a.b,c d 'e#f $ gh i-jklm n o p-q")

        def should_cleanse_input_from_non_alfa_chars(self, topic):
            expect(topic).to_equal("abcdefghijklmnopq")

    class CleanseWhenEmpty(Vows.Context):
        def topic(self):
            return ""

        def should_return_as_is(self, topic):
            expect(topic).to_equal("")
            expect(len(topic)).to_equal(0)

    class Reverse(Vows.Context):
        def topic(self):
            return reverse("T'hi-s Should b-e (ok)")

        def should_reverse_and_cleanse_too(self, topic):
            expect(topic).to_equal("koebdluohSsihT")

    class PalindromeIs(Vows.Context):
        class Madam(Vows.Context):
            def topic(self):
                return isPalindrome("MaDAm")

            def should_be_true(self, topic):
                expect(topic).to_be_true()



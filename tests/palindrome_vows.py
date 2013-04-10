from pyvows import Vows, expect


@Vows.batch
class Palindrome(Vows.Context):
    class RunPalindrome(Vows.Context):
        def topic(self):
            pass

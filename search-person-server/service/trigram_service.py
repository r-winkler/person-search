import re

# ist ein analoger Algorithmus zu pg_trgm von Postgres
# https://stackoverflow.com/questions/46198597/python-string-matching-exactly-equal-to-postgresql-similarity-function
class TrigramService(object):

    def find_ngrams(self, text: str, number: int=3) -> set:
        """
        returns a set of ngrams for the given string
        :param text: the string to find ngrams for
        :param number: the length the ngrams should be. defaults to 3 (trigrams)
        :return: set of ngram strings
        """

        if not text:
            return set()

        words = [f'  {x} ' for x in re.split(r'\W+', text.lower()) if x.strip()]

        ngrams = set()

        for word in words:
            for x in range(0, len(word) - number + 1):
                ngrams.add(word[x:x+number])

        return ngrams


    def similarity(self, text1: str, text2: str, number: int=3) -> float:
        """
        Finds the similarity between 2 strings using ngrams.
        0 being completely different strings, and 1 being equal strings
        """

        ngrams1 = self.find_ngrams(text1, number)
        ngrams2 = self.find_ngrams(text2, number)

        num_unique = len(ngrams1 | ngrams2)
        num_equal = len(ngrams1 & ngrams2)

        return float(num_equal) / float(num_unique)


    def word_similarity(self, text1: str, text2: str, number: int=3) -> float:
        """
        Finds the similarity between 2 strings using ngrams.
        0 being completely different strings, and 1 being equal strings
        """

        ngrams1 = self.find_ngrams(text1, number)
        ngrams2 = self.find_ngrams(text2, number)

        num_equal = len(ngrams1 & ngrams2)

        return float(num_equal) / float(len(ngrams1))

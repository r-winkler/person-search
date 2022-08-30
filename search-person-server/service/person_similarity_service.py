import textdistance
import unidecode
from service.person_service import PersonService
from service.trigram_service import TrigramService


def get_algo_type(algo_type):
    switcher = {
        'strcmp95': textdistance.strcmp95.normalized_similarity,
        'jaro': textdistance.jaro.normalized_similarity,
        'jaro-winkler': textdistance.jaro_winkler.normalized_similarity,
        'levenshtein': textdistance.levenshtein.normalized_similarity,
        'damarau-levenshtein': textdistance.damerau_levenshtein.normalized_similarity,
    }
    return switcher.get(algo_type, textdistance.jaro_winkler.normalized_similarity)


class PersonSimilarityService(object):

    def __init__(self):
        self.person_service = PersonService()
        self.trigram_service = TrigramService()

    def find_similar(self, search_name, search_firstname, algo_type, name_threshold, firstname_threshold, word_similarity, word_similarity_name_threshold, word_similarity_firstname_threshold):
        # case-insensitive und mit ascii suchen
        search_name = unidecode.unidecode(search_name.lower())
        search_firstname = unidecode.unidecode(search_firstname.lower())

        persons = self.person_service.find_all()

        if word_similarity:
            print("word similarity called")
            persons['word_similarity_name'] = persons.apply(lambda row: self.trigram_service.word_similarity(search_name, unidecode.unidecode(row.iloc[0].lower())), axis=1)
            persons['word_similarity_firstname'] = persons.apply(lambda row: self.trigram_service.word_similarity(search_firstname, unidecode.unidecode(row.iloc[1].lower())), axis=1)
            persons = persons[(persons['word_similarity_name'] > word_similarity_name_threshold) & (persons['word_similarity_firstname'] > word_similarity_firstname_threshold)]

        algo = get_algo_type(algo_type)

        if persons.empty:
            return persons
        else:
            persons['similarity_name'] = persons.apply(lambda row: algo(search_name, unidecode.unidecode(row.iloc[0].lower())), axis=1)
            persons['similarity_firstname'] = persons.apply(lambda row: algo(search_firstname, unidecode.unidecode(row.iloc[1].lower())), axis=1)

            return persons[(persons['similarity_name'] > name_threshold) & (persons['similarity_firstname'] > firstname_threshold)]


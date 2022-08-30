import textdistance

from service.trigram_service import TrigramService


class AlgoCompare:

    def __init__(self,
                 hamming=0.0,
                 levenshtein=0.0,
                 damerau_levenshtein=0.0,
                 jaro=0.0,
                 jaro_winkler=0.0,
                 strcmp95=0.0,
                 mlipns=0.0,
                 needleman_wunsch=0.0,
                 gotoh=0.0,
                 smith_waterman=0.0,
                 jaccard=0.0,
                 sorensen=0.0,
                 tversky=0.0,
                 sorensen_dice=0.0,
                 overlap=0.0,
                 cosine=0.0,
                 tanimoto=0.0,
                 monge_elkan=0.0,
                 bag=0.0,
                 lcsseq=0.0,
                 lcsstr=0.0,
                 ratcliff_obershelp=0.0,
                 prefix=0.0,
                 postfix=0.0,
                 length=0.0,
                 identity=0.0,
                 matrix=0.0,
                 mra=0.0,
                 editex=0.0,
                 trigram=0.0,
                 word_trigram=0.0
                 ):
        self.hamming = hamming
        self.levenshtein = levenshtein
        self.damerau_levenshtein = damerau_levenshtein
        self.jaro = jaro
        self.jaro_winkler = jaro_winkler
        self.strcmp95 = strcmp95
        self.mlipns = mlipns
        self.needleman_wunsch = needleman_wunsch
        self.gotoh = gotoh
        self.smith_waterman = smith_waterman
        self.jaccard = jaccard
        self.sorensen = sorensen
        self.tversky = tversky
        self.sorensen_dice = sorensen_dice
        self.overlap = overlap
        self.cosine = cosine
        self.tanimoto = tanimoto
        self.monge_elkan = monge_elkan
        self.bag = bag
        self.lcsseq = lcsseq
        self.lcsstr = lcsstr
        self.ratcliff_obershelp = ratcliff_obershelp,
        self.prefix = prefix,
        self.postfix = postfix,
        self.length = length,
        self.identity = identity,
        self.matrix = matrix,
        self.mra = mra,
        self.editex = editex,
        self.trigram = trigram,
        self.word_trigram = word_trigram


class AlgoCompareService(object):

    def __init__(self,trigramService=TrigramService()):
        self.trigramService = trigramService

    def compare(self, str1, str2):
        # edit-based algorithms
        hamming = textdistance.hamming.normalized_similarity(str1, str2)
        levenshtein = textdistance.levenshtein.normalized_similarity(str1, str2)
        damerau_levenshtein = textdistance.damerau_levenshtein.normalized_similarity(str1, str2)
        jaro = textdistance.jaro.normalized_similarity(str1, str2)
        jaro_winkler = textdistance.jaro_winkler.normalized_similarity(str1, str2)
        strcmp95 = textdistance.strcmp95.normalized_similarity(str1, str2)
        mlipns = textdistance.mlipns.normalized_similarity(str1, str2)
        needleman_wunsch = textdistance.needleman_wunsch.normalized_similarity(str1, str2)
        gotoh = textdistance.gotoh.normalized_similarity(str1, str2)
        smith_waterman = textdistance.smith_waterman.normalized_similarity(str1, str2)

        # token-based algorithms
        cosine = textdistance.cosine.normalized_similarity(str1, str2)
        jaccard = textdistance.jaccard.normalized_similarity(str1, str2)
        sorensen = textdistance.sorensen.normalized_similarity(str1, str2)
        tversky = textdistance.tversky.normalized_similarity(str1, str2)
        sorensen_dice = textdistance.sorensen_dice.normalized_similarity(str1, str2)
        overlap = textdistance.overlap.normalized_similarity(str1, str2)
        tanimoto = textdistance.tanimoto.normalized_similarity(str1, str2)
        monge_elkan = textdistance.monge_elkan.normalized_similarity(str1, str2)
        bag = textdistance.bag.normalized_similarity(str1, str2)
        trigram = self.trigramService.similarity(str1, str2, 3)
        word_trigram = self.trigramService.word_similarity(str1, str2, 3)

        # sequence-based algorithms
        lcsseq = textdistance.lcsseq.normalized_similarity(str1, str2)
        lcsstr = textdistance.lcsstr.normalized_similarity(str1, str2)
        ratcliff_obershelp = textdistance.ratcliff_obershelp.normalized_similarity(str1, str2)

        # simple algorithms
        prefix = textdistance.prefix.normalized_similarity(str1, str2)
        postfix = textdistance.postfix.normalized_similarity(str1, str2)
        length = textdistance.length.normalized_similarity(str1, str2)
        identity = textdistance.identity.normalized_similarity(str1, str2)
        matrix = textdistance.matrix.normalized_similarity(str1, str2)

        # phonetic algorithms
        mra = textdistance.mra.normalized_similarity(str1, str2)
        editex = textdistance.editex.normalized_similarity(str1, str2)

        return AlgoCompare(
            hamming,
            levenshtein,
            damerau_levenshtein,
            jaro,
            jaro_winkler,
            strcmp95,
            mlipns,
            needleman_wunsch,
            gotoh,
            smith_waterman,
            jaccard,
            sorensen,
            tversky,
            sorensen_dice,
            overlap,
            cosine,
            tanimoto,
            monge_elkan,
            bag,
            lcsseq,
            lcsstr,
            ratcliff_obershelp,
            prefix,
            postfix,
            length,
            identity,
            matrix,
            mra,
            editex,
            trigram,
            word_trigram
        )


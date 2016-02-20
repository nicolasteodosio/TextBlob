#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Downloads the necessary NLTK corpora for TextBlob.

Usage: ::

    $ python -m textblob.download_corpora

If you only intend to use TextBlob's default models, you can use the "lite"
option: ::

    $ python -m textblob.download_corpora lite

"""
import sys
import nltk

MIN_CORPORA = [
    'brown',  # Required for FastNPExtractor
    'punkt',  # Required for WordTokenizer
    'wordnet',  # Required for lemmatization
    'averaged_perceptron_tagger',  # Required for NLTKTagger
]

ADDITIONAL_CORPORA = [
    'conll2000',  # Required for ConllExtractor
    'movie_reviews',  # Required for NaiveBayesAnalyzer
]

PORTUGUESE_COOPORA = [
    'floresta',
    'mac_morpho'
    'machado'
]

ALL_CORPORA = MIN_CORPORA + ADDITIONAL_CORPORA + PORTUGUESE_COOPORA


def download_pt():
    for each in PORTUGUESE_COOPORA:
        nltk.download(each)


def download_lite():
    for each in MIN_CORPORA:
        nltk.download(each)


def download_all():
    for each in ALL_CORPORA:
        nltk.download(each)


def main():
    if 'lite' in sys.argv:
        download_lite()
    elif 'pt' in sys.argv:
        download_pt()
    else:
        download_all()
    print("Finished.")

if __name__ == '__main__':
    main()

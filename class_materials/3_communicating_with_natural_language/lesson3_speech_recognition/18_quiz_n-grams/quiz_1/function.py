test_sentences = [
    'the old man spoke to me',
    'me to spoke man old the',
    'old man me old man me',
]

def sentence_to_bigrams(sentence):
    """
    Add start '<s>' and stop '</s>' tags to the sentence and tokenize it into a list
    of lower-case words (sentence_tokens) and bigrams (sentence_bigrams)
    :param sentence: string
    :return: list, list
        sentence_tokens: ordered list of words found in the sentence
        sentence_bigrams: a list of ordered two-word tuples found in the sentence
    """
    #TODO implement
    sentence_tokens = ['<s>'] + sentence.lower().split(" ") + ['</s>']
    sentence_bigrams = []
    for i in range(1,len(sentence_tokens)):
        bigram = (sentence_tokens[i-1], sentence_tokens[i])
        sentence_bigrams.append(bigram)
    return sentence_tokens, sentence_bigrams
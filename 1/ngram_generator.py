from collections import defaultdict


def generate_ngrams(tokens, n):
    """Generate the set of n-grams for a token list"""
    if n <= 0 or n > len(tokens):
        return

    for i in range(len(tokens) - n + 1):
        yield tuple([ str(t) for t in tokens[i:i + n] ])


def generate_ngrams4str(token_sequence_str):
    """Generate the entire set of n-grams for a string"""
    ngrams_dict = defaultdict(set)
    tokens = token_sequence_str.lower().split()
    if len(tokens) == 1:
        ngrams_dict[1].add(tokens[0])
    elif len(tokens) > 1:
        for n in range(1, len(tokens)+1):
            for ngram in generate_ngrams(tokens, n):
                ngrams_dict[n].add(' '.join(ngram))
    return ngrams_dict


print(generate_ngrams4str("I love python programming"))

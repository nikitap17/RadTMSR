# Deviations from the Preregistration

## N-gram Extraction

We deviated from the preregistered CountVectorizer approach in favor of a custom coding approach for greater control over n-gram extraction and to reduce the risk of double-counting.

### CountVectorizer

- Generates unigrams, bigrams, and trigrams independently.
- Makes it difficult to trace which n-grams originate from the same segment of source text.
- Can lead to multiple overlapping matches during category assignments, resulting in potential double-counting of the same content.

### Custom approach

- Collects all n-grams (one trigram, two bigrams, three unigrams) from the same source fragment into a single list.
- Applies a negative binomial distribution to prune out n-grams with low frequencies, retaining only those that occur significantly more often than chance (p < .05).
- After pruning, either a single trigram, one or two bigrams, or a set of unigrams typically remains for each source fragment.
- Ensures that only the most meaningful n-grams are included in the analysis.

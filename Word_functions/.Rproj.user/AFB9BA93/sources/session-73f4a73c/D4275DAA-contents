---
editor_options: 
  markdown: 
    wrap: 72
---

# Topic Models

Author: ANONYMOUS 7/21/2024

## Supplementary Analysis: Subcorpora Detection

To detect whether the corpus consists of subcorpora (e.g., political
science vs. psychology texts), which require a separate anylsis, we
conducted topic modeling using latent Dirichlet allocation (Blei et al.,
2003).

The corpus for analysis 1 consisted of author-provided keywords that
were extracted by document. We further applied an exclusion filter of
methodological terms and non-substantive words and classified closely related terms into phenomena. The resulting corpus consisted of 3093 documents, 13469 keywords (3124 unique keywords).

Following van Lissa's (2022)approach, we used the term frequency/inverse
document frequency (TF-IDF) to select terms used frequently in a
document, but not used frequently in the corpus, which could therefore
be more diagnostic of subgroup membership.

We considered a range from 2-20 topics, evaluating fit based on the BIC,
and interpretability based on the entropy of the posterior
document/topic probabilities. As can be seen in Figure 1, the BICs
followed a near-perfect linearly increasing trend, and the simplest
model had the lowest BIC, indicating that no subcorpora could be
identified.

<div class="figure">

<img src="../RTMR_Output/Keywords_BIC_study1.png" alt="Analysis 1: Bayesian Information Criteria (BIC) for LDA models with 2-20 clusters." width="2100"/>

<p class="caption">

Figure 1: Analysis 1: Bayesian Information Criteria (BIC) for LDA models
with 2-20 clusters.

</p>

</div>

Congruently, all entropies were near-zero, as seen in Figure 2. Entropy reflects the separability of the extracted clusters. The low entropies observed in this analysis indicate that the posterior document/topic probabilities were effectively
uniformly distributed. Thus, no subcorpora could be identified, and we
proceeded with an analysis of the whole sample.

<div class="figure">


<img src="../RTMR_Output/Keywords_entropies_study1.png" alt="Analysis 1: Entropy values for LDA models with 2-20 clusters." width="2100"/>

<p class="caption">

Figure 2: Analysis 1: Entropy values for LDA models with 2-20 clusters.

</p>

</div>

## Analysis 2: Abstracts

The corpus for this second analysis consisted of the abstracts of the
selected articles. To perform feature extraction, we first applied the
natural language processing technique “part-of-speech tagging”
(POS-tagging), which identifies a word’s grammatical function within the
sentence context. Because our analysis sought to identify phenomena, we
retained only nouns (to capture terms like “emotion”) and adjectives (to
capture the “mental” in “mental health”). Retaining nouns and adjectives
generally helps derive more interpretable text mining models (Martin and
Johnson 2015). Finally, we used lemmatizing to reduce the retained terms to
their root form. The resulting corpus consisted of a total of 44687 keywords, 2204 unique terms in 4019 documents.

To assess the homogeneity of the corpus of abstracts, we again conducted
topic modeling.

We considered a range from 2-20 topics, evaluating fit based on the BIC,
and interpretability based on the entropy of the posterior
document/topic probabilities. As can be seen in Figure 3, the BICs 
again followed a near-perfect linearly increasing trend, and the simplest 
model had the lowest BIC, indicating that no subcorpora could be identified.

<div class="figure">

<img src="../RTMR_Output/Keywords_BIC_study2.png" alt="Analysis 2: Bayesian Information Criteria (BIC) for LDA models with 2-20 clusters." width="2100" />

<p class="caption">

Figure 3: Analysis 2: Bayesian Information Criteria (BIC) for LDA models
with 2-20 clusters.

</p>

</div>

Congruently, all entropies were near-zero, as seen in Figure 4. 
Entropy reflects the separability of the extracted clusters. The low 
entropies observed in this analysis indicate that the posterior 
document/topic probabilities were effectively uniformly distributed. 
Thus, no subcorpora could be identified, and we proceeded with an analysis 
of the whole sample.

<div class="figure">

<img src="../RTMR_Output/Keywords_entropies_study2_study2.png" alt="Analysis 2: Entropy values for LDA models with 2-20 clusters." width="2100" />

<p class="caption">

Figure 4: Analysis 2: Entropy values for LDA models with 2-20 clusters.

</p>

</div>

As before, the BICs followed a linearly increasing trend, and entropies
were near-zero. Thus, no subcorpora were identified, and we proceed with
a whole sample analysis.

# References

<div id="refs" class="references">

<div id="ref-bleiLatentDirichletAllocation2003">

Blei, David M., Andrew Y. Ng, and Michael I. Jordan. 2003. “Latent
Dirichlet Allocation.” *Journal of Machine Learning Research* 3 (Jan):
993–1022. <http://www.jmlr.org/papers/v3/blei03a>.

</div>

<div id="ref-martinMoreEfficientTopic2015">

Martin, Fiona, and Mark Johnson. 2015. “More Efﬁcient Topic Modelling
Through a Noun Only Approach.” In *Proceedings of Australasian Language
Technology Association Workshop*, 111–15.

</div>

<div id="ref-vanlissaMappingphenomenarelevant2022">

van Lissa, C. J. (2022). Mapping phenomena relevant to adolescent emotion regulation: A text-mining systematic review. Adolescent Research Review, 7(1), 127-139. https://doi.org/10.1007/s40894-021-00160-7

</div>

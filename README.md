# Japanese Feature Extractor
This project is for my Master Thesis which focuses on the extraction of linguistic complexity measures, and 
criterial features in　L2 Japanese learner texts to model language development. 

## Criterial Features
A total of 154 grammar forms across all 5 levels of the Japanese Language Proficiency Exam JLPT were coded for 
rule-based extraction 
using Spacy's matching package, as criterial features. 


## Linguistic Complexity Measures
The following complexity measures were also coded for extraction:

### Syntactic Complexity
* Average Sentence Length
* Average Clause Length
* Average Clauses per Sentence
* Average Coordinate Clauses per Sentence
* Average Subordinate Clauses per Sentence
* Mean Depedency Distance
* Mean Hierarchical Distance

### Lexical Complexity
* Corrected Type-Token Ratio
* MTLD
* Lexical Frequency Profile


### Morphological Complexity



# Abstract
This study investigates the use of linguistic complexity measures and criterial features to model proficiency levels in Japanese as a second language (L2). Using learner writings from the I-JAS corpus, this research examines whether linguistic complexity, and criterial features can reliably reflect L2 developmental progress and support interpretable proficiency classification. An Explainable Boosting Machine (EBM) was used to model the relationship between these features and proficiency labels, offering transparency in identifying which linguistic measures constribute most to level prediction.

The model achieved .38 weighted F1 score in five-class classification, well above the baseline.  Feature importance analysis revealed that mainly linguistic complexity measures such as, coordinate clauses per sentence, Morphological Complexity Index, and Lexical Frequency profiles were key predictors, although one criterial feature, passive form, was also ranked in the top 15 features. These findings align with established theories that linguistic complexity increases with proficiency, though unexpected trends-such as early subordination and continued growth in coordination-suggest the influence of instruction sequences and parser limitations.

Beyond modeling, the study also highlights developmental trajectories in complexity measures and discusses implications for language assessment, curriculum design, and learner feedback. Limitations include the use of uncorrected learner data, reliance on surface-form features, and imbalanced class sizes, especially for N1 learners. Future work can explore error-based features, discourse-level complexity, and longitudinal data collection. This research contributes to both second language acquisition theory and the development of computational tools for assessing L2 Japanese proficiency.


# アブストラクト
お後ほど
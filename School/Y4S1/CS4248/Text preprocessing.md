---
title: Text Preprocessing
---

# Regex
- **Regular expression** : A formula for specifying a set of strings
- **String** : A sequence of alphanumeric characters (letters, digits, spaces, tabs, punctuation symbols)

>[!note] Goal
>A pattern to specify search strings to search a *corpus* of texts and show the exact part of the string in a line that *first* matches a regular expression pattern


| Regex    | Match                                                          |
| -------- | -------------------------------------------------------------- |
| `*`      | Zero or more occurrences of the previous char or expression    |
| `+`      | One or more occurrences of the previous char or expression     |
| `?`      | Zero or one occurrence of the previous char or expression      |
| `{n}`    | Exactly $n$ occurrences of the previous char or expression     |
| `{n, m}` | From $n$ to $m$ occurrences of the previous char or expression |
| `{n,}`   | At least $n$ occurrences of the previous char or expression    |
| `{,m}`   | At most $m$ occurrences of the previous char or expression     |
| `.`      | One occurrence of any character                                |
| `\*`     | Asterisk                                                       |
| `\.`     | Period                                                         |
| `\?`     | Question mark                                                  |
| `\n`     | Newline                                                        |
| `\t`     | Tab                                                            |
| `[abc]`  | `a` or `b` or `bc`                                             |
| `[A-Z]`  | An uppercase letter                                            |
| `[a-z]`  | A lower case letter                                            |
| `[0-9]`  | A single digit                                                 |
| `[^A-Z]` | Not an uppercase letter                                        |

### Anchors
- `^` : start of a line
- `$` : End of a line

```
/^The dog\.$/
```
matches a line that contains only `The dog.`

### Disjunction
```
/cat|dog/
```
matches `cat` or `dog`

## Hierarchy
**From highest to lowest**:
- Parenthesis
- Counters
- Sequences/anchors
- Disjunction


#### Example in Python
```python
import re

match = re.search("i.", "uninteresting")
```

In the given text `uninteresting`, search for a span that matches `i.` (the letter `i` followed by one occurrence of any character)

---

>[!warning]  Backtracking in Regex
>- [Checking strings – avoiding catastrophic backtracking](https://community.appway.com/screen/kb/article/checking-strings-avoiding-catastrophic-backtracking-1482810891360#:%7E:text=Catastrophic%20backtracking%20is%20a%20condition,the%20string%20to%20not%20match)

# Words and Corpora
- *Corpora* is a computer-readable collections of text or speech

## Words
- **Word instances** is the *total* number of running words
- **Word types** is the number of distinct words in a corpus (or the size of the vocabulary $V$)

# Preprocessing

Every NLP task requires text preprocessing:
1. Tokenizing words
2. Normalizing words
3. Segmenting senteces

## Tokenization
>[!note]
>Segmenting running text into words and breaking of punctuation symbols as separate tokens

2 approaches: Top-down tokenization (rule-based) and bottom-up tokenization (BPE)

### Issues in tokenization
- Punctuation symbols cannot be removed naively
	- For example, dates, prices, URLs, email addresses

### Penn Treebank Tokenization standard
- Separate clitics
	- doesn’t → does n’t
	- John’s → John ‘s
- Keep hyphenated words together
- Separate out all punctuation symbols

### Top-down tokenization
A simple way to tokenize based on white spaces for languages that use space characters between words. Uses Regex.

### Byte-Pair Encoding
Use the data to tell us how to tokenize → subwords tokenization : tokens can be parts of words as well as whole words

Every unseen word can be represented as sequence of known subwords and letters → This handles out-of-vocab words and rare words.

Commonly used in LLMs

#### Learner
>[!note]
>Takes in raw training corpus and induces a vocabulary

1. Initialize vocabulary to the set of all individual *characters*
2. Repeat
	1. Choose *two* symbols that are most frequently adjacent in the training corpus
	2. Add a new merged symbol to the vocabulary
	3. Replace every adjacent 2 symbols in the corpus with the merged symbol
- Until $k$ merges have been done

>[!note]
>- Subword algorithms are run inside space separated tokens (not merged across word boundaries)
>- Add special end-of-word symbol before space in training corpus
>- Next, separate into letters

#### Segmenter
>[!note]
>Takes in a raw *test* sentence and tokenizes it according to the vocabulary

On the test data, run each merge learned from the training data greedily in the order that was learnt

---

### Properties of BPE tokens
- Includes frequent words
- Includes frequent subwords

>[!note] Morpheme
>Smallest meaning bearing unit of a language

---

## Normalization
Normalization converts text into a more convenient, standard form

>[!example] Expanding clitic contractions
>- `we're` → `we are`

## Case folding
In information retrieval, it is common to reduce all letters to lower case.

Case is also helpful to understand context:
- `US` vs `us` is important

## Lemmatization
Represent all words as their lemma (dictionary) form

## Morphology
**Morpheme** : Minimal meaning bearing unit in a language
**Morphology** : Study of the way words are built up from morphemes
**stems** : Core meaning-bearing units
**affixes** : Parts that adhere to stems, often with grammatical functions

**Example**:
- `cats` is made up of 2 morphemes: `cat` (stem) and `-s` (affix)

## Stemming
A simple version of *morphological* analysis by stripping off affixes. This reduce words to *stems* by chopping off affixes crudely

## Sentence segmentation
Punctuation marks are ambiguous. It can be:
1. Sentence boundary
2. Abbreviations
3. Numbers

Common approaches:
1. Use rules or ML to classify period as either
	1. Part of the word
	2. Sentence boundary

## Edit distance
<h1 class="libTop">nlp</h1>


## Initial Goals

Given ASCII or Unicode text, need to be able to extract successively
Sentences and from them WordForms which are a superset of Lexemes which
include Words and MultiWords

## MultiWords

MultiWords include PlaceNames and ProperNames

MultiWords are recognized sequences of words such as

* "[San Franciso ]Bay Area" aka "SF Bay Area" and
* "Joe Biden"

where the canonical form may have upper case characters and

* "data center" aka "datacenter"

where the canonical form consists of lower case letters (and possibly
digits, dashes, underscores, etc).

## Lemmas and Lexemes

Lexemes include for example

* "car" and
* "cars" as well as
* "car's",

all seen as a Lemma "car" plus some wiggly bits.

Similarly

* "child", "child's" "children" "children's"
* "run", "ran", "running"

Where the first word is the Lemma and it and the other words are Lexemes.

So "San Francisco's ambience" should be seeen as containing an inflected
form of the PlaceName as should "you can't have two San Franciscos".

## Context

Emphasis is on the ability to tokenize technical or semi-technical English

## Implementation

It's OK to wrap Natural Language Toolkit (nltk) functions at least in the
short run.

## Project Status

Skeletal.


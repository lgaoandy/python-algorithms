# Mad Libs

Mad Libs is a terminal program written in Python that intakes a mad lib file, prompts user to fill words, writes the final story

## How To Use

```t
    # Install project
    git clone https://github.com/lgaoandy/python-algorithms.git

    # Move to mad libs directory
    cd projects/mad_libs

    # Run mad_libs.py or import it as a class
    python mad_libs.py
```

## Upload Custom Mad Libs

- Add a new file in mad_libs directory
- Edit mad_libs.py to run our text file or replace mad_libs1.txt

## Basic Syntax

- Mad libs must be in a text file
- First line will be treated as title and printed in color
- Any user prompts must be covered in <> brackets (e.g. \<noun\> or \<adjective\>)

## Reoccuring Words

- Assign a number next to the prompt type (e.g. \<noun1\>)
- Program will prompt following basic rules (e.g. "Enter a noun: ") but only for the first occurring \<noun1\>
- All occurrencies of \<noun1\> will use the same input

## Example

- In text file:

```
    Sally was craving for <food1>, so she <adverb> ordered <adjective> <food1> and <drink>.
```

- Running the program:

```
    Enter a food: sushi
    Enter an adverb: quickly
    Enter an adjective: delicious
    Enter a drink: cola
```

- Program reads completed mad libs:

```
    Sally was craving for sushi, so she quickly ordered delicious sushi and cola.
```

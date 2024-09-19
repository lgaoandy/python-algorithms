# Mad Libs

A terminal program that intakes a file, prompts user to fill mad libs, writes the final story for you

## How to use

- Run on downloaded file directly (mad_libs.py) or import class
- Use the .play() method

```
    MadLib().play("mad_libs2.txt")
```

## Mad Libs Basics

- Mad libs must be in a text file
- First line will be treated as title and printed in color
- Any user prompts must be covered in <> brackets (e.g. \<noun\> or \<adjective\>)
- The program will ask "Enter a noun: " or "Enter an adjective: "

## Reoccuring words

- Assign a number next to the prompt type (e.g. \<noun1\>)
- User will be prompt, following basic rules (e.g. "Enter a noun: ") but only for the first occurring \<noun1\>
- All occurrencies of \<noun1\> will use the same prompt

#### Example

- In mad lib text file:

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

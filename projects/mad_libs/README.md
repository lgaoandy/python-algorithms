# Mad Libs

This is a terminal program that intakes a file and writes a mad libs for you replacing every word covered in <> brackets

## How to use

- Run on downloaded file directly (mad_libs.py) or import class
- Use the .play() method

```
    MadLib().play("mad_libs2.txt")
```

## Mad Libs Requirements

- Mad libs must be in a text file
- First line will be treated as title
- Any user prompts must be covered in <> brackets (e.g. \<noun\>)
- The program will ask "Enter a noun:"

## Reoccuring words

- To use the same prompt more than once, assign a number next to the prompt type (e.g. <noun1>)
- The program will ask "Enter a noun:" once for all occurrences of <noun1> (e.g. zombie)
- All <noun1> will be replaced by the user prompt (e.g. <noun1> = zombie)

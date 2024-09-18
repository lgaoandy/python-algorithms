
def load_words(filename):
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """

    # inFile: file
    inFile = open(filename, 'r')

    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        line = line.strip().lower().split()
        for word in line:
            wordlist.append(word.replace("\"", "").replace(",", "").replace("?", "").replace("(","").replace(")",""))
    return wordlist


def lyrics_to_frequencies(lyrics):
    '''
    Returns a dictionary containing every word used as its key 
    and the number of frequency they appeared in the lyrics as the value

    Lyrics, is a list containing lots of words.
    '''
    frequencies = {}
    for word in lyrics:
        if word not in frequencies.keys():
            frequencies[word] = 0
        frequencies[word] += 1
    return frequencies


def most_common_word(freqs):
    '''
    Returns the frequently found word in the dictionary
    '''
    values = freqs.values()
    best = max(values)
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words, best)


def rank_words_by_frequency(freqs):
    rankings = []

    for key in freqs.keys():
        if len(rankings) == 0:
            rankings.append({ "words": [key], "count": freqs[key] })
            continue

        index = 0
        for item in rankings:
            if freqs[key] > item["count"]:
                rankings.insert(index, { "words": [key], "count": freqs[key] })
                break
            elif freqs[key] == item["count"]:
                rankings[index]["words"].append(key)
                break
            index += 1

        if index == len(rankings):
            rankings.append({ "words": [key], "count": freqs[key] })
    return rankings


def print_lyric_analysis(filename):
    wordlist = load_words(filename + ".txt")
    rankings = rank_words_by_frequency(lyrics_to_frequencies(wordlist))

    print("Analysing", filename, "...")
    for ranking in rankings:
        if len(ranking["words"]) == 1:
            print("The word", ranking["words"][0], "appears", ranking["count"], "times.")
        elif len(ranking["words"]) == 2:
            print("The words", " and ".join(ranking["words"]), "appears", ranking["count"], "times.")
        elif ranking["count"] == 1:
            print("Everything else:", ", ".join(ranking["words"]), "appears", ranking["count"], "times.")
        else:
            print("The words", ", ".join(ranking["words"]), "appears", ranking["count"], "times.")
    print("\n")
    # (words, best) = most_common_word(lyrics_to_frequencies(wordlist))
    



print_lyric_analysis("projects/lyrics_analyzer/skater-boi")
print_lyric_analysis("projects/lyrics_analyzer/safe-and-sound")
print_lyric_analysis("projects/lyrics_analyzer/super-villain")


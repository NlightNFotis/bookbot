from collections import Counter
from typing import Dict
from string import ascii_lowercase
from os import PathLike

def count_characters(text: str) -> Dict[str, int]:
    c = Counter(text.lower())
    return c.items()

def count_words(text: str) -> int:
    return len(text.split())

def print_report(filename: PathLike) -> None:
    with open(filename) as f:
        file_contents = f.read()
    
    print(f'-- Begin report of {filename} ---')

    characters = dict(count_characters(file_contents))

    for character in characters:
        if character in ascii_lowercase:
            print(f"The '{character}' character was found {characters[character]} times")

def main():
    print_report('books/frankenstein.txt')

main()

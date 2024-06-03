import sys

def sort_on(list):
    return list[1]

def main():
    args = sys.argv[1:]
    filePath = args[0]
    wordCount = {}
    with open(filePath) as f:
        file_contents = f.read()
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(file_contents.split())} words found in the document")
    for c in file_contents.lower():
        wordCount[c] = wordCount.get(c,0)+1
    wordCount = list(wordCount.items())
    wordCount.sort(reverse=True, key=sort_on)
    for c,count in wordCount:
        if c.isalpha():
            print(f"the '{c}' character was found {count} times")
    print("--- End report ---")
    
main()

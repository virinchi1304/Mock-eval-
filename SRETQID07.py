def ladderLength(beginWord, endWord, wordList):
    if endWord not in wordList:
        return 0
    
    wordList= set(wordList)
    queue = [(beginWord, 1)]
    visited = set()
    visited.add(beginWord)

    while queue:
        current_word, current_length = queue.pop(0)


        for i in range(len(current_word)):
            for char in 'abcedfghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
                next_word = current_word[:i]+char+current_word[i+1:]

                if next_word == endWord:
                    return current_length+1
                
                if next_word in wordList and next_word not in visited:
                    visited.add(next_word)
                    queue.append((next_word, current_length+1))

                    wordList.remove(next_word)

    return 0
            
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
print(ladderLength(beginWord,endWord,wordList))
                                 
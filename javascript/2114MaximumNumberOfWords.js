/* 
A sentence is a list of words that are separated by a single space 
with no leading or trailing spaces.

You are given an array of strings sentences, where each sentences[i]
represents a single sentence.

Return the maximum number of words that appear in a single sentence

Explanation: 
- The first sentence, "alice and bob love leetcode", has 5 words in total.
- The second sentence, "i think so too", has 4 words in total.
- The third sentence, "this is great thanks very much", has 6 words in total.
Thus, the maximum number of words in a single sentence comes from the third sentence, which has 6 words.

https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/description/
*/

const mostWordsFound = function(sentences) {
    let max = 0
    for (sentence of sentences){
        let lists = sentence.split(" ")
        max = Math.max(max, lists.length)
    }
    return max
};
console.log(mostWordsFound(["alice and bob love leetcode","i think so too","this is great thanks very much"]))

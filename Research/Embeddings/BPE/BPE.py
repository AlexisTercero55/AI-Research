'''
This program implements word tokenization using byte pair encoding (BPE) as described in the paper "Neural Machine Translation of Rare Words with Subword Units" by Rico Sennrich, Barry Haddow, and Alexandra Birch.

Reference:
https://arxiv.org/pdf/1508.07909.pdf (Page 4)
'''

import re
import collections

def get_stats(vocab):
  '''
  Returns a dictionary containing pairs of adjacent symbols in words from the vocabulary along with their frequencies.

  Arguments:
  vocab -- A dictionary where keys are words and values are their frequencies.

  Returns:
  A defaultdict containing pairs of adjacent symbols as keys and their frequencies as values.
  '''
  pairs = collections.defaultdict(int)
  for word, freq in vocab.items():
    symbols = word.split()  # Split the word into individual symbols
    for i in range(len(symbols) - 1):
        # Increment the frequency count for the pair of adjacent symbols
        pairs[symbols[i], symbols[i + 1]] += freq
  return pairs

def merge_vocab(pair, v_in):
  '''
  Merges a pair of adjacent symbols in the vocabulary.

  Arguments:
  pair -- A tuple containing a pair of adjacent symbols to merge.
  v_in -- A dictionary representing the input vocabulary.

  Returns:
  A new dictionary representing the merged vocabulary.
  '''
  v_out = {}
  bigram = re.escape(' '.join(pair))  # Escape special characters in the pair
  p = re.compile(r'(?<!\S)' + bigram + r'(?!\S)')  # Compile regex pattern for substitution
  for word in v_in:
    # Substitute the pair of adjacent symbols with the merged symbol
    w_out = p.sub(''.join(pair), word)
    v_out[w_out] = v_in[word]  # Add the merged word to the output vocabulary
  return v_out

# Example vocabulary
vocab = {'l o w </w>': 5, 'l o w e r </w>': 2, 'n e w e s t </w>': 6, 'w i d e s t </w>': 3}
num_merges = 20  # Number of merge operations to perform
for i in range(num_merges):
  pairs = get_stats(vocab)  # Get pairs of adjacent symbols and their frequencies
  # Check if pairs is empty
  if not pairs:
    print("Error: Empty sequence encountered in 'pairs'.")
    break
  # try:
  best = max(pairs, key=pairs.get)  # Find the most frequent pair
  # except ValueError:
  #   print("Error: Empty sequence encountered in 'pairs':", ValueError)
  #   break
  vocab = merge_vocab(best, vocab)  # Merge the most frequent pair in the vocabulary
  print('iter:', i, best)  # Print the iteration number and the most frequent pair

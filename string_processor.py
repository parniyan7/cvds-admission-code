{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "98c1a983-e698-434f-9a29-741d8e244f61",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original text: Python is a great language. Python is also very readable and pythonic.\n",
      "Word frequency: {'python': 2, 'is': 2, 'a': 1, 'great': 1, 'language': 1, 'also': 1, 'very': 1, 'readable': 1, 'and': 1, 'pythonic': 1}\n",
      "Longest word: language.\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "String Processor\n",
    "\"\"\"\n",
    "\n",
    "from typing import List\n",
    "\n",
    "\n",
    "def count_word_frequency(text: str) -> dict:\n",
    "    \"\"\"\n",
    "    Count the frequency of each word in the given text.\n",
    "    Ignores case and punctuation for simplicity.\n",
    "    \"\"\"\n",
    "    if not text:\n",
    "        return {}\n",
    "    \n",
    "    # Clean and split text\n",
    "    cleaned = text.lower().replace(',', '').replace('.', '').replace('!', '').replace('?', '')\n",
    "    words = cleaned.split()\n",
    "    \n",
    "    frequency = {}\n",
    "    for word in words:\n",
    "        frequency[word] = frequency.get(word, 0) + 1\n",
    "    \n",
    "    return frequency\n",
    "\n",
    "\n",
    "def find_longest_word(text: str) -> str:\n",
    "    \"\"\"Return the longest word in the text.\"\"\"\n",
    "    if not text:\n",
    "        return \"\"\n",
    "    \n",
    "    words = text.split()\n",
    "    if not words:\n",
    "        return \"\"\n",
    "    \n",
    "    return max(words, key=len)\n",
    "\n",
    "\n",
    "# Example usage\n",
    "if __name__ == \"__main__\":\n",
    "    sample_text = \"Python is a great language. Python is also very readable and pythonic.\"\n",
    "    \n",
    "    word_count = count_word_frequency(sample_text)\n",
    "    longest = find_longest_word(sample_text)\n",
    "    \n",
    "    print(\"Original text:\", sample_text)\n",
    "    print(\"Word frequency:\", word_count)\n",
    "    print(\"Longest word:\", longest)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dff5ef14-4f38-4f6e-8448-3f251fb849e3",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.20"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

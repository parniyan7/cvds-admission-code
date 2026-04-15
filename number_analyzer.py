{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "0baba874-7284-48e5-8688-8b56050688c8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original data: [12.5, -3.2, 45.8, 0.0, 67.1, -12.4, 33.9]\n",
      "Statistics: {'count': 7, 'sum': 143.7, 'average': 20.5286, 'min': -12.4, 'max': 67.1, 'range': 79.5}\n",
      "Positive numbers: [12.5, 45.8, 67.1, 33.9]\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "Number Analyzer\n",
    "\"\"\"\n",
    "\n",
    "from typing import List, Dict\n",
    "\n",
    "\n",
    "def calculate_statistics(numbers: List[float]) -> Dict[str, float]:\n",
    "    \"\"\"\n",
    "    Calculate basic statistics for a list of numbers.\n",
    "    \n",
    "    This function shows clean code with proper documentation and type hints.\n",
    "    \"\"\"\n",
    "    if not numbers:\n",
    "        raise ValueError(\"The list of numbers cannot be empty\")\n",
    "    \n",
    "    total = sum(numbers)\n",
    "    count = len(numbers)\n",
    "    average = total / count\n",
    "    minimum = min(numbers)\n",
    "    maximum = max(numbers)\n",
    "    \n",
    "    # Calculate range\n",
    "    data_range = maximum - minimum\n",
    "    \n",
    "    return {\n",
    "        \"count\": count,\n",
    "        \"sum\": total,\n",
    "        \"average\": round(average, 4),\n",
    "        \"min\": minimum,\n",
    "        \"max\": maximum,\n",
    "        \"range\": data_range\n",
    "    }\n",
    "\n",
    "\n",
    "def filter_positive(numbers: List[float]) -> List[float]:\n",
    "    \"\"\"Return only positive numbers from the list.\"\"\"\n",
    "    return [num for num in numbers if num > 0]\n",
    "\n",
    "\n",
    "# Example usage\n",
    "if __name__ == \"__main__\":\n",
    "    data = [12.5, -3.2, 45.8, 0.0, 67.1, -12.4, 33.9]\n",
    "    \n",
    "    stats = calculate_statistics(data)\n",
    "    positive_numbers = filter_positive(data)\n",
    "    \n",
    "    print(\"Original data:\", data)\n",
    "    print(\"Statistics:\", stats)\n",
    "    print(\"Positive numbers:\", positive_numbers)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4dfa7de8-7f77-4b7a-960b-3f6a04be0066",
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

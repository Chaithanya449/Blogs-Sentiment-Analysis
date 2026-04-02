{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "05f44af2",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd \n",
    "import matplotlib.pyplot as plt\n",
    "from textblob import TextBlob"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "86c264df",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Data loaded! Shape: (2000, 3)\n"
     ]
    }
   ],
   "source": [
    "# Load the cleaned data \n",
    "df = pd.read_csv('Cleaned_blogs.csv')\n",
    "print(\"Data loaded! Shape:\", df.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "e536ab01",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sentiment counts:\n",
      "Sentiment\n",
      "Positive    1543\n",
      "Negative     457\n",
      "Name: count, dtype: int64\n"
     ]
    }
   ],
   "source": [
    "# Calculate sentiment polarity for each blog post\n",
    "'''TextBlob reads the text and gives a polarity score:\n",
    "polarity > 0  = Positive\n",
    "polarity = 0  = Neutral\n",
    "polarity < 0  = Negative'''\n",
    "\n",
    "def get_sentiment(text):\n",
    "    score = TextBlob(text).sentiment.polarity\n",
    "    if score > 0:\n",
    "        return 'Positive'\n",
    "    elif score < 0:\n",
    "        return 'Negative'\n",
    "    else:\n",
    "        return 'Neutral'\n",
    "    \n",
    "# Apply original text blog to get sentiment(cleaned text will fail to give accurate sentiment)\n",
    "df['Sentiment'] = df['Data'].apply(get_sentiment)\n",
    "print('Sentiment counts:')\n",
    "print(df['Sentiment'].value_counts())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "02bcd19f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Chart saved → sentiment_distribution.png\n"
     ]
    }
   ],
   "source": [
    "plt.figure(figsize=(8,5))\n",
    "\n",
    "counts = df['Sentiment'].value_counts()\n",
    "ax = counts.plot(kind='bar', color=['green','red','blue'])\n",
    "\n",
    "for i, v in enumerate(counts):\n",
    "    ax.text(i, v, v, ha='center')\n",
    "\n",
    "plt.title('Sentiment Distribution of Blogs')\n",
    "plt.xlabel('Sentiment')\n",
    "plt.ylabel('Count')\n",
    "plt.xticks(rotation=0)\n",
    "\n",
    "plt.tight_layout()\n",
    "plt.savefig('sentiment_distribution.png')\n",
    "plt.close()\n",
    "\n",
    "print(\"\\nChart saved → sentiment_distribution.png\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "0b87d3cc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sentiment distribution by category:\n",
      "\n",
      "Chart saved → sentiment_by_category_stacked.png\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<Figure size 1000x600 with 0 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Sentiment distribution by category\n",
    "print('Sentiment distribution by category:')\n",
    "Sentiment_by_category = df.groupby(['Labels','Sentiment']).size().unstack(fill_value = 0)\n",
    "plt.figure(figsize=(10,6))\n",
    "Sentiment_by_category.plot(kind = 'bar', stacked = True, color = ['red','green','blue'])\n",
    "[plt.text(i, v, v, ha='center') for i, v in enumerate(Sentiment_by_category.sum(axis=1))]\n",
    "plt.title('Sentiment distribution by category',fontweight = 'bold')\n",
    "plt.xlabel('Category')\n",
    "plt.ylabel('Count')\n",
    "plt.xticks(rotation = 45,ha = 'right')\n",
    "plt.tight_layout()\n",
    "plt.legend(title='Sentiment')\n",
    "plt.savefig('sentiment_by_category_stacked.png')\n",
    "plt.close()\n",
    "\n",
    "\n",
    "print(\"\\nChart saved → sentiment_by_category_stacked.png\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "b144b98b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Saved → blogs_with_sentiment.csv\n"
     ]
    }
   ],
   "source": [
    "df.to_csv('blogs_with_sentiment.csv', index=False)\n",
    "print(\"\\nSaved → blogs_with_sentiment.csv\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": ".venv",
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
   "version": "3.11.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

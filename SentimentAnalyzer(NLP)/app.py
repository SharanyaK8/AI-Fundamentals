from textblob import TextBlob
print("========== Customer Review Sentiment Analyzer ==========")
review = input("Enter your review: ")
analysis = TextBlob(review)

polarity = analysis.sentiment.polarity
print("\nPolarity Score:", polarity)

if polarity > 0:
    print("😊 Sentiment: Positive")

elif polarity < 0:
    print("😞 Sentiment: Negative")

else:
    print("😐 Sentiment: Neutral")
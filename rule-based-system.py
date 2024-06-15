import re

def sentiment_analysis(text):
    # Define positive and negative patterns using regular expressions
    positive_patterns = [
        r"\b(?:good|great|excellent|awesome|happy)\b",
        r"\b(?:love|like)\b"
    ]
    
    negative_patterns = [
        r"\b(?:bad|terrible|awful|horrible|sad)\b",
        r"\b(?:hate|dislike)\b"
    ]
    
    # Count occurrences of positive and negative patterns in the text
    positive_count = sum(1 for pattern in positive_patterns if re.search(pattern, text, flags=re.IGNORECASE))
    negative_count = sum(1 for pattern in negative_patterns if re.search(pattern, text, flags=re.IGNORECASE))
    
    # Determine sentiment based on counts
    if positive_count > negative_count:
        return "Positive"
    elif negative_count > positive_count:
        return "Negative"
    else:
        return "Neutral"

# Example usage:
text1 = "I love this product, it's great!"
text2 = "This movie was terrible, I hated it."
text3 = "The weather today is neither good nor bad."

print(text1,":",sentiment_analysis(text1))  # Output: Positive
print(text2,":",sentiment_analysis(text2))  # Output: Negative
print(text3,":",sentiment_analysis(text3))  # Output: Neutral

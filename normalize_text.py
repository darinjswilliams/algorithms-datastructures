import numpy as np
import re

def normalize_text(texts):
    """
    Normalizes a batch of text strings.

    Args:
        texts (np.ndarray): Raw input strings.

    Returns:
        tuple[np.ndarray, float]: Normalized strings and normalization rate.
    """

    #Recount total amount of characters
    total_original = 0  
    total_removed = 0 

    normalize= []

    for t in texts:

        original_length = len(t)
        
        #lower the text
        t = t.lower()
    
        #create translation table to remove punctuation
        t = t.translate(str.maketrans("", "", '.,!?;:\'"()-'))
               
        #remove any sequence of whitespaces (spaces, tabs, newlines) with a single space
        t = re.sub(r"\s+", " ", t)
    
        #trim leading and trailing spaces
        t = t.strip()

        #append string
        normalize.append(t)
        
        #final Length
        final_length = len(t)
    
        # Count total original and final length
        total_original += original_length
        total_removed += (original_length - final_length)

    #normalize rate
    r = total_removed/total_original

    return np.array(normalize), r

# Example Usage
texts = [
  "Hello,   WORLD!!\nNLP  is fun.",
  " Text-normalization... (in NLP) "
]

result = normalize_text(np.array(texts))
print(result)
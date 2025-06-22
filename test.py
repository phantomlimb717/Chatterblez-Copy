import re
import string

# Define only "speakable" punctuation - ones that affect how text is read aloud
SPEAKABLE_PUNCT = '.!?,:;-\'"'
ESCAPED_SPEAKABLE = re.escape(SPEAKABLE_PUNCT)

# All punctuation for removal purposes
ALL_PUNCT = re.escape(string.punctuation)

# Compiled regex patterns
remove_unwanted = re.compile(rf'[^\w\s{ALL_PUNCT}]+')
remove_unspeakable = re.compile(rf'[{re.escape("".join(set(string.punctuation) - set(SPEAKABLE_PUNCT)))}]+')
normalize_quotes = re.compile(r'[""''`]')  # Smart quotes and backticks to normalize
collapse_punct = re.compile(rf'[{ESCAPED_SPEAKABLE}][\s{ESCAPED_SPEAKABLE}]*(?=[{ESCAPED_SPEAKABLE}])')

def clean_string(text):
    """
    Remove non-alphanumeric chars, keep only speakable punctuation,
    normalize quotes, and collapse multiple punctuation to keep only the last one.
    """
    # First, remove all characters that aren't alphanumeric, whitespace, or punctuation
    step1 = remove_unwanted.sub('', text)
    
    # Normalize smart quotes and backticks to standard quotes
    step2 = normalize_quotes.sub(lambda m: '"' if m.group() in '""' else "'", step1)
    
    # Remove unspeakable punctuation (symbols like @#$%^&*()[]{}|\ etc.)
    step3 = remove_unspeakable.sub('', step2)
    
    # Then collapse sequences of speakable punctuation (with optional whitespace) to keep only the last one
    step4 = collapse_punct.sub('', step3)
    
    # Clean up any remaining multiple whitespace
    result = re.sub(r'\s+', ' ', step4).strip()
    
    return result

# Alternative approach
def clean_string_v2(text):
    """
    Alternative approach - directly keep only alphanumeric, whitespace, and speakable punctuation
    """
    # Normalize smart quotes first
    cleaned = normalize_quotes.sub(lambda m: '"' if m.group() in '""' else "'", text)
    
    # Remove everything except alphanumeric, whitespace, and speakable punctuation
    cleaned = re.sub(rf'[^\w\s{ESCAPED_SPEAKABLE}]+', '', cleaned)
    
    # Find sequences of punctuation/whitespace and keep only the last punctuation
    cleaned = re.sub(rf'[{ESCAPED_SPEAKABLE}\s]*([{ESCAPED_SPEAKABLE}])(?=\s*$|[^\s{ESCAPED_SPEAKABLE}])', r'\1', cleaned)
    
    # Clean up whitespace
    return re.sub(r'\s+', ' ', cleaned).strip()

# Test examples
if __name__ == "__main__":
    test_strings = [
        "Hello!? World",
        "What- ? ! is this",
        "Test@#$%^&*()string!!!",
        "Multiple   spaces    and...punctuation???",
        "Mix3d ch@rs & punct!!!"
    ]
    
# Test examples
if __name__ == "__main__":
    test_strings = [
        "Hello!? World",
        "What- ? ! is this",
        "Test@#$%^&*()string!!!",
        "Multiple   spaces    and...punctuation???",
        "Mix3d ch@rs & punct!!!",
        "Email: user@domain.com, visit https://site.org",
        "Price: $19.99 (20% off!)",
        "Code: {variable} = [1, 2, 3]",
        "Don't use \"smart quotes\" or \'other quotes\' or `backticks\`",
        "He said: \"I can't believe it\'s working!\"",
        "She's won't they're isn't"
    ]
    
    print(f"Speakable punctuation kept: {SPEAKABLE_PUNCT}")
    print("\nMain approach:")
    for test in test_strings:
        result = clean_string(test)
        print(f"'{test}' -> '{result}'")
    
    print("\nAlternative approach:")
    for test in test_strings:
        result = clean_string_v2(test)
        print(f"'{test}' -> '{result}'")
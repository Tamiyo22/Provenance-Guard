"""
Signal two: the style signal. ← YOU BUILD THIS IN MILESTONE 4

Signal one reads the text for meaning. This one measures it *as text* — the
shape of it, without understanding a word.

Three measures are stubbed below because the brief names those three. They are
stubs, not implementations: what they compute is yours, and so is how you
combine them.

    sentence_length_spread   do sentences vary in length, or march in step?
    type_token_ratio         how much of the vocabulary repeats?
    punctuation_density      how much punctuation, and how varied?

Why these might differ between human and AI writing: generated prose tends
toward even, mid-length sentences and a narrower band of vocabulary, because
that's what "most likely next word" produces on average. Human writing is
lumpier — a three-word sentence next to a forty-word one.

⚠️ **The blind spot, which you have to name in Milestone 1.**

This signal cannot read. It has no idea what the text says. Anything that
changes the shape without changing the substance moves it — adding typos,
breaking up sentences, pasting in a quotation. That is a very cheap thing for
someone to do on purpose, and unit 8's attack set will do it to you.

Build each function on its own and call it from a terminal before you wire
anything together:

    python stylometry.py "some text to look at"
"""

import re
import statistics


def sentences(text: str) -> list[str]:
    """Split into sentences. Rough and good enough — given to you."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Split into lowercase words, punctuation stripped. Given to you."""
    return re.findall(r"[a-z0-9']+", text.lower())


# ── The three measures — YOU BUILD THESE ─────────────────────────────────────

def sentence_length_spread(text: str) -> float:
    """
    How much sentence length varies. ← TODO

    Returns:
        A float. Decide yourself what scale it's on and which direction means
        "more human" — then write that down, because your combining rule
        depends on knowing it.

    A hint on what you're reaching for: the standard deviation of sentence
    lengths, probably divided by the mean so a long text and a short one are
    comparable. `statistics.stdev` is imported for you.

    Watch the edge case: a one-sentence submission has no spread at all, and
    `stdev` raises on fewer than two values. Decide what that should return
    before the attack set decides for you.
    """

    # Count the number of words in each sentence.
    lengths = [len(words(sentence)) for sentence in sentences(text)]

    # Fewer than two sentences cannot provide a meaningful spread.
    if len(lengths) < 2:
        return 0.0

    # Avoid dividing by zero when sentences contain no words.
    mean_length = statistics.mean(lengths)
    if mean_length == 0:
        return 0.0

    # Coefficient of variation:
    # standard deviation divided by the average sentence length.
    spread = statistics.stdev(lengths) / mean_length

    return round(spread, 4)


def type_token_ratio(text: str) -> float:
    """
    Unique words over total words. ← TODO

    Returns:
        A float between 0 and 1. Higher means more varied vocabulary.

    Worth knowing before you rely on it: this measure falls as text gets
    longer, because common words repeat. Two texts of different lengths aren't
    directly comparable on it, and if your test inputs vary a lot in length,
    that alone can look like a signal.
    """

    # Split the text into lowercase words.
    tokens = words(text)

    # Avoid division by zero if the text contains no words.
    if not tokens:
        return 0.0

    # Count unique words and divide by the total word count.
    unique_words = len(set(tokens))
    total_words = len(tokens)

    ratio = unique_words / total_words

    return round(ratio, 4)


def punctuation_density(text: str) -> float:
    """
    How much punctuation, relative to length. ← TODO

    Returns:
        A float. Whether you count all punctuation or only some kinds — commas,
        semicolons, dashes — is a real choice. Semicolons and em dashes are
        more interesting than full stops, because they vary more between
        writers.
    """

    # Count the words in the text.
    total_words = len(words(text))

    # Avoid dividing by zero.
    if total_words == 0:
        return 0.0

    # Count punctuation marks, including common sentence punctuation.
    punctuation_marks = re.findall(r"[.,;:!?\-—–]", text)
    punctuation_count = len(punctuation_marks)

    # Calculate punctuation marks per word.
    density = punctuation_count / total_words

    return round(density, 4)


# ── Combining them ───────────────────────────────────────────────────────────

def style_signal(text: str) -> float:
    """
    The style signal as a 0–1 score. **Higher means more likely AI.** ← TODO

    Combine your three measures into one number. Same direction as
    `detector.model_signal`, so that `scoring.combine_signals` can treat them
    the same way — if one of your signals runs backwards, everything above it
    is wrong in a way that's hard to see.

    Two things to decide and write down:

      1. Which direction each measure points. Low spread means more AI-ish, so
         it needs flipping. Work out which of your three need that.
      2. How to get each onto a comparable scale. A raw type-token ratio sits
         between 0 and 1; a raw punctuation count doesn't. Adding them
         unscaled means whichever has the bigger numbers wins by default.

    Test it on the four calibration inputs from Milestone 4 — clearly AI,
    clearly human, plain conventional human writing, lightly-edited AI — before
    you trust it. Plain and ordinary, not formal: formal prose reads as *human*
    to signal one, and it is plain writing that gets accused.
    """

    # Get the three stylometry measurements.
    spread = sentence_length_spread(text)
    vocabulary = type_token_ratio(text)
    punctuation = punctuation_density(text)

    # Short texts do not provide enough evidence for reliable
    # stylometric analysis. Return a neutral score.
    if len(words(text)) < 30 or len(sentences(text)) < 2:
        return 0.5

    # Convert each measurement into a 0–1 score.
    # Higher values should indicate more AI-like writing.

    # Lower sentence-length variation is treated as more AI-like.
    spread_score = 1.0 - min(spread, 1.0)

    # Lower vocabulary diversity is treated as more AI-like.
    vocabulary_score = 1.0 - vocabulary

    # Use a conservative punctuation heuristic.
    # Density of 0.2 or higher maps to zero on this component.
    punctuation_score = 1.0 - min(punctuation / 0.2, 1.0)

    # Combine the three scores using weighted averaging.
    combined = (
        0.40 * spread_score
        + 0.35 * vocabulary_score
        + 0.25 * punctuation_score
    )

    # Keep the final score between 0 and 1.
    return round(max(0.0, min(combined, 1.0)), 4)


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")
    print(f"sentence_length_spread   {sentence_length_spread(text)}")
    print(f"type_token_ratio         {type_token_ratio(text)}")
    print(f"punctuation_density      {punctuation_density(text)}")
    print(
        f"style_signal             {style_signal(text)}   (higher = more likely AI)")
    print("\nAll zeros? These are stubs — Milestone 4 is where you build them.")

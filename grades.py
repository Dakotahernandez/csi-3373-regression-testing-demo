"""Grade calculator: turns a numeric score (0-100) into a letter grade."""

# Minimum score needed for each letter, highest first.
CUTOFFS = [
    (90, "A"),
    (80, "B"),
    (70, "C"),
    (60, "D"),
]


def meets_cutoff(score, cutoff):
    """Return True if the score is high enough for this cutoff."""

    # return score > cutoff

    return score >= cutoff


def letter_grade(score):
    """Return the letter grade (A, B, C, D, or F) for a score from 0 to 100."""
    if score < 0 or score > 100:
        raise ValueError("score must be between 0 and 100")

    for cutoff, letter in CUTOFFS:
        if meets_cutoff(score, cutoff):
            return letter
    return "F"

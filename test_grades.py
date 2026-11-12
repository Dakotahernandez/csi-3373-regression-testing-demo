"""
Run:  pytest -v
"""

import pytest

from grades import letter_grade


# Typical scores in the middle of each grade range.
@pytest.mark.parametrize(
    "score, expected",
    [
        (95, "A"),
        (85, "B"),
        (75, "C"),
        (65, "D"),
        (30, "F"),
    ],
)
def test_typical_scores(score, expected):
    assert letter_grade(score) == expected


# Scores exactly on a cutoff. These are where bugs like to hide.
@pytest.mark.parametrize(
    "score, expected",
    [
        (90, "A"),
        (80, "B"),
        (70, "C"),
        (60, "D"),
    ],
)
def test_exact_cutoffs(score, expected):
    assert letter_grade(score) == expected


# Scores just below a cutoff.
@pytest.mark.parametrize(
    "score, expected",
    [
        (89.9, "B"),
        (79.9, "C"),
        (69.9, "D"),
        (59.9, "F"),
    ],
)
def test_just_below_cutoffs(score, expected):
    assert letter_grade(score) == expected


def test_perfect_and_zero():
    assert letter_grade(100) == "A"
    assert letter_grade(0) == "F"


@pytest.mark.parametrize("bad_score", [-1, 101])
def test_out_of_range_rejected(bad_score):
    with pytest.raises(ValueError):
        letter_grade(bad_score)

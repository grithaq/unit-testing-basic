from src.intro import max


def test_max():
    assert max(1, 2) == 2
    assert max(2, 1) == 2
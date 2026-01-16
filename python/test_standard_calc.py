from standard_calc import bound_to_180, is_angle_between


""" Tests for bound_to_180() """


def test_bound_basic1():
    assert bound_to_180(0) == 0


def test_bound_wrap_positive():
    assert bound_to_180(360) == 0
    assert bound_to_180(720) == 0


def test_bound_wrap_negative():
    assert bound_to_180(-360) == 0
    assert bound_to_180(-720) == 0


def test_bound_edges():
    assert bound_to_180(180) == -180
    assert bound_to_180(-180) == -180


def test_bound_general():
    assert bound_to_180(200) == -160
    assert bound_to_180(-190) == 170


""" Tests for is_angle_between() """


def test_between_basic1():
    assert is_angle_between(0, 1, 2)


def test_between_simple_false():
    assert not is_angle_between(0, 3, 2)


def test_between_wraparound_true():
    assert is_angle_between(350, 0, 10)


def test_between_wraparound_false():
    assert not is_angle_between(350, 180, 10)


def test_between_reflex_case():
    assert not is_angle_between(45, 90, 270)

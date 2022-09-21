from .trailblaze import _RunningMean


def test_running_mean():
    x = [0, 1, 2, 3, 4]
    rm = _RunningMean()
    for val in x:
        rm.update(val)
    assert abs(rm.mean - 2) < 1e-6

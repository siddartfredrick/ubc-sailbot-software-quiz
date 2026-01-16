def bound_to_180(angle):

    """
    Bounds the provided angle between [-180, 180) degrees.

    We first add 180° to shift the angle into a 0–360° coordinate system.
    Then we take modulo 360 to find where that angle lies on the unit circle.
    Finally, we subtract 180° to shift back into the −180° to +180° coordinate system.

    """

    wrapped = (angle + 180) % 360
    wrapped = wrapped - 180
    return wrapped


def is_angle_between(first_angle, middle_angle, second_angle):
    """Determines whether an angle is between two other angles.

    e.g.)
        is_angle_between(0, 45, 90) = True
        is_angle_between(45, 90, 270) = False

    Args:
        first_angle (float): The first bounding angle in degrees.
        middle_angle (float): The angle in question in degrees.
        second_angle (float): The second bounding angle in degrees.

    Returns:
        bool: True when `middle_angle` is not in the reflex angle of `first_angle` and `second_angle`, false otherwise.
    """

    a = first_angle % 360
    b = middle_angle % 360
    c = second_angle % 360

    def CCW_dist(x):
        return (x-a) % 360
    
    dist_ac = CCW_dist(c)
    dist_ab = CCW_dist(b)
    if dist_ac <= 180:
        return dist_ab <= dist_ac

    return dist_ab >= dist_ac

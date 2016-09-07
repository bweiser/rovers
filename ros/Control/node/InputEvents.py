class InputEvents():
    """Constants which identify joystick directions and button presses"""

    FORWARD          = 'Forward'
    FORWARD_RELEASE  = 'Neutral'
    BACKWARD         = 'Backward'
    BACKWARD_RELEASE = 'Neutral'
    LEFT             = 'Left'
    LEFT_RELEASE     = 'Neutral'
    RIGHT            = 'Right'
    RIGHT_RELEASE    = 'Neutral'

    START            = 'Start'
    START_RELEASE    = 'StartRelease'
    TOP              = 'GypsumPress'
    TOP_RELEASE      = 'Gypsum'
    MIDDLE           = 'MudPress'
    MIDDLE_RELEASE   = 'Mud'
    BOTTOM           = 'FossilPress'
    BOTTOM_RELEASE   = 'Fossil'

    GENERIC_RELEASE  = 'Release'

    UNKNOWN_EVENT    = 'Unknown'

    buttonPresses = [
        START,
        TOP,
        MIDDLE,
        BOTTOM
        ]
    buttonReleases = [
        START_RELEASE,
        TOP_RELEASE,
        MIDDLE_RELEASE,
        BOTTOM_RELEASE,
        GENERIC_RELEASE
        ]
    joystickPresses = [
        FORWARD,
        BACKWARD,
        LEFT,
        RIGHT
        ]
    joystickReleases = [
        FORWARD_RELEASE,
        BACKWARD_RELEASE,
        LEFT_RELEASE,
        RIGHT_RELEASE,
        GENERIC_RELEASE
        ]

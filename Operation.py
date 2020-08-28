from enum import Enum
class Operation(Enum):
    """
    An enum for each type of operation that can be performed on a column
    """
    NOT = 1
    AND = 2
    OR = 3
    IMPLIES = 4
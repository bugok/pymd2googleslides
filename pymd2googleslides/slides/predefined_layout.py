from enum import Enum, auto


class PredefinedLayout(Enum):
    """
    https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations/request?authuser=0#LayoutReference
    """

    PREDEFINED_LAYOUT_UNSPECIFIED = auto()
    BLANK = auto()
    CAPTION_ONLY = auto()
    TITLE = auto()
    TITLE_AND_BODY = auto()
    TITLE_AND_TWO_COLUMNS = auto()
    TITLE_ONLY = auto()
    SECTION_HEADER = auto()
    SECTION_TITLE_AND_DESCRIPTION = ()
    ONE_COLUMN_TEXT = auto()
    MAIN_POINT = auto()
    BIG_NUMBER = auto()

from typing import Tuple, Dict, List


def tableize(headings:List[str], data:List) -> None:

    """
    Prints headings and data as a table with borders.
    Arguments:
        headings: iterable of heading texts
        data: iterable of data
    """

    col_widths = __calc_col_widths(headings, data)
    borders = __create_border_strings(col_widths) 

    __print_headings(headings, col_widths, borders)

    __print_data(data, col_widths, borders)


def __calc_col_widths(headings:List[str], data:List) -> Tuple[int]:

    widths = []

    # add widths of headings    
    for heading in headings:

        widths.append(len(heading))

    # overwrite current widths with data widths if longer
    for row in data:

        for index, datum in enumerate(row):

            if len(str(datum)) > widths[index]:

                widths[index] = len(datum)

    return tuple(widths)


def __create_border_strings(col_widths:Tuple[int]) -> Dict[str, str]:

    # first characters in each row type
    heading_top_border = ["╒"]
    heading_bottom_border = ["╞"]
    data_top_border = ["├"]
    data_bottom_border = ["└"]
    
    for index, width in enumerate(col_widths):

        # add characters for borders sections above/below data
        heading_top_border.append("═" * width)
        heading_bottom_border.append("═" * width)
        data_top_border.append("─" * width)
        data_bottom_border.append("─" * width)

        # intermediate border interesctions
        if index < len(col_widths) - 1:
            heading_top_border.append("╤")
            heading_bottom_border.append("╪")
            data_top_border.append("┼")
            data_bottom_border.append("┴")

    # ending border interesctions
    heading_top_border.append("╕")
    heading_bottom_border.append("╡")
    data_top_border.append("┤")
    data_bottom_border.append("┘")

    # assemble into a dictionary
    return {"heading_top_border": "".join(heading_top_border),
            "heading_bottom_border": "".join(heading_bottom_border),
            "data_top_border": "".join(data_top_border),
            "data_bottom_border": "".join(data_bottom_border)}


def __format_heading(heading: str, width: int) -> str:

    # left-align heading text and pad to column width
    return f"{heading:<{width}}"


def __format_data(datum, width: int) -> str:

    """
    strings are left aligned
    other types are right aligned
    """

    data_str = str(datum)
    
    fmt_str = ""

    if isinstance(datum, str):
        fmt_str = f"{data_str:<{width}}"
    else:
        fmt_str = f"{data_str:>{width}}"                

    return fmt_str


def __print_headings(headings: List[str], col_widths: Tuple[int], borders: Dict[str, str]) -> None:
    
    heading_row = ["│"]

    for index, heading in enumerate(headings):

        heading_row.append(__format_heading(heading, col_widths[index]))          
        heading_row.append("│")

    print(borders["heading_top_border"])
    print("".join(heading_row))
    print(borders["heading_bottom_border"])


def __print_data(data: List, col_widths: Tuple[int], borders: Dict[str, str]) -> None:

    row_count = len(data)

    for rowindex, rowdata in enumerate(data):

        data_row = ["│"]

        for index, datum in enumerate(rowdata):

            data_row.append(__format_data(datum, col_widths[index]))
            data_row.append("│")

        print("".join(data_row))

        if rowindex < row_count - 1:
            print(borders["data_top_border"])
        else:
            print(borders["data_bottom_border"])
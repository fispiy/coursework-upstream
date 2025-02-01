"""
CMSC 14100
Winter 2025
Homework #5

We will be using anonymous grading, so please do NOT include your name
in this file

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URL of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

from math import log

# Exercise 1
def extract_column(table, column):
    """
    Produce a list of values in the given column from the given table.

    Input:
        table (list[list]): table of data
        column (str): name of column

    Output (list): list of column data
    """
    ### YOUR CODE HERE
    return None


# Exercise 2
def is_valid_table(table):
    """
    Check whether the table is a valid table.

    Input:
        table (list[list]): table of data

    Output (bool): True if table is valid, False otherwise
    """
    ### YOUR CODE HERE
    return None


# Exercise 3
def filter_exact(table, column, value, negate=False):
    """
    Produce a new table that consists of the rows that
    * contain value in column, if negate is False.
    * do not contain value in column, if negate is True.

    negate is False by default.

    Input:
        table (list[list]): table of data
        column (str): column name
        value (any): value to be matched
        negate (bool): negate match if True (False by default)

    Output (list[list]): table of rows with value in column
    """
    ### YOUR CODE HERE
    return None


# Exercise 4
def select_columns(table, columns):
    """
    Produce a new table that consists of the given columns from the given table.

    Input:
        table (list[list]): table of data
        columns (list[str]): list of column names

    Output (list[list]): new table with given columns
    """
    ### YOUR CODE HERE
    return None


# Exercise 5
def add_row_sum_column(table, columns, name):
    """
    Extend the table with a new column with given name that contains the sum
    of the values in the specified columns for each row.

    Input:
        table (list[list]): table of data
        column (list[str]): list of column names
        name (str): name of new column

    Output (None): None, mutates table
    """
    ### YOUR CODE HERE
    return None


# Exercise 6
def add_running_mean_column(table, column, name):
    """
    Extend the table with a new column with given name that contains the 
    running mean of the values in the specified column. The running mean is the
    mean of the values in the column of the current and previous rows.

    Input:
        table (list[list]): table of data
        column (str): column name
        name (str): name of new column

    Output (None): None, mutates table
    """
    ### YOUR CODE HERE
    return None


# Exercise 7
def add_difference_column(table, column, name, start_from=0):
    """
    Extend the table with a new column with given name that contains the 
    difference of the value in the column of the current row with the value of
    the value in the row above in the same column.

    Input:
        table (list[list]): table of data
        column (str): column name
        name (str): name of new column
        start_from (float): initial value

    Output (None): None, mutates table
    """
    ### YOUR CODE HERE
    return None


# Exercise 8
def inverse_document_frequency(table):
    """
    Given a document-term matrix as a table, compute the inverse document 
    frequency (idf) of the terms, relative to the table.

    Input:
        table (list[list]): table representing the document-term matrix

    Output (list[tuple[str,float]]): list of (term, idf) pairs
    """
    ### YOUR CODE HERE
    return None

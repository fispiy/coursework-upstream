'''
Common helper functions for autograders.
'''

import pytest

def add_quotes_if_needed(val):
    """ Add quotes to a value to be printed """
    return f"'{val}'" if isinstance(val, str) else f"{val}"

def gen_recreate_commands(module, commands):
    '''
    Generate a message that can be used to recreate a test in ipython3
    that relies on a series of commands to setup the test.

    Parameters
        - module: the name of the module containing the function
        - commands: commands needed to recreate the test

    Returns
        - a string containing the recreate message
    '''
    commands_tabbed = \
        [f"  {p}" if not p.startswith("  ") else f"{p}" for p in commands]
    commands_tabbed_str = "\n".join(commands_tabbed)
    recreate_msg = (f"\n\nTo recreate this test in ipython3, run:\n"
                    f"  import {module}\n"
                    f"{commands_tabbed_str}\n")

    return recreate_msg

def gen_recreate_msg(module, function, *params):
    '''
    Generate a message that can be used to recreate a test in ipython3.

    Parameters
        - module: the name of the module containing the function
        - function: the name of the function
        - params: the parameters passed to the function

    Returns
        - a string containing a message that can be used to recreate the test
    '''
    params = [add_quotes_if_needed(p) for p in params]
    params_str = ", ".join(params)

    recreate_msg = (f"\n\nTo recreate this test in ipython3\n"
                    "and recreate the actual value, run:\n"
                    f"  import {module}\n"
                    f"  {module}.{function}({params_str})\n")

    return recreate_msg

def fail_and_augment_recreate_unexpected_exception(recreate_msg, exception):
    '''
    Augment the recreate message with information about an unexpected exception.

    Parameters
        - recreate_msg: the recreate message generated by gen_recreate_msg
        - exception: the exception that was raised

    Returns
        - a string containing the augmented recreate message
    '''
    new_msg = (f"\n\nAn unexpected exception {type(exception).__name__,} was "
               f"raised that is causing your code to fail:\n  {exception}\n"
               f"This is likely due to a bug in your code.\n{recreate_msg}")
    pytest.fail(new_msg)

def check_type(actual, expected, checking_return_val=True):
    '''
    Generate error message if the actual value has the wrong type. Return None
    if no problem is found.

    Parameters
        - actual: the actual value returned by the function being tested
        - expected: the expected type of the actual value

    Returns
        - None if no problem is found, otherwise an error message
    '''
    actual_type = type(actual)
    expected_type = type(expected)

    if checking_return_val:
        msg = (f"The function returned a value of the wrong type.\n"
               f"  Expected return type: {expected_type.__name__}\n"
               f"  Actual return type: {actual_type.__name__}")               
    else:
        msg = (f"The actual value has the wrong type.\n"
               f"  Expected type: {expected_type.__name__}\n"
               f"  Actual type: {actual_type.__name__}")
    
    if isinstance(actual, expected_type):
        return None
    else:
        return msg


def check_number(actual):
    '''
    Generate error message if the actual value is not a number. Return None if
    no problem is found.

    Parameters
        - actual: the actual value returned by the function being tested. there
        is no expected value because we are only checking that the actual value
        is an int or a float.

    Returns
        - None if no problem is found, otherwise an error message
    '''
    actual_type = type(actual)

    msg = (f"\n\nThe function returned a value of the wrong type.\n"
           f"  Expected return type: an integer or a float.\n"
           f"  Actual return type: {actual_type.__name__}.")

    if isinstance(actual, (int, float)):
        return None
    else:
        return msg


def check_equals(actual, expected):
    '''
    Generate an error if the actual and expected values are not
    equal. If we expect a float, check that the actual value is close enough.
    Return None if no problem is found.

    Parameters
        - actual: the actual value returned by the function being tested
        - expected: the expected value

    Returns
        - None if no problem is found, otherwise an error message
    '''
    msg = ("The actual and expected values do not match\n"
           f"  Expected: {add_quotes_if_needed(expected)}\n"
           f"  Actual: {add_quotes_if_needed(actual)}")

    if isinstance(expected, float):
        if pytest.approx(expected) == actual:
            return None
        else:
            return msg
    else:
        if actual == expected:
            return None
        else:
            return msg

def check_none(actual, expected):
    '''
    If expected is None, generate an error if the actual value is not None.
    If expected is not None, generate error message if the actual value is None. 
    Return None if no problem is found.

    Parameters
        - actual: the actual value returned by the function being tested

    Returns
        - None if no problem is found, otherwise an error message
        - expected: the expected value

    Notes:
        Previously check_not_none(actual) and check_expected_none(actual)
    '''
    # When we expect a result of None
    if expected is None:
        msg = (f"\n\nThe function returned a value other than the "
               f"expected value: None.")
        if actual is not None:
            return msg
        else:
            return None

    # When we expect a result of not None
    msg = ("\n\nThe function returned None when a value "
           "other than None was expected.\n"
           "Common sources of this problem include:\n"
           "  - forgetting to replace the None placeholder in return statements,\n"
           "  - including a print statement rather than a return statement, and\n"
           "  - forgetting to include a return statement.")
    if actual is None:
        return msg
    else:
        return None

def check_result(actual, expected):
    '''
    Comprehensive check of the actual value returned by a function. Return None
    if no problem is found, otherwise an error message.
    
    Parameters
        - actual: the actual value returned by the function being tested
        - expected: the expected value
        
    Returns
        - None if no problem is found, otherwise an error message
    '''
    # Checking for None values
    msg = check_none(actual, expected)
    if expected is None or msg is not None:
        return msg

    # Checking that the actual value is the correct type
    msg = check_type(actual, expected)
    if msg is not None:        
        return "\n\n" + msg

    msg = check_equals(actual, expected)
    if msg is not None:
        return "\n\n" + msg
    return None

def __check_dict_keys(actual, expected):
    '''
    Generate an error if the keys in the actual and expected dictionaries do
    not match. Return None if no problem is found.

    Parameters
        - actual: the actual dictionary returned by the function being tested
        - expected: the expected dictionary

    Returns
        - None if no problem is found, otherwise an error message
    '''
    # generate an error if the keys do not match, None otherwise
    rmsg = ("  A key {} appears in the expected result\n"
            "  and is missing from the actual result.")
    for expected_key in expected:
        if expected_key not in actual:
            return rmsg.format(add_quotes_if_needed(expected_key))
    
    rmsg2 = ("  A key {} appears in the actual result\n"
             "  that does not appear in the expected result.")
    for actual_key in actual:
        if actual_key not in expected:
            return rmsg2.format(add_quotes_if_needed(actual_key))

    # no error: the keys match
    return None


def check_list_unmodified(param_name, before, after):
    '''
    Generate an error if a list was modified when modifications are
    disallowed.

    Parameters
        - param_name: the name of the parameter being checked
        - before: the value of the parameter before the function was called
        - after: the value of the parameter after the function was called
    
    Returns
        - None if no problem is found, otherwise an error message
    '''
    msg = f'\n\nYou modified the parameter {param_name}, which is not allowed.\n'
    msg += f'  Value before your code: {before}\n'
    msg += f'  Value after your code:  {after}'

    if before != after:
        return msg
    else:
        return None

        
def __check_list_length(actual, expected, desc=""):
    '''
    Generate an error if the actual list is not the same length as the expected
    list. Return None if no problem is found.

    Parameters
        - actual: the actual list returned by the function being tested
        - expected: the expected list
        - desc: a description of the list being checked
    
    Returns
        - None if no problem is found, otherwise an error message
    '''
    if isinstance(actual, list):
        t_str = "list"
    elif isinstance(actual, tuple):
        t_str = "tuple"
    elif isinstance(actual, str):
        t_str = "str"
    else:
        assert("Did not expect to get here")    
    if desc:
        msg = (f"The actual length ({len(actual)}) of the {t_str} of {desc} "
               f"does not match the expected length ({len(expected)}) of "
               f"the list of {desc}")
    else:
        msg = (f"The actual length ({len(actual)}) does not match the "
               f"expected length ({len(expected)}).")

    if len(actual) != len(expected):
        msg += f"\nExpected {t_str}: {expected}\nActual {t_str}: {actual}"
        return msg

    else:
        return None


def check_1d_iterable(actual, expected):
    '''
    This function is used to check tuples and lists. Generates an error if the 
    actual iterable is not the same as the expected. Return None if no problem 
    is found.

    Parameters
        - actual: the actual iterable returned by the function being tested
        - expected: the expected iterable

    Returns
        - None if no problem is found, otherwise an error message
    '''
    # Checking for None values
    msg = check_none(actual, expected)
    if expected is None or msg is not None:
        return msg

    # Check the type of actual value
    msg = check_type(actual, expected)
    if msg is not None:
        return "\n\n" + msg

    # Check that the actual value is the correct length
    msg = __check_list_length(actual, expected)
    if msg is not None:
        return "\n\n" + msg

    if isinstance(actual, list):
        t_str = "list"
    elif isinstance(actual, tuple):
        t_str = "tuple"
    elif isinstance(actual, str):
        t_str = "str"
    else:
        assert("Did not expect to get here") 

    # Check that all the elements are the correct type, and equal to the expected
    for idx, (acutal_element, expected_element) in enumerate(zip(actual, expected)):
        if not isinstance(acutal_element, type(expected_element)):
            msg = (f"\n\nChecking a {t_str}.\nProblem found at index {idx}:\n"
                   f"  Expected type: {type(expected_element).__name__}\n"
                   f"  Actual type: {type(acutal_element).__name__}")            
            return msg

        if acutal_element != expected_element:
            msg = (f"\n\nChecking a {t_str}.\nProblem found at index {idx}:\n"
                   f"  Expected value: {add_quotes_if_needed(expected_element)}\n"
                   f"  Actual value: {add_quotes_if_needed(acutal_element)}")          
            return msg
        
    return None

def check_2D_list_unstructured(actual, expected):
    '''
    This function is used to check unstructured lists. This is a list where the 
    sublists are not uniform. Generates an error if the actual iterable
    is not the same as the expected. Return None if no
    problem is found. Return the error message if a problem is found.
    Lists where the sublists are unstructured.

    Parameters
        - actual: the actual iterable returned by the function being tested
        - expected: the expected iterable

    Returns
        - None if no problem is found, otherwise an error message
    '''
    # Checking for None values
    msg = check_none(actual, expected)
    if expected is None or msg is not None:
        return msg

    # Check that the actual value is the correct length
    msg = __check_list_length(actual, expected)
    if msg is not None:
        return "\n\n" + msg
    
    # Check all the sub-iterables
    for outer_idx, (actual_sub, expected_sub) in \
        enumerate(zip(actual, expected)):
        # don't use check 1D iterable here, because we want better
        # error messages.
        
        # Check that actual_sub is a list
        if not isinstance(actual_sub, type(expected_sub)):
            msg = (f"\n\nChecking a list. \nValue at index"
                   f" {outer_idx} is a value of {type(actual_sub)} when a "
                   f" {type(expected_sub)} was expected.")
            return msg
        
        # Check that the actual value is the correct length
        #TODO: check in line and generate error message for context
        msg = __check_list_length(actual_sub, expected_sub)
        if msg is not None:
            return (f"\n\nChecking a list with complex values.\n"
                    f"Problem at index {outer_idx} in the outer list: {msg}.")

        # Check that all the elements of the sub list are the correct type,
        # and equal to the expected
        for inner_idx, (actual_val, expected_val) in \
            enumerate(zip(actual_sub, expected_sub)):
            sub_msg = check_none(actual_val, expected_val)
            err_msg = ("\n\nChecking a list with complex values. "
                       "Problem found at at index ({}, {}): {}")
            if expected_val is None or sub_msg is not None:
                if sub_msg is not None:
                    return err_msg.format(outer_idx, inner_idx, sub_msg)
            else:
                sub_msg = check_type(actual_val, expected_val)
                if sub_msg is not None:
                    return err_msg.format(outer_idx, inner_idx, sub_msg)

                sub_msg = check_equals(actual_val, expected_val)
                if msg is not None:
                    return err_msg.format(outer_idx, inner_idx, sub_msg)
    return None


def check_dict(actual, expected):
    '''
    Function to check the values and keys in a dictionary. 
    Generates an error if the actual dictionary is not the same as the expected. 
    Return None if no problem is found.

    First, this function checks the keys in the actual and expected dictionaries
    to make sure they match. Then, it checks the values in the actual and
    expected dictionaries to make sure they match.

    Parameters
        - actual: the actual dictionary returned by the function being tested
        - expected: the expected dictionary

    Returns
        - None if no problem is found, otherwise an error message
    '''
    # Checking for None values
    msg = check_none(actual, expected)
    if expected is None or msg is not None:
        return msg

    # Check keys
    msg = __check_dict_keys(actual, expected)
    if msg is not None:
        return msg
    
    # Check values
    for key in expected:
        msg = check_type(actual[key], expected[key])
        if msg is not None:
            return f'\n\nValue error at key "{key}"\n{msg}'

        msg = check_equals(actual[key], expected[key])
        if msg is not None:
            return f'\n\nValue error at key "{key}"\n{msg}'
        
    return None

def __check_rgb_color(t):
    """
    Verify that t has type (int, int, int) and that the values
    all fall between 0 and 255 inclusive

    Parameters
        - t: value with expected type of (int, int, int)

    Returns
        - Bool value true if it meets the parameters for being a color
    """
    return (isinstance(t, tuple) and
            len(t) == 3 and
            all(isinstance(v, int) and 0 <= v <= 255 for v in t))

def check_2D_shape(actual, expected):
    """
    Check that a list of lists has the right shape. Check the all rows are
    the same (correct) length.

    Parameters 
        - actual: the actual list of lists returned by the function being tested
        - expected: the expected list of lists
    
    Returns
        - None if no problem is found, otherwise an error message
    """
    msg = "The actual shape of the result does not match the expected shape\n"
    msg += "  Expected: {} x {}\n"
    msg += "  Actual: {} x {}\n"

    expected_n = len(expected)
    expected_m = len(expected[0])

    actual_n = len(actual)
    actual_m = len(actual[0])

    if actual_n != expected_n or actual_m != expected_m:
        return msg.format(expected_n, expected_m, actual_n, actual_m)

    msg = "The rows in the actual result should all be of length {}"

    for row in actual:
        if len(row) != actual_m:
            return msg.format(expected_m)

    return None

def check_2D_vals(check_val_fn, actual, expected):
    """
    Checks that the values in a list of lists are the same

    Parameters
        - check_val_fn: function that checks if vals are a set type
        - actual: the actual list of lists returned by the function being tested
        - expected: the expected list of lists
    
    Returns
        - None if no problem is found, otherwise an error message
    """
    msg = check_2D_shape(actual, expected)
    if msg is not None:
        return "\n\n" + msg

    msg = "Actual and expected values do not match at location ({}, {}).\n"
    msg += "   Expected value: {}\n"
    msg += "   Actual value: {}"

    for i, row in enumerate(expected):
        for j, val in enumerate(row):
            if not check_val_fn(val, actual[i][j]):
                return msg.format(i, j, val, actual[i][j])
    return None

def check_2D_type(check_element_type_fn, actual, error_msg=None):
    """
    Generate an error if actual is not a list of lists.  Or if an
    element has the wrong type.

    Parameters
        - check_element_type_fn: function that checks if vals are a set type
        - actual: the actual list of lists returned by the function being tested
        - error_msg: error message with the appropriate error message based on type
    
    Returns
        - None if no problem is found, otherwise an error message
    """
    if not isinstance(actual, list):
        return error_msg

    for row in actual:
        if not isinstance(row, list):
            return error_msg
            
        for val in row:
            if not check_element_type_fn(val):
                return error_msg
    return None


def check_2D_general(check_element_type_fn,
                     element_type_str,
                     check_element_equality_fn,
                     actual,
                     expected):
    """
    This function is used to check that a 2D list has the right type, shape, and
    value.

    Parameters:
        - check_element_type_fn: function that checks if vals are a set type
        - element_type_str: a string with the expected element type
        - check_element_equality_fn: function that checks the values
        - actual: the actual list of lists returned by the function being tested
        - expected: the expected list of lists
       
    Returns
        - None if no problem is found, otherwise an error message
    """

    # Checking for None values
    msg = check_none(actual, expected)
    if expected is None or msg is not None:
        return msg
    
    type_error_msg = (f"The actual value does not have the correct type.\n"
                      f"The expected type is List[List[{element_type_str}]]")
    msg = check_2D_type(check_element_type_fn, actual, type_error_msg)
    if msg is not None:
        return "\n\n" + msg
    
    msg = check_2D_no_aliasing(actual, expected)
    if msg is not None:
        return msg

    msg = check_2D_vals(check_element_equality_fn, actual, expected)
    if msg is not None:
        return "\n\n" + msg

    return None



def check_rgb_image(actual, expected):
    """
    This function is used to check if the actual image is the same as 
    the expected image.

    Parameters
        - actual: the actual image returned by the function being tested
        - expected: the expected image

    Returns
        - None if no problem is found, otherwise an error message
    """
    # Checking for None values
    msg = check_none(actual, expected)
    if expected is None or msg is not None:
        return msg
    
    type_error_msg = ("The actual value does not have the correct type.\n"
                      "The expected type is List[List[Tuple(int, int, int)]]")
    msg = check_2D_type(__check_rgb_color, actual, type_error_msg)
    if msg is not None:
        return "\n\n" + msg
    
    msg = check_2D_no_aliasing(actual, expected)
    if msg is not None:
        return msg

    msg = check_2D_vals(lambda a, e: a == e, actual, expected)
    if msg is not None:
        return "\n\n" + msg

    return None

### Future fix:
### This function should be renamed and take the actual value.
### It check to see if the rows of the actual list are aliases
### of each other.  We need a separate function that checks
### To see if the rows of actual are aliases of the rows of expected.
def check_2D_no_aliasing(actual, expected):
    """
    Generate an error if rows in a list of list do not refer to separate lists.

    Parameters
        - expected: the expected lists of lists
        - actual: the actual list of lists returned by the function being tested
    
    Returns
        - None if no problem is found, otherwise an error message
    """
    if len(expected) > 1:
        msg = ("\n\nThe elements of the outer list must refer to separate"
               " lists.\n There are at least two indexes "
               "(index {} and index {}) that refer to the same list")
        for i, row1 in enumerate(actual):
            for j, row2 in enumerate(actual):
                if i != j and row1 is row2:
                    return msg.format(i, j)  


def check_2D_list_unmodified(param_name, before, after, inequality_fn=lambda x, y: x != y):
    """
    Generate an error if a list of lists was modified when modifications
    are disallowed.

    Parameters
        - param_name: the name of the parameter being checked
        - before: the value of the parameter before the function was called
        - after: the value of the parameter after the function was called
        - inequality_fn: a function for checking that two values are different.
              (default function uses built in != operator).
    
    Returns
        - None if no problem is found, otherwise an error message
    """

    msg = ("\n\nYou modified the contents of the parameter {} "
           "(which is not allowed).\n")
    msg = msg.format(param_name)
    msg += "  Value at index ({}, {}) before your code: {}\n"
    msg += "  Value at index ({}, {}) after your code:  {}"

    for i, row in enumerate(before):
        for j, before_val in enumerate(row):
            if inequality_fn(after[i][j], before_val):
                return msg.format(i, j, before_val, i, j, after[i][j])
    return None

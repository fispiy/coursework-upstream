"""
CMSC 14100
Winter 2025
Homework #8

We will be using anonymous grading, so please do NOT include your name
in this file.

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

import random
from grammars import Variable, Terminal

# Constants for indicating variables in evaluation
LEFT_VAR_BRACKET = '«'  # LEFT-POINTING DOUBLE ANGLE QUOTATION MARK, chr(0xAB)
RIGHT_VAR_BRACKET = '»' # RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK, chr(0xBB)


# Exercise 1
def is_pal(seq, transform):
    """
    Given a sequence and an involutive antimorphism, determine whether the
    sequence is a palindrome with respect to the antimorphism.

    Input:
        seq (list[str]): sequence as a list
        transform (dict[str,str]): dictionary that maps a letter to a letter,
            is involutive

    Output (bool): True if seq is palindromic under transform, False otherwise
    """
    return None

# Exercise 2
def derivation_length(tree):
    """
    Given a parse tree, compute the length of the derivation represented by the 
    parse tree. The length of the derivation is the number of production rules
    that are applied according to the parse tree.

    Input: 
        tree (Variable | Terminal): parse tree

    Output (int): length of derivation for parse tree
    """
    return None

# Exercise 3
def is_equal(tree1, tree2):
    """
    Given two parse trees, determine if they are equal.

    Input:
        tree1 (Variable | Terminal): a parse tree
        tree2 (Variable | Terminal): a parse tree

    Output (bool): True if tree1 and tree2 are equal, False otherwise
    """
    return None

# Exericse 4
def evaluate(tree, separator=''):
    """
    Given a parse tree, produce the string that it represents. Terms may be 
    separated by a given separator. If the parse tree is incomplete, then for
    each variable with name V and no children, the string '«V»' is produced.

    Input:
        tree (Variable | Terminal): parse tree
        separator (str): Separator in between terminal symbols in the resulting
            string. Empty string by default.

    Output (str): the string represented by the parse tree
    """
    return None


# Exercise 5
def morph(tree, ph):
    """
    Given a parse tree and a morphism, produce a new parse tree that represents 
    the string for the parse tree after applying the morphism. The new parse 
    tree may not necessarily be a valid parse tree for the original grammar.

    Input:
        tree (Variable | Terminal): parse tree
        ph (dict[str,str]): a dictionary that maps a terminal to another string

    Output (Variable | Terminal): parse tree for the morphic image of the string
    """
    return None


# Exercise 6
def reversal(tree):
    """
    Given a parse tree, produce a new parse tree that represents the string
    in reverse. The new parse tree may not necessarily be a valid parse tree 
    for the original grammar.

    Input:
        tree (Variable | Terminal): parse tree

    Output (Variable | Terminal): parse tree for the reversal of the string
    """
    return None


# Exercise 7
def is_valid_parse_tree(tree, grammar):
    """
    Given a parse tree and a grammar, determine if the parse tree is valid with
    respect to the given grammar.

    Input:
        tree (Variable | Terminal): parse tree
        grammar (Grammar): grammar definition

    Output (bool): True if tree is valid for grammar, False otherwise
    """
    return None


# Exericse 8
def generate_parse_tree(grammar, var, depth=20):
    """
    Given a grammar, produce a randomly generated parse tree. Provide a depth
    to control the height of the resulting parse tree, which may produce an
    incomplete, but valid, parse tree.

    Input:
        grammar (Grammar): a grammar
        var (str): the name of the variable for the root of the tree
        depth (int): maximum depth of the parse tree to generate, 20 by default

    Output (Variable): A parse tree rooted at the given variable
    """
    return None




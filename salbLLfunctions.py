"""
# Copyright Nick Cheng, 2016
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 1, CSCA48, Winter 2017
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
"""

from salboard import SALboard
from salbnode import SALBnode

# Add your functions here.


def salb2salbLL(salb):
    '''(SALboard) -> SALBnode
    Given a SALboard, the function will create a circularly linked list and
    return the head node.
    REQ: The last square can't be the start or destination of a snadder.
    REQ: salb.numSquares must be 1 or greater.
    REQ: A square can't be the start of a snadder and destination of a snadder.
    '''
    numSquares = salb.numSquares
    snadders = salb.snadders
    # New list used to store al the nodes.
    node_list = []

    head = SALBnode()
    curr = head
    for counter in range(numSquares):
        # Add every node to the list.
        node_list.append(curr)
        # Create a new node
        newNode = SALBnode()
        curr.next = newNode
        curr = curr.next

    # Makes the linked list circular.
    curr.next = head

    for key in snadders:
        node_list[key-1].snadder = node_list[snadders[key]-1]

    # Returns te head of the linked list.
    return head


def willfinish(first, stepsize):
    '''(SALBnode, int) -> bool
    Given the head of a circularly linked list, and a step size, the function
    will determine if the player can finish the game.
    REQ: The last square can't be the start or destination of a snadder.
    REQ: A square can't be the start of a snadder and destination of a snadder.
    >>> first = salb2salbLL(SALboard(100, {}))
    >>> willfinish(first, 1)
    True
    >>> first = salb2salbLL(SALboard(100, {2:4, 45:100}))
    >>> willfinish(first, 1)
    True
    >>> first = salb2salbLL(SALboard(1998, {}))
    >>> willfinish(first, 9)
    True
    >>> first = salb2salbLL(SALboard(100, {6:5, 99:1}))
    >>> willfinish(first, 1)
    False
    '''
    curr = first.next
    moves = 0
    looped = False
    # Calls another funciton ot get the size of the board.
    boardSize = boardsize(first)

    while (curr != first) and not(looped):
        # If the amount of moves the player made is greater than the board size
        # , the player is in a loop.
        if moves > boardSize:
            looped = True
        else:
            moves += 1
            # If the current tile isn't a snadder, then the next tile is
            # however big the stepsize to the right.
            if curr.snadder is None:
                for counter in range(stepsize):
                    curr = curr.next
            # If the current tile is a snadder, the current tile is whereever
            # the snadder takes it.
            else:
                curr = curr.snadder

    # If the current tile equals the first one, and the player wasn't in a loop
    # , the player has finished the game.
    if (curr == first) and not(looped):
        result = True
    # If not, then the player hasn't finished the game.
    else:
        result = False

    # Returns whether or not the player finished the game.
    return result


def whowins(first, step1, step2):
    '''(SALBnode, int, int) -> int
    Given the head of the cicularly linked list and 2 step sizes, the function
    will return the number of the player who wins the game.
    REQ: The last square can't be the start or destination of a snadder.
    REQ: A square can't be the start of a snadder and destination of a snadder.
    >>> first = salb2salbLL(SALboard(100, {}))
    >>> whowins(first, 1, 1)
    1
    >>> first = salb2salbLL(SALboard(100, {2:4, 45:93}))
    >>> whowins(first, 7, 9)
    1
    >>> first = salb2salbLL(SALboard(6, {1:4, 5:3}))
    >>> whowins(first, 1, 2)
    2
    >>> first = salb2salbLL(SALboard(99, {7:3, 10:50, 57:8}))
    >>> whowins(first, 7, 7)
    2
    '''
    # Calls another function to determine if a player finished the game.
    player1 = willfinish(first, step1)
    player2 = willfinish(first, step2)
    result = 0

    # Player 2 wins if both players did not complete the game.
    if not(player1) and not(player2):
        result = 2
    # PLayer 1 wins if player 1 finished and player 2 did not.
    elif player1 and not(player2):
        result = 1
    # PLayer 2 wins if player 2 finished and player 1 did not.
    elif not(player1) and player2:
        result = 2
    # PLayer 1 wins if they both finished the game.
    elif player1 and player2:
        result = 1

    # Returns the number of the player who won.
    return result


def dualboard(first):
    '''(SALBnode) -> SALBnode
    Given the head of a circularly linked list, the function will return the
    head of a new circularly linked list that has reversed snadders.
    REQ: The last square can't be the start or destination of a snadder.
    REQ: A square can't be the start of a snadder and destination of a snadder.
    >>> first = salb2salbLL(SALboard(99, {7:3, 10:50, 57:8}))
    >>> dualboard(first)
    new_first = salb2salbLL(SALboard(99, {3:7, 50:10, 8:57}))
    >>> first = salb2salbLL(SALboard(10, {1:2, 3:4, 5:6}))
    >>> dualboard(first)
    new_first = salb2salbLL(SALboard(99, {2:1, 4:3, 6:5}))
    >>> first = salb2salbLL(SALboard(99, {}))
    >>> dualboard(first)
    new_first = salb2salbLL(SALboard(99, {}))
    '''
    curr = first
    # Calls another function to get the size of the board.
    boardSize = boardsize(first)

    # Creates a new head for the dualbaord.
    new_head = SALBnode()
    new_curr = new_head

    for counter in range(boardSize):
        # Connects all the nodes in the new linked list.
        newNode = SALBnode()
        new_curr.next = newNode
        new_curr = new_curr.next

    # Makes the linked list circular.
    new_curr.next = new_head

    # starts the new linked list from the head.
    new_curr = new_head
    current = new_curr

    for counter in range(boardSize):
        if curr.snadder is not None:
            a = curr
            # Counter is set back to 0.
            counter = 0

            # Continues to increase counter by 1 until a equals the current
            # snadder.
            while a != curr.snadder:
                counter += 1
                # Continues to loop through the original linked list.
                a = a.next

            b = current
            for i in range(counter):
                # Continues to loop through the new lined list.
                b = b.next

            # The current snadder in the new linked list equals the node in the
            # new linked list.
            b.snadder = current

        # Both lists move on to the next node.
        curr = curr.next
        current = current.next

    # Returns the head of the new linked list.
    return new_head


def boardsize(first):
    '''(SALBnode) -> int
    Given the head of a circularly linked list, the function will return the
    size of the list.
    REQ: The size of the list must be 1 or greater.
    '''
    curr = first.next
    size = 0
    # Continues to add 1 to the size of the board.
    while (curr != first):
        curr = curr.next
        size += 1

    # Returns the size of the board.
    return size

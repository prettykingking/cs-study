"""Binary search
"""


def binary_search(data, target, low, high):
    """Returns True if target is found in indicated portion of a Python list

    The search only considers the portion from data[low] to data[high] inclusive.
    """
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:     # found a match
            return True
        elif target < data[mid]:
            # recur on the portion left of the middle
            return binary_search(data, target, low, mid - 1)
        elif target > data[mid]:
            # recur on the portion right of the middle
            return binary_search(data, target, mid + 1, high)


print("found={!r}\ttarget={:d}\tlow={:d}\thigh={:d}".format(
    binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7, 2, 9), 7, 2, 9))
print("found={!r}\ttarget={:d}\tlow={:d}\thigh={:d}".format(
    binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11, 2, 9), 11, 2, 9))

#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for index in range(length):
        hash_table_insert(ht, weights[index], index)

    for index in range(length):
        other_index = hash_table_retrieve(ht, (limit - weights[index]))

        if other_index:
            if other_index > index:
                return [other_index, index]
            else:
                return [index, other_index]

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

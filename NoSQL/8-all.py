#!/usr/bin/env python3
"""lists all documents in a collection"""


def list_all(mongo_collection):
    """func that returns the data of a collect

    Args:
        mongo_colection: pymongo collection object

    Returns:
        data or empty list
    """
    docs = mongo_collection.find()
    if docs:
        return docs
    else:
        return []


if __name__ == '__main__':
    list_all(mongo_collection)

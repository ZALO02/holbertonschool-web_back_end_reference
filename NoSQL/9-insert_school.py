#!/usr/bin/env python3
"""lists all documents in a collection"""


def insert_school(mongo_collection, **kwargs):
    """func that returns the data of a collect

    Args:
        mongo_colection: pymongo collection object
        kwargs: variable k-word arguments

    Returns:
        result.inserted_id: id of object
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id


if __name__ == '__main__':
    insert_school(mongo_collection, **kwargs)

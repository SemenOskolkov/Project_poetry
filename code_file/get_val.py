def get_val(collection, key, default=None):
    if key in collection:
        return collection.get(key)
    else:
        return default

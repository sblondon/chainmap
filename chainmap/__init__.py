class ChainMap(dict):
    def __init__(self, *maps):
        if maps:
            self.maps = maps
        else:
            self.maps = [{}]

    def __getitem__(self, key):
        for mapping in self.maps:
            try:
                return mapping[key]
            except KeyError:
                pass
        raise KeyError(key)

    def __setitem__(self, key, value):
        self.maps[0][key] = value

    def __delitem__(self, key):
        del self.maps[0][key]

    def __contains__(self, key):
        try:
            self[key]
            return True
        except KeyError:
            return False

    def __iter__(self):
        """lazy implementation would have been better"""
        _keys = []
        for m in self.maps:
            _keys.extend(m.keys())
        _keys = list(set(_keys))
        return iter(_keys)

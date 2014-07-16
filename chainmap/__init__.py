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
        _keys = self._all_keys()
        return iter(_keys)

    def _all_keys(self):
        _keys = []
        for m in self.maps:
            _keys.extend(m.keys())
        return list(set(_keys))

    def __len__(self):
        return len(self._all_keys())

    def __nonzero__(self):
        return any(self.maps)



import kwic

document = "rox is ok\na b"

assert(kwic.kwic(document) == [(["a", "b"],1), (["b", "a"],1), (['is', 'ok', 'rox'], 0), (['ok', 'rox', 'is'],0), (['rox', 'is', 'ok'],0)])

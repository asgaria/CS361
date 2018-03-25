import kwic

document = "a b c"

assert(kwic.kwic(document) == [(['a', 'b', 'c'],0), (['b', 'c', 'a'],0), (['c', 'a', 'b'],0)])

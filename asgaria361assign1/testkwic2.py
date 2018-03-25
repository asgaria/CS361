import kwic

document = "hello world"

assert(kwic.kwic(document) == [(['hello', 'world'],0), (['world', 'hello'],0)])

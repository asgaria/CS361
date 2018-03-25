import kwic

document = "This test\nfor caps"

assert(kwic.kwic(document) == [(["caps", "for"],1), (["for", "caps"],1), (["test", "This"], 0), (["This", "test"],0)])

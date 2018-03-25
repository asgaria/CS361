import kwic

document = "This test. for caps"

assert(kwic.kwic(document,"This", False, True) == [(["caps", "for"],1), (["for", "caps"],1), (["test.", "This"], 0)])

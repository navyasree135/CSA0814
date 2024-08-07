s = "Hi im ksdf askdf asdf"
print(s.upper(), s.lower(), len(s.split(" ")), len([x for x in s.split(" ") if x[0].lower() == "a"]))
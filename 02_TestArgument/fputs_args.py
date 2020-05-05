import fputs
print('fputs.__doc__:', fputs.__doc__)
#'Python interface for the fputs C library function'
print('fputs.__name_:', fputs.__name__)
#'fputs'
# Write to an empty file named `write.txt`
fputs.fputs("Hello Python!", "test_write.txt")
#13
with open("test_write.txt", "r") as f:
    print("f.read()", f.read())
#'Hello Python!'
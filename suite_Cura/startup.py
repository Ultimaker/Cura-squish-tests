import os

print(os.getcwd())
print("file path: ", os.path.abspath("Performance.txt"))
f = open("suite_Cura/shared/scripts/TestResults/Performance.txt", "w+")
for i in range(10):
    f.write("This is line %d\r\n" % (i + 1))
f.close()

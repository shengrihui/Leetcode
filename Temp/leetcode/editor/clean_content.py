import glob

py_list = glob.glob("cn/*.py")
py_list.remove("cn\imports.py")
for file in py_list[10:]:
    lines = open(file, encoding="utf-8").readlines()
    lines.pop()
    while lines[-1].startswith("#"):
        lines.pop()
    while lines[-1] == "\n":
        lines.pop()
    with open(file, "w", encoding="utf-8") as f:
        f.writelines(lines)

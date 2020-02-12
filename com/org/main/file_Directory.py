from pathlib import Path


# Absolute Path = starting from hardisk
# Relative path = starts with current directory
path = Path()
for file in path.glob("*.py"):
    print(file)
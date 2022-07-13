import json
def create():
    create_file = open("data.json", "x")
    with open('data.json', 'w') as f:
        f.write("{}")

if __name__ == "__main__":
    create()


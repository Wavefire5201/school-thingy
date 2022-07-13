import json

with open('data.json', 'r') as f:
    temp = json.load(f)
    temp_list = [f'Assignment: {value["Assignment"]} | Priority {value["Priority"]} | Time: {value["Time"]} hours' for
                 key, value in temp.items()]

    # print(sorted(temp.items()))
    priority_dicts = dict(sorted(temp.items(), key=lambda item: item[1]["Priority"], reverse=True))
    for dictionary in priority_dicts:
        print(priority_dicts[dictionary])


import json
import make_file
import os.path
import datetime

today = datetime.datetime.now()
print(today)


def main_function():
    while True:
        with open('data.json', 'r') as f:
            temp = json.load(f)
            priority_dicts = dict(sorted(temp.items(), key=lambda item: item[1]["Priority"], reverse=True))
            assignment_dicts = dict(sorted(temp.items(), key=lambda item: item[1]["Assignment"]))
            subjects_dicts = dict(sorted(temp.items(), key=lambda item: item[1]["Subject"]))
            date_dicts = dict(sorted(temp.items(), key=lambda item: item[1]["Date"], reverse=True))
            time_dicts = dict(sorted(temp.items(), key=lambda item: item[1]["Time"], reverse=True))

        action_to_perform = input("What is the action you would like to perform? ")
        if action_to_perform == "q":
            quit()
        elif action_to_perform == "assignments":
            subject_selected = input("What is the subject of the assignment? ")
            assignment_selected = input("What is the name of the assignment? ")
            time_total = float(input("How long will it take in hours? "))
            date_due = float(input("In how many days is this due in? "))
            priority = round(time_total / date_due, 1) * 10

            if os.path.exists("data.json"):
                with open("data.json", "r") as f:
                    data = json.load(f)
                    data[len(data) + 1] = {
                        "Assignment": assignment_selected,
                        "Subject": subject_selected,
                        "Time": time_total,
                        "Date": date_due,
                        "Priority": priority,
                    }

                with open("data.json", "w") as f:
                    json.dump(data, f, indent=4)

        elif action_to_perform == "sort":
            def sorting():
                list_of_options = ["Assignment Name", "Priority", "Date Due", "Time", "Subject"]
                for option in list_of_options:
                    print(option)
                thing_to_sort = input("What do you want to sort by? ")
                if thing_to_sort.title() in list_of_options:
                    if thing_to_sort.title() == "Assignment Name":
                        for assignment in assignment_dicts:
                            print(assignment_dicts[assignment])
                    elif thing_to_sort.title() == "Priority":
                        for priority_ in priority_dicts:
                            print(priority_dicts[priority_])
                    elif thing_to_sort.title() == "Subject":
                        for subject in subjects_dicts:
                            print(subjects_dicts[subject])
                    elif thing_to_sort.title() == "Time":
                        for time in time_dicts:
                            print(time_dicts[time])
                    elif thing_to_sort.title() == "Date Due":
                        for date in date_dicts:
                            print(date_dicts[date])
                else:
                    sorting()
            sorting()

if __name__ == "__main__":
    if not os.path.exists("data.json"):
        make_file.create()
    main_function()

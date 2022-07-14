import json
import make_file
import os.path
import datetime
import pandas

today = datetime.datetime.now()
print(today)

def main_function():
    while True:
        # Presort and make pandas DataFrame
        with open('data.json', 'r') as f:
            temp = json.load(f)
            # pandas_dataframe = pandas.DataFrame(temp)
            # print(pandas_dataframe.to_string())
            priority_dicts = dict(sorted(temp.items(), key=lambda item: item[1]["Priority"], reverse=True))
            assignment_dicts = dict(sorted(temp.items(), key=lambda item: item[1]["Assignment"]))
            subjects_dicts = dict(sorted(temp.items(), key=lambda item: item[1]["Subject"]))
            date_dicts = dict(sorted(temp.items(), key=lambda item: item[1]["Date"], reverse=True))
            time_dicts = dict(sorted(temp.items(), key=lambda item: item[1]["Time"], reverse=True))

        action_list = ["q", "assignments", "sort", "del"]
        print(f"Available actions: {' | '.join(action_list)}")
        action_to_perform = input("What is the action you would like to perform? ")

        # Possible actions
        match action_to_perform.lower():
            case "q":
                quit()
            case "assignments":
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

            case "sort":
                def sorting():
                    list_of_options = ["All", "Assignment Name", "Priority", "Date Due", "Time", "Subject"]
                    print(" | ".join(list_of_options))
                    thing_to_sort = input("What do you want to sort by? ")
                    match thing_to_sort.title():
                        case "Assignment Name":
                            assignment_df = pandas.DataFrame(assignment_dicts)
                            print(assignment_df.to_string())
                        case "Priority":
                            priority_df = pandas.DataFrame(priority_dicts)
                            print(priority_df.to_string())
                        case "Subject":
                            subject_df = pandas.DataFrame(subjects_dicts)
                            print(subject_df.to_string())
                        case "Time":
                            time_df = pandas.DataFrame(time_dicts)
                            print(time_df.to_string())
                        case "Date Due":
                            date_df = pandas.DataFrame(date_dicts)
                            print(date_df.to_string())
                        case "All":
                            print(pandas.DataFrame(temp).to_string())
                        case default:
                            sorting()
                sorting()
            case "del":
                selected_deletion = input("Which item would you like to delete? ")
                temp_df = pandas.DataFrame(temp)
                temp_dict = temp_df.to_dict()
                del temp_dict[selected_deletion]
                with open("data.json", "w") as f:
                    json.dump(temp_dict, f, indent=4)

            case default:
                print("Not a valid option!")

if __name__ == "__main__":
    if not os.path.exists("data.json"):
        make_file.create()
    main_function()

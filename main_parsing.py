import json


def open_json(name):
    with open(name) as file:
        problem_names = json.load(file)

    return problem_names


def get_all_data(tasks_json):
    res_data = dict()
    for num_task in tasks_json:
        res_data[num_task] = dict()
        task_name = tasks_json[num_task]["name"].split('.')[-1].strip()
        res_data[num_task]["task_name"] = task_name
        res_data[num_task]["link"] = tasks_json[num_task]["link"]
        print(res_data)


def main():
    tasks_json = open_json("links_to_tasks.json")
    get_all_data(tasks_json)



if __name__ == "__main__":
    main()





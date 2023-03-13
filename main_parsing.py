import json
from get_editorial import get_data_editorial
from get_solutions import get_data_solutions_page


def open_json(name):
    with open(name) as file:
        problem_names = json.load(file)

    return problem_names


def get_data_task_from_json(task_json):
    data_task = dict()
    task_name = task_json["name"].split('.')[-1].strip()
    task_link = task_json["link"]
    status_prem = task_json["is_premium"]
    data_task["name"] = task_name
    data_task["link"] = task_link
    data_task["status_prem"] = status_prem

    return data_task


def main():
    res_data = dict()
    tasks_json = open_json("links_to_tasks.json")

    with open("total.json", "w") as file:
        pass

    for task in tasks_json:
        res_data[task] = get_data_task_from_json(tasks_json[task])

        data_editorial = get_data_editorial(res_data[task]["link"])
        res_data[task]["editorial"] = data_editorial["editorial solution"]

        if res_data[task]["status_prem"]:
            res_data[task]["solutions"] = None
        else:
            data_solutions = get_data_solutions_page(res_data[task]["link"])
            res_data[task]["solutions"] = data_solutions

        # write data
        with open("total.json", "a") as file:
            json.dump(res_data, file, indent=4)



if __name__ == "__main__":
    main()





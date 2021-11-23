from parse import read_input_file, write_output_file
import os

def solve(tasks):
    """
    Args:
        tasks: list[Task], list of igloos to polish
    Returns:
        output: list of igloos in order of polishing  
    """
    # Basic Greedy to see if it works
    # Sort by deadline
    # Keep adding the nearest deadlined thing until you don't have any more you can add

    sorted_tasks = sorted(tasks, key=lambda x: x.deadline)
    
    time = 0
    taskList = []
    i = 0
    while time < 1440:
        
        # if you run out of possible tasks, break the loop
        if i >= len(sorted_tasks):
            break
        
        # if you can fit in another task before the deadline is up
        if (sorted_tasks[i].deadline - sorted_tasks[i].duration >= time) and time + sorted_tasks[i].duration < 1440:
            taskList.append(sorted_tasks[i].task_id)
            time += sorted_tasks[i].duration
        i += 1

    
    return taskList


# Here's an example of how to run your solver.
if __name__ == '__main__':
    for input_path in os.listdir('inputs/'):
        output_path = 'outputs/' + input_path[:-3] + '.out'
        tasks = read_input_file('inputs/' + input_path)
        output = solve(tasks)
        write_output_file(output_path, output)
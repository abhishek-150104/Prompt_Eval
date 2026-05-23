from statistics import mean

from run_testcase import run_test_case

def run_eval(dataset):
    """Loads the dataset and calls run_test_case with each case"""
    results = []
    
    for test_case in dataset:
        result = run_test_case(test_case)
        results.append(result)

    average = mean([result["score"] for result in results])

    print(f"Average Score:{average}")
    
    return results



from run_prompt import run_prompt
from prompt_eval_grader import grade_by_model
from code_prompt_grader import grade_syntax

def run_test_case(test_case):
    """Calls run_prompt, then grades the result"""
    output = run_prompt(test_case)
    
    # Grading
    model_grade= grade_by_model(test_case, output)
    model_score= model_grade["score"]
    reasoning= model_grade["reasoning"]

    syntax_score= grade_syntax(output, test_case)

    score = (model_score + syntax_score)/2;
    
    return {
        "output": output,
        "test_case": test_case,
        "score": score,
        "reasoning": reasoning,
    }

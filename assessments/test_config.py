"""
Global Test Configuration
Controls whether tests import from candidate solutions or model solutions.
"""

# Set this to True to test model solutions, False to test candidate solutions
TEST_MODEL_SOLUTIONS = True

# Alternative: Use environment variable for more flexibility
import os
if 'TEST_MODEL_SOLUTIONS' in os.environ:
    TEST_MODEL_SOLUTIONS = os.environ.get('TEST_MODEL_SOLUTIONS', 'false').lower() == 'true'

def get_solution_path(assessment_name, level):
    """
    Get the import path for the solution based on configuration.
    
    Args:
        assessment_name (str): Name of the assessment (e.g., 'banking_system')
        level (str): Level name (e.g., 'level1')
        
    Returns:
        str: Import path for the solution
    """
    if TEST_MODEL_SOLUTIONS:
        return f"assessments.{assessment_name}.{level}.model_solution"
    else:
        return f"assessments.{assessment_name}.{level}.candidate"

def get_solution_module_name(assessment_name):
    """
    Get the module name for the solution based on assessment.
    
    Args:
        assessment_name (str): Name of the assessment
        
    Returns:
        str: Module name (e.g., 'banking', 'chat', 'task_queue')
    """
    # Map assessment names to their module names
    module_map = {
        'banking_system': 'banking',
        'chat_platform': 'chat',
        'task_queue': 'task_queue',
        'inventory_system': 'inventory',
        'model_welfare_tracker': 'welfare_tracker',
        'file_system_commands': 'file_system'
    }
    
    return module_map.get(assessment_name, assessment_name)

def get_full_import_path(assessment_name, level):
    """
    Get the full import path for testing.
    
    Args:
        assessment_name (str): Name of the assessment
        level (str): Level name
        
    Returns:
        str: Full import path (e.g., 'assessments.banking_system.level1.model_solution.banking')
    """
    solution_path = get_solution_path(assessment_name, level)
    module_name = get_solution_module_name(assessment_name)
    return f"{solution_path}.{module_name}"

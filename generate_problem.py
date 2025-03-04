#!/usr/bin/env python3

import os
import sys

def convert_to_camel_case(snake_case):
    """Convert a snake_case name to camelCase."""
    components = snake_case.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def generate_problem_file(path):
    # Extract folder and problem name from path
    if '/' in path:
        folder_name, problem_name = path.rsplit('/', 1)
    else:
        folder_name = ""
        problem_name = path
    
    # Remove .py extension if present
    if problem_name.endswith('.py'):
        problem_name = problem_name[:-3]
    
    # Generate problem name variations
    problem_title = problem_name.replace('_', ' ').title()
    problem_url = problem_name.replace('_', '-')
    problem_method = convert_to_camel_case(problem_name)
    
    # Create full path
    full_path = os.path.join(os.path.dirname(__file__), folder_name)
    full_file_path = os.path.join(full_path, f"{problem_name}.py")
    
    # Create directory if it doesn't exist
    if folder_name and not os.path.exists(full_path):
        os.makedirs(full_path)
    
    # Generate file content
    template = f'''"""
{problem_title}

Leetcode # - https://leetcode.com/problems/{problem_url}/

Time Complexity - 
Space Complexity -

Solution:

Explanation:

"""

from utils import LeetTester

class Solution:
    def {problem_method}(self):
        return ""

# Example test cases
tester = LeetTester()
solution = Solution()


tester.summary()
'''
    
    # Write to file
    with open(full_file_path, 'w') as f:
        f.write(template)
    
    print(f"Generated problem file: {full_file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 generate_problem.py folder_name/problem_name.py")
        sys.exit(1)
    
    generate_problem_file(sys.argv[1])

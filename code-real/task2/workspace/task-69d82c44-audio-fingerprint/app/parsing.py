import dataclasses
import json
import sys
import re
from enum import Enum
from pathlib import Path
from typing import List

class TestStatus(Enum):
    """The test status enum."""
    PASSED = 1
    FAILED = 2
    SKIPPED = 3
    ERROR = 4

@dataclasses.dataclass
class TestResult:
    """The test result dataclass."""
    name: str
    status: TestStatus

### DO NOT MODIFY THE CODE ABOVE ###
### Implement the parsing logic below ###

def parse_test_output(stdout_content: str, stderr_content: str) -> List[TestResult]:
    """
    Parse the test output content and extract test results.
    """
    results = []
    # Regex to match pytest verbose output
    # Example: tests/test_f2p.py::TestFileStructure::test_fingerprint_module_importable PASSED
    pattern = re.compile(r'::([^\s]+)\s+(PASSED|FAILED|ERROR|SKIPPED)')
    
    for line in stdout_content.splitlines():
        match = pattern.search(line)
        if match:
            test_name = match.group(1)
            status_str = match.group(2)
            
            if status_str == 'PASSED':
                status = TestStatus.PASSED
            elif status_str == 'FAILED':
                status = TestStatus.FAILED
            elif status_str == 'SKIPPED':
                status = TestStatus.SKIPPED
            else:
                status = TestStatus.ERROR
                
            results.append(TestResult(name=test_name, status=status))
            
    return results

### Implement the parsing logic above ###
### DO NOT MODIFY THE CODE BELOW ###

def export_to_json(results: List[TestResult], output_path: Path) -> None:
    json_results = {
        'tests': [
            {'name': result.name, 'status': result.status.name} for result in results
        ]
    }
    with open(output_path, 'w') as f:
        json.dump(json_results, f, indent=2)

def main(stdout_path: Path, stderr_path: Path, output_path: Path) -> None:
    with open(stdout_path) as f:
        stdout_content = f.read()
    with open(stderr_path) as f:
        stderr_content = f.read()

    results = parse_test_output(stdout_content, stderr_content)
    export_to_json(results, output_path)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: python parsing.py <stdout_file> <stderr_file> <output_json>')
        sys.exit(1)

    main(Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3]))

import re
from pathlib import Path
from datetime import datetime

log_file_path = r".\P1\build\Testing\Temporary\LastTest.log"
html_output_path = r".\gtest_report.html"

def parse_gtest_log(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    test_pattern = re.compile(
        r'(?P<index>\d+)/\d+ Testing: (?P<test_name>.+?)\n.*?'
        r'"(?P=test_name)" start time: .+?\nOutput:\n-+\n'
        r'(?P<output>.+?)<end of output>\n'
        r'Test time =\s+(?P<duration>[\d.]+) sec\n-+\n'
        r'Test (?P<result>Passed|Failed)\.\n'
        r'"(?P=test_name)" end time: .+?\n'
        r'"(?P=test_name)" time elapsed: (?P<elapsed>[\d:]+)', re.DOTALL
    )

    tests = []

    for match in test_pattern.finditer(content):
        tests.append({
            "Index": match.group("index"),
            "Test Name": match.group("test_name"),
            "Result": match.group("result"),
            "Duration": match.group("duration") + " sec",
            "Elapsed Time": match.group("elapsed"),
            "Output": match.group("output").strip().replace("\n", "<br>")
        })

    return tests

def generate_html_report(tests, output_path):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    rows = ""

    for test in tests:
        color = "#d4edda" if test['Result'] == 'Passed' else "#f8d7da"
        rows += f"""
        <tr style="background-color: {color};">
            <td>{test['Index']}</td>
            <td>{test['Test Name']}</td>
            <td>{test['Result']}</td>
            <td>{test['Duration']}</td>
            <td>{test['Elapsed Time']}</td>
            <td><details><summary>View</summary>{test['Output']}</details></td>
        </tr>
        """

    html_content = f"""
    <html>
    <head>
        <title>Google Test Report</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            table {{ width: 100%; border-collapse: collapse; }}
            th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
            th {{ background-color: #f2f2f2; }}
            details summary {{ cursor: pointer; }}
        </style>
    </head>
    <body>
        <h2>Google Test Report</h2>
        <p>Generated on: {now}</p>
        <table>
            <tr>
                <th>#</th>
                <th>Test Name</th>
                <th>Result</th>
                <th>Duration</th>
                <th>Elapsed Time</th>
                <th>Output</th>
            </tr>
            {rows}
        </table>
    </body>
    </html>
    """

    Path(output_path).write_text(html_content, encoding='utf-8')
    print(f"HTML report generated at: {output_path}")

if __name__ == "__main__":
    tests = parse_gtest_log(log_file_path)
    generate_html_report(tests, html_output_path)
import json
import traceback
import lxml.etree


def parse_edulint_output():
    def clean(line):
        line = line[line.find(' '):]
        return line

    with open('/grade/lint_output.txt') as infile:
        lint_output = infile.readlines()

    lint_output = [ f'{i+1}. {clean(line)}' for i, line in enumerate(lint_output) if line.split()[1][0] in ['R', 'C'] ]
    return {'name': 'Teste de Qualidade de Código',
            'points': 0 if len(lint_output) > 0 else 1,
            'max_points': 1,
            'output': 'Seu código apresentou os seguintes erros de qualidade:\n' +  '\n'.join(lint_output)}

def parse_pytest_output():
    pytest_results = []

    with open('/grade/pytest_output.xml', 'rb') as infile:
        pytest_output = infile.read()

    pytest_output = lxml.etree.fromstring(pytest_output)

    for test in pytest_output.iter('testcase'):
        pytest_results.append({
            'name': test.get('name'),
            'points': 1 if len(test.getchildren()) == 0 else 0,
            'max_points': 1,
            'output': test.find('failure').get('message') if len(test.getchildren()) > 0 else ''
        })

    return pytest_results


if __name__ == '__main__':
    try:
        results = []
        # results.append(parse_edulint_output())
        results.extend(parse_pytest_output())

        # Compile total number of points
        max_points = sum([test['max_points'] for test in results])
        earned_points = sum([test['points'] for test in results])

        # Assemble final grading results
        grading_result = {}
        grading_result['tests'] = results
        grading_result['score'] = float(earned_points) / float(max_points)
        grading_result['succeeded'] = True
        #print(json.dumps(grading_result, allow_nan=False))

        with open('results.json', mode='w') as out:
            json.dump(grading_result, out)
    except:
        # Last-ditch effort to capture meaningful error information
        grading_result = {}
        grading_result['score'] = 0.0
        grading_result['succeeded'] = False
        grading_result['output'] = traceback.format_exc()

        with open('results.json', mode='w') as out:
            json.dump(grading_result, out)

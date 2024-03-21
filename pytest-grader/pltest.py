import json
import traceback
import lxml.etree


def parse_pytest_output():
    pytest_results = []

    with open('/grade/pytest_output.xml', 'rb') as infile:
        pytest_output = infile.read()

    pytest_output = lxml.etree.fromstring(pytest_output)

    for test in pytest_output.iter('testcase'):
        max_points = 1
        properties = test.findall('properties/property')
        for property in properties:
            if property.get('name') == 'max_points':
                max_points = int(property.get('value'))
        other_children = [child for child in test.getchildren() if child.tag != 'properties']
        pytest_results.append({
            'name': test.get('name'),
            'points': max_points if len(other_children) == 0 else 0,
            'max_points': max_points,
            'output': test.find('failure').get('message') if len(other_children) > 0 else ''
        })

    return pytest_results


if __name__ == '__main__':
    try:
        results = []
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

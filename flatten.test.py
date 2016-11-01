import sys
from flatten import flatten

subject = [[1, [2, [[3]]]], 4, 5]
expectation = [1, 2, 3, 4, 5]
results = flatten(subject)

print('subject: ')
print(subject)
print()

print('expectation: ')
print(expectation)
print()

print('results: ')
print(results)
print()

try:
    assert type(results) is list, \
        'expected a list type; got type %s.' % type(results)

    assert len(results) is len(expectation), \
        'expected %s elements in list; got %s' % (len(expectation), len(results))

    for idx, val in enumerate(results):
        assert val is expectation[idx], \
          'expected element %s to be %s; got %s' % (idx, expectation[idx], results[idx])

    print('Tests passed!')

except AssertionError:
    raise AssertionError

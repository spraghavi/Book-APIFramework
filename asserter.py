from logger import Logger


def assert_eval(value, reference, message):
    if reference in str(value):
        result = True
        assert result, message
    else:
        result = False
        assert result, message
    Logger.log_assertion(expression=message, result=result)


def assert_equal(value, reference, entity_name, compare_types=False):
    if compare_types:
        result = value == reference
    else:
        result = str(value) == str(reference)
    assert result, f'{entity_name} actual value [{value}] is not equal to expected value [{reference}]'
    Logger.log_assertion(
        expression=f'{entity_name} actual value [{value}] is equal to expected value [{reference}]',
        result=result
    )


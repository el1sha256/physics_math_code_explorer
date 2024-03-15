from manticore_utils.init_tables import init_tables
from manticore_utils.fill import fill_manticore


def init_db(data: list[dict]) -> bool:
    init_result = init_tables()
    try:
        assert init_result[0]['error'] == ''
    except AssertionError:
        raise Exception(str(init_result))

    fill_result = fill_manticore(data)
    assert fill_result

    return True


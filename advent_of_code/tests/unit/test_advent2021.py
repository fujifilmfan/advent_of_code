from unittest import mock

import pytest

from advent_of_code.advent2021 import day1_sonar_sweep as day1

_MODULE = 'advent_of_code.advent2021'


@pytest.fixture
def mock_cli_args():
    """PostgresConnections object for mocking database responses.

    Use it like this:
    pg_connections = mock_pg_connections(row=response)
    """

    class Namespace:

        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    return Namespace


@pytest.mark.parametrize('look_ahead, expected', [
    (1, 7),
    (2, 5),
])
@mock.patch(f'{_MODULE}.day1_sonar_sweep.return_file_contents')
@mock.patch(f'{_MODULE}.day1_sonar_sweep.return_parsed_args')
def test_day1(
        mock_parsed_args,
        mock_file_contents,
        look_ahead,
        expected,
        mock_cli_args
):
    """Test advent2021.day1_sonar_sweep() results.

    :param mock_parsed_args: MagicMock obj
    :param mock_file_contents: MagicMock obj
    :param look_ahead: int
    :param expected: int
    :param mock_cli_args: MagicMock obj
    :return: None
    """

    # Arrange
    day1_input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    args = ['-w', '2']
    cli_args = mock_cli_args(filename=None, window=look_ahead)
    mock_parsed_args.return_value = cli_args
    mock_file_contents.return_value = day1_input

    # Act
    actual = day1.main(args)

    # Assert
    assert actual == expected




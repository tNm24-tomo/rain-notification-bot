import unittest
from unittest.mock import patch
import main

class TestWeatherNotify(unittest.TestCase):

    @patch('main.send_line_message')
    @patch('main.get_weather')
    def test_rainy_weather_sends_message(self, mock_get_weather, mock_send_message):
        mock_get_weather.return_value = "小雨"

        main.main()

        mock_send_message.assert_called_once_with(
            "今日の天気は「小雨」です。傘を忘れずに☂️"
        )

    @patch('main.send_line_message')
    @patch('main.get_weather')
    def test_clear_weather_does_not_send_message(self, mock_get_weather, mock_send_message):
        mock_get_weather.return_value = "晴れ"

        main.main()

        mock_send_message.assert_not_called()

if __name__ == '__main__':
    unittest.main()

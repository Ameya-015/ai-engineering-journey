import numpy as np
import day29_usage_report

def test_active_days():
    test_list = [14, 67, 35, 55, 20, 8]
    test_array = np.array(test_list).reshape(2, 3)
    expected_count = np.array([1 , 1])
    result = day29_usage_report.active_days(test_array, 50)
    assert (result == expected_count).all()


def test_active_days_without_threshold():
    test_list = [30, 29, 67, 55, 20, 8]
    test_array = np.array(test_list).reshape(2, 3)
    expected_count = np.array([2 , 1])
    result = day29_usage_report.active_days(test_array)
    assert (result == expected_count).all()
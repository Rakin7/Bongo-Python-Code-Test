# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 23:36:29 2020

@author: Rakin
"""
import pytest
from BongoTest2 import print_depth, Person
class TestTask1:
    @pytest.fixture
    def person_a(self):
        return Person("User", "1", None)

    @pytest.fixture
    def person_b(self, person_a):
        return Person("User", "2", person_a)

    def test_mixed_data(self, capsys, person_b):
        data = {
            "key1": 1,
            "key2": {
                "key3": 1,
                "key4": {
                    "key5": 4,
                    "user": person_b,
                }
            },
        }
        print_depth(data)
        out, err = capsys.readouterr()
        assert out == (
            "key1 1\n"
            "key2 1\n"
            "key3 2\n"
            "key4 2\n"
            "key5 3\n"
            "user 3\n"
            "first_name: 4\n"
            "last_name: 4\n"
            "father: 4\n"
            "first_name: 5\n"
            "last_name: 5\n"
            "father: 5\n"
        )
        assert err == ""

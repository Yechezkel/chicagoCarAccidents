from routes.accident_bp import *

def test_get_accidents_by_zone():
    assert len(get_accidents_by_zone(1651)) == 1663
    assert len(get_accidents_by_zone(165)) == 0

def test_get_accidents_by_zone_and_date():
    assert len(get_accidents_by_zone_and_date(1651, datetime(2019, 2, 19),3)) == 3

def test_get_accidents_by_zone_and_cause():
    assert get_accidents_by_zone_and_cause(225)[None]["total_accidents"] == 2022

def test_get_injures_by_zone():
    assert get_injures_by_zone(225)[0]["caused_death"] == 5 and get_injures_by_zone(225)[0]["not_caused_death"] == 369
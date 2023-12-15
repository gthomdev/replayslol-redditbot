from replayslol_reddit_scraper.url_element_extractor import URLElementExtractor
import pytest


@pytest.mark.parametrize("link, expected_result", [
    # op.gg links
    ("https://www.op.gg/summoners/euw/Goated%20Tre", "euw"),
    ("https://www.op.gg/summoners/na/Goated%20Tre", "na"),
    ("https://www.op.gg/summoners/kr/Goated%20Tre", "kr"),
    ("https://www.op.gg/summoners/oce/Goated%20Tre", "oce"),
    ("https://www.op.gg/summoners/jp/Goated%20Tre", "jp"),
    ("https://www.op.gg/summoners/br/Goated%20Tre", "br"),
    ("https://www.op.gg/summoners/eune/Goated%20Tre", "eune"),
    ("https://www.op.gg/summoners/las/Goated%20Tre", "las"),
    ("https://www.op.gg/summoners/lan/Goated%20Tre", "lan"),
    ("https://www.op.gg/summoners/tr/Goated%20Tre", "tr"),
    ("https://www.op.gg/summoners/ru/Goated%20Tre", "ru"),
    ("https://www.op.gg/summoners/sg/Goated%20Tre", "sg"),
    ("https://www.op.gg/summoners/ph/Goated%20Tre", "ph"),
    ("https://www.op.gg/summoners/tw/Goated%20Tre", "tw"),
    ("https://www.op.gg/summoners/vn/Goated%20Tre", "vn"),
    ("https://www.op.gg/summoners/th/Goated%20Tre", "th"),
    # u.gg links
    ("https://u.gg/lol/profile/euw1/exoll/overview", "euw"),
    ("https://u.gg/lol/profile/euw2/exoll/overview", "euw"),
    ("https://u.gg/lol/profile/na1/exoll/overview", "na"),
    ("https://u.gg/lol/profile/na2/exoll/overview", "na"),
    ("https://u.gg/lol/profile/kr1/exoll/overview", "kr"),
    ("https://u.gg/lol/profile/kr2/exoll/overview", "kr"),
    ("https://u.gg/lol/profile/oce1/exoll/overview", "oce"),
    ("https://u.gg/lol/profile/oce2/exoll/overview", "oce"),
    ("https://u.gg/lol/profile/jp1/exoll/overview", "jp"),
    ("https://u.gg/lol/profile/jp2/exoll/overview", "jp"),
    ("https://u.gg/lol/profile/br1/exoll/overview", "br"),
    ("https://u.gg/lol/profile/br2/exoll/overview", "br"),
    ("https://u.gg/lol/profile/eune1/exoll/overview", "eune"),
    ("https://u.gg/lol/profile/eune2/exoll/overview", "eune"),
    ("https://u.gg/lol/profile/las1/exoll/overview", "las"),
    ("https://u.gg/lol/profile/las2/exoll/overview", "las"),
    ("https://u.gg/lol/profile/lan1/exoll/overview", "lan"),
    ("https://u.gg/lol/profile/lan2/exoll/overview", "lan"),
    ("https://u.gg/lol/profile/tr1/exoll/overview", "tr"),
    ("https://u.gg/lol/profile/ru1/exoll/overview", "ru"),
    ("https://u.gg/lol/profile/sg1/exoll/overview", "sg"),
    ("https://u.gg/lol/profile/ph1/exoll/overview", "ph"),
    ("https://u.gg/lol/profile/tw1/exoll/overview", "tw"),
    ("https://u.gg/lol/profile/vn1/exoll/overview", "vn"),
    ("https://u.gg/lol/profile/th1/exoll/overview", "th"),
    # blitz links
    ("https://blitz.gg/lol/profile/euw1/exoll", "euw"),
    ("https://blitz.gg/lol/profile/euw2/exoll", "euw"),
    ("https://blitz.gg/lol/profile/na1/exoll", "na"),
    ("https://blitz.gg/lol/profile/na2/exoll", "na"),
    ("https://blitz.gg/lol/profile/kr1/exoll", "kr"),
    ("https://blitz.gg/lol/profile/kr2/exoll", "kr"),
    ("https://blitz.gg/lol/profile/oce1/exoll", "oce"),
    ("https://blitz.gg/lol/profile/oce2/exoll", "oce"),
    ("https://blitz.gg/lol/profile/jp1/exoll", "jp"),
    ("https://blitz.gg/lol/profile/jp2/exoll", "jp"),
    ("https://blitz.gg/lol/profile/br1/exoll", "br"),
    ("https://blitz.gg/lol/profile/br2/exoll", "br"),
    ("https://blitz.gg/lol/profile/eune1/exoll", "eune"),
    ("https://blitz.gg/lol/profile/eune2/exoll", "eune"),
    ("https://blitz.gg/lol/profile/las1/exoll", "las"),
    ("https://blitz.gg/lol/profile/las2/exoll", "las"),
    ("https://blitz.gg/lol/profile/lan1/exoll", "lan"),
    ("https://blitz.gg/lol/profile/lan2/exoll", "lan"),
    ("https://blitz.gg/lol/profile/tr1/exoll", "tr"),
    ("https://blitz.gg/lol/profile/ru1/exoll", "ru"),
    ("https://blitz.gg/lol/profile/sg1/exoll", "sg"),
    ("https://blitz.gg/lol/profile/ph1/exoll", "ph"),
    ("https://blitz.gg/lol/profile/tw1/exoll", "tw"),
    ("https://blitz.gg/lol/profile/vn1/exoll", "vn"),
    ("https://blitz.gg/lol/profile/th1/exoll", "th")])
def test_extract_region(link, expected_result):
    result = URLElementExtractor.extract_region(link)
    assert result == expected_result


@pytest.mark.parametrize("link, expected_result", [
    ("https://www.op.gg/summoners/kr/%EB%8C%95%EC%B2%AD%EC%9E%87", True),
    ("https://euw.op.gg/summoners/euw/manouche%20zaatar", True),
    ("https://www.op.gg/summoners/eune/joona5", True),
    ("https://www.op.gg/summoners/na/FLY%20VicLa", True),
    ("https://www.op.gg/summoners/sg/%E6%9C%88%E6%86%94%E6%86%94%E5%A4%A7%E7%BE%8E%E5%A5%B3", True),
    ("https://www.op.gg/summoners/ph/Mafumafu", True),
    ("https://www.op.gg/summoners/br/twitch%20nicklink", True),
    ("https://www.op.gg/summoners/oce/LV1%20Daystar", True),
    ("https://www.op.gg/summoners/na/Recon419A", True),
    ("https://www.op.gg/summoners/na/Goated%20Tre?hl=en_US", True), ])
def test_has_matching_link(link, expected_result):
    result = URLElementExtractor.has_matching_link(link)
    assert result == expected_result


def test_has_matching_link_should_return_true_when_link_matches_pattern():
    link = "https://www.op.gg/summoners/euw/Goated%20Tre"
    result = URLElementExtractor.has_matching_link(link)
    assert result is True


def test_extract_region_should_return_none_when_url_does_not_contain_a_region():
    link = "https://www.op.gg/summoners/Goated%20Tre"
    result = URLElementExtractor.extract_region(link)
    assert result is None


def test_extract_summoner_should_return_summoner_name_when_url_contains_locale_query_parameter():
    link = "https://www.op.gg/summoners/na/Goated%20Tre?hl=en_US"
    result = URLElementExtractor.extract_summoner(link)
    assert result == "Goated%20Tre"


def test_extract_summoner_should_return_summoner_name_when_url_contains_encoded_character():
    link = "https://euw.op.gg/summoners/euw/manouche%20zaatar"
    result = URLElementExtractor.extract_summoner(link)
    assert result == "manouche%20zaatar"


def test_extract_summoner_should_return_summoner_name_when_summoner_name_is_long():
    link = "https://www.op.gg/summoners/euw/%E4%B8%8D%E5%A5%BD%E6%84%8F%E6%80%9D"
    result = URLElementExtractor.extract_summoner(link)
    assert result == "%E4%B8%8D%E5%A5%BD%E6%84%8F%E6%80%9D"


def test_extract_summoner_should_return_summoner_name_when_summoner_name_contains_additional_element():
    link = "https://www.op.gg/summoners/euw/Junko%20Challenger/champions"
    result = URLElementExtractor.extract_summoner(link)
    assert result == "Junko%20Challenger"


def test_extract_summoner_should_return_summoner_name_when_url_contains_trailing_forward_slash():
    link = "https://www.op.gg/summoners/euw/Junko%20Challenger/"
    result = URLElementExtractor.extract_summoner(link)
    assert result == "Junko%20Challenger"

import unittest
from espn import app
from espn.league import League


class TestRegularSeasonPages(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_year(self):
        response = self.app.get("/regularSeason/season/1107328/2018", follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_performance(self):
        response = self.app.get("/regularSeason/performance/1107328", follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_records(self):
        response = self.app.get("/regularSeason/records/1107328", follow_redirects=True)
        self.assertEqual(response.status_code, 200)


class TestPostSeasonPages(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_performance(self):
        response = self.app.get('postseason/performance/1107328', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


class TestAllTimePages(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_performance(self):
        response = self.app.get("/alltime/performance/1107328", follow_redirects=True)
        self.assertEqual(response.status_code, 200)


class TestLeagueObject(unittest.TestCase):

    def test_league_init(self):
        testLeague = League(1107328)
        league_id = testLeague.id
        self.assertEqual(league_id, 1107328)

    def test_playoffCount(self):
        testLeague = League(1107328)
        playoffCount = testLeague.playoffTeamCount
        self.assertEqual(playoffCount, 6)


if __name__ == '__main__':
    unittest.main()

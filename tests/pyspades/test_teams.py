# -*- encoding: utf-8 -*-
"""
test pyspades/teams.pyx
"""

from twisted.trial import unittest

from pyspades.team import Team


class TestTeams(unittest.TestCase):
    name = "Team name"
    color = (255, 0, 255)

    def test_initial_values(self):
        team = Team(0, self.name, self.color, False, None)
        self.assertEquals(0, team.kills)
        self.assertEquals(0, team.score)

    def test_team_from_team(self):
        team_template = Team(0, self.name, self.color, False, None)
        team_template.kills = 9
        team_template.score = 5
        team = Team(team_template)
        self.assertEquals(0, team.kills)
        self.assertEquals(0, team.score)
        self.assertEquals(team_template.name, team.name)
        self.assertEquals(team_template.color, team.color)

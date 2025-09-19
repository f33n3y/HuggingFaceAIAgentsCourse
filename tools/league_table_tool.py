from smolagents import Tool


class LeagueTableTool(Tool):
    name = "league_table_lookup"
    description = ("This tool allows you to lookup a Scottish football league table using a team's name. "
                   "It will returns the number of points that team has")
    inputs = {
        "football_team_name": {
            "type": "string",
            "description": "The name of a football team e.g. Celtic, Hearts, Hibs, Rangers, Aberdeen."
        }
    }

    output_type = "integer"

    def forward(self, football_team_name: str) -> int:
        league_table = {
            "Celtic": 10,
            "Hibs": 7,
            "Rangers": 6,
            "Aberdeen": 5,
            "Hearts": 3
        }
        return league_table[football_team_name]

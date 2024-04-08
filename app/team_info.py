from dataclasses import dataclass
from typing import List

@dataclass
class Team:
    name: str
    description: str
    members: list[str]

TEAM = {
    "Procurement":Team(
        "Procurement",
        "Procure and cook the meals for the class week and clean up",
        ["Bri", "Ryan", "Kera"]),
    "Documentation":Team(
        "Documentation",
        "Photography and handle social media posts at least twice a week",
        ["Justin Jenkins", "Kariel Mosley"]),
    "Management":Team(
        "Management",
        "Manage the other teams, make list of cleaning duties for 6 weeks, and reach out and acquire guest speakers for class",
        ["Kelvin Owens", "Nathan Griggs"])
}
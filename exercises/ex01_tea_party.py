"""ex 01 tea party program yay"""

__author__ = "730769478"


def main_planner(guests: int) -> None:
    """entry point of da program"""
    print("A Cozy Tea Party for", guests, "People")
    print("Tea Bags:", tea_bags(people=guests))
    print("Treats:", treats(people=guests))
    print("Cost: $" + str(cost(tea_bags(people=guests), treats(people=guests))))


def tea_bags(people: int) -> int:
    """i assume itll define how many tea bags itll take"""
    return people * 2


def treats(people: int) -> int:
    """how many treats im gonna need"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """take a guess what this function does"""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))

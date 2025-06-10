class Player:
    def __init__(self, name: str, age: int, position: str) -> None:
        self.name = name
        self.age = age
        self.position = position

    def __str__(self) -> str:
        return f"Name: {self.name} \n Age: {self.age} \n Position:{self.position}"

class Team:
    def __init__(self, team_name: str, main_coach: str) -> None:
        self.team_name = team_name
        self.main_coach = main_coach
        self.list_of_players = []

    def add_player(self, player) -> None:
        self.list_of_players.append(player)

    def remove_player(self, player) -> None:
        self.list_of_players.remove(player)

    def list_players(self) -> None:
        print(f"Team: {self.team_name}")
        for player in self.list_of_players:
            print(player)


if __name__ == "__main__":
    # Создаем игроков
    player1 = Player("Иванов", 25, "Нападающий")
    player2 = Player("Петров", 30, "Полузащитник")
    player3 = Player("Сидоров", 28, "Защитник")

    # Создаем команды
    team1 = Team("Красные", "Краснов")
    team2 = Team("Синие", "Синёв")

    # Добавляем игроков в команды
    team1.add_player(player1)
    team1.add_player(player2)
    team2.add_player(player3)

    # Выводим список игроков в командах
    team1.list_players()
    team2.list_players()

    # Удаляем игрока из команды
    team1.remove_player(player2)

    # Выводим обновленный список игроков
    team1.list_players()


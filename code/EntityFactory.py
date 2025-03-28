from code.Constants import WIN_WIDTH
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'Player':
                return Player("Player", (WIN_WIDTH / 2, 465))
            case 'Zombie_1':
                pass
            case 'Zombie_2':
                pass
            case 'Zombie_3':
                pass
            case 'Zombie_4':
                pass

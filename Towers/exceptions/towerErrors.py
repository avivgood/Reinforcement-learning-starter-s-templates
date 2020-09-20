class InvalidTowerOperationError(Exception):
    pass


class TowersAreNotConnectedError(InvalidTowerOperationError):
    pass


class InsufficientTroopCountError(InvalidTowerOperationError):
    pass


class TowerOperationPreformedOnTheWrongTeamError(InvalidTowerOperationError):
    pass


class InvalidTowerDataError(ValueError):
    pass


class TowerIDAlreadyExistsError(InvalidTowerDataError):
    pass

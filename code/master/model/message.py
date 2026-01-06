from dataclasses import dataclass, field
from uuid import uuid4


@dataclass(frozen=True)
class Action:
    # M -> Move | # H -> Home | N -> Nothing
    action: str
    slave: int
    clock: int
    clock_hand: int
    position: int
    speed: int

    def build_action(self) -> str:
        if self.action == 'N':
            return f'[{self.action}]s{self.slave}c{self.clock}ch{self.clock_hand}'

        if self.action == 'H':
            return f'[{self.action}]s{self.slave}c{self.clock}ch{self.clock_hand}sp{self.speed}'

        return f'[{self.action}]s{self.slave}c{self.clock}ch{self.clock_hand}p{self.position}sp{self.speed}'


@dataclass
class MessageBuilder:
    actions: list[Action]

    def __init__(self, message_id=''):
        self.actions = []
        self._message_id = message_id

    def clear(self):
        self._message_id = ''
        self.actions.clear()

    def set_move(self, slave, clock, clock_hand, position, speed):
        # Key (slave, clock, clock_hand) -> Check if the action was previously added, if so, remove the previous one.
        idx_to_remove = None
        for i, action in enumerate(self.actions):
            if action.slave == slave and action.clock == clock and action.clock_hand == clock_hand:
                idx_to_remove = i
                break

        if idx_to_remove is not None:
            self.actions.pop(idx_to_remove)

        self.actions.append(
            Action('M', slave, clock, clock_hand, position, speed))

    def set_home(self, slave, clock, clock_hand, speed):
        self.actions.append(
            Action('H', slave, clock, clock_hand, 0, speed)
        )

    def build_command(self):
        final_message = ''
        for action in self.actions:
            final_message += action.build_action()


from typing import Iterator

from InquirerPy import inquirer


class ActionSource:
	def __init__(self):
		raise NotImplemented()
	
	def __iter__(self) -> Iterator[str]:
		raise NotImplemented()
	
class UserInput(ActionSource):
	def __init__(self):
		pass

	def __iter__(self) -> Iterator[str]:
		while True:
			yield inquirer.select(
				message="What action would you like to perform?",
				choices=[
					"play", "skip", "delete", "quit"
				],
			).execute()

	
class PreLoadedActionSource(ActionSource):
	def __init__(self, actions: list[str]):
		self.actions = actions
		self.action_generator = self.__create_actions_generator(actions)

	def __iter__(self) -> Iterator[str]:
		return self.action_generator

	def __create_actions_generator(self, actions) -> Iterator[str]:
		for action in actions:
			yield action

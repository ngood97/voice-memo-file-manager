from pathlib import Path
import random
import time
from typing import Iterable, Iterator
import simpleaudio
from simpleaudio.shiny import PlayObject

class AudioMemoDirectory(Iterable):
	def __init__(self, memo_dir: Path):
		# avoid dot underscore files
		self.memo_dir = memo_dir
		self.current_file_iter = memo_dir.glob('*')

	def __iter__(self) -> 'Iterator[AudioMemo]':
		while True:
			try:
				yield RealAudioMemo(next(self.current_file_iter))
			except StopIteration:
				return

class MockAudioMemoDirectory(AudioMemoDirectory):
	def __init__(self):
		self.audio_memos: list[MockAudioMemo] = []

	def get_audio_memos(self):
		return self.audio_memos

	def __iter__(self) -> 'Iterator[AudioMemo]':
		while True:
			new_audio_memo = MockAudioMemo()
			self.audio_memos.append(new_audio_memo)
			yield new_audio_memo


class AudioMemo:
	def __init__(self):
		raise NotImplemented()

	def play(self):
		raise NotImplemented()

	def delete(self):
		raise NotImplemented()
	
	def get_filepath(self) -> str:
		raise NotImplemented()
"▁▂▃▄▅▆▇█"

class RealAudioMemo(AudioMemo):
	ANIMATION_1 = "|/-\\"
	thingy = "▇█▇▆▅▄▃▂▁"
	thingy = "▇█▆▄▂"
	def __init__(self, filepath: Path):
		self.filepath = filepath
		self.is_deleted = False

	@staticmethod
	def cool_animation_thing_single_character(offset: int = 0):
		thingy = RealAudioMemo.thingy
		first = True

		if offset >= len(thingy):
			raise ValueError(f"offset cannot be longer than {len(thingy) -1}")

		while True:
			for idx, char in enumerate(thingy):
				if not (first and idx < offset):
					yield char

			for i in range(0, random.randint(0, 5)):
				yield "▁"
				
	@staticmethod
	def cool_animation_thing(length: int = 10):
		cool_animation_characters = []
		for i in range(length):
			offset = random.randint(0, len(RealAudioMemo.thingy) -1)
			cool_animation_characters.append(RealAudioMemo.cool_animation_thing_single_character(offset))
		
		while True:
			return_str = " "
			for animator in cool_animation_characters:
				return_str += next(animator)
			yield return_str

	@staticmethod
	def audio_animation_frame_generator():
		animation = RealAudioMemo.cool_animation_thing()
		while True:
			for frame in animation:
				print(frame, end="\r")
				yield


	def play(self):
		wave_obj = simpleaudio.WaveObject.from_wave_file(str(self.filepath))
		play_obj: PlayObject = wave_obj.play()
		frame_generator = self.audio_animation_frame_generator()
		while play_obj.is_playing():
			next(frame_generator)
			time.sleep(0.1)

	def delete(self):
		self.filepath.unlink(missing_ok=True)
		self.is_deleted = True

	def get_filepath(self) -> str:
		return str(self.filepath)


class MockAudioMemo(AudioMemo):
	def __init__(self):
		self.actions_performed: list[str] = []

	def play(self):
		self.actions_performed.append('play')

	def delete(self):
		self.actions_performed.append('delete')
		
	def get_actions_performed(self):
		return self.actions_performed
	
	def get_filepath(self) -> str:
		return "mock_filepath"

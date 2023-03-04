from pathlib import Path
from typing import Iterable, Iterator
import simpleaudio

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
				print("Reached the end of the directory! Restarting from the beginning...")
				self.current_file_iter = self.memo_dir.glob('*')
				yield RealAudioMemo(next(self.current_file_iter))

class MockAudioDirectory(AudioMemoDirectory):
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

class RealAudioMemo(AudioMemo):
	def __init__(self, filepath: Path):
		self.filepath = filepath
		self.is_deleted = False

	def play(self):
		wave_obj = simpleaudio.WaveObject.from_wave_file(str(self.filepath))
		play_obj = wave_obj.play()
		play_obj.wait_done()

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

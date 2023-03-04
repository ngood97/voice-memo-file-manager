from pathlib import Path
from typing import Iterable, Iterator
import simpleaudio

class AudioMemoDirectory(Iterable):
	def __init__(self, memo_dir: Path):
		# avoid dot underscore files
		self.current_file_iter = memo_dir.glob('*')

	def __iter__(self) -> 'Iterator[AudioMemo]':
		yield AudioMemo(next(self.current_file_iter))


class AudioMemo:
	def __init__(self, filepath: Path):
		self.filepath = filepath

	def play(self):
		print(f'playing file {self.filepath}!')
		wave_obj = simpleaudio.WaveObject.from_wave_file(str(self.filepath))
		play_obj = wave_obj.play()
		play_obj.wait_done()

	def delete(self):
		print(f'deleting file {self.filepath}')
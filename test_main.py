from pathlib import Path
from voice_memo_file_manager.audio_manager import AudioMemoDirectory, MockAudioMemoDirectory
from voice_memo_file_manager.commands import PreLoadedActionSource
from voice_memo_file_manager.__main__ import process_memo_directory


def test_skip_works():
	action_source = PreLoadedActionSource(['play', 'skip', 'play', 'quit'])

	mock_audio_directory = MockAudioMemoDirectory()

	process_memo_directory(action_source, mock_audio_directory)

	audio_memos = mock_audio_directory.get_audio_memos()

	assert len(audio_memos) == 2
	assert len(audio_memos[0].get_actions_performed()) == 1
	assert audio_memos[0].get_actions_performed()[0] == 'play'
	assert len(audio_memos[1].get_actions_performed()) == 1
	assert audio_memos[1].get_actions_performed()[0] == 'play'

def test_memo_manager_ends_gracefully():
	EMPTY_DIR = Path("artifacts/empty_memo_dir")
	try:
		for audio_memo in AudioMemoDirectory(EMPTY_DIR):
			pass
	except RuntimeError as e:
		if "generator raised StopIteration" in str(e):
			assert False, "AudioMemo iteration raised a StopIteration exception"
		else:
			raise e

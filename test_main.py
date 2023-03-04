

from audio_manager import MockAudioMemoDirectory
from commands import PreLoadedActionSource
from main import process_memo_directory


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
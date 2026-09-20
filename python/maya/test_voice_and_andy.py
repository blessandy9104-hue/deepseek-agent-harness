from maya_voice_startup import prepare_voice_command, status
from maya_chat import maya_local_command

voice = prepare_voice_command('Hello Maya')
assert voice['wake_phrase_matched'] == 'hello maya'
assert voice['action'] == 'wake_and_launch'
assert voice['microphone_started'] is False
assert voice['privileged_action_allowed'] is False
assert status()['microphone_listening_enabled'] is False

queries = {
    'Who is Andy?': 'Andy is my creator, owner, and human supervisor.',
    'Tell me who Andy is.': 'Andy is my creator, owner, and human supervisor.',
    'What do you know about Andy?': 'Andy is my creator, owner, and human supervisor.',
    'Do you know Andy?': 'Andy is my creator, owner, and human supervisor.',
}
for query, expected in queries.items():
    assert maya_local_command(query) == expected, query
warhol = maya_local_command('Who is Andy Warhol?')
assert warhol is None or 'creator, owner' not in warhol
print('voice_preparation=OK')
print('microphone_disabled=OK')
print('andy_identity_variants=OK')
print('andy_warhol_separation=OK')

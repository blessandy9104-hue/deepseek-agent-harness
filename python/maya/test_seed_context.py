from maya_chat import compact_seed_context

context = compact_seed_context()
assert 'Compact approved seed guidance' in context
assert 'world patterns' in context
assert 'current requests override it' in context
assert len(context) < 2200
assert 'external_actions' not in context
print('compact_seed_loaded=OK')
print('seed_bounded=OK')
print('current_request_precedence=OK')
print('no_action_authorization=OK')

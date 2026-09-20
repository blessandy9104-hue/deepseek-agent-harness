from maya_self_improvement import suggestion_summary
from maya_chat import maya_local_command

summary = suggestion_summary()
assert 'Mother Maya seed hypotheses' in summary
assert 'directional, not learned facts' in summary
assert 'verified outcomes' in summary
assert 'No verified learning suggestions are pending.' in summary
assert maya_local_command(':suggestions') == summary
print('mother_maya_seed_visible=OK')
print('seed_hypotheses_labeled=OK')
print('verified_learning_still_required=OK')
print('router_suggestions=OK')

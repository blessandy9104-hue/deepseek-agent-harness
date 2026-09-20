import argparse, json
from datetime import datetime, timezone
from pathlib import Path
ROOT = Path(__file__).resolve().parent

def load(name, default):
    path = ROOT / name
    if not path.exists(): return default
    return json.loads(path.read_text(encoding="utf-8"))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', default='andy_income_opportunity_report_candidate.json')
    args = ap.parse_args()
    profile = load('andy_profile.json', {})
    policy = load('maya_values_policy.json', {})
    report_policy = load('maya_opportunity_report.json', {})
    evidence_path = ROOT / 'andy_evidence_pending.jsonl'
    research_count = 0
    if evidence_path.exists():
        research_count = sum(1 for line in evidence_path.read_text(encoding="utf-8").splitlines() if '"category": "public_research"' in line)
    interests = profile.get('interests', [])
    interest_names = []
    for item in interests if isinstance(interests, list) else []:
        interest_names.append(item.get('label', item.get('key', '')) if isinstance(item, dict) else str(item))
    report = {
      'generated_at': datetime.now(timezone.utc).isoformat(),
      'status': 'review_only',
      'purpose': 'map income opportunities for Andy; no financial action is performed',
      'approved_interests_used': interest_names,
      'public_research_records_available': research_count,
      'opportunity_tracks': [
        {'track': 'skill_services', 'question': 'What service could Andy offer using existing skills?', 'first_experiment': 'define one small service and test demand before spending money'},
        {'track': 'digital_products', 'question': 'What reusable product could Andy create?', 'first_experiment': 'make a small prototype and seek feedback before building further'},
        {'track': 'automation', 'question': 'What repetitive problem could be turned into a useful tool?', 'first_experiment': 'identify one real problem and test a minimal workflow'},
        {'track': 'career_growth', 'question': 'Which skill or role could improve earning potential?', 'first_experiment': 'compare requirements, time, cost, and evidence of demand'},
        {'track': 'business_research', 'question': 'Which public market gaps or business models merit research?', 'first_experiment': 'compare multiple sources and write a risk-aware opportunity brief'}
      ],
      'required_analysis': report_policy.get('required_report_fields', []),
      'values_lenses': policy.get('available_lenses', policy.get('philosophical_lens', {}).get('available_lenses', [])),
      'must_show': ['tradeoffs', 'uncertainty', 'missing information', 'startup cost', 'time to first experiment', 'downside risks', 'sources', 'confidence', 'Andy-specific values'],
      'controls': report_policy.get('controls', {}),
      'final_note': 'This is research and planning, not a guarantee of income. Andy decides whether to pursue anything.',
      'activation': {'automatic': False, 'requires_andy_approval': True}
    }
    (ROOT / args.output).write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n', encoding="utf-8")
    print(json.dumps(report, indent=2, ensure_ascii=False))

if __name__ == '__main__': main()
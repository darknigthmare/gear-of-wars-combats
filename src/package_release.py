"""Assemble the reviewed first delivery without temporary renders or dependencies."""
from pathlib import Path
import hashlib
import json
import shutil
import zipfile

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT.parent
OUT = WORK / 'outputs/gears_combats_v1'
RENDER = WORK / 'tmp/qa/bible_release'


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    evidence = {}
    for report in sorted((ROOT / 'docs').glob('qa_*.json')):
        data = json.loads(report.read_text())
        for page in data.get('pages', []):
            if isinstance(page, dict) and page.get('sha256'):
                evidence.setdefault(page['sha256'], []).append(report.name)

    coverage = []
    for png in sorted(RENDER.glob('page-*.png'), key=lambda p: int(p.stem.split('-')[-1])):
        digest = sha256(png)
        coverage.append({
            'page': int(png.stem.split('-')[-1]),
            'sha256': digest,
            'visual_review_reports': evidence.get(digest, []),
        })
    missing = [p['page'] for p in coverage if not p['visual_review_reports']]
    if len(coverage) != 78 or missing:
        raise RuntimeError(f'Incomplete release review: {len(coverage)} pages; unreviewed {missing}')

    (ROOT / 'docs/release_visual_validation.json').write_text(json.dumps({
        'document': 'Gears_of_War_Combats_Bible_v1',
        'pages': 78,
        'coverage': coverage,
        'result': 'All final page images have visual-review evidence. Byte-identical pages reuse their previous review.',
    }, ensure_ascii=False, indent=2))
    shutil.copy2(WORK / 'tmp/qa/workbook/validation.json', ROOT / 'docs/workbook_validation.json')

    report = {
        'date': '2026-11-19',
        'document_pages': 78,
        'word_count_approx': 36068,
        'workbook_sheets': 14,
        'workbook_formula_errors': 0,
        'engine_tests_passed': 15,
        'data_validation': json.loads((ROOT / 'docs/data_validation.json').read_text()),
        'images_present': 6,
        'images_integrated': 2,
        'images_fidelity_approved': 0,
        'browser_visual_validation': 'Not run: environment blocked browser launch; canvas and JS checks completed.',
        'hardware_gamepad_validation': 'Not run',
        'canonical_art_fidelity': 'Pending comparison with precise game captures',
    }
    (ROOT / 'docs/release_validation.json').write_text(json.dumps(report, ensure_ascii=False, indent=2))

    deliverables = [
        'Gears_of_War_Combats_Bible_v1.pdf',
        'Gears_of_War_Combats_Bible_v1.docx',
        'Gears_of_War_Combats_Bible_v1.md',
        'Gears_of_War_Combats_Production.xlsx',
    ]
    destination = OUT / 'Gears_of_War_Combats_Pack_v1.zip'
    prefix = 'Gears_of_War_Combats_v1'
    records = []
    with zipfile.ZipFile(destination, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
        for source in sorted(ROOT.rglob('*')):
            if not source.is_file() or source.is_symlink():
                continue
            relative = source.relative_to(ROOT)
            if any(p.startswith('.') or p in ('node_modules', '__pycache__') for p in relative.parts):
                continue
            if relative.parts[:2] == ('prototype', 'qa') and source.suffix == '.png':
                continue
            archive.write(source, f'{prefix}/{relative.as_posix()}')
            records.append({'path': relative.as_posix(), 'bytes': source.stat().st_size, 'sha256': sha256(source)})
        for name in deliverables:
            source = OUT / name
            archive.write(source, f'{prefix}/livrables/{name}')
            records.append({'path': f'livrables/{name}', 'bytes': source.stat().st_size, 'sha256': sha256(source)})
        archive.writestr(f'{prefix}/CONTENTS.json', json.dumps(records, ensure_ascii=False, indent=2))
    with zipfile.ZipFile(destination) as archive:
        bad = archive.testzip()
        if bad:
            raise RuntimeError(f'Archive checksum failure: {bad}')
        count = len(archive.namelist())
    print(json.dumps({'archive': str(destination), 'files': count, 'bytes': destination.stat().st_size, 'sha256': sha256(destination), 'visual_review_pages': len(coverage)}, ensure_ascii=False))


if __name__ == '__main__':
    main()

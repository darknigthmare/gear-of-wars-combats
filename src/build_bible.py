from pathlib import Path
import re, json
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT.parent/'outputs/gears_combats_v1'
OUT.mkdir(parents=True,exist_ok=True)
doc=Document()
sec=doc.sections[0]
sec.page_width=Inches(8.5);sec.page_height=Inches(11)
sec.top_margin=Inches(.7);sec.bottom_margin=Inches(.65)
sec.left_margin=Inches(.8);sec.right_margin=Inches(.8)
sec.header_distance=Inches(.28);sec.footer_distance=Inches(.28)
styles=doc.styles
for n in ['Normal','Title','Subtitle','Heading 1','Heading 2','Heading 3','Heading 4','Caption','List Bullet','List Number']:
 st=styles[n];st.font.name='Arial';st.font.color.rgb=RGBColor(0,0,0)
 st.element.get_or_add_rPr().append(OxmlElement('w:rFonts')) if st.element.rPr is None else None
 st.paragraph_format.widow_control=True
styles['Normal'].font.size=Pt(11)
styles['Normal'].paragraph_format.space_after=Pt(6)
styles['Normal'].paragraph_format.line_spacing=1.07
styles['Title'].font.size=Pt(32);styles['Title'].font.bold=True
styles['Subtitle'].font.size=Pt(17)
for n,size in [('Heading 1',18),('Heading 2',14),('Heading 3',12),('Heading 4',11)]:
 styles[n].font.size=Pt(size);styles[n].font.bold=True
 styles[n].paragraph_format.space_before=Pt(14)
 styles[n].paragraph_format.space_after=Pt(7)
 styles[n].paragraph_format.keep_with_next=True
styles['Caption'].font.size=Pt(9)
styles['Caption'].font.italic=True
styles['Caption'].font.bold=False
styles['Caption'].paragraph_format.space_after=Pt(8)
# Remove bundled Word title rules and theme borders rather than inheriting them.
for style in styles:
 for border in list(style.element.iter(qn('w:pBdr'))):
  border.getparent().remove(border)
doc.core_properties.title='Gears of War Combats Bible de conception'
doc.core_properties.subject='Combat 2D et Boss Battle'
doc.core_properties.author='Darknigthmare'
doc.core_properties.keywords='Gears of War, bible, combat 2D, boss, parallax'

# Footer supports orientation in a long manual; all headings remain black.
p=sec.header.paragraphs[0];p.text='GEARS OF WAR COMBATS';p.runs[0].font.size=Pt(8)
footer=sec.footer.paragraphs[0];footer.alignment=WD_ALIGN_PARAGRAPH.RIGHT
r=footer.add_run('Bible de conception  •  ');r.font.size=Pt(8)
fld=OxmlElement('w:fldSimple');fld.set(qn('w:instr'),'PAGE');footer._p.append(fld)

def text_clean(t):
 t=t.replace('**','').replace('`','')
 t=re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)',r'\1 (\2)',t)
 return t.replace('\u2011','-').replace('\u2013','-').replace('\u2014','-')

def runs(p,text):
 # Preserve emphasis while rendering links as readable references.
 text=re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)',r'\1 (\2)',text)
 for i,part in enumerate(re.split(r'(\*\*.*?\*\*)',text)):
  r=p.add_run(text_clean(part));r.bold=part.startswith('**')
 return p

def heading(t,level):
 t=re.sub(r'[^\w\sÀ-ÿ]',' ',text_clean(t));t=re.sub(r'\s+',' ',t).strip()
 return doc.add_heading(t,level)

def paragraph(t,style=None):return runs(doc.add_paragraph(style=style),t)

def cell_text(cell,t,bold=False):
 cell.text='';p=cell.paragraphs[0];runs(p,t)
 p.paragraph_format.space_after=Pt(3);p.paragraph_format.space_before=Pt(3)
 p.paragraph_format.line_spacing=1.02
 for r in p.runs:r.font.size=Pt(9.5);r.bold=bold or r.bold
 cell.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER

def table(rows):
 if len(rows)<2:return
 cols=max(map(len,rows));t=doc.add_table(rows=0, cols=cols);t.alignment=WD_TABLE_ALIGNMENT.CENTER;t.autofit=False
 # Give descriptive columns room rather than making every column equal.
 lens=[sum(len(r[c]) if c<len(r) else 0 for r in rows)/len(rows) for c in range(cols)]
 weights=[max(7,min(v,70))**.6 for v in lens];widths=[6.9*w/sum(weights) for w in weights]
 for c,w in zip(t.columns,widths):c.width=Inches(w)
 for ri,row in enumerate(rows):
  cells=t.add_row().cells
  for ci,cell in enumerate(cells):
   cell.width=Inches(widths[ci]);cell_text(cell,row[ci] if ci<len(row) else '',ri==0)
   tcPr=cell._tc.get_or_add_tcPr();m=OxmlElement('w:tcMar')
   for side,v in [('top','65'),('left','85'),('bottom','65'),('right','85')]:
    e=OxmlElement('w:'+side);e.set(qn('w:w'),v);e.set(qn('w:type'),'dxa');m.append(e)
   tcPr.append(m)
   borders=OxmlElement('w:tcBorders')
   for side in ['top','left','bottom','right']:
    e=OxmlElement('w:'+side);e.set(qn('w:val'),'single');e.set(qn('w:sz'),'4');e.set(qn('w:color'),'D9D9D9');borders.append(e)
   tcPr.append(borders)
   shd=OxmlElement('w:shd');shd.set(qn('w:fill'),'29313A' if ri==0 else ('F1F3F5' if ri%2 else 'FFFFFF'));tcPr.append(shd)
   if ri==0:
    for run in cell.paragraphs[0].runs:run.font.color.rgb=RGBColor(255,255,255)
  pr=t.rows[-1]._tr.get_or_add_trPr()
  # Let very long rows split if necessary, but keep usual record rows intact.
  if max(map(len,row))<900:pr.append(OxmlElement('w:cantSplit'))
  if ri==0:pr.append(OxmlElement('w:tblHeader'))
 paragraph('')

def markdown(s,skip_top=False):
 # Some authored sections separate table records with blank lines.
 # Normalize only those gaps, preserving ordinary paragraph spacing.
 while re.search(r'(?m)(^\|[^\n]+\|[ \t]*\n)\n+(?=\|)',s):
  s=re.sub(r'(?m)(^\|[^\n]+\|[ \t]*\n)\n+(?=\|)',r'\1',s)
 lines=s.splitlines();i=0;in_code=False
 while i<len(lines):
  line=lines[i].strip()
  if not line:i+=1;continue
  if line.startswith('```'):in_code=not in_code;i+=1;continue
  if in_code:
   p=paragraph(line);p.paragraph_format.space_after=Pt(1)
   for r in p.runs:r.font.name='DejaVu Sans Mono';r.font.size=Pt(8)
   i+=1;continue
  m=re.match(r'^(#{1,6})\s+(.*)',line)
  if m:
   if not(skip_top and len(m[1])==1):heading(m[2],min(3,max(1,len(m[1])-1)))
   i+=1;continue
  if line.startswith('|') and i+1<len(lines) and re.match(r'^\s*\|?\s*:?-',lines[i+1]):
   rows=[]
   while i<len(lines) and lines[i].strip().startswith('|'):
    parts=[x.strip() for x in lines[i].strip().strip('|').split('|')]
    if not all(re.match(r'^:?-+:?$',x or ' ') for x in parts):rows.append(parts)
    i+=1
   table(rows);continue
  if re.match(r'^([-*]|\d+[.)])\s+',line):
   paragraph(re.sub(r'^([-*]|\d+[.)])\s+','',line),'List Bullet');i+=1;continue
  if line.startswith('> '):paragraph(line[2:]);i+=1;continue
  if line in ['---','***']:i+=1;continue
  paragraph(line);i+=1

# Cover
doc.add_paragraph('Gears of War Combats','Title')
doc.add_paragraph('Bible du mode de combat 2D','Subtitle')
paragraph('Duel  •  Histoire  •  Tournois  •  Boss Battle')
paragraph('Darknigthmare\nVersion 1  |  19 novembre 2026')
if (ROOT/'assets/stage_ephyra.png').exists():
 doc.add_picture(str(ROOT/'assets/stage_ephyra.png'),width=Inches(6.9))
 doc.add_paragraph('Ephyra — premier master de décor généré. Composition à valider et à séparer en couches.','Caption')
paragraph('Un jeu de combat de profil fondé sur les personnages, les armes et les créatures de Gears of War. Cette version définit le corpus, les systèmes et les contenus à produire, avec un prototype autonome pour essayer les premières mécaniques.')
paragraph('36 combattants  •  24 rencontres de boss  •  24 arènes\nLes fiches de conception et les réalisations sont suivies séparément.')
doc.add_page_break()
heading('Plan du document',1)
paragraph('Les titres constituent la navigation du document Word. Le classeur et les JSON associés contiennent les valeurs filtrables et les identifiants de production.')
for t in ['Vision et système de combat','Rechargement actif et exécutions','Histoire et tournois','Boss Battle et arènes en parallaxe','Direction artistique et animation','Roster et movesets détaillés','Boss stages et campagne détaillés','État du premier lot et prochaines productions']:
 paragraph(t,'List Bullet')
paragraph('Les scènes et mécaniques créées pour cette adaptation sont identifiées. Les références canoniques accompagnent les entrées ; les détails visuels non encore comparés aux jeux gardent leur statut de validation.')
doc.add_page_break()

files=['core_bible.md','roster_movesets.md','boss_stages_story.md','delivery_status.md']
full=[]
for i,name in enumerate(files):
 p=ROOT/'docs'/name
 if not p.exists():raise SystemExit('Required document missing: '+str(p))
 s=p.read_text();full.append(s)
 if i:doc.add_page_break()
 markdown(s,skip_top=(i==0))

art=ROOT/'assets'
images=[('marcus_reference.png','Marcus Fenix en pose neutre'),('kait_reference.png','Kait Diaz en pose neutre'),('stage_hollow.png','Le Hollow en décor complet')]
if any((art/n).exists() for n,_ in images):
 doc.add_page_break();heading('Premières références visuelles',1)
 paragraph('Ces illustrations sont les premières références de production. Les poses neutres ne sont pas des séquences animées et les décors complets ne sont pas encore des jeux de calques indépendants.')
 for n,label in images:
  p=art/n
  if p.exists():
   from PIL import Image
   im=Image.open(p);w,h=im.size
   doc.add_picture(str(p),width=Inches(min(6.9,4.5*w/h)))
   doc.add_paragraph(label+' — contrôle de fidélité à poursuivre.','Caption')

path=OUT/'Gears_of_War_Combats_Bible_v1.docx';doc.save(path)
(OUT/'Gears_of_War_Combats_Bible_v1.md').write_text('\n\n'.join(full))
print(json.dumps({'docx':str(path),'words':sum(len(s.split()) for s in full),'sections':len(doc.paragraphs)},ensure_ascii=False))

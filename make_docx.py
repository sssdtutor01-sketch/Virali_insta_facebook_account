# -*- coding: utf-8 -*-
from docx import Document
from docx.shared import Pt, RGBColor, Mm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

SAFFRON = "FF9933"
GREEN = "138808"
LIGHT_SAFF = "FFF5EC"
LIGHT_GREEN = "E8F5E9"
HINDI_FONT = "Nirmala UI"  # Windows default Hindi font

doc = Document()

# ---- Base font (incl. complex-script for Hindi) ----
style = doc.styles["Normal"]
style.font.name = HINDI_FONT
style.font.size = Pt(11)
rpr = style.element.get_or_add_rPr()
rf = rpr.find(qn('w:rFonts'))
if rf is None:
    rf = OxmlElement('w:rFonts'); rpr.append(rf)
for a in ('w:ascii', 'w:hAnsi', 'w:cs'):
    rf.set(qn(a), HINDI_FONT)

# page margins
for s in doc.sections:
    s.top_margin = Mm(14); s.bottom_margin = Mm(14)
    s.left_margin = Mm(16); s.right_margin = Mm(16)

def set_cs_font(run, name=HINDI_FONT):
    rpr = run._element.get_or_add_rPr()
    rf = rpr.find(qn('w:rFonts'))
    if rf is None:
        rf = OxmlElement('w:rFonts'); rpr.append(rf)
    for a in ('w:ascii', 'w:hAnsi', 'w:cs'):
        rf.set(qn(a), name)

def shade(paragraph, fill):
    pPr = paragraph._p.get_or_add_pPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear'); shd.set(qn('w:color'), 'auto'); shd.set(qn('w:fill'), fill)
    pPr.append(shd)

def left_border(paragraph, color, size=24):
    pPr = paragraph._p.get_or_add_pPr()
    pbdr = OxmlElement('w:pBdr')
    left = OxmlElement('w:left')
    left.set(qn('w:val'), 'single'); left.set(qn('w:sz'), str(size))
    left.set(qn('w:space'), '6'); left.set(qn('w:color'), color)
    pbdr.append(left); pPr.append(pbdr)

def section_head(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8); p.paragraph_format.space_after = Pt(4)
    shade(p, LIGHT_SAFF); left_border(p, SAFFRON)
    r = p.add_run(text); r.bold = True; r.font.size = Pt(13)
    r.font.color.rgb = RGBColor(0x22, 0x22, 0x22); set_cs_font(r)
    return p

def bullets(items):
    for it in items:
        p = doc.add_paragraph(style="List Bullet")
        p.paragraph_format.space_after = Pt(3)
        if isinstance(it, tuple):
            r = p.add_run(it[0]); r.bold = True; set_cs_font(r)
            r2 = p.add_run(it[1]); set_cs_font(r2)
        else:
            r = p.add_run(it); set_cs_font(r)

# ================= HEADER =================
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run("भारतीय जनता पार्टी — जिला दतिया (मध्य प्रदेश)"); r.bold = True; r.font.size = Pt(13); set_cs_font(r)
p.paragraph_format.space_after = Pt(2)

p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run("परिचय — पत्र"); r.bold = True; r.font.size = Pt(22)
r.font.color.rgb = RGBColor(0, 0, 0); set_cs_font(r)
p.paragraph_format.space_after = Pt(6)

# Objective box
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
shade(p, LIGHT_SAFF)
r = p.add_run("उद्देश्य: एक समर्पित, अनुशासित एवं संघर्षशील कार्यकर्ता — जिसका एकमात्र लक्ष्य "
              "दतिया जिले में संगठन को बूथ-स्तर तक सशक्त कर पार्टी को पुनः विजयी बनाना है।")
r.bold = True; r.font.size = Pt(11); set_cs_font(r)
p.paragraph_format.space_after = Pt(10)

# ================= PERSONAL INFO TABLE =================
info = [
    ("नाम", "एडवोकेट कप्तान सिंह कुशवाह"),
    ("पिता का नाम", "इंजीनियर रामस्वरूप सिंह कुशवाह (शासकीय सेवक, लोक निर्माण विभाग)"),
    ("जन्म तिथि", "05 जनवरी 1993"),
    ("शैक्षणिक योग्यता", "B.Sc (गणित), M.S.W (समाज कार्य), LL.B"),
    ("व्यवसाय", "1. श्री गिरिराज जी प्राइवेट ITI कॉलेज, दतिया\n2. जिला एवं सत्र न्यायालय (डिस्ट्रिक्ट कोर्ट), दतिया — अधिवक्ता, 4 वर्ष"),
    ("निवास स्थान", "रिछरा फाटक के बाहर, चिरईटोर माता मंदिर के पास, दतिया"),
    ("कार्यालय पता", "सेवड़ा चुंगी मार्ग, चिरईटोर माता, दतिया"),
    ("मोबाइल", "9584523005"),
    ("ईमेल", "singhdatkaptan@gmail.com"),
]
tbl = doc.add_table(rows=0, cols=2)
tbl.columns[0].width = Mm(45); tbl.columns[1].width = Mm(130)
for label, val in info:
    cells = tbl.add_row().cells
    pl = cells[0].paragraphs[0]; rl = pl.add_run(label); rl.bold = True
    rl.font.color.rgb = RGBColor(0x13, 0x88, 0x08); set_cs_font(rl)
    pv = cells[1].paragraphs[0]
    for i, line in enumerate(val.split("\n")):
        if i > 0: pv.add_run("\n")
        rv = pv.add_run(line); rv.bold = True; set_cs_font(rv)

doc.add_paragraph().paragraph_format.space_after = Pt(2)

# ================= SPECIAL ACHIEVEMENT =================
p = doc.add_paragraph(); shade(p, LIGHT_GREEN); left_border(p, GREEN)
r = p.add_run("★ विशेष उपलब्धि — बूथ क्रमांक 156"); r.bold = True; r.font.size = Pt(12)
r.font.color.rgb = RGBColor(0x0a, 0x7d, 0x0a); set_cs_font(r)
p2 = doc.add_paragraph(); shade(p2, LIGHT_GREEN)
r2 = p2.add_run("हाल के दतिया उपचुनाव में पूरे जिले में पराजय के बावजूद, मेरे प्रभार वाले बूथ "
                "क्रमांक 156 पर पार्टी को विजय/बढ़त प्राप्त हुई — जो मेरी बूथ-स्तरीय पकड़ का प्रमाण है।")
set_cs_font(r2)
p2.paragraph_format.space_after = Pt(8)

# ================= SECTIONS =================
section_head("संगठनात्मक अनुभव (12 वर्ष का समर्पण)")
bullets([
    ("वर्तमान दायित्व : ", "जिला उपाध्यक्ष, भारतीय जनता युवा मोर्चा, दतिया"),
    ("पूर्व दायित्व : ", "जिला मंत्री, भारतीय जनता युवा मोर्चा, दतिया (2020)"),
    ("चुनावी दायित्व : ", "पोलिंग प्रभारी — बूथ क्रमांक 156"),
    "विगत 12 वर्षों से पार्टी में निरंतर सक्रिय एवं समर्पित कार्यकर्ता।",
    "मुख्यमंत्री, मंत्रीगण व विधायकों के दतिया आगमन पर निरंतर सहभागिता व समन्वय।",
    "बूथ स्तर से जिला स्तर तक संगठन को मज़बूत करने का व्यावहारिक अनुभव।",
])

section_head("संगठन के प्रति अटूट निष्ठा एवं समर्पण")
bullets([
    "पार्टी के हर दौर में — सुख हो या चुनौती — संगठन के प्रति पूर्ण निष्ठा के साथ निरंतर सक्रिय रहा।",
    "23 मई 2026 को माननीय डॉ. नरोत्तम मिश्रा जी द्वारा आयोजित कार्यक्रम में सक्रिय सहभागिता कर, संगठन को और अधिक सशक्त करने हेतु कार्य किया।",
    "23 मई 2026 को संगठन को मज़बूत करने का दृढ़ संकल्प लेकर बूथ-स्तर तक जनसंपर्क तेज़ किया।",
    "उपचुनाव में पार्टी के प्रत्याशी चयन का पूर्ण सम्मान करते हुए — व्यक्ति नहीं, बल्कि \"कमल\" एवं विचारधारा को सर्वोपरि रखते हुए — कठिन परिस्थितियों में भी पूरी शक्ति से प्रचार किया।",
    "पार्टी हित सर्वोपरि — यही मेरी कार्यशैली एवं पहचान है।",
])

section_head("वैचारिक एवं सामाजिक पृष्ठभूमि")
bullets([
    "राष्ट्रीय स्वयंसेवक संघ (RSS) के प्रत्येक कार्यक्रम/आयोजन में निरंतर सहभागिता।",
    "M.S.W एवं अधिवक्ता होने के नाते जनसेवा व निःशुल्क कानूनी सहायता में सक्रिय।",
    "राष्ट्रवादी विचारधारा, पार्टी अनुशासन व संगठन के प्रति पूर्ण निष्ठा।",
])

section_head("दतिया जिले हेतु संकल्प / विज़न")
bullets([
    "बूथ-स्तर तक संगठन को पुनः सशक्त कर हर कार्यकर्ता को सक्रिय व सम्मानित करना।",
    "पार्टी की नीतियों व जनकल्याणकारी योजनाओं को घर-घर पहुँचाना।",
    "युवाओं व समाज के हर वर्ग को जोड़कर दतिया को पार्टी का मज़बूत गढ़ बनाना।",
])

section_head("सोशल मीडिया / जनसंपर्क (अनेक पोस्ट व रील वायरल)")
bullets([
    "Instagram : @adv.KaptanSingh",
    "Facebook : adv.KaptanSingh1",
    "Facebook Page : adv.KaptanSingh",
    "Twitter (X) : @adv.KaptanSingh",
    "Threads : @adv.KaptanSingh",
])
p = doc.add_paragraph()
r = p.add_run("रुचि : "); r.bold = True; r.font.color.rgb = RGBColor(0x13,0x88,0x08); set_cs_font(r)
r2 = p.add_run("समाज सेवा, जनसंपर्क एवं संगठनात्मक कार्य"); set_cs_font(r2)

# ================= PHOTO APPENDIX (editable table) =================
section_head("फोटो परिशिष्ट (यहाँ फोटो लगाएँ)")
labels = ["वरिष्ठ नेताओं के साथ - फोटो 1","वरिष्ठ नेताओं के साथ - फोटो 2","वरिष्ठ नेताओं के साथ - फोटो 3",
          "कार्यक्रम - फोटो 4","कार्यक्रम - फोटो 5","कार्यक्रम - फोटो 6"]
pt = doc.add_table(rows=2, cols=3); pt.style = "Table Grid"
idx = 0
for row in pt.rows:
    row.height = Mm(30)
    for c in row.cells:
        pp = c.paragraphs[0]; pp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        rr = pp.add_run(labels[idx]); rr.font.size = Pt(9); rr.font.color.rgb = RGBColor(0x88,0x88,0x88); set_cs_font(rr)
        idx += 1

doc.add_paragraph().paragraph_format.space_after = Pt(2)
section_head("वायरल पोस्ट / रील (यहाँ स्क्रीनशॉट लगाएँ)")
vt = doc.add_table(rows=1, cols=6); vt.style = "Table Grid"
vlabels = ["पोस्ट/रील 1","पोस्ट/रील 2","पोस्ट/रील 3","पोस्ट/रील 4","पोस्ट/रील 5","QR कोड"]
vt.rows[0].height = Mm(34)
for i, c in enumerate(vt.rows[0].cells):
    pp = c.paragraphs[0]; pp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    rr = pp.add_run(vlabels[i]); rr.font.size = Pt(9); rr.font.color.rgb = RGBColor(0x88,0x88,0x88); set_cs_font(rr)

# ================= SIGN OFF =================
doc.add_paragraph()
p = doc.add_paragraph()
r = p.add_run("दिनांक: ____________          स्थान: दतिया          हस्ताक्षर: एडवोकेट कप्तान सिंह कुशवाह")
r.bold = True; set_cs_font(r)

p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run("जय हिन्द • जय भाजपा"); r.bold = True; r.font.size = Pt(15)
r.font.color.rgb = RGBColor(0xFF,0x99,0x33); set_cs_font(r)

out = "/projects/sandbox/Virali_insta_facebook_account/Bio-Data-Kaptan-Singh.docx"
doc.save(out)
print("Saved styled DOCX ->", out)

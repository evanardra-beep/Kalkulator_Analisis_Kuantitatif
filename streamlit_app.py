import streamlit as st

st.set_page_config(
    page_title="Kalkulator Analisis Kuantitatif",
    page_icon="⚗️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Mono:wght@400;500&family=DM+Sans:wght@300;400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.main > div {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.badge {
    display: inline-block;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #5F5E5A;
    border: 1px solid #D3D1C7;
    border-radius: 999px;
    padding: 4px 14px;
    margin-bottom: 1rem;
}

.main-title {
    font-family: 'DM Serif Display', serif;
    font-size: 42px;
    line-height: 1.15;
    color: #1a1a1a;
    margin: 0 0 0.5rem;
}

.main-title em {
    font-style: italic;
    color: #1D9E75;
}

.subtitle {
    font-size: 15px;
    color: #6b6b6b;
    line-height: 1.6;
    max-width: 560px;
    margin-bottom: 2rem;
}

.divider {
    border: none;
    border-top: 1px solid #e8e8e8;
    margin: 0.5rem 0 2rem;
}

.section-label {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #9a9a9a;
    margin-bottom: 1rem;
}

.module-card {
    background: #ffffff;
    border: 1px solid #e8e8e8;
    border-radius: 14px;
    padding: 1.4rem 1.4rem 1.1rem;
    position: relative;
    overflow: hidden;
    transition: border-color 0.2s, transform 0.15s;
    height: 100%;
    cursor: pointer;
}

.module-card:hover {
    border-color: #aaa;
    transform: translateY(-2px);
    box-shadow: 0 4px 16px rgba(0,0,0,0.06);
}

.card-accent {
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    border-radius: 14px 14px 0 0;
}

.card-icon {
    width: 38px;
    height: 38px;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    margin-bottom: 0.9rem;
}

.card-num {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.06em;
    color: #b0b0b0;
    margin: 0 0 4px;
}

.card-title {
    font-size: 15px;
    font-weight: 500;
    color: #1a1a1a;
    margin: 0 0 7px;
    line-height: 1.3;
}

.card-desc {
    font-size: 13px;
    color: #7a7a7a;
    line-height: 1.55;
    margin: 0 0 1rem;
}

.tag-row {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
}

.tag {
    font-size: 11px;
    font-family: 'DM Mono', monospace;
    padding: 2px 9px;
    border-radius: 999px;
    border: 1px solid #e0e0e0;
    color: #7a7a7a;
}

.footer-bar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding-top: 1.5rem;
    border-top: 1px solid #e8e8e8;
    margin-top: 1rem;
}

.footer-text {
    font-size: 12px;
    color: #b0b0b0;
}

.footer-text b {
    color: #6b6b6b;
}

.formula-box {
    background: #f7f9fc;
    border: 1px solid #e0eaf5;
    border-radius: 10px;
    padding: 1rem 1.2rem;
    font-family: 'DM Mono', monospace;
    font-size: 13px;
    color: #185FA5;
    text-align: center;
    letter-spacing: 0.04em;
    margin-top: 0.5rem;
}

/* Streamlit button override */
div.stButton > button {
    background: transparent;
    border: 1px solid #d0d0d0;
    border-radius: 10px;
    color: #1a1a1a;
    font-size: 13px;
    font-weight: 500;
    padding: 8px 20px;
    transition: background 0.15s;
}
div.stButton > button:hover {
    background: #f5f5f5;
    border-color: #aaa;
    color: #1a1a1a;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="badge">⚗ Kimia Analitik</div>', unsafe_allow_html=True)
st.markdown("""
<h1 class="main-title">Kalkulator <em>Analisis</em><br>Kuantitatif</h1>
<p class="subtitle">Alat perhitungan untuk kimia analitik — dari pengenceran sederhana hingga propagasi galat. Pilih modul untuk memulai.</p>
""", unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)
st.markdown('<p class="section-label">Modul tersedia — 5 topik</p>', unsafe_allow_html=True)

modules = [
    {
        "num": "01",
        "icon": "💧",
        "title": "Pengenceran Larutan",
        "desc": "Hitung volume atau konsentrasi pada proses pengenceran tunggal maupun bertingkat menggunakan hukum C₁V₁ = C₂V₂.",
        "tags": ["C₁V₁ = C₂V₂", "serial dilution", "faktor pengenceran"],
        "accent": "#1D9E75",
        "icon_bg": "#E1F5EE",
        "page": "pages/1_Pengenceran.py",
        "formula": "C₁V₁ = C₂V₂"
    },
    {
        "num": "02",
        "icon": "⇌",
        "title": "Satuan Konsentrasi & Stoikiometri",
        "desc": "Konversi antar satuan konsentrasi (M, m, %, ppm, ppb) dan hitung hubungan mol dalam reaksi kimia.",
        "tags": ["molaritas", "molalitas", "ppm / ppb", "mol ratio"],
        "accent": "#378ADD",
        "icon_bg": "#E6F1FB",
        "page": "pages/2_Konsentrasi.py",
        "formula": "M = n / V(L)"
    },
    {
        "num": "03",
        "icon": "📈",
        "title": "Kesetimbangan & Perubahan pH",
        "desc": "Teori asam-basa, hitung Ka/Kb, dan prediksi perubahan pH larutan setelah proses pengenceran.",
        "tags": ["Ka / Kb", "pH asam lemah", "pH basa lemah", "ΔpH"],
        "accent": "#EF9F27",
        "icon_bg": "#FAEEDA",
        "page": "pages/3_Kesetimbangan.py",
        "formula": "pH = ½(pKa − log C)"
    },
    {
        "num": "04",
        "icon": "🧪",
        "title": "Pembuatan Larutan Buffer",
        "desc": "Rancang buffer dengan pH target menggunakan persamaan Henderson–Hasselbalch, pilih pasangan asam-basa konjugat.",
        "tags": ["Henderson–Hasselbalch", "kapasitas buffer", "pKa"],
        "accent": "#7F77DD",
        "icon_bg": "#EEEDFE",
        "page": "pages/4_Buffer.py",
        "formula": "pH = pKa + log([A⁻]/[HA])"
    },
    {
        "num": "05",
        "icon": "±",
        "title": "Galat & Propagasi Error",
        "desc": "Hitung ketidakpastian hasil pengukuran: galat absolut, relatif, dan propagasi error untuk operasi penjumlahan, perkalian, dan fungsi.",
        "tags": ["galat absolut", "galat relatif", "propagasi", "RSD"],
        "accent": "#D85A30",
        "icon_bg": "#FAECE7",
        "page": "pages/5_Galat.py",
        "formula": "δf = √(Σ(∂f/∂xᵢ · δxᵢ)²)"
    },
]

cols = st.columns(3)
for i, mod in enumerate(modules[:3]):
    with cols[i]:
        st.markdown(f"""
        <div class="module-card">
            <div class="card-accent" style="background:{mod['accent']};"></div>
            <div class="card-icon" style="background:{mod['icon_bg']}; font-size:20px; display:flex; align-items:center; justify-content:center;">
                {mod['icon']}
            </div>
            <p class="card-num">{mod['num']}</p>
            <p class="card-title">{mod['title']}</p>
            <p class="card-desc">{mod['desc']}</p>
            <div class="tag-row">
                {"".join(f'<span class="tag">{t}</span>' for t in mod['tags'])}
            </div>
            <div class="formula-box">{mod['formula']}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

cols2 = st.columns([1, 1, 1])
for i, mod in enumerate(modules[3:]):
    with cols2[i]:
        st.markdown(f"""
        <div class="module-card">
            <div class="card-accent" style="background:{mod['accent']};"></div>
            <div class="card-icon" style="background:{mod['icon_bg']}; font-size:20px; display:flex; align-items:center; justify-content:center;">
                {mod['icon']}
            </div>
            <p class="card-num">{mod['num']}</p>
            <p class="card-title">{mod['title']}</p>
            <p class="card-desc">{mod['desc']}</p>
            <div class="tag-row">
                {"".join(f'<span class="tag">{t}</span>' for t in mod['tags'])}
            </div>
            <div class="formula-box">{mod['formula']}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<div class="footer-bar">
    <span class="footer-text"><b>5 modul</b> · kimia analitik kuantitatif</span>
    <span class="footer-text">Gunakan sidebar atau navigasi di atas untuk membuka modul</span>
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.info("💡 Navigasi ke setiap modul melalui **sidebar kiri** (klik tanda > jika tersembunyi), atau tambahkan file halaman di folder `pages/`.")
st.set_page_config(page_title="Galat & Propagasi Error", page_icon="±", layout="wide")
 
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=DM+Sans:wght@300;400;500&display=swap');
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
.formula-box { background:#FAECE7; border:1px solid #F0997B; border-radius:10px; padding:10px 16px;
               font-family:'DM Mono',monospace; font-size:14px; color:#4A1B0C; text-align:center; margin:1rem 0; }
.result-card { background:#fff5f2; border:1.5px solid #D85A30; border-radius:12px; padding:1rem 1.4rem; margin-top:1rem; }
.result-label { font-size:11px; color:#993C1D; font-family:'DM Mono',monospace; text-transform:uppercase; letter-spacing:.07em; margin:0 0 4px; }
.result-value { font-size:30px; font-weight:500; color:#4A1B0C; margin:0; font-family:'DM Mono',monospace; }
.result-unit  { font-size:14px; color:#D85A30; }
.step-box { background:#fafafa; border:1px solid #e0e0e0; border-left:3px solid #D85A30;
            border-radius:8px; padding:10px 14px; margin-top:8px;
            font-size:12.5px; color:#555; font-family:'DM Mono',monospace; line-height:1.9; }
</style>""", unsafe_allow_html=True)
 
st.markdown("""
<div style="border-left:4px solid #D85A30;padding-left:1rem;margin-bottom:1.5rem">
  <p style="font-family:'DM Mono',monospace;font-size:11px;color:#9a9a9a;letter-spacing:.08em;margin:0">MODUL 05</p>
  <h2 style="font-size:26px;font-weight:500;color:#1a1a1a;margin:4px 0 4px">± Galat & Propagasi Error</h2>
  <p style="font-size:14px;color:#7a7a7a;margin:0">Hitung ketidakpastian dan perambatan galat pengukuran</p>
</div>""", unsafe_allow_html=True)
 
tab1, tab2, tab3 = st.tabs(["📏 Galat Absolut & Relatif", "⚡ Propagasi Error", "📊 Statistik (SD & RSD)"])
 
with tab1:
    st.markdown('<div class="formula-box">Δx = |x_ukur − x_benar| &nbsp;|&nbsp; Galat relatif = (Δx / x_benar) × 100%</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        xu = st.number_input("Nilai terukur (x_ukur)",        value=9.87, step=0.001, format="%.5f")
        xb = st.number_input("Nilai benar / referensi (x_benar)", value=10.00, step=0.001, format="%.5f")
    abs_e = abs(xu - xb)
    rel_e = abs_e / abs(xb) * 100 if xb != 0 else 0
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f'<div class="result-card"><p class="result-label">Galat Absolut (Δx)</p><p class="result-value">{abs_e:.5g}</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="result-card"><p class="result-label">Galat Relatif</p><p class="result-value">{rel_e:.4f} <span class="result-unit">%</span></p></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="step-box">Δx = |{xu} − {xb}| = <b>{abs_e:.5g}</b><br>Galat relatif = ({abs_e:.5g}/{abs(xb)}) × 100 = <b>{rel_e:.4f}%</b></div>', unsafe_allow_html=True)
 
with tab2:
    op = st.selectbox("Operasi:", [
        "Penjumlahan / Pengurangan (x ± y)",
        "Perkalian / Pembagian (x × y atau x/y)",
        "Pemangkatan (xⁿ)",
        "Logaritma natural ln(x)",
        "Logaritma basis-10 log(x)"
    ])
    col1, col2 = st.columns(2)
    with col1:
        x  = st.number_input("Nilai x", value=10.0, step=0.001, format="%.5f")
        dx = st.number_input("Ketidakpastian δx", min_value=0.0, value=0.05, step=0.001, format="%.5f")
    with col2:
        if "±" in op or "×" in op:
            y  = st.number_input("Nilai y", value=5.0, step=0.001, format="%.5f")
            dy = st.number_input("Ketidakpastian δy", min_value=0.0, value=0.03, step=0.001, format="%.5f")
        elif "xⁿ" in op:
            n = st.number_input("Eksponen n", value=2.0, step=0.1, format="%.3f")
        
    if "±" in op:
        f    = x + y
        df   = math.sqrt(dx**2 + dy**2)
        steps = f"f = x+y = {x}+{y} = {f:.5g}<br>δf = √(δx²+δy²) = √({dx}²+{dy}²) = <b>{df:.5g}</b>"
        lbl   = "f = x + y"
    elif "×" in op:
        f    = x * y
        rf   = math.sqrt((dx/x)**2 + (dy/y)**2) if x and y else 0
        df   = abs(f) * rf
        steps = f"f = {x}×{y} = {f:.5g}<br>δf/f = √((δx/x)²+(δy/y)²) = {rf:.5g}<br>δf = <b>{df:.5g}</b>"
        lbl   = "f = x × y"
    elif "xⁿ" in op:
        f    = x**n
        df   = abs(n * x**(n-1)) * dx
        steps = f"f = {x}^{n} = {f:.5g}<br>δf = |n·x^(n-1)|·δx = {df:.5g}"
        lbl   = f"f = x^{n}"
    elif "ln" in op:
        f    = math.log(abs(x)) if x > 0 else float('nan')
        df   = dx / abs(x) if x != 0 else float('nan')
        steps = f"f = ln({x}) = {f:.5g}<br>δf = δx/x = {dx}/{x} = <b>{df:.5g}</b>"
        lbl   = "f = ln(x)"
    else:
        f    = math.log10(abs(x)) if x > 0 else float('nan')
        df   = dx / (abs(x) * math.log(10)) if x != 0 else float('nan')
        steps = f"f = log({x}) = {f:.5g}<br>δf = δx/(x·ln10) = {dx}/({x}×{math.log(10):.4f}) = <b>{df:.5g}</b>"
        lbl   = "f = log(x)"
 
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f'<div class="result-card"><p class="result-label">Nilai {lbl}</p><p class="result-value">{f:.5g}</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="result-card"><p class="result-label">Ketidakpastian δf</p><p class="result-value">± {df:.4g}</p></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="step-box">{steps}<br><br><b>Hasil: {f:.5g} ± {df:.4g}</b></div>', unsafe_allow_html=True)
 
with tab3:
    st.markdown('<div class="formula-box">x̄ = Σxᵢ/n &nbsp;|&nbsp; SD = √(Σ(xᵢ−x̄)²/(n−1)) &nbsp;|&nbsp; RSD = (SD/x̄)×100%</div>', unsafe_allow_html=True)
    raw = st.text_area("Data pengukuran (pisahkan dengan koma atau baris baru):", value="9.87, 9.92, 9.85, 9.90, 9.88", height=100)
    arr = []
    for token in raw.replace('\n', ',').split(','):
        token = token.strip()
        if token:
            try: arr.append(float(token))
            except: pass
    if len(arr) < 2:
        st.warning("Masukkan minimal 2 data.")
    else:
        n     = len(arr)
        mean  = sum(arr) / n
        var   = sum((x - mean)**2 for x in arr) / (n - 1)
        sd    = math.sqrt(var)
        rsd   = sd / abs(mean) * 100
        se    = sd / math.sqrt(n)
        ci95  = 1.96 * se  # approx normal
        col1, col2, col3, col4 = st.columns(4)
        with col1: st.markdown(f'<div class="result-card"><p class="result-label">Rata-rata (x̄)</p><p class="result-value">{mean:.5g}</p></div>', unsafe_allow_html=True)
        with col2: st.markdown(f'<div class="result-card"><p class="result-label">Std. Deviasi (SD)</p><p class="result-value">{sd:.4g}</p></div>', unsafe_allow_html=True)
        with col3: st.markdown(f'<div class="result-card"><p class="result-label">RSD (%)</p><p class="result-value">{rsd:.4f} <span class="result-unit">%</span></p></div>', unsafe_allow_html=True)
        with col4: st.markdown(f'<div class="result-card"><p class="result-label">Std. Error (SE)</p><p class="result-value">{se:.4g}</p></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="step-box">n = {n} &nbsp;|&nbsp; min = {min(arr)} &nbsp;|&nbsp; max = {max(arr)} &nbsp;|&nbsp; range = {max(arr)-min(arr):.4g}<br>x̄ = <b>{mean:.5g}</b> &nbsp;|&nbsp; SD = <b>{sd:.4g}</b> &nbsp;|&nbsp; RSD = <b>{rsd:.4f}%</b><br>SE = SD/√n = {sd:.4g}/√{n} = <b>{se:.4g}</b><br>CI 95% ≈ x̄ ± 1.96×SE = {mean:.5g} ± {ci95:.4g}</div>', unsafe_allow_html=True)

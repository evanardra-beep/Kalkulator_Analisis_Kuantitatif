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
# =====================================================
# PENGENCERAN
# =====================================================
if menu == "Pengenceran":

    st.header("Pengenceran Larutan")

    st.latex(r"M_1V_1=M_2V_2")

    M1 = st.number_input("M1 (M)", min_value=0.0)
    V1 = st.number_input("V1 (mL)", min_value=0.0)
    V2 = st.number_input("V2 (mL)", min_value=0.0)

    if st.button("Hitung Konsentrasi Akhir"):
        if V2 > 0:
            M2 = (M1 * V1) / V2
            st.success(f"M2 = {M2:.6f} M")

# =====================================================
# KONSENTRASI
# =====================================================
elif menu == "Hubungan Satuan Konsentrasi":

    st.header("Konversi Konsentrasi")

    pilihan = st.selectbox(
        "Jenis Konversi",
        [
            "Molaritas → ppm",
            "ppm → Molaritas"
        ]
    )

    if pilihan == "Molaritas → ppm":

        M = st.number_input("Molaritas (M)")
        Mr = st.number_input("Mr zat")

        if st.button("Konversi"):
            ppm = M * Mr * 1000
            st.success(f"{ppm:.4f} ppm")

    else:

        ppm = st.number_input("ppm")
        Mr = st.number_input("Mr zat")

        if st.button("Konversi"):
            M = ppm / (Mr * 1000)
            st.success(f"{M:.6e} M")

# =====================================================
# STOIKIOMETRI
# =====================================================
elif menu == "Stoikiometri":

    st.header("Stoikiometri")

    pilihan = st.selectbox(
        "Perhitungan",
        [
            "Massa → Mol",
            "Mol → Massa"
        ]
    )

    if pilihan == "Massa → Mol":

        massa = st.number_input("Massa (gram)")
        Mr = st.number_input("Mr")

        if st.button("Hitung Mol"):
            mol = massa / Mr
            st.success(f"Mol = {mol:.6f}")

    else:

        mol = st.number_input("Mol")
        Mr = st.number_input("Mr")

        if st.button("Hitung Massa"):
            massa = mol * Mr
            st.success(f"Massa = {massa:.6f} gram")

# =====================================================
# KESETIMBANGAN
# =====================================================
elif menu == "Teori Kesetimbangan":

    st.header("Tetapan Kesetimbangan Kc")

    st.write("Untuk reaksi:")
    st.latex(r"aA+bB \rightleftharpoons cC+dD")

    C = st.number_input("[C]")
    D = st.number_input("[D]")
    A = st.number_input("[A]")
    B = st.number_input("[B]")

    c = st.number_input("Koefisien C", value=1)
    d = st.number_input("Koefisien D", value=1)
    a = st.number_input("Koefisien A", value=1)
    b = st.number_input("Koefisien B", value=1)

    if st.button("Hitung Kc"):

        if A > 0 and B > 0:
            Kc = (C**c * D**d)/(A**a * B**b)
            st.success(f"Kc = {Kc:.6f}")

# =====================================================
# pH SETELAH PENGENCERAN
# =====================================================
elif menu == "Perubahan pH Setelah Pengenceran":

    st.header("Perubahan pH Setelah Pengenceran")

    jenis = st.radio(
        "Jenis Larutan",
        ["Asam Kuat", "Basa Kuat"]
    )

    C1 = st.number_input("Konsentrasi Awal (M)")
    V1 = st.number_input("Volume Awal (mL)")
    V2 = st.number_input("Volume Akhir (mL)")

    if st.button("Hitung pH"):

        C2 = (C1 * V1) / V2

        if jenis == "Asam Kuat":

            pH = -math.log10(C2)

        else:

            pOH = -math.log10(C2)
            pH = 14 - pOH

        st.success(f"Konsentrasi akhir = {C2:.6e} M")
        st.success(f"pH = {pH:.3f}")

# =====================================================
# BUFFER
# =====================================================
elif menu == "Pembuatan Larutan Buffer":

    st.header("Larutan Buffer")

    st.latex(
        r"pH = pK_a + \log\frac{[A^-]}{[HA]}"
    )

    pKa = st.number_input("pKa")

    basa = st.number_input(
        "Konsentrasi Basa Konjugat [A-]"
    )

    asam = st.number_input(
        "Konsentrasi Asam Lemah [HA]"
    )

    if st.button("Hitung pH Buffer"):

        pH = pKa + math.log10(basa/asam)

        st.success(f"pH = {pH:.3f}")

# =====================================================
# PROPAGATION OF ERROR
# =====================================================
elif menu == "Propagation of Error":

    st.header("Propagation of Error")

    st.write("Untuk operasi perkalian/pembagian")

    x = st.number_input("Nilai x")
    dx = st.number_input("Galat x")

    y = st.number_input("Nilai y")
    dy = st.number_input("Galat y")

    if st.button("Hitung"):

        z = x * y

        dz = z * math.sqrt(
            (dx/x)**2 +
            (dy/y)**2
        )

        st.success(f"Hasil = {z:.6f}")
        st.success(f"Galat = ± {dz:.6f}")

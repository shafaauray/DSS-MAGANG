import streamlit as st
import pandas as pd

from saw import saw

st.set_page_config(
    page_title="SPK Pemilihan Tempat Magang",
    page_icon="🎓",
    layout="wide"
)

# =====================================
# HEADER
# =====================================

st.title("🎓 Sistem Pendukung Keputusan Pemilihan Tempat Magang")

st.markdown("""
Aplikasi ini membantu mahasiswa menentukan tempat magang terbaik menggunakan
metode **Simple Additive Weighting (SAW)** berdasarkan beberapa kriteria penilaian.
""")

with st.expander("📖 Tentang Metode SAW"):
    st.write("""
    SAW (Simple Additive Weighting) merupakan metode pengambilan keputusan
    multikriteria yang melakukan normalisasi nilai setiap alternatif,
    kemudian mengalikan dengan bobot masing-masing kriteria untuk
    menghasilkan ranking terbaik.
    """)

# =====================================
# SESSION STATE
# =====================================

if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(
        columns=[
            "Perusahaan",
            "C1",
            "C2",
            "C3",
            "C4",
            "C5",
            "C6"
        ]
    )

# =====================================
# DATA CONTOH
# =====================================

col_btn1, col_btn2 = st.columns(2)

with col_btn1:
    if st.button("📌 Muat Data Contoh"):

        st.session_state.data = pd.DataFrame({
            "Perusahaan": [
                "PT Telkom Indonesia",
                "PT Pertamina",
                "PT Astra International",
                "Startup XYZ"
            ],
            "C1": [5, 5, 4, 3],
            "C2": [3, 2, 3, 5],
            "C3": [4, 4, 3, 4],
            "C4": [5, 5, 5, 3],
            "C5": [4, 5, 4, 5],
            "C6": [5, 5, 4, 3]
        })

        st.success("Data contoh berhasil dimuat")

with col_btn2:
    if st.button("🗑 Hapus Semua Data"):
        st.session_state.data = pd.DataFrame(
            columns=[
                "Perusahaan",
                "C1",
                "C2",
                "C3",
                "C4",
                "C5",
                "C6"
            ]
        )
        st.success("Semua data berhasil dihapus")
        st.rerun()

# =====================================
# DASHBOARD
# =====================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Jumlah Perusahaan",
        len(st.session_state.data)
    )

with col2:
    st.metric(
        "Jumlah Kriteria",
        6
    )

with col3:
    st.metric(
        "Metode",
        "SAW"
    )

st.divider()

# =====================================
# SIDEBAR BOBOT
# =====================================

st.sidebar.header("⚖️ Bobot Kriteria (%)")

b1 = st.sidebar.number_input(
    "Kesesuaian Bidang",
    min_value=0,
    max_value=100,
    value=30
)

b2 = st.sidebar.number_input(
    "Jarak",
    min_value=0,
    max_value=100,
    value=15
)

b3 = st.sidebar.number_input(
    "Uang Saku",
    min_value=0,
    max_value=100,
    value=15
)

b4 = st.sidebar.number_input(
    "Reputasi",
    min_value=0,
    max_value=100,
    value=15
)

b5 = st.sidebar.number_input(
    "Fasilitas",
    min_value=0,
    max_value=100,
    value=10
)

b6 = st.sidebar.number_input(
    "Peluang Direkrut",
    min_value=0,
    max_value=100,
    value=15
)

total_bobot = b1 + b2 + b3 + b4 + b5 + b6

if total_bobot == 100:
    st.sidebar.success(f"Total Bobot = {total_bobot}%")
else:
    st.sidebar.warning(f"Total Bobot = {total_bobot}%")

# =====================================
# FORM TAMBAH DATA
# =====================================

st.header("➕ Tambah Perusahaan")

with st.form("form_tambah"):

    nama = st.text_input("Nama Perusahaan")

    c1 = st.slider(
        "Kesesuaian Bidang",
        1, 5, 3
    )

    c2 = st.slider(
        "Jarak",
        1, 5, 3
    )

    c3 = st.slider(
        "Uang Saku",
        1, 5, 3
    )

    c4 = st.slider(
        "Reputasi",
        1, 5, 3
    )

    c5 = st.slider(
        "Fasilitas",
        1, 5, 3
    )

    c6 = st.slider(
        "Peluang Direkrut",
        1, 5, 3
    )

    tambah = st.form_submit_button(
        "Tambah Perusahaan"
    )

if tambah:

    if nama != "":

        baru = pd.DataFrame({
            "Perusahaan": [nama],
            "C1": [c1],
            "C2": [c2],
            "C3": [c3],
            "C4": [c4],
            "C5": [c5],
            "C6": [c6]
        })

        st.session_state.data = pd.concat(
            [st.session_state.data, baru],
            ignore_index=True
        )

        st.success("Data berhasil ditambahkan")

# =====================================
# DATA PERUSAHAAN
# =====================================

st.header("📋 Data Perusahaan")

if len(st.session_state.data) > 0:

    st.dataframe(
        st.session_state.data,
        use_container_width=True
    )

    st.subheader("🗑 Hapus Data")

    perusahaan_hapus = st.selectbox(
        "Pilih Perusahaan yang Akan Dihapus",
        st.session_state.data["Perusahaan"]
    )

    if st.button("Hapus Data"):

        st.session_state.data = (
            st.session_state.data[
                st.session_state.data["Perusahaan"]
                != perusahaan_hapus
            ]
        )

        st.success("Data berhasil dihapus")
        st.rerun()

    # =====================================
    # EDIT DATA
    # =====================================

    st.subheader("✏️ Edit Data")

    perusahaan_edit = st.selectbox(
        "Pilih Perusahaan",
        st.session_state.data["Perusahaan"],
        key="edit"
    )

    row = st.session_state.data[
        st.session_state.data["Perusahaan"]
        == perusahaan_edit
    ].iloc[0]

    with st.form("edit_form"):

        ec1 = st.slider(
            "Kesesuaian Bidang",
            1, 5,
            int(row["C1"])
        )

        ec2 = st.slider(
            "Jarak",
            1, 5,
            int(row["C2"])
        )

        ec3 = st.slider(
            "Uang Saku",
            1, 5,
            int(row["C3"])
        )

        ec4 = st.slider(
            "Reputasi",
            1, 5,
            int(row["C4"])
        )

        ec5 = st.slider(
            "Fasilitas",
            1, 5,
            int(row["C5"])
        )

        ec6 = st.slider(
            "Peluang Direkrut",
            1, 5,
            int(row["C6"])
        )

        simpan = st.form_submit_button(
            "Simpan Perubahan"
        )

    if simpan:

        idx = st.session_state.data[
            st.session_state.data["Perusahaan"]
            == perusahaan_edit
        ].index[0]

        st.session_state.data.loc[idx] = [
            perusahaan_edit,
            ec1,
            ec2,
            ec3,
            ec4,
            ec5,
            ec6
        ]

        st.success("Data berhasil diperbarui")
        st.rerun()

# =====================================
# HITUNG RANKING
# =====================================

if len(st.session_state.data) > 1:

    st.divider()

    if st.button("🏆 Hitung Ranking SAW"):

        if total_bobot != 100:

            st.error(
                "Total bobot harus 100%"
            )

        else:

            bobot = [
                b1/100,
                b2/100,
                b3/100,
                b4/100,
                b5/100,
                b6/100
            ]

            hasil = saw(
                st.session_state.data,
                bobot
            )

            st.header("🏆 Hasil Ranking")

            ranking = hasil[
                ["Perusahaan", "Skor"]
            ]

            # PODIUM
            st.subheader("🥇 Podium Ranking")

            medal = ["🥇", "🥈", "🥉"]

            top = ranking.head(3).reset_index()

            for i in range(min(3, len(top))):
                st.markdown(
                    f"### {medal[i]} {top.loc[i,'Perusahaan']} — {top.loc[i,'Skor']:.4f}"
                )

            st.divider()

            st.dataframe(
                ranking,
                use_container_width=True
            )

            csv = ranking.to_csv(index=False)

            st.download_button(
                label="⬇ Download Hasil Ranking (CSV)",
                data=csv,
                file_name="hasil_ranking.csv",
                mime="text/csv"
            )

            st.subheader("📊 Visualisasi Ranking")

            st.bar_chart(
                ranking.set_index(
                    "Perusahaan"
                )
            )

            st.caption(
                "Sistem Pendukung Keputusan Pemilihan Tempat Magang menggunakan metode SAW"
            )
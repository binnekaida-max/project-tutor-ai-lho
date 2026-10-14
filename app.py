import streamlit as st

# Konfigurasi Halaman Web
st.set_page_config(
    page_title="AI Tutor Teks LHO - Bahasa Indonesia",
    page_icon="📚",
    layout="wide"
)

# Konten Materi Teks LHO
materi_lho = """
### TEKS LAPORAN HASIL OBSERVASI (LHO) - KELAS X

**1. Pengertian:**
Teks Laporan Hasil Observasi (LHO) adalah teks yang memberikan informasi secara umum tentang sesuatu berdasarkan fakta dari hasil pengamatan secara langsung di lapangan.

**2. Ciri-ciri Teks LHO:**
- Ditulis berdasarkan fakta lapangan hasil pengamatan nyata.
- Bersifat objektif, global, dan universal.
- Objek yang dibahas adalah objek tunggal.
- Tidak mengandung prasangka atau dugaan yang menyimpang.

**3. Struktur Utama Teks LHO:**
- **Pernyataan Umum / Klasifikasi:** Berisi pembuka, definisi umum, atau pengantar tentang objek yang dilaporkan.
- **Deskripsi Bagian:** Berisi rincian detail mengenai bagian-bagian objek yang diamati.
- **Deskripsi Manfaat / Kesimpulan:** Berisi kegunaan atau manfaat objek tersebut dalam kehidupan sehari-hari.

**4. Kaidah Kebahasaan Teks LHO:**
- Menggunakan kata kerja material dan relasional.
- Menggunakan kata benda (nomina) dan frasa nomina.
- Menggunakan istilah teknis atau ilmiah sesuai bidang ilmu objek.
- Menggunakan kalimat definisi (menggunakan kata 'adalah', 'merupakan') dan kalimat deskripsi.
"""

# Konten LKPD
lkpd_content = """
**Tugas Analisis Mandiri Teks LHO:**
1. Carilah sebuah contoh Teks Laporan Hasil Observasi di internet atau buku paket!
2. Analisislah teks tersebut berdasarkan strukturnya (Pernyataan Umum, Deskripsi Bagian, dan Deskripsi Manfaat)!
3. Tuliskan hasil analisis Anda pada kolom jawaban di bawah ini.
"""

link_kahoot = "https://kahoot.it/"

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("📚 AI Tutor Bahasa Indonesia")
st.sidebar.caption("Teks Laporan Hasil Observasi (LHO)")

menu = st.sidebar.radio(
    "Pilih Menu Pembelajaran:",
    [
        "📖 Materi Teks LHO", 
        "💬 AI Tutor (Tanya Jawab)", 
        "📝 LKPD Interaktif", 
        "🎯 Kuis Kahoot", 
        "💡 Panduan Penggunaan"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("Aplikasi AI Tutor khusus materi Teks Laporan Hasil Observasi (LHO).")

# --- MENU 1: MATERI TEKS LHO ---
if menu == "📖 Materi Teks LHO":
    st.title("📖 Modul Materi: Teks Laporan Hasil Observasi (LHO)")
    st.markdown("---")
    st.markdown(materi_lho)

# --- MENU 2: AI TUTOR (TANYA JAWAB) ---
elif menu == "💬 AI Tutor (Tanya Jawab)":
    st.title("💬 Tanyakan Sesuatu Seputar Teks LHO")
    st.write("Ketik pertanyaan Anda seputar Teks Laporan Hasil Observasi di bawah ini:")
    
    query = st.text_input("Pertanyaan Anda:", placeholder="Contoh: Apa saja struktur teks LHO?")
    
    if st.button("🔍 TANYAKAN", type="primary"):
        if not query.strip():
            st.warning("Silakan ketik pertanyaan terlebih dahulu.")
        else:
            words = [w.lower() for w in query.split() if len(w) > 2]
            content_lower = materi_lho.lower()
            
            matches = sum(1 for word in words if word in content_lower)
            
            if matches > 0:
                st.success("Materi yang relevan berhasil ditemukan!")
                st.markdown("### 💡 Penjelasan AI Tutor:")
                st.info(materi_lho)
            else:
                st.error("Maaf, pertanyaan Anda belum tercakup dalam database materi.")

# --- MENU 3: LKPD INTERAKTIF ---
elif menu == "📝 LKPD Interaktif":
    st.title("📝 Lembar Kerja Peserta Didik (LKPD)")
    st.markdown("### 📌 Petunjuk & Soal LKPD:")
    st.info(lkpd_content)

    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        nama = st.text_input("Nama Lengkap Siswa:")
    with col2:
        kelas = st.text_input("Kelas / Rombel:", value="X - ")
        
    jawaban = st.text_area("Tuliskan Jawaban LKPD Anda di sini:", height=180)
    
    if st.button("📤 Kirim LKPD", type="primary"):
        if nama and kelas and jawaban.strip():
            st.success(f"Terima kasih **{nama}** ({kelas})! Jawaban LKPD Anda berhasil dikirim.")
            st.balloons()
        else:
            st.error("Mohon lengkapi Nama, Kelas, dan Jawaban Anda sebelum mengirim.")

# --- MENU 4: KUIS KAHOOT ---
elif menu == "🎯 Kuis Kahoot":
    st.title("🎯 Kuis Evaluasi Interaktif (Kahoot)")
    st.write("Uji pemahaman Anda dengan mengikuti Kuis Kahoot yang telah disiapkan!")
    st.markdown("---")
    
    st.success("Tautan Kuis Kahoot sudah siap!")
    st.markdown("👉 **Klik tombol atau link di bawah ini untuk memulai kuis:**")
    st.link_button("🚀 Buka Kuis Kahoot", link_kahoot)
    st.markdown(f"**Link langsung:** [{link_kahoot}]({link_kahoot})")

# --- MENU 5: PANDUAN PENGGUNAAN ---
elif menu == "💡 Panduan Penggunaan":
    st.title("💡 Panduan Penggunaan AI Tutor Teks LHO")
    st.markdown("""
    Aplikasi ini dirancang sebagai media pembelajaran interaktif khusus untuk materi **Teks Laporan Hasil Observasi (LHO)** Bahasa Indonesia Kelas X.
    """)

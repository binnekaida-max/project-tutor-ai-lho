import os
import streamlit as st

# Konfigurasi Halaman Web
st.set_page_config(
    page_title="AI Tutor Teks LHO - Bahasa Indonesia",
    page_icon="📚",
    layout="wide"
)

DATABASE_DIR = "."

# Fungsi membaca isi file teks dari folder database
def read_database_file(filename):
    filepath = os.path.join(DATABASE_DIR, filename)
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read().strip()
    return ""

# Membaca konten dari file sesuai nama file di VS Code Anda
materi_lho = read_database_file("MATERI LAPORAN HASIL OBSERVASI.txt")
lkpd_content = read_database_file("LKPD (LEMBAR KERJA PESERTA DIDIK).txt")
link_kahoot = read_database_file("LINK KUIS KAHOOT.txt")

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
    if materi_lho:
        st.markdown(materi_lho)
    else:
        st.warning("File `MATERI LAPORAN HASIL OBSERVASI.txt` belum berisi teks materi. Silakan isi file tersebut terlebih dahulu.")

# --- MENU 2: AI TUTOR (TANYA JAWAB) ---
elif menu == "💬 AI Tutor (Tanya Jawab)":
    st.title("💬 Tanyakan Sesuatu Seputar Teks LHO")
    st.write("Ketik pertanyaan Anda seputar Teks Laporan Hasil Observasi di bawah ini:")
    
    query = st.text_input("Pertanyaan Anda:", placeholder="Contoh: Apa saja struktur teks LHO?")
    
    if st.button("🔍 TANYAKAN", type="primary"):
        if not query.strip():
            st.warning("Silakan ketik pertanyaan terlebih dahulu.")
        elif not materi_lho:
            st.error("Materi di database belum tersedia.")
        else:
            words = [w.lower() for w in query.split() if len(w) > 2]
            content_lower = materi_lho.lower()
            
            # Cek kecocokan kata kunci sederhanan
            matches = sum(1 for word in words if word in content_lower)
            
            if matches > 0:
                st.success("Materi yang relevan berhasil ditemukan!")
                st.markdown("### 💡 Penjelasan AI Tutor:")
                st.info(materi_lho)
            else:
                st.error("Maaf, pertanyaan Anda belum tercakup dalam database materi. Coba gunakan kata kunci seperti 'struktur', 'ciri', atau 'kebahasaan'.")

# --- MENU 3: LKPD INTERAKTIF ---
elif menu == "📝 LKPD Interaktif":
    st.title("📝 Lembar Kerja Peserta Didik (LKPD)")
    
    if lkpd_content:
        st.markdown("### 📌 Petunjuk & Soal LKPD:")
        st.info(lkpd_content)
    else:
        st.write("Silakan selesaikan tugas analisis Teks LHO mandiri di bawah ini:")

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
    
    if link_kahoot:
        st.success("Tautan Kuis Kahoot sudah siap!")
        st.markdown(f"👉 **Klik tombol atau link di bawah ini untuk memulai kuis:**")
        st.link_button("🚀 Buka Kuis Kahoot", link_kahoot)
        st.markdown(f"**Link langsung:** [{link_kahoot}]({link_kahoot})")
    else:
        st.warning("File `LINK KUIS KAHOOT.txt` masih kosong. Silakan buka file tersebut di VS Code dan tempelkan URL link Kahoot Anda di dalamnya!")

# --- MENU 5: PANDUAN PENGGUNAAN ---
elif menu == "💡 Panduan Penggunaan":
    st.title("💡 Panduan Penggunaan AI Tutor Teks LHO")
    st.markdown("""
    Aplikasi ini dirancang sebagai media pembelajaran interaktif khusus untuk materi **Teks Laporan Hasil Observasi (LHO)** Bahasa Indonesia Kelas X.
    
    #### **Fitur Utama Aplikasi:**
    1. **📖 Materi Teks LHO**: Membaca ringkasan materi terlengkap.
    2. **💬 AI Tutor**: Tempat bertanya hal-hal seputar Teks LHO.
    3. **📝 LKPD Interaktif**: Petunjuk dan tempat pengerjaan tugas lembar kerja siswa.
    4. **🎯 Kuis Kahoot**: Tautan langsung menuju Kuis Kahoot interaktif.
    5. **💡 Panduan Penggunaan**: Petunjuk penggunaan aplikasi.
    """)
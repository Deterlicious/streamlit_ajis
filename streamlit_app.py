import streamlit as st

def main():
    st.title("Ajis Sangat Mencintai Silfani 💖")
    st.write("Halo Silfani, ini adalah sebuah program khusus yang dibuat oleh Ajis untukmu.")
    st.write("Aku ingin menyatakan perasaanku dengan beberapa kalimat romantis dan lucu!")

    # Romantis dan lucu berbagai kalimat
    romantis = [
        "Cintaku padamu bagaikan angin, tak terlihat tetapi selalu hadir.",
        "Aku mencintaimu lebih dari cara pizza mencintai keju.",
        "Kamu seperti bintang, indah dan selalu bersinar di hatiku.",
        "Aku ingin menjadi password WiFi-mu, karena aku takkan pernah lupa padamu.",
        "Cinta kita itu seperti kopi, semakin lama semakin kuat.",
        "Jika kamu adalah lagu, aku ingin menjadi liriknya yang selalu mengiringi hidupmu.",
        "Kalau kamu adalah hujan, aku ingin menjadi tanah yang selalu kau basahi.",
    ]

    lucu = [
        "Kamu tahu, aku menyimpan foto kamu di bawah bantal. Biar bisa nyenyak tidur.",
        "Kamu adalah sosok yang membuatku pusing, tapi pusing yang menyenangkan.",
        "Kamu tahu, aku bahagia banget ketika berdua. Satu-satunya saat aku bisa ngomong tanpa harus diberhentikan.",
        "Kamu seperti WiFi di tempat umum, susah banget connect.",
        "Kalau cinta itu kayak makanan, aku milih sambal. Selalu ada buat kamu, kapanpun dan di manapun.",
        "Aku suka kamu, walau kadang-kadang aku nggak suka sama perangai kamu.",
        "Cinta itu sebenarnya simpel, cuma ditambahin harapan, kecemburuan, dan drama aja jadi rumit.",
    ]

    st.write("\n\n")
    st.write("Romantis:")
    st.write(romantis)

    st.write("Lucu:")
    st.write(lucu)

if __name__ == "__main__":
    main()

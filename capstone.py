import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt

st.set_page_config(layout='wide')

df1 = pd.read_csv('pertumbuhan_ekonomi_gdpusd.csv')
df2 = pd.read_csv('iiikn_tahunan.csv')
df3 = pd.read_csv('pertumbuhan_jumlah_investor_rev.csv')
dff = pd.read_csv('iiik_provinsi_2022.csv')

st.title("Pengaruh Literasi Keuangan Terhadap Pertumbuhan Investor di Indonesia")
st.markdown (
    """
    By : [Kurniawan](https://www.linkedin.com/in/kurniawan-5b7a651b5/)
    """)

from PIL import Image

image = Image.open('gambar.jpg')

st.image(image, use_column_width=True)

st.markdown(
    """
       Di tengah dinamika ekonomi global, Indonesia terus mengalami pertumbuhan ekonomi yang pesat.
       Seiring dengan perkembangan ini, masyarakat Indonesia semakin menyadari pentingnya literasi
       keuangan dalam mengelola aspek keuangan pribadi mereka. Salah satu aspek penting dalam literasi
       keuangan adalah investasi. Investasi menjadi salah satu cara yang efektif untuk mengembangkan
       kekayaan dan memastikan kesejahteraan finansial di masa depan.

       Penelitian ini bermaksud untuk menyelidiki hubungan antara literasi keuangan dan jumlah
       investor di Indonesia. Dengan meningkatnya literasi keuangan diharapkan dapat memberikan
       dampak positif terhadap peningkatan jumlah investor di pasar keuangan domestik. Peningkatan
       jumlah investor ini bukan hanya memberikan kontribusi terhadap pertumbuhan ekonomi, tetapi
       juga dapat membantu masyarakat Indonesia untuk memahami manfaat dan potensi investasi dalam
       mencapai tujuan keuangan mereka.

    """,unsafe_allow_html=True)


st.header("Pertumbuhan Ekonomi Indonesia (GDP-USD)")
df1['tahun'] = df1['tahun'].astype(str).str.replace(',', '')
tahun_pilih = st.selectbox("Pilih rentang tahun", ("1967-2022", "2013-2022"))
if tahun_pilih == '1967-2022':
    start_year = 1967
    end_year = 2022
elif tahun_pilih == '2013-2022' :
    start_year = 2013
    end_year = 2022

filtered_data = df1[(df1['tahun'].astype(int) >= start_year) & (df1['tahun'].astype(int) <= end_year)]

chart = alt.Chart(filtered_data).mark_line().encode(
    x='tahun',
    y='pendapatan'
).properties(
    width=800,
    height=500
)

# Menampilkan line chart
st.altair_chart(chart, use_container_width=True)

st.markdown (
    """
    Sumber : [Data World Bank](https://data.worldbank.org/indicator/NY.GDP.MKTP.CD?locations=ID)
    """)

st.markdown(
    """
       GDP (Gross Domestic Product) adalah suatu ukuran yang digunakan untuk menilai nilai
       keseluruhan dari barang dan jasa yang dihasilkan dalam suatu negara dalam suatu periode
       waktu tertentu. Pertumbuhan ekonomi negara dapat dilihat salah satunya berdasarkan GDP
       indikator utama untuk mengukur kesehatan dan kinerja ekonomi suatu negara.
       Dari data diatas dapat dilihat bahwa pendapatan GDP Indonesia cenderung meningkat setiap tahunnya,
       yang artinya Indonesia memiliki pertumbuhan ekonomi yang positif.

    """,unsafe_allow_html=True)




st.header('Index Literasi Keuangan Di Indonesia')

chart_bar = alt.Chart(df2).mark_bar().encode(
    x=alt.X('tahun:N', title='Tahun', axis=alt.Axis(labelAngle=0)),
    y=alt.Y('literasi:Q', title='Tingkat Literasi Keuangan')  
).properties(
    width=600,        # Lebar chart
    height=400        # Tinggi chart
) 

st.altair_chart(chart_bar,use_container_width=True)


st.markdown (
    """
    Sumber : [ojk.go.id](https://www.ojk.go.id/id/Default.aspx)
    """)

st.markdown(
    """
Literasi keuangan merujuk pada kemampuan seseorang untuk memahami dan menggunakan
pengetahuan keuangan secara efektif dalam pengambilan keputusan finansial sehari-hari.
Individu yang memiliki literasi keuangan yang baik dapat membuat keputusan finansial
yang lebih cerdas, mengelola risiko dengan lebih baik, dan memahami dampak dari
keputusan keuangan jangka panjang.
""")


st.header('Index Inklusi Keuangan Di Indonesia')

chart_bar1 = alt.Chart(df2).mark_bar().encode(
    x=alt.X('tahun:N', title='Tahun', axis=alt.Axis(labelAngle=0)),
    y=alt.Y('inklusi:Q', title='Tingkat Inklusi Keuangan'),
).properties(
    width=600,        # Lebar chart
    height=400        # Tinggi chart
)

st.altair_chart(chart_bar1,use_container_width=True)

st.markdown (
    """
    Sumber : [ojk.go.id](https://www.ojk.go.id/id/Default.aspx)
    """)

st.markdown(
    """
    Inklusi keuangan, menurut Consultative Group to Assist the Poor (CGAP, 2016), menjelaskan inklusi
keuangan adalah akses yang dimiliki oleh rumah tangga dan bisnis terhadap penggunaan produk dan
layanan jasa keuangan secara efektif. Produk dan layanan jasa keuangan tersebut harus tersedia secara
berkelanjutan dan teregulasi dengan baik. Menurut World Bank (2016) inklusi keuangan didefinisikan sebagai
akses terhadap produk dan layanan jasa keuangan yang bermanfaat dan terjangkau dalam memenuhi kebutuhan
masyarakat maupun usahanya dalam hal ini transaksi, pembayaran, tabungan, kredit dan asuransi yang digunakan
secara bertanggung jawab dan berkelanjutan.
"""
)



df2['pertumbuhan_literasi'] = df2['literasi'].pct_change() * 100
df2['pertumbuhan_inklusi'] = df2['inklusi'].pct_change() * 100

# Membuat line chart
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(df2['tahun'], df2['pertumbuhan_literasi'], marker='o', label='Pertumbuhan Literasi (%)')
ax.plot(df2['tahun'], df2['pertumbuhan_inklusi'], marker='o', label='Pertumbuhan Inklusi (%)')
ax.set_xlabel('Tahun')
ax.set_ylabel('Pertumbuhan (%)')
ax.set_title('Pertumbuhan Tingkat Literasi dan Inklusi Tahunan')
ax.set_xticks(df2['tahun'])
ax.grid(True)
ax.legend()
plt.tight_layout()

# Menampilkan line chart di Streamlit
st.pyplot(fig)

st.header("Pertumbuhan Jumlah Investor Berdasarkan Instrumen Investasi")
chart_bar3 = alt.Chart(df3).mark_bar().encode(
    x=alt.X('tahun:N', title='Tahun', axis=alt.Axis(labelAngle=0)),
    y=alt.Y('jumlah_investor:Q', title='Jumlah Investor'),
    color='instrumen_investasi:N'
).properties(
    width=600,
    height=400
)

st.altair_chart(chart_bar3, use_container_width=True)

# Membuat picklist untuk memilih provinsi
provinsi_pilihan = st.selectbox("Pilih Provinsi:", dff['provinsi'])

# Menampilkan nilai tingkat literasi dan tingkat inklusi berdasarkan provinsi yang dipilih
nilai_literasi = dff[dff['provinsi'] == provinsi_pilihan]['tingkat_literasi'].values[0]
nilai_inklusi = dff[dff['provinsi'] == provinsi_pilihan]['tingkat_inklusi'].values[0]

st.write(f"Tingkat Literasi di {provinsi_pilihan}: {nilai_literasi}%")
st.write(f"Tingkat Inklusi di {provinsi_pilihan}: {nilai_inklusi}%")

# st.markdown (
#     """
#     Sumber : [ojk.go.id](https://www.ojk.go.id/id/Default.aspx)
#     """)

# st.markdown(
#     """
# Pentingnya literasi keuangan dalam meningkatkan jumlah investor juga dapat dihubungkan
# dengan upaya pemerintah Indonesia dalam mendorong inklusi keuangan. Inklusi keuangan adalah
# ketersediaan akses bagi masyarakat untuk memanfaatkan produk dan/atau layanan jasa keuangan di lembaga
# keuangan formal sesuai dengan kebutuhan dan kemampuan masyarakat dalam rangka mewujudkan kesejahteraan
# """)


st.subheader("Inshigt")
st.markdown(
    """
Dapat dilihat dari data index literasi keuangan dan index inklusi keuangan terjadi ketimpangan,
dimana akses keuangan yang tinggi tidak diimbangi dengan literasi keuangan. Pemerintah dapat memaksimalkan
kegiatan edukasi tentang keuangan agar masyarakat memiliki kesadaran untuk berinvestasi.
"""
)

st.subheader("Kesimpulan")

st.markdown(
    """
Jika dilihat korelasi Spearman antara index literasi keuangan dengan pertumbuhan jumlah investor di indonesia
maka korelasinya memilikin nilai 1.0 (korelasi positif), semakin tinggi tingkat literasi keuangan maka akan semakin tinggi
jumlah investor di indonesia.
"""
)

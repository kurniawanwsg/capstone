import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(layout='wide')

df1 = pd.read_csv('pertumbuhan_ekonomi_gdpusd.csv')
df2 = pd.read_csv('iiikn_tahunan.csv')
df3 = pd.read_csv('pertumbuhan_jumlah_investor_rev.csv')
df_provinsi = pd.read_csv('iiik_provinsi_2022.csv')

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

chart = alt.Chart(df1).mark_point().encode(
    x=alt.X('tahun:O', title='Tahun'),
    y=alt.Y('pendapatan:Q', title='Pendapatan (USD)')   
)
st.altair_chart(chart,use_container_width=True)

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


st.markdown(
    """
Sayangnya, literasi keuangan di Indonesia masih cukup rendah di kalangan
masyarakat. Banyak orang tidak sepenuhnya memahami konsep investasi, risiko, dan strategi
keuangan yang tepat. Hal ini tercermin dari jumlah investor di pasar keuangan Indonesia
yang masih terbatas, terutama jika dibandingkan dengan potensi pasar yang sebenarnya yaitu jumlah
penduduk yang lebih dari 270 juta jiwa.
"""
)

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

st.markdown (
    """
    Sumber : [ojk.go.id](https://www.ojk.go.id/id/Default.aspx)
    """)

st.markdown(
    """
Pentingnya literasi keuangan dalam meningkatkan jumlah investor juga dapat dihubungkan
dengan upaya pemerintah Indonesia dalam mendorong inklusi keuangan. Inklusi keuangan adalah
ketersediaan akses bagi masyarakat untuk memanfaatkan produk dan/atau layanan jasa keuangan di lembaga
keuangan formal sesuai dengan kebutuhan dan kemampuan masyarakat dalam rangka mewujudkan kesejahteraan
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
Jika dilihat korelasi antara index literasi keuangan dengan pertumbuhan jumlah investor di indonesia
maka korelasinya berbanding lurus, semakin tinggi tingkat literasi keuangan maka akan semakin tinggi
jumlah investor di indonesia.
"""
)
import streamlit as st
from PIL import Image

st.title('顔認識アプリ')

# 画像投稿フォーム file_uploader()
uploaded_file = st.file_uploader("Choose an image...", type='jpg')
# if 変数 is not None: 変数の中に値が入っていたら、、、
if uploaded_file is not None:

    img = Image.open(uploaded_file)
    st.image(img, caption='Uploaded Image.', use_column_width=True)


# st.write('データフレーム')
# # pd.DataFrame() Pandasのデータフレーム型を書くことができる
# st.write(
#     pd.DataFrame({
#         '1st column': [1, 2, 3, 4],
#         '2nd column': [10, 20, 30, 40]
#     })
# )

# """
# # My 1st App
# こんな感じでマジックコマンドを使用できる。Markdown対応。

# """
# # if文　checkboxにおけるtrue.falseで判定
# # ネストに注意
# if st.checkbox('Show DataFrame'):
#     # チャート作成
#     # np.random.randn 乱数作成、正規分布(平均0,標準偏差1)
#     chart_df = pd.DataFrame(
#         np.random.randn(20, 3),
#         columns=['a', 'b', 'c']
#     )
#     # チャートを表示
#     st.line_chart(chart_df)

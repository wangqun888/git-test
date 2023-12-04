import os

import numpy as np
import streamlit as st
from streamlit_chatbox import ChatBox
from streamlit_option_menu import option_menu

st.set_page_config(
    "QE",
    os.path.join("img", "logo1.jpg"),
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/chatchat-space/Langchain-Chatchat',
        'Report a bug': "https://github.com/chatchat-space/Langchain-Chatchat/issues",
        'About': f"""欢迎使用！"""
    }
)

# Using "with" notation
with st.sidebar:
    # col1, col2 = st.columns(2)
    # with col1:
    st.image("img/logo.png", width=200)
    # with col2:
        # st.header('QE-CHAT')
    st.caption(
        f"""<p style="font-size: 15px; color: #676D67; text-align: left;" >QE-CHAT</p>""",
        unsafe_allow_html=True,
        )
    st.divider()

    pages = {
        "对话": {
            "icon": "chat",
            # "func": dialogue_page,
        },
        "知识库管理": {
            "icon": "hdd-stack",
            # "func": knowledge_base_page,
        },
    }
    options = list(pages)
    icons = [x["icon"] for x in pages.values()]
    default_index = 0
    styles= {
            "container": {"padding": "0!important", "background-color": "white"},
            "icon": {"color": "black", "font-size": "15px"},
            "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#1E95DC"},
        }
    selected_page = option_menu(
        "菜单",
        options=options,
        icons=icons,
        menu_icon="cast",
        default_index=default_index,
        styles=styles,
    )

    st.number_input("历史对话轮数：", 0, 20, 3)
    list_knowledge_bases = st.selectbox("选择要加载的知识库", ("国铁集团", "中国移动", "test"))

    option = st.selectbox(
        '选择LLM模型',
        ("chatglm2-6b", "YuLan"))

    # st.write(f"LLM模型 {option} 已加载")
    # st.radio("选择LLM模型", ("chatglm2-6b", "YuLan"))
    with st.expander("知识库配置", False):
        # kb_list = list_knowledge_bases(no_remote_api=True)
        # selected_kb = st.selectbox(
        #     "请选择知识库：",
        #     kb_list,
        #     on_change=on_kb_change,
        #     key="selected_kb",
        # )
        kb_top_k = st.number_input("匹配知识条数：", 1, 5, 3, help='知识库匹配出处条数')

        ## Bge 模型会超过1
        score_threshold = st.slider("知识匹配分数阈值：", 0.0, 1.0, float(0.5), 0.01, help='取值范围在0-1之间，SCORE越小，相关度越高，取到1相当于不筛选，建议设置在0.5左右')
        chunk_content = st.checkbox("关联上下文", False, help='提问是否关联上下文')
        chunk_size = st.slider("关联长度：", 0, 500, 250, help='上下文关联的长度')

    # with st.echo():
    # st.write("This code will be printed to the sidebar.")

    # with st.spinner("Loading..."):
    #         time.sleep(5)
    # st.success("Done!")

    tab1, tab2, tab3 = st.tabs(["菜单1", "菜单2", "菜单3"])

    with tab1:
        color = st.color_picker('Pick A Color', '#00f900')
        st.write('The current color is', color)

    with tab2:
        st.header("A dog")

    with tab3:
        st.header("An owl")
with st.chat_message("user"):
    st.write("Hello 👋")
    # st.line_chart(np.random.randn(30, 3))

with st.chat_message("ai"):
    st.write("Hello human")
# message.bar_chart(np.random.randn(30, 3))
prompt = st.chat_input("Say something")
if prompt:
    with st.chat_message('human'):
        st.write(f"{prompt}")
    with st.chat_message('ai'):
        st.line_chart(np.random.randn(30, 3))

chat_box = ChatBox(
    assistant_avatar=os.path.join(
        "img",
        "logo1.jpg"
    )
)
if not chat_box.chat_inited:
    st.toast(
        f"欢迎使用 [`QE-Chat`](https://github.com/chatchat-space/Langchain-Chatchat) ! \n\n"
        f"当前使用模型`{option}`, 您可以开始提问了."
    )
import streamlit as st
import numpy as np 
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import toml
import json
from streamlit_lottie import st_lottie


from streamlit_extras.let_it_rain import rain

def load_config(config_path):
    with open(config_path, 'r') as f:
        config = toml.load(f)
    return config

config = load_config('config.toml')

#----Lottie----#
def load_lottie(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

cow = load_lottie('my_storage/lottie_cow.json')

st.set_page_config(page_title='Lecture 6', page_icon='\U0001F412')

st.header(':violet[:ferris_wheel:**Lecture 6: Energy in Rotating System and Moment of Inertia** :ferris_wheel:]')
main_col = st.columns([3,1])
with main_col[0]:
    st.markdown(
    '''
#### เนื้อหาใน Lecture นี้   
1. :blue[**พลังงานในระบบที่กำลังหมุน**]   
    1.1. Kinetic Energy in Rotating System   
    1.2. The Moment of Inertia   
2. :blue[**โมเมนต์ของความเฉื่อย**]   
    2.1. Moment of Inertia of Rigid Body   
    2.2. Table of Moment of Inertia
3. :blue[**ทฤษฎีบทแกนขนาน**]   
    3.1. The Parallel Axis Theorem
'''
)

with main_col[1]:
    st.markdown(
        '''
   
'''
    )
    st.markdown(
        '''
   
'''
    )
    snow = st.checkbox('Snow')
    if snow:
        rain(
        emoji='❄️',
        font_size=10,
        falling_speed=15,
        animation_length='infinite'
)
    raining = st.checkbox('Rain')
    if raining:
        rain(
        emoji='💧',
        font_size=5,
        falling_speed=5,
        animation_length='infinite')
        rain(
        emoji='💧',
        font_size=5,
        falling_speed=2.5,
        animation_length='infinite')   

st.divider()

#---- Topics Tabs ----#
topic = st.tabs([':octagonal_sign: **พลังงานในระบบที่กำลังหมุน**', ':octagonal_sign: **โมเมนต์ของความเฉื่อย**', ':octagonal_sign: **ทฤษฎีบทแกนขนาน**'])

#---- Topic 1 ----#
topic[0].markdown(
    '''
ลองจินตนาการถึงล้ออันหนึ่งที่กำลังหมุนอยู่ . . . แน่นอนว่าอยู่ดีๆมันจะหมุนเองไม่ได้ มันต้องคนไปทำให้มันหมุน
> ต้องใส่พลังงานเข้าไปในวัตถุเพื่อทำให้วัตถุเริ่มหมุน

ลองจินตนาการต่อไปว่าถ้าเราเอาล้อที่กำลังหมุนไปแตะกับเหรียญ แน่นอนว่าเหรียญต้องกระเด็นออกไป
> วัตถุที่กำลังหมุนสามารถให้พลังงานกับวัตถุอื่นได้

เพราะฉะนั้นเราควรสรุปได้ว่า
> :blue[**มีพลังงานสะสมอยู่ในวัตถุที่กำลังหมุน**]   

คำถามคือ :blue[พลังงานนี้สะสมอยู่ในรูปแบบไหน] และ :blue[จะหาพลังงานนี้ได้ยังไง]
'''
)
col01 = topic[0].columns([1.5,1])
col01[1].image('my_storage/lecture_06/example01.png',use_column_width=True)
col01[0].markdown(
    '''
ลองจินตนาการว่ามีล้ออันหนึ่งกำลังหมุนอยู่ ข้างในล้ออันนี้มีอนุภาคอนู่ :blue[$N$] ตัว
อนุภาคตัวที่ :blue[$i$] มีระยะจากแกนหมุนเป็น :blue[$r_i$] และมีความเร็ว :blue[$\\vec{v}_i$]
เพราะฉะนั้นอนุภาคตัวนี้มีพลังงานจลน์เป็น
$$
KE_i = \\frac{1}{2}m_i v_i^2
$$
อนุภาคแต่ละตัวในล้อที่กำลังหมุนมี :blue[พลังงานจลน์] เพราะฉะนั้น ล้อทั้งอันที่กำลังหมุนก้ต้องมี :blue[พลังงานจลน์รวม] ค่าหนึ่ง
เราเรียกพลังงานตัวนี้ว่า :blue[**พลังงานจลน์ที่สะสมในการหมุน, Kinetic Energy associated with rotation**]
จะได้
'''
)
topic[0].markdown(
    '''
$$
\\begin{align}
KE_{tot} &= \\frac{1}{2}m_1 v_1^2 + \\frac{1}{2}m_2 v_2^2 + \\frac{1}{2}m_3 v_3^2 + . . . \\\\
&= \\frac{1}{2}m_1 (\\omega r_1)^2 + \\frac{1}{2}m_2 (\\omega r_2)^2 + \\frac{1}{2}m_3 (\\omega r_3)^2 + . . . \\\\
KE_{tot} &= \\frac{1}{2} (\\sum_{i=1}^n m_i r_i^2) \\omega ^2
\\end{align}
$$

สมการนี้บอกว่าพลังงานจลน์ในการหมุนแปรตาม :blue[$\\; \\omega^2 \\;$] ซึ่ง Make-sense เพราะยิ่งหมุนเร็ว พลังงานก็ยิ่งเยอะ   
ที่น่าสงสัยคือเทอมในวงเล็บ :blue[$\\; (\\sum_{i=1}^n m_i r_i^2) \\;$] ถ้าเราเทียบพลังงานจลน์ปกติ :blue[$KE=\\frac{1}{2}mv^2$] กับพลังงานจลน์ในการหมุน
:blue[$KE=\\frac{1}{2}(...)\\omega^2$] จะเห็นว่าเทอม :blue[$\\; (\\sum_{i=1}^n m_i r_i^2) \\;$] เทียบได้กับ :blue[มวลในการหมุน]
> นิยาม :red[**โมเมนต์ของความเฉื่อย, Moment of Inertia**] ของวัตถุที่กำลังหมุน เป็น :violet[**$\\; I=\\sum m_i r_i^2 \\;$**]   
> จะได้ :red[พลังงานจลน์ในวัตถุที่กำลังหมุน,] 
$$
🔸🔸🔸 \\;KE_{rot} = \\frac{1}{2}I\\omega^2\\; 🔸🔸🔸
$$
'''
)

topic[1].markdown(
    '''
เราสามารถหา :blue[**Moment of Inertia**] ของวัตถุได้ผ่านสมการ 
$$
🔸🔸🔸 I=\\sum m_i r_i^2 🔸🔸🔸
$$
สมการนี้บอกว่า :orange[ความเฉื่อยในการหมุน] ขึ้นอยู่กับสองอย่าง
1. :blue[**Mass:**] ตัวนี้ตรงไปตรงมา ยิ่งมวลมาก ยิ่งหมุนยาก, ของสองอย่างที่หมุนเร็วเท่ากัน ตัวที่มวลมากกว่าต้องมีพลังงานจลน์มากกว่า   
2. :blue[**Spread of Masses:**] ตัวนี้ค่อนข้างน่าแปลกใจเพราะมันบอกว่า ความยาก(เฉื่อย)ในการหมุนไม่ได้ขึ้นกับแค่มวล แต่ขึ้นกับการกระจายตัวของมวลด้วย
ดูได้ผ่านเทอม :red[$\\; r_i^2 \\;$, ระยะ ***ตั้งฉาก*** จากแกนหมุน] เทอมนี้บอกเราว่า :red[***ยิ่งมวลกระจายตัวจากแกนหมุนมาก ยิ่งหมุนยาก***]
'''
)
top1_col = topic[1].columns([1,1])
top1_col[1].image('my_storage/lecture_06/hum_bird.png')
top1_col[1].image('my_storage/lecture_06/example02.png')
top1_col[0].markdown(
    '''
ลองดูภาพทางขวา นี่คือ :green[Hummingbird] หนึ่งในนกที่กระพือปีกเร็วที่สุดในโลก(70 ครั้งต่อวิ)
ลองสังเกตุการกระจายตัวของมวลในปีกนกตัวนี้ดู จะเห็นว่ามวลส่วนใหญ่ไปกองกันอยู่แถวๆโคนปีก คือ :red[$\\;r\\;$] น้อย เพราะฉะนั้นปีกของนกตัวนี้จะมี
Moment of Inertia น้อย นกตัวนี้เลยกระพือปีกได้เร็ว
> :orange[**Evolution** ในทางชีววิทยาพิจารณากฏทางฟิสิกส์ด้วย . . ]   
      
:red[**Example 1**]
1. จงหา Moment of Inertia ของวัตถุในภาพ หากวัตถุหมุนรอบแกนที่ตั้งฉากกับจาน A ผ่านรูตรงกลาง
2. จงหา Moment of Inertia ของวัตถุในภาพ หากวัตถุหมุนรอบแกนที่ผ่านทะลุรูตรงกลางของ B และ C
3. หากวัตถุกำลังหมุนรอบแกนในข้อ A ในอัตรา :red[$\\;\\omega = 4.0\\;rad/s\\;$] จงหาพลังงานจลน์ที่สะสมในวัตถุ
'''
)
example1 = topic[1].expander(':green[**Solution for Example 1**]')
with example1:
    st.markdown(
        '''
:red[**Part 1**]   
$$
\\begin{align}
I_A &= \\sum_{i=1}^3 m_i r_i^2 \\\\
&= m_A r_A^2 + m_B r_B^2 + m_C r_C^2 \\\\
&= m_A (0)^2 + m_B (0.50\\;m)^2 + m_C (0.40\\;m)^2  
\\end{align}
$$
เนื่องจาก :blue[$A$] อยู่ที่แกนหมุน เพราะฉะนั้น :blue[ระยะตั้งฉากจากแกนหมุน] ของ :blue[$A$] เลยเป็น :blue[$0$]   
แทนค่ามวลต่างๆลงไปจะได้ :green[$\\; I_A = 0.057\\;kg.m^2  \\;$] :balloon:   
:red[**Part 2**]   
$$
\\begin{align}
I_{BC} &= \\sum_{i=1}^3 m_i r_i^2 \\\\
&= m_A r_A^2 + m_B r_B^2 + m_C r_C^2 \\\\
&= m_A (0.40\\;m)^2 + m_B (0)^2 + m_C (0)^2  
\\end{align}
$$
แทนค่ามวลต่างๆลงไปจะได้ :green[$\\; I_{BC} = 0.048\\;kg.m^2  \\;$] :balloon:   
:red[**Part 3**]   
เราหาพลังงานจลน์ในการหมุนได้จากสมการ :blue[$KE = \\frac{1}{2}I\\omega^2$] โดย :blue[$I$] ที่ใช้ ต้องเป็น :blue[$I$] ของแกนหมุนที่เรากำลังสนใจ
$$
\\begin{align}
(KE)_A &= \\frac{1}{2}I_A\\omega^2 \\\\
&= \\frac{1}{2}(0.057\\;kg.m^2)(4.0\\;rad/s)^2
\\end{align}
$$
แทนค่าลงไปจะได้ :green[$\\;(KE)_A = 0.46\\; J\\;$] :balloon:
'''
    )
topic[1].markdown(
    '''
:blue[**Moment of Inertia**] แบบที่เราหาด้านบน ใช้กับระบบที่ประกอบด้วยมวลหลายๆตัว มองเป็นจุดมวล แต่ปัญหาจริงๆที่เราจะเจอจะเป็นแบบ :blue[มวลกระจายตัวอน่างต่อเนื่อง เป็นรูปทรง] มากกว่า   
วิธีแก้ปัฐหาคือเราแบ่งมวลที่กระจายตัวอย่างตัวอย่างตือเนื่องออกเป็นชิ้นเล็กๆ :blue[$\\; dV,\\;dA,\\;dL\\;$,ปริมาตรเล็กๆ, พื้นที่เล็กๆ, ความยาวเล็กๆ] ตามที่ปัญหาให้มา   
เราจะได้มวลชิ้นเล็กๆ :blue[$\\; dm=\\rho dV,\\; = \\sigma dA,\\; = \\lambda dL \\;$]    
โดยที่มวลชิ้นเล็กๆพวกนี้จะมี :blue[Moment of Inertia] เล็กๆ :blue[$\\; dI=r^2dm \\;$ จากสมการ $\\; I=mr^2$]   
สุดท้ายเราอินทิเกรตรวม Moment of inertia เล็กๆนี้เข้าด้วยกัน จะได้
$$
🔸🔸🔸 I=\\int r^2 dm 🔸🔸🔸
$$
นี่คือวิธีหา :blue[Moment of Inertia] ของวัตถุที่กระจายตัวอย่างต่อเนื่อง   
ด่านล่างคือตาราง Moment of Inertia ของรูปทรงที่พบบ่อย (ไม่ต้องจำ รู้แค่ว่ามันอยู่ตรงนี้ ถ้าต้องใช้งานมาเปิดย้อนดูเอาได้)
'''
)
topic[1].image('my_storage/lecture_06/moment_table.png', use_column_width=True)
topic[1].caption('Note: ดูรูปทรงในปัญหาว่าตรงกับรูปไหน จากนั้นดูว่าหมุนรอบแกนไหน ค่า Moment of Inertia ของรูปทรงเดียวกันแต่หมุนคนละแบบ อาจจะไม่เท่ากัน')

topic[2].markdown(
    '''
ในหัวข้อนี้เราจะศึกษา :blue[***Parallel-Axis Theorem***] ซึ่งจะเป็นตัวที่ช่วยให้เราหา Moment of Inertia รอบแกนอื่นๆที่ไม่ได้ผ่าน CM ของวัตถุ   
ให้ :blue[$\\;I_{CM} \\;$] แทน Moment of Inertia ของแกนที่ผ่าน CM ของวัตถุ และ :blue[$\\;I_{P} \\;$] แทน Moment of Inertia ของแกนที่ขนานกันแกนที่ผ่าน CM 
และอยู่ห่างกันเป็นระยะ :blue[$\\;d\\;$]
> :red[**Parallel-Axis Theorem:** $\\;I_P = I_{CM} + Md^2 \\;$]
'''
)
topic2_col = topic[2].columns([1,1])
topic2_col[1].image('my_storage/lecture_06/example03.png',use_column_width=True)
topic2_col[0].markdown(
    '''
:red[**Example 2**]   
วัตถุในภาพมีมวล :red[$\\;3.6\\;kg\\;$] และมี Moment of Inertia รอบแกน P เป็น :red[$\\; I_P = 0.132\\;kg.m^2\\;$]
> จงหา Moment of Inertia รอบแกนที่ผ่าน CM ของวัตถุนี้, หา :red[$\\; I_{CM}\\;$] ในภาพ
'''
)
example2 = topic[2].expander(':green[**Solution for Example 2**]')
with example2:
    st.markdown(
        '''
เราใช้ :blue[**Parallel-Axis Theorem**] โดยข้อนี้เรามีข้อมูล Moment of Inertia ของแกนขนาน(Parallel-Axis),:blue[$\\;I_P\\;$] ที่อยู่ห่างจาก :blue[$\\;I_{CM}\\;$]
เป็นระยะ :blue[$\\;d=0.15\\;m\\;$] และเราอยากได้ :blue[$I_{CM}$]   
$$
\\begin{align}
I_P &= I_{CM} +Md^2 \\\\
I_{CM} &= I_P - Md^2 \\\\
&= (0.132\\;kg.m^2) - (3.6\\;kg)(0.15\\;m)^2 \\\\ 
\\end{align}
$$
จะได้ :green[$\\; I_{CM}=0.051\\;kg.m^2$] :balloon:
'''
    )

st.divider()

st.subheader(':violet[**Practice Zone**. . .:lower_left_fountain_pen:]')
col = st.columns(2)
ex01 = col[0].checkbox(':green[**Exercises 1**]:books:')
ex02 = col[0].checkbox(':green[**Exercises 2**]:books:')
ex03 = col[0].checkbox(':green[**Exercises 3**]:books:')
ex04 = col[0].checkbox(':green[**Exercises 4**]:books:')
ex05 = col[0].checkbox(':green[**Exercises 5**]:books:')

ex06 = col[1].checkbox(':green[**Exercises 6**]:books:')
ex07 = col[1].checkbox(':green[**Exercises 7**]:books:')
ex08 = col[1].checkbox(':green[**Exercises 8**]:books:')
ex09 = col[1].checkbox(':green[**Exercises 9**]:books:')
ex10 = col[1].checkbox(':green[**Exercises 10**]:books:')

st.divider()
#---- Exercise 1 -----#
if ex01:
    st.markdown(
        '''
:blue[**Exercise 1:**] จากภาพเป็นทรงกลมมวล :red[$\\; 0.200\\;kg\\;$] สี่ตัวอยู่ที่มุมของสี่เหลี่ยมจัตุรัศยาวด้านละ 
:red[$\\;0.400\\;m \\;$] ทั้งสี่เชื่อมกันด้วยแท่งไม้ที่เบามากๆ
> A: จงหา Moment of Inertia ของระบบนี้ผ่านแกนหมุนที่ตั้งฉากกับ :red[$\\;O\\;$] และตั้งฉากกับระนาบของสี่เหลี่ยมนี้    
> B: จงหา Moment of Inertia ของระบบนี้ผ่านแกนหมุน :red[$\\;AB\\;$] ในภาพ   
> C: จงหา Moment of Inertia ของระบบนี้ผ่านแกนหมุนที่ผ่านมวล บนซ้าย และผ่านมวล ล่างขวา
'''
    )
    st.image('my_storage/lecture_06/ex01.png')
    ex1_a = st.number_input(':violet[**Ans A:**] ในหน่วย $\\;kg.m^2$')
    if abs(ex1_a - (0.0640)) < 0.003:
        st.write(':green[:balloon::balloon:**CongratZ**]:balloon::balloon:')
        st.balloons()
    elif abs(ex1_a - 0.00) < 0.000001:
        st.write(':orange[Waiting for your answer . . .]') 
    else:
        st.write(':red[Too bad. . .:crying_cat_face:] ')
        st_lottie(cow, loop=False, width=200)
    ex1_b = st.number_input(':violet[**Ans B:**] ในหน่วย $\\;kg.m^2$')
    if abs(ex1_b - (0.0640)) < 0.003:
        st.write(':green[:balloon::balloon:**CongratZ**]:balloon::balloon:')
        st.balloons()
    elif abs(ex1_b - 0.00) < 0.000001:
        st.write(':orange[Waiting for your answer . . .]') 
    else:
        st.write(':red[Too bad. . .:crying_cat_face:] ')
        st_lottie(cow, loop=False, width=200)
    ex1_c = st.number_input(':violet[**Ans C:**] ในหน่วย $\\;kg.m^2$')
    if abs(ex1_c - (0.0640)) < 0.003:
        st.write(':green[:balloon::balloon:**CongratZ**]:balloon::balloon:')
        st.balloons()
    elif abs(ex1_c - 0.00) < 0.000001:
        st.write(':orange[Waiting for your answer . . .]') 
    else:
        st.write(':red[Too bad. . .:crying_cat_face:] ')
        st_lottie(cow, loop=False, width=200)
 

#---- Exercise 2 -----#
if ex02:
    st.markdown(
        '''
:blue[**Exercise 2:**] ล้ออันหนึ่งมีเส้นผ่านศูนย์กลาง :red[$\\; 0.600\\;m \\;$] ของล้อทำมาจากไม้มวล :red[$\\; 1.40\\;kg \\;$]   
แกนล้อทำมาจากแท่งไม้ 8 แท่ง ยาวแท่งละ :red[$\\; 0.300\\;m \\;$] มวล :red[$\\; 0.280\\;kg \\;$]
> จงหา Moment of Inertia ของล้อนี้ในขณะที่กำลังหมุนผ่านแกนที่ผ่านศูนย์กลางและตั้งฉากกับล้อ
'''
    )
    st.image('my_storage/lecture_06/ex02.png')
    ex2_a = st.number_input(':violet[**Ans A:**] ในหน่วย $\\;kg.m^2$')
    if abs(ex2_a - (0.193)) < 0.003:
        st.write(':green[:balloon::balloon:**CongratZ**]:balloon::balloon:')
        st.balloons()
    elif abs(ex2_a - 0.00) < 0.000001:
        st.write(':orange[Waiting for your answer . . .]') 
    else:
        st.write(':red[Too bad. . .:crying_cat_face:] ')
        st_lottie(cow, loop=False, width=200)

#---- Exercise 3 -----#
if ex03:
    st.markdown(
        '''
:blue[**Exercise 3:**] ล้ออันหนึ่งหมุนผ่านแกนล้อด้วยความเร่งเชิงมุมคงที่เริ่มจากหยุดนิ่ง เมื่อผ่านไป :red[$\\; 12.0\\;s \\;$]
ล้อหมุนไปได้ :red[$\\; 8.20\\;rev \\;$] และในขณะนั้นล้อกำลังมีพลังงานจลน์ :red[$\\; 36.0\\;J \\;$]
> จงหา Moment of Inertia ของล้อตัวนี้รอบแกนที่ล้อกำลังหมุนอยู่
'''
    )
    ex3_a = st.number_input(':violet[**Ans A:**] ในหน่วย $\\;kg.m^2$')
    if abs(ex3_a - (0.976)) < 0.003:
        st.write(':green[:balloon::balloon:**CongratZ**]:balloon::balloon:')
        st.balloons()
    elif abs(ex3_a - 0.00) < 0.000001:
        st.write(':orange[Waiting for your answer . . .]') 
    else:
        st.write(':red[Too bad. . .:crying_cat_face:] ')
        st_lottie(cow, loop=False, width=200)
   
#---- Exercise 4 -----#
if ex04:
    st.markdown(
        '''
:blue[**Exercise 4:**] ทรงกลมกลวงมวล :red[$\\; 8.20\\;kg \\;$] รัศมี :red[$\\; 0.220\\;m \\;$] เริ่มหมุนจากหยุดนิ่ง
ผ่านแกนที่วางตัวตามแนวเส้นผ่านศูนย์กลาง ด้วยความเร่งคงที่ :red[$\\; 0.890\\;rad/s^2 \\;$]
> จงหา :red[Kinetic Energy] ของระบบนี้เมื่อมันหมุนไปได้ :red[$\\; 6.00\\;rev \\;$]
'''
    )
    ex4_a = st.number_input(':violet[**Ans A:**] ในหน่วย $\\;J$')
    if abs(ex4_a - (8.88)) < 0.03:
        st.write(':green[:balloon::balloon:**CongratZ**]:balloon::balloon:')
        st.balloons()
    elif abs(ex4_a - 0.00) < 0.000001:
        st.write(':orange[Waiting for your answer . . .]') 
    else:
        st.write(':red[Too bad. . .:crying_cat_face:] ')
        st_lottie(cow, loop=False, width=200)
   

#---- Exercise 5 -----#
if ex05:
    st.markdown(
        '''
:blue[**Exercise 5:**] หนึ่งในวิธีเก็บพลังงานในสมัยก่อนคือ :blue[**flywheel**] คือเอาพลังงานไปทำให้ล้อหมุน ล้อก็จะเก็บพลังงานไว้
ถ้าอยากได้พลังงานก็เอามือไปแตะล้อ ล้อก็จะคืนพลังงานกลับมา   
flywheel ตัวหนึ่งมวล :red[$\\; 70.0\\;kg \\;$] รูปทรงเป็นจานรัศมี :red[$\\; 1.20\\;m \\;$] 
โดยโครงสร้างของล้อสามารถรับความเร่งสู่ศูนย์กลางสูงสุดที่ขอบล้อได้ที่ :red[$\\; 3500\\;m/s^2 \\;$]
> จงหาพลังงานมากสุดที่สามารถสะสมในล้อตัวนี้ได้
'''
    )
    ex5_a = st.number_input(':violet[**Ans A:**] ในหน่วย $10^4\\;J$')
    if abs(ex5_a - (7.35)) < 0.03:
        st.write(':green[:balloon::balloon:**CongratZ**]:balloon::balloon:')
        st.balloons()
    elif abs(ex5_a - 0.00) < 0.000001:
        st.write(':orange[Waiting for your answer . . .]') 
    else:
        st.write(':red[Too bad. . .:crying_cat_face:] ')
        st_lottie(cow, loop=False, width=200)
   

#---- Exercise 6 -----#
if ex06:
    st.markdown(
        '''
:blue[**Exercise 6:**] รอกไร้แรงเสียดทานตัวหนึ่งทำจากจานมวล :red[$\\; 2.50\\;kg\\;$] รัศมี :red[$\\; 20.0\\;cm\\;$]
หากนำหินมวล :red[$\\; 1.50\\;kg\\;$] มาผูกเชือกแล้วร้อยผ่านรอก โดยเชือกกับรอกไม่ใถลจากกัน จากนั้นปล่อยหินให้ตกลงจากหยุดนิ่ง
> หินต้องตกลงมาเป็นระยะเท่าไหร่ รอกจึงจะมีพลังงาน :red[$\\; 4.50\\;J\\;$] สะสมอยู่   
'''
    )
    st.image('my_storage/lecture_06/ex06.png')
    ex6_a = st.number_input(':violet[**Ans:**] ในหน่วย $\\;m$')
    if abs(ex6_a - (0.673)) < 0.03:
        st.write(':green[:balloon::balloon:**CongratZ**]:balloon::balloon:')
        st.balloons()
    elif abs(ex6_a - 0.00) < 0.000001:
        st.write(':orange[Waiting for your answer . . .]') 
    else:
        st.write(':red[Too bad. . .:crying_cat_face:] ')
        st_lottie(cow, loop=False, width=200)


#---- Exercise 7 -----#
if ex07:
    st.markdown(
        '''
:blue[**Exercise 7:**] จากภาพ รอกทำมาจากจานรัศมี :red[$\\;R=0.280\\;m\\;$] วัตถุมวล :red[$\\;m=4.20\\;kg\\;$]
ถูกนำมาแขวน จากนั้นปล่อยระบบจากหยุดนิ่งโดยมวลที่ตกลงมาตกลงด้วยความเร่งคงที่ ถ้ามวลตกลงมาได้ระยะ :red[$\\;3.00\\;m\\;$]
ใน :red[$\\;2.00\\;s\\;$]
> จงหามวลของรอก
'''
    )
    st.image('my_storage/lecture_06/ex07.png')
    ex7_a = st.number_input(':violet[**Ans:**] ในหน่วย $\\;kg$')
    if abs(ex7_a - (46.5)) < 0.3:
        st.write(':green[:balloon::balloon:**CongratZ**]:balloon::balloon:')
        st.balloons()
    elif abs(ex7_a - 0.00) < 0.000001:
        st.write(':orange[Waiting for your answer . . .]') 
    else:
        st.write(':red[Too bad. . .:crying_cat_face:] ')
        st_lottie(cow, loop=False, width=200)
   

#---- Exercise 8 -----#
if ex08:
    st.markdown(
        '''
:blue[**Exercise 8:**] บันไดมวล :red[$\\; 9.00\\;kg \\;$] ยาว :red[$\\; 2.00\\;m \\;$] วางพิงกับกำแพงโดยทำมุม :red[$\\; 53^o \\;$] กับพื้น
> จงหาว่าหากต้องการดันบันไดเข้าไปจนชิดกำแพง ต้องทำงานอย่างน้อยเท่าไหร่
''')
    ex8_a = st.number_input(':violet[**Ans:**] ในหน่วย $\\;J$')
    if abs(ex8_a - (17.7)) < 0.3:
        st.write(':green[:balloon::balloon:**CongratZ**]:balloon::balloon:')
        st.balloons()
    elif abs(ex8_a - 0.00) < 0.000001:
        st.write(':orange[Waiting for your answer . . .]') 
    else:
        st.write(':red[Too bad. . .:crying_cat_face:] ')
        st_lottie(cow, loop=False, width=200)
    
#---- Exercise 9 -----#
if ex09:
    st.markdown(
        '''
:blue[**Exercise 9:**] ต้องหมุนทรงกลมตันรอบแกนไหน ทรงกลมตันถึงจะมี Moment of Inertia เท่ากับเปลือกทรงกลม
ที่มีมวลเท่ากัน รัศมีเท่ากัน ที่กำลังหมุนรอบเส้นผ่านศูนย์กลางของตัวเองอยู่
'''
    )
    ex9_a = st.number_input('ถ้าทั้งสองมีรัศมี :red[$\\; R \\;$] แกนหมุนในคำตอบต้องอยู่ห่างจากแกนเดิมเป็นกี่เท่าของ :red[$\\;R$]')
    if abs(ex9_a - (0.516)) < 0.03:
        st.write(':green[:balloon::balloon:**CongratZ**]:balloon::balloon:')
        st.balloons()
    elif abs(ex9_a - 0.00) < 0.000001:
        st.write(':orange[Waiting for your answer . . .]') 
    else:
        st.write(':red[Too bad. . .:crying_cat_face:] ')
        st_lottie(cow, loop=False, width=200)
 
#---- Exercise 10 -----#
if ex10:
    st.markdown(
        '''
:blue[**Exercise 10:**] จงหา Moment of Inertia ของวงแหวนบางมวล :red[$\\;M\\;$] รัศมี :red[$\\;R\\;$]
ที่กำลังหมุนรอบแกนที่ตั้งฉากกับระนาบของวงแหวน และแกนนี้อยู่ที่ขอบของวงแหวน
'''
    )
    ex10_a = st.number_input(':violet[**Ans:**] ในหน่วย $\\;MR^2$')
    if abs(ex10_a - (2)) < 0.001:
        st.write(':green[:balloon::balloon:**CongratZ**]:balloon::balloon:')
        st.balloons()
    elif abs(ex10_a - 0.00) < 0.000001:
        st.write(':orange[Waiting for your answer . . .]') 
    else:
        st.write(':red[Too bad. . .:crying_cat_face:] ')
        st_lottie(cow, loop=False, width=200)

st.divider()

# Music-Player
music = [
    'pages/my_storage/music/majesty_by_ben_moon_ft_veela.mp3',
    'pages/my_storage/music/wings_of_freedom_by_epica_x_titan.mp3',
    'pages/my_storage/music/invincible_by_world_of_warcraft_ost.mp3',
    'pages/my_storage/music/a_song_played_by_the_stars_by_steinsgate_ost.mp3',
    'pages/my_storage/music/awe_of_she_by_guilty_gear_ost.mp3',
    'pages/my_storage/music/beyond_the_matrix_by_epica_acoustic.mp3',
    'pages/my_storage/music/beyond_the_matrix_by_epica.mp3',
    'pages/my_storage/music/crimson_bow_and_arrow_by_epica_x_titan.mp3',
    'pages/my_storage/music/davy_jones_by_unknow_source.mp3',
    'pages/my_storage/music/dedicate_your_heart_by_epica_x_titan.mp3',
    'pages/my_storage/music/endlessness_by_nightwish.mp3',
    'pages/my_storage/music/gate_of_steiner_by_steinsgate_ost.mp3',
    'pages/my_storage/music/mayuri_sadness_by_steinsgate_ost.mp3',
    'pages/my_storage/music/natural_corruption_by_epica.mp3',
    ]
music_name = [
    'Majesty - Ben Moon ft. Veela',
    'Wings of Freedom - Epica X Titan',
    'Invincible - World of Warcraft OST',
    'A Song Played by the Star - Steins;Gate OST',
    'Awe of She - Guilty Gear OST',
    'Beyond the Matrix - Epica Acoustic Version',
    'Beyond the Matrix - Epica',
    'Crimson Bow and Arrow - Epica X Titan',
    'Davy Jones - Unknown Source',
    'Dedicate Your Heart - Epica X Titan',
    'Endlessness - Nightwish',
    'Gate of Steiner - Steins;Gate OST',
    'Mayuri Sadness - Steins;Gate OST',
    'Natural Corruption - Epica',
]
music_selector = st.selectbox(
    'เพลงเพลินๆระหว่างทำโจทย์ . . .:notes:', music_name
)
for i in range(len(music_name)):
    if music_selector == music_name[i]:
        st.audio(music[i])
  

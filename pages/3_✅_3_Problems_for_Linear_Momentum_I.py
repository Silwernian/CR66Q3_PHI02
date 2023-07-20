import streamlit as st
import numpy as np 
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import toml

from streamlit_extras.let_it_rain import rain

def load_config(config_path):
    with open(config_path, 'r') as f:
        config = toml.load(f)
    return config

config = load_config('config.toml')

st.set_page_config(page_title='Lecture 3', page_icon='\U0001F412')


st.header(':violet[Lecture 3 Problems For Linear Momentum I 📚]')
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

st.subheader(''':green[:orange_book:สรุปหลักการสำคัญในเรื่อง Linear Momentum:orange_book:]''')
tab = st.tabs([
    ':orange[**Impulse and Momentum**]', ':orange[**Conservation of Linear Momentum**]', ':orange[**Collisions**]'
])
with tab[0]:
    st.markdown(
        '''
:blue[**Linear Momentum**] ของมวล $m$ ที่กำลังเคลื่อนที่ด้วยความเร็ว $\\vec{v}$ คือ 
$$
🔸🔸\\vec{p}=m\\vec{v} 🔸🔸
$$
ปริมาณนี้ใช้วัด :blue[สภาพการเคลื่อนที่ของวัตถุ. . .🚀].   

ถ้ามีแรง $\\vec{F}(t)$ กระทำกับวัตถุตั้งแต่เวลา $t_1$ ถึง $t_2$ นิยาม :blue[**Impulse**] ที่เกิดบนวัตถุเป็น   
$$
🔸🔸\\vec{J}=\\int_{t_1}^{t_2} \\vec{F}(t)dt🔸🔸
$$   
กรณีพิเศษที่แรงคงที่ ไม่ขึ้นกับเวลา จะได้ว่า Impulse หาได้จาก $\\;\\vec{J}=\\vec{F}\\Delta{t}$   
:blue[Impulse] เป็นปริมาณที่ใช้วัด :blue[ผลของแรงในแง่เวลา. . .⏱️]   

:blue[Impulse] และ :blue[Linear Momentum] มีความสัมพันธ์กันผ่าน :red[❗**The Impulse-Momentum Theorem**❗] ที่กล่าวว่า
$$
🔸🔸\\vec{J}=\\Delta\\vec{p}🔸🔸
$$
มีความหมายคือ: ในช่วงเวลาหนึ่งๆ เกิด :blue[**Impulse**] ขึ้นบนวัตถุเท่าไหร่ :blue[**Linear Momentum**] ของวัตถุจะเปลี่ยนไปเท่านั้น
'''
    )

with tab[1]:
    st.markdown(
        '''
จากการนิยาม :blue[Linear Momentum] $\\vec{p}=m\\vec{v}$ เราสามารถเขียน $Newton's \\; 2^{nd} \\; Law$ ใหม่ได้เป็น   
$$
🔸🔸\\Sigma{\\vec{F}}=\\frac{d\\vec{p}}{dt} 🔸🔸
$$
สมการนี้มีความหมายคือ: :blue[**Force**, $\\vec{F}$] คือ อัตราการเปลี่ยนแปลงของ :blue[**Motion**, :blue[$\\vec{p}$]]   
   
ถ้าเราขยายสมการด้านบนไปใช้กับ :orange[ระบบอนุภาค] มวลรวม :orange[$M$] โดยนิยาม :blue[Total Linear Momentum ของระบบ] 
$$
\\vec{P}=M\\vec{v}=m_1 \\vec{v_1}+m_2 \\vec{v_2}+m_3 \\vec{v_3}+...
$$
เมื่อรวม :blue[แรง] ที่กระทำกับทั้งระบบอนุภาคเข้าด้วยกัน :orange[แรงภายในระบบ] จะหักล้างกันไปตาม $Newton's \\; 3^{rd} \\; Law$ เหลือแค่ :orange[แรงภายนอก] ที่กระทำต่อระบบ   
จะได้ $Newton's \\; 2^{nd} \\; Law$ สำหรับระบบอนุภาค เป็น
$$
🔸🔸\\Sigma{\\vec{F_{ext}}}=\\frac{d\\vec{P}}{dt} 🔸🔸
$$

จะเห็นได้ทันทีว่า หาก :orange[แรงภายนอกสุทธิ] ที่กระทำต่อระบบเป็นศูนย์ แล้วจะได้ :orange[$\\frac{d\\vec{P}}{dt}=0$] หรือ :orange[$\\vec{P}=Const.$]
สรุปเป็น :red[❗**Principle of Conservation of Linear Momentum**❗] ที่กล่าวว่า
> :violet[หาก ***Net External Force*** ที่กระทำต่อระบบเป็นศูนย์ แล้ว ***Total Linear Momentum*** ของระบบจะคงที่]   

ก็คือ ถ้ามี event บางอย่างเกิดขึ้นกับระบบอนุภาค แต่ระหว่าง event นั้นมีแค่แรงภายในระบบเท่านั้นที่ส่งผล แรงภายนอกสุทธิที่กระทำต่อระบบเป็นศูนย์ จะได้ว่า Linear Momentum ของระบบ ก่อนเกิด event ต้องเท่ากับตอนหลังเกิด event นั้นแล้ว
'''
    )

with tab[2]:
    st.markdown(
        '''
:blue[การชน (Collision)] คือการที่วัตถุสองตัวขึ้นไปมี Interaction กันในช่วงเวลาสั้นๆ (ไม่จำเป็นต้องสัมผัสกันจริงๆ)
หลักการวิเคราะห์ การชน เป็นการประยุกต์ใช้ :blue[หลักอนุรักษ์โมเมนตัมเชิงเส้น] โดยตรง   
   
หากเราพิจารณาให้ระบบเป็นอนุภาคสองตัวที่เข้ามาชนกัน จะได้ว่าแรงที่เกิด ระหว่างการชน เป็นแรงภายในระบบ และหากไม่มีแรงอื่นมายุ่งระหว่างการชน จะได้ว่า
> :violet[Total Linear Momentum ของระบบที่ เสี้ยววินาทีก่อนชน ต้องเท่ากันตอน เสี้ยววินาทีหลังชน]

หลักอนุรักษ์โมเมนตัมเชิงเส้น ใช้ได้แทบจะ 100% ในปัญหาการชน   
   
**ประเภทของการชน**: เราจำแนกประเภทของการชนโดยพิจารณาพลังงานจลน์รวมของระบบเป็นเกฌฑ์ได้ดังนี้
1. :blue[**🔸Elastic Collisions🔸:**] คือการชนที่พลังงานจนล์ของระบบไม่สูญหายไประหว่างการชน เพราะฉะนั้น
    - :green[อนุรักษ์โมเมนตัม:] โมเมนตัมของระบบก่อนชน เท่ากับ โมเมนตัมของระบบหลังชน
    - :green[อนุรักษ์พลังงาน:] พลังงานของระบบก่อนชน เท่ากับ พลังงานของระบบหลังชน

2. :blue[**🔸Inelastic Collisions🔸:**] คือการชนที่มีการสูญเสียพลังงานบางส่วนไปในการชน
    - :green[อนุรักษ์โมเมนตัม:] โมเมนตัมของระบบก่อนชน เท่ากับ โมเมนตัมของระบบหลังชน 
    
    2.1 :blue[**🔸Completely Inelastic Collisions🔸:**] เป็นการชนที่วัตถุติดกันไปหลังชน การชนแบบนี้จะมีการสูญเสียพลังงานเสมอ
'''
    )

st.divider()
st.header(':green[📝Exercises📝]')
ex_tabs = st.tabs([':orange[**Guided Examples**]',':orange[**Exercises (Homework)**]'])

with ex_tabs[0]:
    example_col = st.columns(3)
    with example_col[0]:
        e1_chk = st.checkbox(':violet[**Example 1**🔖]')
        e2_chk = st.checkbox(':violet[**Example 2**🔖]')
    with example_col[1]:
        e3_chk = st.checkbox(':violet[**Example 3**🔖]')
        e4_chk = st.checkbox(':violet[**Example 4**🔖]')
    with example_col[2]:
        e5_chk = st.checkbox(':violet[**Example 5**🔖]')
        e6_chk = st.checkbox(':violet[**Example 6**🔖]')

#---Example 1---#
    if e1_chk:
        st.info(
            '''
:red[**Ex 1:**] เด็กคนหนึ่งมวล :red[$40.0\\;kg$] กำลัง slide อยู่บนพื้นลื่นโดยมี Momentum ขนาด :red[$90.0\\;kg.m/s$] ไปทางทิศตะวันออก.
ที่เวลา :red[$t=0$] มีแรงขนาด :red[$F=8.20t\\;(N)$] กระทำกับเด็กคนนี้ในทิศตะวันตก.   
> A. ที่เวลาเท่าไหร่เด็กคนนี้ถึงจะมี momentum ขนาด :red[$60.0\\;kg.m/s$] ในทิศตะวันตก   
> B. จงหางานที่เกิดขึ้นกับเด็กคนนี้ในช่วงเวลา :red[$t=0$] ถึงเวลาในคำตอบข้อแรก   
> C. จงหาความเร่งของเด็กคนนี้ ณ เวลาที่หามาในข้อแรก   
'''
        )
        e1_ans = st.checkbox(':green[**Ex 1: Answers** 🖋️]')
        if e1_ans:
            st.markdown(
                '''
> ***Ans A:***  :green[$\\;\\;$  $t=6.05\\;s$] :balloon:    
> ***Ans B:***  :green[$\\;\\;$   $W_{tot}=-56.2\\;J$] :balloon:    
> ***Ans C:***  :green[$\\;\\;$   $a=1.24\\;m/s^{2}$] :balloon:
'''
            )
        e1_sol = st.checkbox(':orange[**Ex 1: Solutions**🔎]')
        if e1_sol:
            st.markdown(
                '''
:green[**Part A**]   
ในพาร์ทนี้เรารู้ :orange[Linear Momentum] ทั้งตอนแรกและตอนหลังที่อยากได้, และเรารู้ :orange[แรงในรูปเวลา, $F(t)$] เขาถามเราว่า :red[ใช้เวลาเท่าไหร่] แรงที่ออกถึงจะทำให้โมเมนตัมเปลี่ยนไปเท่านั้น   
เราให้เวลา $t_2$ เป็นเวลาที่เราอยากได้ จากนั้น Apply :violet[Momentum-Impulse Theorem]
$$
\\int_{t=0}^{t_2} F(t)dt = \\vec{p_f} - \\vec{p_i}
$$
$$
\\int_{t=0}^{t_2}(-8.20t)dt = (-60.0) - (90.0)
$$
จะแก้ได้ :green[$t_2=6.05 s$] :balloon:  
   
:green[**Part B**]   
ข้อนี้เราอยากได้ :red[งานที่เกิดบนวัตถุ] โดยทั่วไปเราหาได้สองวิธีคือ
1. หาจากแรง ผ่านสมการ $\\;W=\\int F(x)dx$ แต่ว่าข้อนี้เราไม่รู้ :orange[แรงในรูปฟังก์ชันของตำแหน่ง] :heavy_multiplication_x:
2. อีกวิธีคือหาอ้อมๆผ่าน :violet[Work-Energy Theorem] $\\;W_{tot}=\\Delta KE$ ซึ่งเราสามารถหา :orange[Kinetic Energy] ได้ :heavy_check_mark:

จาก $KE = \\frac{1}{2} mv^2=\\frac{p^2}{2m}$ จะได้ว่า
$$
W_{tot}=\\frac{p_{f}^{2}}{2m}-\\frac{p_{i}^{2}}{2m}
$$
จะแก้ได้ :green[$\\; W_{tot}=-56.2 \\;J$]  :balloon: 
   
:green[**Part C**]   
ในพาร์นี้เราอยากได้ :red[ความเร่งที่เวลา $\\; t=6.05\\;s $] เรารู้ :orange[แรงในรูปเวลา] เพราะฉะนั้นเราหาจาก :violet[$Newton's \\; 2^{nd} \\; Law$] ได้ตรงๆ   
$$
a = \\frac{F}{m}=\\frac{-8.20t}{m}
$$
แทนค่า $t=6.05$ ลงไป จะได้ :green[$\\; a=1.24 \\; m/s^2 $] :balloon:
$$

''')

#---Example 2---#
    if e2_chk:
           st.info(
            '''
:red[Ex 2:] ในการระเบิดของภูเขาไฟลูกหนึ่ง ก้อนหินมวล :red[$2400\\;kg$] ถูกดีดขึ้นตรงๆไปบนฟ้า.   
ในขณะที่หินก้อนนี้เคลื่อนที่ไปถึงจุดสูงสุด มันได้ระเบิดและแตกตัวออกเป็นสองส่วน โดยส่วนหนึ่งมีมวลเป็นสามเท่าของอีกส่วน.   
ทันทีหลังการระเบิด แต่ละส่วนมีความเร็วในแนวระดับเท่านั้น โดนที่ส่วนที่เบากว่าไปตกที่ระยะ :red[$318\\;m$] ทางเหนือของภูเขาไฟ.   
> หากไม่พิจารณาแรงต้านอากาศ จงหาว่าอีกส่วนจะตกห่างจากภูเขาไฟเท่าไหร่
'''
)
           e2_ans = st.checkbox(':green[**Ex 2: Answers** 🖋️]')
           if e2_ans:
                st.markdown(
                '''
> ***Ans:*** :green[$\\;\\;$ $106\\;m\\;$ ทางใต้ของภูเขาไฟ] :balloon:  
'''
)
           e2_sol = st.checkbox(':orange[**Ex 2: Solutions**🔎]')
           if e2_sol:
                st.markdown(
                '''
เนื่องจากการระเบิดเป็นผลจากแรงภายในเท่านั้น เรา Apply :violet[**หลักอนุรักษ์โมเมนตัมเชิงเส้นในแนวระดับ**] โดยให้ทิศเหนือเป็นบวกได้ดังนี้
$$
\\begin{align}
\\Sigma P_i &= \\Sigma P_f \\\\
0 &= mv_{small} + (3m)v_{big} \\\\
v_{big} &= -\\frac{1}{3}v_{small}
\\end{align}
$$
เพราะฉะนั้น :blue[ความเร็วในแนวระดับตอนเริ่ม] ของตัวที่ใหญ่กว่าจะมีขนาดเป็น :blue[$\\frac{1}{3}$] เท่าของตัวที่เบากว่า   
หลังระเบิด ทั้งสองจะมี :blue[ความเร็วเริ่มต้นในแนวระดับ] จากนั้นทั้งสองจะถูกแรงโน้มถ่วงทำให้เกิดความเร่ง :orange[$g$, ในทิศลง] เท่ากัน
เพราะฉะนั้นทั้งสองจะ:orange[ใช้เวลาเท่ากันเพื่อตกลงมาถึงพื้น]   
เมื่อเรารู้ว่าตัวใหญ่มีความเร็วในแนวระดับเป็น $\\frac{1}{3}$ เท่าของตัวเล็ก และทั้งสองใช้เวลาเท่ากันเพื่อมาถึงพื้น เพราะฉะนั้น :green[ระยะทางของตัวใหญ่ในแนวระดับจะเป็น $\\frac{1}{3}$ เท่าของระยะทางในแนวระดับของตัวเล็ก]   

จะได้ว่า $ \\Delta S_{x,Big}=\\frac{1}{3} \\Delta S_{x,Small}$ คือ :green[$\\; \\Delta S_{Big}=106\\;m$, South] :balloon:

''')


#---Example 3---#
    if e3_chk:
        st.info(
            '''
:red[**Example 3:**] ลูกเทนนิสหนัก :red[$0.560\\;N$] มีความเร็ว :red[$20.0\\hat{i}-4.0\\hat{j} \\; (m/s)$] ถูกตีด้วยไม้เทนนิส.        
ระหว่างที่ถูกตี ลูกเทนนิสสัมผัสกับไม้เป็นเวลา :red[$3.00\\;ms$] และไม้ทำให้เกิดแรง :red[$-380\\hat{i}+110\\hat{j}\\;N$] คงที่บนลูกเทนนิส.       
> A: จงหา x-,y-components ของ Impulse ที่เกิดบนลูกเทนนิสตลอดการตีครั้งนี้.   
> B: จงหา final-velocity ทั้งสอง components ของลูกเทนนิสหลังถูกตี.
'''
        )

        e3_ans = st.checkbox(':green[**Ex 3: Answers** 🖋️]')
        if e3_ans:
            st.markdown(
                '''
> A: :green[$\\;J_x=-1.14 \\;Ns$] :green[$,\\;J_y=0.330\\;Ns\\;$] :balloon:   
> B: :green[$\\;v_x=-0.04 \\;m/s$] :green[$,\\;v_y=1.8\\;m/s\\;$] :balloon:
'''
            )
        
        e3_sol = st.checkbox(':orange[**Ex 3: Solutions**🔎]')
        if e3_sol:
            st.markdown(
                '''
:green[**Part A**]   
เนื่องจากในข้อนี้แรงเป็นแรงคงที่ เราสามารถหา :blue[**Impulse**] ได้จากสมมการ :blue[$\\vec{J}=\\vec{F}\\Delta t$] ตรงๆ จะได้ว่า
$$
\\begin{align}
J_x &= F_x \\Delta t \\\\
J_y &= F_y \\Delta t
\\end{align}
$$
แทน :orange[Force $F_x,\\;F_y$] และ :orange[ช่วงเวลา $\\Delta t$] ลงไปจะได้ :green[$\\;J_x=-1.14 \\;Ns$] :green[$,\\;J_y=0.330\\;Ns\\;$] :balloon:   
   
:green[**Part B**]   
เราใช้ :blue[**Weight ของวัตถุ**] ที่ให้มาเพื่อหามวล และใช้ :blue[**ความเร็วเริ่มต้น**] ที่ให้มาเพื่อหา :blue[**Momentum**] ในตอนแรกได้   
จากนั้นเราใช้ :red[:exclamation:**Momentum-Impulse Theorem**:exclamation:] ประกอบกับ :blue[**Impulse**] ที่ได้จากข้อ A เพื่อหาโมเมนตัมตอนสุดท้าย   
$$
\\begin{align}
\\vec{J} &= \\vec{p}_f - \\vec{p}_i \\\\
\\vec{J} &= m\\vec{v}_f - m \\vec{v}_i \\\\
\\vec{v}_f &= \\frac{\\vec{J}}{m} + \\vec{v}_i
\\end{align}
$$   
จะได้ :green[$\\;v_x=-0.04 \\;m/s$] :green[$,\\;v_y=1.8\\;m/s\\;$] :balloon:

''')

#---Example 4---#
    if e4_chk:
        st.info(
            '''
:red[***Example 4:***] วัตถุสามตัวมีแม่เหล็กติดอยู่ทำให้ทั้งสามพยายามผลักกันตลอดเวลา.    
ในตอนแรกทั้งสามถูกจับให้อยู่นิ่งติดกัน จากนั้นปล่อยให้ทั้งสามดีดออกจากกัน โดยที่ทั้งสามจะมี :red[อัตราเร็ว] เท่ากันเสมอ.   
> หากมีตัวหนึ่งกำลังเคลื่อนที่ไปในทิศตะวันตก จงหาทิศทางการเคลื่อนที่ของอีกสองตัวที่เหลือ
'''
        )

        e4_ans = st.checkbox(':green[**Ex 4: Answers** 🖋️]')
        if e4_ans:
            st.markdown(
                '''
> ***Ans:*** :green[$\\; 60^o$ ทางเหนือและทางใต้ของทิศตะวันออก] :balloon: 
'''
            )
        
        e4_sol = st.checkbox(':orange[**Ex 4: Solutions**🔎]')
        if e4_sol:
            st.markdown(
                '''
หลังจากปล่อยมือออก ทั้งสามมีความเร็วชั่วขณะเป็นศูนย์ เพราะฉะนั้น :blue[Total Momentum] ของระบบในตอนแรกคือ :blue[$0$].   
จากนั้นทั้งสามดีดออกจากกันด้วยแรงที่ทำกันเอง (แรงภายใน) เพราะฉะนั้น เราสามารถ apply   
:red[:exclamation: Principle of Conservation of Linear Momentum :exclamation:] กับทั้งระบบได้ คือ
> :blue[Total Momentum] ของระบบเสี้ยววินาทีหลังปล่อยมือ = :blue[Total Momentum] ของระบบที่เวลาใดๆ.   

ให้ :orange[$v$] แทนอัตราเร็วของทั้งสามตัว ให้ทิศตะวันออกแทนแนว :orange[$+x$] และทิศเหนือแทนแนว :orange[$+y$]   
ให้ มวลตัวแรกไปทางตะวันตก ตัวที่สองทำมุม :orange[$+\\alpha$] กับทิศตะวันออก และตัวที่สามทำมุม :orange[$-\\beta$] กับทิศตะวันออก
$$
\\begin{align}
P_{y,i} &= P_{y,f} \\\\
0 &= v\\sin{\\alpha} - v\\sin{\\beta} \\\\
\\alpha &= \\beta
\\end{align}
$$
เพราะฉะนั้นตัวที่สองและตัวที่สามทำมุมกับทิศตะวันออกเท่ากัน แต่คนละทิศ ให้มุมนั้นเป็น :orange[$\\theta$]  
$$
\\begin{align}
P_{x,i} &= P_{x,f} \\\\
0 &= [-v]_{obj 1} + [v\\cos{\\theta}]_{obj2} + [v\\cos{\\theta}]_{obj3} \\\\
0 &= -1 + 2\\cos{\\theta}  \\\\
\\cos{\\theta} &= \\frac{1}{2} \\\\
\\theta &= 60^o
\\end{align}
$$
จะได้ว่าตัวที่สองและตัวที่สามมีความเร็วในทิศ  :green[$\\; 60^o$ ทางเหนือและทางใต้ของทิศตะวันออก] :balloon: 
'''
            )

#---Example 5---#
    if e5_chk:
        st.info(
            '''
:red[***Example 5:***] กล่องไม้มวล :red[$8.00\\;kg$] วางอยู่ที่ขอบโต๊ะสูง :red[$2.20\\;m$] จากพื้น.   
ก้อนหินมวล :red[$0.500\\;kg$] ถูกดีดเข้าหากล่องไม้ด้วยอัตราเร็ว :red[$24.0\\;m/s$] จากนั้นก้อนหินชนกับกล่องไม้แล้วติดกันไป. 
> จงหาว่าทั้งสองจะตกถึงพื้นห่างจากโต๊ะเป็นระยะเท่าไหร่
''')

        e5_ans = st.checkbox(':green[**Ex 5: Answers** 🖋️]')
        if e5_ans:
            st.markdown(
                '''
> ***Ans:*** :green[$\\;0.946\\;m$] :balloon:
'''
            )
        
        e5_sol = st.checkbox(':orange[**Ex 5: Solutions**🔎]')
        if e5_sol:
            st.markdown(
                '''
ในขั้นตอนแรกเราพิจารณา :orange[Collision] ระหว่างก้อนหินกับกล่องไม้ก่อน เพื่อหาอัตราเร็วของทั้งสองทันทีหลังชน.   
หลังจากได้อัตราเร็วหลังชนแล้ว เราพิจารณา :orange[Projectile Motion] ของทั้งสอง โดยมี :orange[ความเร็วหลังชน] เป็นความเร็วต้นในแนวระดับ.   
   
เนื่องจากทั้งสองชนแล้วติดกันไป เพราะฉะนั้นการชนนี้เป็นแบบ :red[Completely Inelastic Collision] เราจึงใช้ได้แค่ :blue[หลักอนุรักษ์โมเมนตัม] เพื่อพิจารณาเท่านั้น.   
$$
\\begin{align}
[\\; P_f &= P_i \\;] \\\\
(m_{wood}+m_{stone})V &= m_{stone} v_{stone} \\\\
V &= \\frac{m_{stone}}{m_{wood}+m_{stone}} v_{stone}
\\end{align}
$$
จะแก้ได้ :blue[อัตราเร็วของทั้งสองหลังชน] เป็น :blue[$V =1.412\\;m/s .$]   
   
จากนั้นจะเป็น :orange[Projectile Motion] ของวัตถุสูง :blue[$2.20\\;m$] จากพื้น ที่มีความเร็วต้นในแนวระดับเป็น :blue[$V =1.412\\;m/s .$]
$$
\\begin{align}
[\\; \\Delta S_y &= u_y \\Delta t + \\frac{1}{2}g \\Delta^2 t \\;] \\\\
\\Delta t &= \\sqrt{\\frac{2\\Delta S_y}{g}}
\\end{align}
$$
เมื่อแก้ออกมาจะได้ :blue[เวลาที่ทั้งสองใช้เพื่อตกถึงพื้น, $\\Delta t = 0.6701\\;s.$]   
$$
\\begin{align}
[\\; \\Delta S_x &= u_x \\Delta t \\;] \\\\
\\end{align}
$$
สมการนี้จะแก้หา :blue[ระยะตามแกน $x$] ที่ทั้งสองเคลื่อนที่ได้ เป็น :green[$\\Delta S_x = 0.946\\;m$] :balloon:



'''
            )

#---Example 6---#
    if e6_chk:
        st.info(
            '''
:red[***Example 6:***] ขี้หมาก้อนหนึ่งมวล :red[$5.00\\;kg$] กำลังสไลด์อยู่บนพื้นลื่นด้วยอัตราเร็ว :red[$12.0\\;m/s$].   
จากนั้นขี้หมาก้อนแรกเข้าชนกับขี้หมาอีกก้อน มวลเท่ากัน จากหมาตัวเดียวกัน ที่วางนิ่งอยู่บนพื้น โดยทั้งสองติดกันไปหลังชน.   
> หากคุณยืนอยู่ข้างๆขี้หมาก้อนที่อยู่นิ่ง แล้วเห็นขี้หมาอีกก้อนวิ่งมา คุณต้องวิ่งหนีขึ้นเนินสูงอย่างน้อยเท่าไหร่จึงจะปลอดภัย
'''
        )
        st.image('my_storage/lecture_03/example_6_01.png')

        e6_ans = st.checkbox(':green[**Ex 6: Answers** 🖋️]')
        if e6_ans:
            st.markdown(
                '''
***Ans:*** :green[$\\; 1.8\\;m$] :balloon:
'''
            )
        
        e6_sol = st.checkbox(':orange[**Ex 6: Solutions**🔎]')
        if e6_sol:
            st.markdown(
                '''
เราแบ่ง Motion ออกเป็นสองช่วง คือ :blue[ช่วงที่ทั้งสองกำลังชนกัน] กับ :blue[ช่วงหลังชนที่ทั้งสองไต่ขึ้นเนิน].   
   
เนื่องจากทั้งสองชนแล้วติดกันไป เพราะฉะนั้นนี่คือ :red[Completely Inelastic Collision] วิเคราะห์ได้โดย   
:blue[Principle of Conservation of Linear Momentum].   
ให้ :orange[$m$] แทนมวลของขี้หมาทั้งสองก้อน, :orange[$v$] แทนอัตราเร็วของขี้หมาก้อนแรก และ :orange[$V$] แทนอัตราเร็วทั้งสองหลังติดกันไป.
$$
\\begin{align}
[\\; P_f &= Pi \\;] \\\\
2mV &= mv \\\\
V &= \\frac{1}{2} v
\\end{align}
$$
เพราะฉะนั้น :orange[อัตราเร็วของทั้งสองทันทีหลังชนคือ $V=6.0\\;m/s$]
   
ช่วงที่สองทั้งสองจะไต่ขึ้นเนินไปบนพื้นลื่น เพราะฉะนั้น เราใช้ :blue[Principle of Conservation of Energy] วิเคราะห์ช่วงนี้ได้.   
ให้ :orange[$H$] แทนความสูงที่ตั้งสองใต่ขึ้นเนินได้.
$$
\\begin{align}
[\\; E_f &= E_i \\;] \\\\
(2m)gH &= \\frac{1}{2}(2m)V^2 \\\\
H &= \\frac{V^2}{2g}
\\end{align}
$$
จะแก้ใด้ :green[ความสูงที่ต้องหลบคือ] :green[$H=1.8\\;m$] :balloon:
'''
            )


with ex_tabs[1]:
    example_col = st.columns(3)
    with example_col[0]:
        p1_chk = st.checkbox(':violet[**Problem 1**🧑‍💻]')
        p2_chk = st.checkbox(':violet[**Problem 2**🧑‍💻]')
        p3_chk = st.checkbox(':violet[**Problem 3**🧑‍💻]')
    with example_col[1]:
        p4_chk = st.checkbox(':violet[**Problem 4**🧑‍💻]')
        p5_chk = st.checkbox(':violet[**Problem 5**🧑‍💻]')
        p6_chk = st.checkbox(':violet[**Problem 6**🧑‍💻]')
    with example_col[2]:
        p7_chk = st.checkbox(':violet[**Problem 7**🧑‍💻]')
        p8_chk = st.checkbox(':violet[**Problem 8**🧑‍💻]')
        p9_chk = st.checkbox(':violet[**Problem 9**🧑‍💻]')


#---Problems 1---#
    if p1_chk:
        st.info(
            '''
:red[***Problem 1:***] ปล่อยลูกบอลมวล :red[$40.0\\;kg$] ที่ความสูง :red[$2.00\\;m$] จากพื้น.   
หากลูกบอลกระทบกับพื้นแล้วเด้งขึ้นไปได้สูง :red[$1.60\\;m$]
> A: จงหา Impulse ที่เกิดบนบอลลูกนี้จากการชน   
> B: ถ้าบอลสัมผัสกับพื้นเป็นเวลา :red[$2.00\\;ms$] จงหาแรงเฉลี่ยที่พื้นกระทำกับบอล
'''
        )
        
        p1_ans = st.checkbox(':green[**Problem 1: Answers** 🖋️]')
        if p1_ans:
            st.markdown(
                '''
> ***Ans A:*** :green[$\\; -0.474\\;kg.m/s \\;$] :balloon:   
> ***Ans B:*** :green[$\\; 237\\;N \\;$, UP] :balloon:
'''
            )

#---Problems 2---#
    if p2_chk:
        st.info(
            '''
:red[***Problem 2:***] กระต่ายมวล :red[$1500\\;kg$] กำลังเคลื่อนที่ไปทางใต้ และเป็ดมวล :red[$2000\\;kg$] กำลังเคลื่อนที่ไปทางทิศตะวันตก.   
หาก **Total Linear Momentum** ของระบบมีค่าเป็น :red[$7200\\;kg.m/s$] ทิศ :red[$60^o$] ทางตะวันตกของทิศใต้
> จงหาอัตราเร็วของ กระต่าย และ เป็ด
'''
        )

        p2_ans = st.checkbox(':green[**Problem 2: Answers** 🖋️]')
        if p2_ans:
            st.markdown(
                '''
> ***Ans A:*** กระต่าย :green[$\\; 2.40\\;m/s \\;$] :balloon:, เป็ด :green[$\\; 3.12\\;m/s \\;$] :balloon:
'''
            )

#---Problems 3---#
    if p3_chk:
        st.info(
            '''
:red[***Problem 3:***] ทรงกลม :red[**A**] มวล :red[$\\;0.020\\;kg\\;$], :red[**B**] มวล :red[$\\;0.030\\;kg\\;$], :red[**C**] มวล :red[$\\;0.050\\;kg\\;$]
กำลังวิ่งเข้าหา Origin ดังภาพ.   
ทั้ง 3 มาถึง Origin พร้อมกัน ชนกัน และติดไปด้วยกัน.
> A: จงหา Components ตามแกน x และ y ของความเร็วของ C หากต้องการให้ทั้งสามมีความเร็ว :red[$0.50\\;m/s$, ในแนว +x] หลังชน.   
> B: ต่อจากข้อ (A) จงหาพลังงานจลน์ที่เปลี่ยนไปของทั้งระบบ.
'''
)
        st.image('my_storage/lecture_03/p_03_01.png')
        p3_ans = st.checkbox(':green[**Problem 3: Answers** 🖋️]')
        if p3_ans:
            st.markdown(
                '''
> ***Ans A:*** :green[$\\; v_{c,x}=1.75\\;m/s, \\; v_{c,y}=0.260\\;m/s \\;$] :balloon:   
> ***Ans B:*** :green[$\\; \\Delta KE = -0.092 \\; J \\;$] :balloon:
'''
            )

#---Problems 4---#
    if p4_chk:
        st.info(
            '''
:red[***Problem 4:***] คนสองคนเล่นกันบนพื้นน้ำแข็ง :red[Sam] มวล :red[$\\; 80.0\\;kg \\;$] กำลังเคลื่อนที่ไปทางตะวันออก 
:red[Abigial] มวล :red[$\\; 50.0\\;kg \\;$] กำลังเคลื่อนที่ไปทางเหนือ.   
หากหลังจากที่ทั้งสองชนกัน :red[Sam] เคลื่อนที่ด้วยอัตราเร็ว :red[$\\; 6.00 \\; m/s \\;$] ในทิศ :red[$\\; 37.0^o \\;$] ทางเหนือของทิศตะวันออก
:red[Abigial] เคลื่อนที่ด้วยอัตราเร็ว :red[$\\; 9.00 \\; m/s \\;$] ในทิศ :red[$\\; 23.0^o \\;$] ทางใต้ของทิศตะวันออก.   
> A: จงหาอัตราเร็วของแต่ละคนก่อนชนกัน.   
> B: พลังงานจลน์ของทั้งสองคนรวมกันลดลงเท่าไหร่จากการชน.
'''
        )

        p4_ans = st.checkbox(':green[**Problem 4: Answers** 🖋️]')
        if p4_ans:
            st.markdown(
                '''
> ***Ans A:*** :green[$\\; v_{Sam}=9.97 \\;m/s, \\; v_{Abigial}=2.26\\;m/s \\;$] :balloon:   
> ***Ans B:*** :green[$\\; \\Delta KE = -639 \\; J \\;$] :balloon:
'''
            )

#---Problems 5---#
    if p5_chk:
        st.info(
            '''
:red[***Problem 5:***] นิวเคลียสของ :red[$ \\; .^{214}Po \\; $] สลายตัวและปล่อย :red[Alpha-Particle] มวล :red[$\\; 6.65 \\times 10^{-27} \\;kg\\;$]
ที่มีพลังงาน :red[$\\; 1.23 \\times 10^{-12} \\;J \\;$] ออกมาหนึ่งตัว.   
> หากในตอนแรกพิจารณาว่า :red[$\\; .^{214}Po \\;$] อยู่นิ่ง จงหา :red[Reciol Velocity] ของนิวเคลียสที่เหลืออยู่.
'''
        )

        p5_ans = st.checkbox(':green[**Problem 5: Answers** 🖋️]')
        if p5_ans:
            st.markdown(
                '''
> ***Ans :*** :green[$\\; v_{recoil}=3.65 \\times 10^{5} \\; m/s \\; \\;$] :balloon:
'''
            )

#---Problems 6---#
    if p6_chk:
        st.info(
            '''
:red[***Problem 6:***] พิจารณารถสองคัน :red[A] มวล :red[$\\; 840 \\; kg \\;$] วิ่งด้วยอัตราเร็ว :red[$\\; 9.0 \\; m/s \\;$]
:red[B] มวล :red[$\\; 1620 \\; kg \\;$] วิ่งด้วยอัตราเร็ว :red[$\\; 5.0 \\; m/s \\;$].   
> A: จงหาสัดส่วนพลังงานจล์ของรถทั้งสอง $\\; KE_A : KE_B \\;$.   
> B: จงหาสัดส่วนโมเมนตัมของรถทั้งสอง $\\; p_A : p_B \\;$.   
> C: ให้ $\\; F_A, F_B\\;$ เป็นแรงที่ต้องใช้หยุดรถ A และ B ในเวลา $\\; \\Delta t \\;$ เท่ากัน จงหา $\\; F_A:F_B\\;$.   
> D: ให้ $\\; F_A, F_B\\;$ เป็นแรงที่ต้องใช้หยุดรถ A และ B ในระยะ $\\; \\Delta S \\;$ เท่ากัน จงหา $\\; F_A:F_B\\;$.   
'''
        )

        p6_ans = st.checkbox(':green[**Problem 6: Answers** 🖋️]')
        if p6_ans:
            st.markdown(
                '''
> ***Ans A:*** :green[$\\; \\frac{KE_A}{KE_B}=1.68 \\;$] :balloon:      
> ***Ans B:*** :green[$\\; \\frac{p_A}{p_B}=0.933 \\;$] :balloon:   
> ***Ans C:*** :green[$\\; \\frac{F_A}{F_B}=0.933 \\;$] :balloon:      
> ***Ans D:*** :green[$\\; \\frac{F_A}{F_B}=1.68 \\;$] :balloon:   
ลองหาวิธีอธิบาย Pattern ของคำตอบดูไหม . . .   😵‍💫
'''
            )

#---Problems 7---#
    if p7_chk:
        st.info(
            '''
:red[***Problem 7:***] แท่งไม้มวล :red[$\\; 0.800 \\; kg \\;$] แขวนอยู่กับเชือกยาว :red[$\\; 1.60\\; m\\;$] โดยห้อยอยู่นิ่งๆ.   
จากนั้นมีกระสุนมวล :red[$\\; 12.0 \\;g\\;$] ยิงเข้ามาด้วยอัตราเร็ว :red[$\\; v_o \\;$] แล้วฝังเข้าไปในเนื้อไม้.   
ในขณะที่ทั้งสองแกว่งขึ้นไปได้สูง :red[$\\; 0.800\\;m \\;$] จากจุดต่ำสุด แรงตึงในเส้นเชือกมีค่าเป็น :red[$\\; 4.80\\;N \\;$].   
> จงหาค่าของ $v_o$   

'''
        )

        p7_ans = st.checkbox(':green[**Problem 7: Answers** 🖋️]')
        if p7_ans:
            st.markdown(
                '''
> ***Ans:*** :green[$\\; 281 \\; m/s \\;$] :balloon:
'''
            )

#---Problems 8---#
    if p8_chk:
        st.info(
            '''
:red[***Problem 8:***] รถ :red[B] มวล :red[$\\; 1900 \\; kg \\;$] จอดติดไฟแดงอยู่นิ่งๆ ถูกรถ :red[A] มวล :red[$\\; 1500 \\; kg \\;$] เข้าชนจากด้านหลัง.   
ทั้งสองติดกันไปหลังการชนโดยที่เบรกของทั้งสองทำงานทันที(ล้อไม่หมุน) และเมื่อดูจากรอยล้อพบว่าทั้งสองใถลไปเป็นระยะ :red[$\\; 7.15 \\; m \\;$].   
> หาก ส.ป.ส ความเสียดทานจลน์ระหว่างล้อกับพื้นมีค่าเป็น :red[$\\; 0.65\\;$] จงหาอัตราเร็วของ :red[A] ก่อนชน
'''
        )

        p8_ans = st.checkbox(':green[**Problem 8: Answers** 🖋️]')
        if p8_ans:
            st.markdown(
                '''
> ***Ans:*** :green[$\\; v_A = 21.6 \\; m/s \\;$] :balloon:
'''
            )

#---Problems 9---#
    if p9_chk:
        st.info(
            '''
:red[***Problem 9:***] รถ :red[A] มวล :red[$\\; 1500 \\; kg \\;$] วิ่งจากเหนือลงใต้ รถ :red[B] มวล :red[$\\; 2200 \\; kg \\;$] วิ่งจากตะวันออกไปตะวันตก.   
ทั้งสองชนกันที่สี่แยกแล้วติดไปด้วยกัน.   
หากทั้งสองไปหยุดที่ระยะ  :red[$\\; 5.39\\;m:West,\\;6.43\\;m:South \\;$] จากสี่แยก.
> จงหาอัตราเร็วของรถทั้งสองคันก่อนชนกัน หากกำหนดให้ ส.ป.ส ความเสียดทานจลน์ระหว่างล้อกับพื้นมีค่าเป็น :red[$\\; 0.75\\;$]
'''
        )

        p9_ans = st.checkbox(':green[**Problem 9: Answers** 🖋️]')
        if p9_ans:
            st.markdown(
                '''
> ***Ans:*** :green[$\\; v_A = 21 \\; m/s, \\; v_B = 12 \\; m/s \\;$] :balloon:
'''
            )








st.divider()
# Music-Player
music = [
    '/my_storage/music/wings_of_freedom_-_epica_x_titan.mp3',
    ]
music_name = [
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
    'Majesty - Ben Moon ft. Veela',
    'Mayuri Sadness - Steins;Gate OST',
    'Natural Corruption - Epica',
]
music_selector = st.selectbox(
    'เพลงเพลินๆระหว่างทำโจทย์ . . .:notes:', music_name
)
for i in range(len(music_name)):
    if music_selector == music_name[i]:
        st.audio(music[i])


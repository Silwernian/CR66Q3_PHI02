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

st.set_page_config(page_title='Lecture 5', page_icon='\U0001F412')

st.header(':violet[:ferris_wheel:**Lecture 5: Kinematics of Rotations** :ferris_wheel:]')
main_col = st.columns([3,1])
with main_col[0]:
    st.markdown(
    '''
#### เนื้อหาใน Lecture นี้   
1. :blue[**ตัวแปรสำหรับอธิบายการหมุน**]   
    1.1. Angular Position and Angular Displacement   
    1.2. Angular Velocity   
    1.3. Angular Acceleration
2. :blue[**การหมุนในกรณีที่ความเร่งเชิงมุมคงที่**]   
3. :blue[**ความสัมพันธ์ระหว่างการเคลื่อนที่เชิงเส้นและการหมุน**]   
    3.1. ความเร็วเชิงเส้นและความเร็วเขิงมุม   
    3.2. ความเร่งเชิงเส้นและความเร่งในแนวเส้นสัมผัส
'''
)

with main_col[1]:
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
topic = st.tabs([':octagonal_sign: **ตัวแปรสำหรับอธิบายการหมุน**', ':octagonal_sign: **การหมุนเมื่อความเร่งเชิงมุมคงที่**', ':octagonal_sign: **Linear VS Angular Variables**'])

#---- Topic 1 ----#
topic[0].markdown(
    '''
ในหัวข้อนี้เราจะเรียนเรื่อง :violet[การหมุนของวัตถุแข็งเกร็ง] เพราะงั้น concept แรกที่ควรเข้าใจตรงกันคือ :blue[วัตถุแข็งเกร็ง]   
> :blue[วัตถุแข็งเกร็ง] หรือ :blue[Rigid Body] คือ :blue[Object ที่มีรูปร่างคงที่, ไม่เปลี่ยนรูปทรง]   
> นิยามแบบเป็นทางการคือ :blue[วัตถุที่มีระยะห่างระหว่างแต่ละอนุภาคคงที่เสมอ]   

เพราะฉะนั้น เวลาที่วัตถุแข็งเกร็งหมุน มันจะต้องหมุนไปทั้งก้อน พร้อมๆกัน.   
'''
)
topic[0].markdown(
    '''
* :red[**Angular Position and Displacement**]

ตัวแปรแรกที่เราสนใจคือ :blue[ตำแหน่งเชิงมุม, Angular Position] มีนิยามดังนี้
> :blue[Angular Position, $\\; \\theta \\;$] = มุมที่อนุภาคอ้างอิงตัวหนึ่งบนวัตถุแข็งเกร็งทำกับแกนอ้างอิง   

เพราะงั้นเวลาเราจะอธิบายว่าวัตถุตัวหนึ่งหมุนไปได้มุมเท่าไหร่ เราต้องเลือกมา 1 จุดอ้างอิงบนวัตถุ แล้วดูว่าจุดนั้นอยู่ที่มุมเท่าไหร่   
โดยทั่วไปเราให้แกนอ้างอิงคือแกน :orange[$x$] โดยมุมที่วัดจะวัดให้ :orange[CCW] เป็นบวก และวัดในหน่วย :orange[Radian]   
   
มุมในหน่วย :orange[Radian] เรานิยามผ่านวงกลม โดยให้ :orange[$r$] แทนรัศมีวงกลม, :orange[$\\theta$] แทนมุมที่เราสนใจ และ :orange[$s$] แทนความยาวส่วนโค้งที่รองรับมุม   
จะได้
$$
🔸🔸🔸 \\theta = \\frac{s}{r} 🔸🔸🔸
$$
ใน 1 รอบวงกลม $s=2\\pi r$ เพราะฉะนั้น $1 \\; revolution = 2\\pi \\; radian$ หรือ :red[$\\pi \\; rad = 180^o$]

> :blue[Angular Displacement, $\\; \\Delta \\theta \\;$] = มุมที่เปลี่ยนไป, มุมที่หมุนไปได้ (หน่วย :orange[Radian] และมีทิศ :orange[CW or CCW]) 

'''
)
topic[0].image('pages/my_storage/lecture_05/top1_pic1.png',use_column_width=True)
topic[0].markdown(
    '''
* :red[**Angular Velocity**] 
> :blue[Angular Velocity, $\\omega$] = มุมที่เปลี่ยนไป ต่อ เวลาที่ใช้เปลี่ยนมุม, (อัตราการเปลี่ยนมุม)
$$
🔸🔸🔸 \\omega = \\frac{\\Delta \\theta}{\\Delta t} 🔸🔸🔸
$$

หน่วยของ :blue[ความเร็วเชิงมุม] คือ :blue[Radian : Sec, $rad/s$] แต่บางครั้งเราอาจเจอหน่วย :blue[$rev/min$] ซึ่งแปลว่า :blue[รอบต่อนาที]   

ในทำนองเดียวกับการนิยามความเร็วชั่วขณะ หากเราสนใจความเร็วเชิงมุมในช่วงเวลาที่่สั้นมากๆ จะได้
$$
🔸🔸🔸\\; \\omega = \\lim_{\\Delta t \\to 0}\\frac{\\Delta \\theta}{\\Delta t} =\\frac{d\\theta}{dt}\\;🔸🔸🔸
$$

เพราะฉะนั้น ถ้าบอกว่าวัตถุหนึ่งกำลังหมุนด้วยความเร็ว :orange[$\\; 3\\;rad/s \\;$] แปลว่า ใน :orange[$\\; 1 s\\;$] วัตถุจะหมุนไปได้ :orange[$\\; 3 \\;rad\\;$]   
:red[Side Note:] :blue[คาบ, Period] = เวลาที่วัตถุใช้หมุน/เคลื่อนที่ ครบ 1 รอบ สัมพันธ์กันความเร็วเชิงมุมผ่าน :blue[$\\; T=\\frac{2\\pi}{\\omega}$]

* :red[**Angular Acceleraion**]   
> :blue[Angular Acceleration, $\\; \\alpha \\;$]= ความเร็วเชิงมุมที่เปลี่ยนไป ต่อ เวลาที่ใช้เปลี่ยนความเร็ว   
เขียนเป้นสมการได้เป็น
$$
🔸🔸🔸\\alpha = \\frac{\\Delta \\omega}{\\Delta t} =\\frac{d\\omega}{dt}🔸🔸🔸
$$
มีหน่วยเป็น :blue[$\\; rad/s^2 \\;$]
ปริมาณนี้บอกว่า ใน 1 วินาที ความเร็วเชิงมุมเปลี่ยนไปเท่าไหร่

'''
)

ex_1 = topic[0].expander(':blue[ :orange_book: **Example 1:** :orange_book:] :blue[**ปริมาณพื้นฐานสำหรับอธิบายการหมุน**]')
with ex_1:
    st.markdown(
        '''
จุดๆหนึ่งบนล้ออันหนึ่งเส้นผ่านศูนย์กลาง :red[$0.36\\;m$] กำลังหมุนโดยมีตำแหน่งเชิงมุมเทียบเวลาเป็น :red[$\\; \\theta = 2.0t^3\\;rad$] 
> :orange[**Q1:**] จงหาระยะที่จุดนี้เคลื่อนที่ได้ในช่วง :red[$\\; t\\in[2.0\\;s, 5.0\\;s] \\;$]   

ที่เวลา :blue[$t=2.0\\;s$] วัตถุอยู่ที่มุม :blue[$16.0\\;rad$] ต่อมาที่เวลา :blue[$t=5.0\\;s$] วัตถุอยู่ที่มุม :blue[$250\\;rad$] เพราะฉะนั้นในช่วงนี้
วัตถุเคลื่อนที่ไปได้ :blue[$250-16 = 243\\;rad$]   
ล้ออันนี้มีรัศมี :blue[$0.18\\;m$] เพราะฉะนั้น จากสมการ :blue[$\\Delta S = r\\Delta \\theta$] จะได้ว่าล้อนี้เคลื่อนที่ไปได้ :green[$42\\;m$]:balloon:

> :orange[**Q2:**] จงหาอัตราเร็วเชิงมุมเฉลี่ยในช่วง :red[$\\; t\\in[2.0\\;s, 5.0\\;s] \\;$]

เราหาความเร็วเชิงมุมเฉลี่ยได้จาก
$$
\\begin{align}
\\omega &= \\frac{\\Delta \\theta}{\\Delta t} \\\\
&= \\frac{\\theta_2 - \\theta_1}{t_2 - t_1} 
\\end{align}
$$
แทนตัวเลขลงไปจะได้ :green[$\\; \\omega = 78\\;rad/s \\;$] :balloon:   
> :orange[**Q3:**] จงหาความเร็วเชิงมุมที่เวลา :red[$\\;  t=2.0\\;s \\;$] และที่เวลา :red[$\\;  t=5.0\\;s \\;$]   

ใช้นิยาม :blue[ความเร็วเชิงมุม(ชั่วขณะ), $\\; \\omega=\\frac{d\\theta}{dt} \\;$] จะได้ :blue[$\\; \\omega(t)= 6.0t^2\\;rad/s \\;$]   
จะได้ :green[$\\;  \\omega(2.0)= 24\\;rad/s \\;$ และ $\\;  \\omega(5.0)= 150\\;rad/s \\;$ ] :balloon:   

> :orange[**Q4:**] จงหาความเร่งเฉลี่ยในช่วง :red[$\\; t\\in[2.0\\;s, 5.0\\;s] \\;$]   

ใช้นิยามของ :blue[ความเร่งเฉลี่ย]
$$
\\begin{align}
\\alpha_{av} &= \\frac{\\Delta \\omega}{\\Delta t} \\\\
&= \\frac{\\omega_2 - \\omega_1}{t_2 - t_1} \\\\
\\end{align}
$$
แทนตัวเลขลงไปจะได้ :green[$\\; \\alpha_{av}=42\\;rad/s^2 \\;$] :balloon:  

> :orange[**Q5:**] จงหาความเร่งที่เวลา :red[$\\;  t=2.0\\;s \\;$] และที่เวลา :red[$\\;  t=5.0\\;s \\;$]   

ใช้นิยาม :blue[ความเร่งเชิงมุม(ชั่วขณะ), $\\; \\alpha=\\frac{d\\omega}{dt} \\;$] จะได้ :blue[$\\; \\alpha(t)= 12.0t\\;rad/s^2 \\;$]   
จะได้ :green[$\\;  \\alpha(2.0)= 24\\;rad/s^2 \\;$ และ $\\;  \\alpha(5.0)= 60\\;rad/s^2 \\;$ ] :balloon:   

'''
    )

#---- Topic 2 ----#
topic[1].markdown(
    '''
ถ้าเราพิจารณาดูดีๆ เราจะพบว่านิยามของปริมาณเชิงมุมใกล้เคียงกับปริมาณเชิงเส้นมาก   
|Linear Variables|Angular Variables|
|:----:|:----:|
|Position, :green[$\\;x$]|Angular Position, :green[$\\;\\theta$]|
|Displacement, :green[$\\;\\Delta x = x_2 - x_1$]|Angular Displacement, :green[$\\;\\Delta \\theta = \\theta_2 - \\theta_1$]|
|Velocity, :green[$\\;v=\\frac{dx}{dt}$]|Angular Velocity, :green[$\\;\\omega=\\frac{d\\theta}{dt}$]|
|Acceleration, :green[$\\; a=\\frac{dv}{dt}\\;$]|Angular Acceleration, :green[$\\; \\alpha=\\frac{d\\omega}{dt}\\;$]|

.    
เพราะฉะนั้น :blue[4-สูตรการเคลื่อนที่] กรณี :blue[ความเร่งคงที่] ก็ควรมีหน้าตาคล้ายกับ :blue[4-สูตรการหมุน] กรณี :blue[ความเร่งเชิงมุมคงที่]   
|Linear Formula|Angular Formula|
|:----:|:----:|
|:blue[$\\; v(t)=v_o+a\\Delta t \\;$]|:blue[$\\; \\omega(t)=\\omega_o+\\alpha \\Delta t  \\;$]|
|:blue[$\\;  x(t)=x_o + v_o\\Delta t + \\frac{1}{2}a\\Delta^2 t\\;$]|:blue[$\\; \\theta(t)=\\theta_o + \\omega_o\\Delta t + \\frac{1}{2}\\alpha\\Delta^2 t  \\;$]|
|:blue[$\\; v^{2}(t)=v_{0}^{2} + 2a(x(t)-x_o) \\;$]|:blue[$\\; \\omega^{2}(t)=\\omega_{0}^{2} + 2\\alpha(\\theta(t)-\\theta_o)  \\;$]|
|:blue[$\\; x(t) - x_o = \\frac{1}{2}(v_o + v(t))\\Delta t  \\;$]|:blue[$\\; \\theta(t) - \\theta_o = \\frac{1}{2}(\\omega_o + \\omega(t))\\Delta t  \\;$]|
   
.   
การใช้งาน :blue[4-สูตร] ยังเหมือนเดิม เพียงแต่ระวังตอนกำหนดทิศ ต้องกำหนดให้ :orange[ CW หรือ CCW] เป็น :heavy_plus_sign:   
ปริมาณพวกนี้ :blue[$\\theta, \\; \\omega, \\; \\alpha \\;$] จริงๆแล้วมีทิศ
'''
)


#---- Topic 3 ----#
topic[2].markdown(
    '''
#### :red[**ความเร็วเขิงเส้น VS ความเร็วเชิงมุม**]
ในหัวข้อนี้เราจะเรียนเกี่ยวกับ :blue[ความสัมพันธ์ระหว่างตัวแปรเชิงเส้นและตัวแปรเชิงมุม] ในการหมุน   
พิจารณาล้ออันหนึ่งที่กำลังหมุน เมื่อเวลาผ่านไปค่าหนึ่ง แต่ละจุดบนล้อจะเคลื่อนที่ได้ระยะทางไม่เท่ากัน   
> :blue[**ความเร็วเชิงเส้น, $v\\;$ ของแต่ละจุดบนล้อมีค่าไม่เท่ากัน**]

แต่ถ้าพิจารณามุมที่แต่ละตัวหมุนไปได้ จะเห็นว่าทุกตัวหมุนได้มุมเท่ากัน
> :blue[**ความเร็วเชิงมุม, $\\omega\\;$ของแต่ละจุดในล้อมีค่าเท่ากัน**]
'''
)
topic[2].image('pages/my_storage/lecture_05/topic3_pic1.png')

topic[2].markdown(
    '''
ถ้าวัตถุกำลังหมุนด้วย :blue[ความเร็วเชิงมุม, $\\;\\omega\\;$] เมื่อเวลาผ่านไป :blue[$\\Delta t \\;$] แต่ละตัวจะกวาดมุมไปได้ :blue[$\\; \\Delta \\theta = \\omega \\Delta t \\;$] เท่ากัน จะได้   
|Particle 1|Particle 2|Particle 3|
|:----:|:----:|:----:|
|$\\Delta S_1 = r_1 \\Delta \\theta$|$\\Delta S_2 = r_2 \\Delta \\theta$|$\\Delta S_3 = r_3 \\Delta \\theta$|
|$\\frac{\\Delta S_1}{\\Delta t}=r_1 \\frac{\\Delta \\theta}{\\Delta t}$|$\\frac{\\Delta S_2}{\\Delta t}=r_2 \\frac{\\Delta \\theta}{\\Delta t}$|$\\frac{\\Delta S_3}{\\Delta t}=r_3 \\frac{\\Delta \\theta}{\\Delta t}$|
|:blue[$v_1=\\omega r_1$]|:blue[$v_2=\\omega r_2$]|:blue[$v_3=\\omega r_3$]|

จะได้ความสัมพันธ์ระหว่าง :violet[**ความเร็วเชิงเส้น**,$v\\;$] และ :violet[**ความเร็วเชิงมุม**,$\\omega\\;$] ของอนุภาคที่:violet[อยู่ห่างจากแกนหมุน]เป็นระยะ :violet[$\\;r\\;$] คือ
$$
🔸🔸🔸v=\\omega r🔸🔸🔸
$$

#### :red[**ความเร่งในแนวเส้นสัมผัส VS ความเร่งเชิงมุม**]   
ถ้าเราโฟกัสไปที่จุดๆหนึ่งบนล้อที่ระยะ :blue[$\\;r\\;$] จากแกนหมุน ไม่ว่าล้อจะหมุนด้วยอัตราเร็วเชิงมุมเร็วขึ้น ช้าลง หรือเท่าเดิม จุดนั้นจะมีความเร่งสู่ศูนย์กลาง $\\; a_c = \\frac{v^2}{r}\\;$เสมอ   
แต่ว่า:blue[ความเร็วเชิงเส้น,$v\\;$] กับ :blue[ความเร็วเชิงมุม,$\\omega\\;$] สัมพันธ์กันผ่านสมการ :blue[$\\; v=\\omega r$] จะได้
> :orange[วัตถุที่หมุนด้วยความเร็วเชิงมุม $\\omega$ อยู่ที่ระยะ $r$ จากแกนหมุน จะต้องมีความเร่งสู่ศูนย์กลาง] :orange[$a_c = \\frac{v^2}{r} =\\omega^2 r$ เสมอ]
'''
)
topic[2].image('pages/my_storage/lecture_05/topic3_pic2.png',width=300)

topic[2].markdown(
    '''
คำถามคือ เกิดอะไรขึ้นเมื่อ :orange[วัตถุหมุนเร็วขึ้น หรือ หมุนช้าลง] แน่นอนว่า :blue[ความเร็วเชิงเส้น, $v$] ต้องเปลี่ยน(ยาวขึ้นหรือสั้นลง)
แต่ว่า :blue[$v$] มีทิศสัมผัสกับแนวการเคลื่อนที่(สัมผัสกับวงกลม)  เพราะฉะนั้น :blue[ทิศของความเร่งตัวใหม่ที่ทำให้วัตถุหมุนเร็วขึ้นหรือช้าลงต้องอยู่ในแนวสัมผัสกับวงกลม]
$$
\\begin{align}
a_{tan} &= \\frac{dv}{dt} \\\\
&= \\frac{d(\\omega r)}{dt} \\\\
&= r \\frac{d\\omega}{dt} \\\\
&= \\alpha r
\\end{align}
$$
เราเลยได้ข้อสรุปดังนี้
> :orange[เมื่อวัตถุหมุนเร็วขึ้น หรือ ช้าลง วัตถุที่ระยะ $r$ จากแกนหมุนจะรู้สึกถึงความเร่ง.ในแนวเส้นสัมผัส.$\\;a_{tan}=\\alpha r$]

ซึ่ง Make sense เพราะถ้าเรานึกถึงล้อที่กำลังหมุน ถ้าเราอยากให้มันหมุนเร็วขึ้น เราต้องเอามือไปปัดที่ขอบล้อ ในแนวสัมผัสกับล้อ และถ้าเราอยากให้ล้อหมุนช้าลง เราต้องเอาไปไปจับขอบล้อทำให้เกิดแรงเสียดทาน
แรงพวกนี้อยู่ในแนวสัมผัสกับการเคลื่อนที่ เพราะฉะนั้นความเร่งที่เกิดก็จะสัมผัสกับวงกลมเสมอ   
:red[**Note:**] หากโจทย์ถามหา :red[**ความเร่ง**] เฉยๆ เขาหมายถึงความเร่งสุทธิ ต้องหาจาก :red[$\\; a^2=a_c^2 + a_{tan}^2$]

'''
)

ex2 = topic[2].expander(':blue[ :orange_book: **Example 2:** :orange_book:] :blue[**ความเร่งในการหมุน**]')
with ex2:
    st.markdown(
        '''
นักกีฬาขว้างจานคนหนึ่งหมุนตัวเองเพื่อขว้างจาน จานนี้อยู่ที่ปลายมือของเขาซึ่งห่างจากแกนหมุนเป็นระยะ :red[$\\;80.0\\;cm\\;$]
ชั่วขณะหนึ่ง นักกีฬาคนนี้กำลังหมุนด้วยอัตราเร็วเชิงมุม :red[$\\; 10.0\\;rad/s \\;$] และกำลังเพิ่มขึ้นในอัตรา :red[$\\; 50.0\\;rad/s^2  \\;$]
> :red[**Q1:**] จงหาความเร่งของจานใน moment นั้น

:blue[**Solution:**]   
ความเร่งของจานที่กำลังหมุนจะมีสองส่วน ส่วนแรกคือ :blue[ความเร่งสู่ศูนย์กลาง] ซึ่งเกิดขึ้นเสมอในการหมุน อีกส่วนคือ :blue[ความเร่งในแนวเส้นสัมผัส] ซึ่งเกิดเพราะจานกำลังหมุนเร็วขึ้น   
:blue[ความเร่งสุทธิ] เกิดจากความเร่งสองตัวนี้รวมกัน(แบบเวกเตอร์)   
   
จานกำลังหมุนด้วย:blue[ความเร็วเชิงมุม,$\\;\\omega\\;$] เพราะฉะนั้นจะมีความเร่งสู่ศูนย์กลาง :blue[$a_c=\\frac{v^2}{r}=\\omega^2 r$]   
   
จานกำลังหมุนเร็วขึ้น คือมี :blue[ความเร่งเชิงมุม, $\\;\\alpha\\;$] จะมีความเร่งในแนวเส้นสัมผัส :blue[$\\; a_{tan}=\\alpha r \\;$]   

ความเร่งรวมที่เกิดบนวัตถุคือ
$$
\\begin{align}
a &= \\sqrt{(a_c)^2 + (a_{tan})^2} \\\\
&= \\sqrt{(\\omega^2 r)^2 + (\\alpha r)^2} \\\\
&= r\\sqrt{\\omega^4+\\alpha^2}
\\end{align}
$$
แทนค่าลงไปจะได้ :green[$\\; a=89.4\\;m/s^2  \\;$] :balloon:
'''
    )
    st.image('pages/my_storage/lecture_05/topic3_pic3.png')

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
:blue[**Exercise 1:**] ใบพัดของเครื่องบินลำหนึ่งกำลังหมุนในอัตรา :red[$\\;1900\\;rpm\\;(revolution/min)$]
> A: จงหาอัตราการหมุนนี้ในหน่วย :red[$rad/s$]   
> B: ต้องใช้เวลากี่วินาที ใบพัดจึงจะหมุนไปได้ :red[$35^o$]
'''
    )
    ex1_a = st.number_input(':violet[**Ans A:**] ในหน่วย $rad/s$')
    if abs(ex1_a - (199)) < 10:
        st.write(':green[:balloon::balloon:**CongratZ**]:balloon::balloon:')
        st.balloons()
    else:
        st.write(':red[Too bad. . .:crying_cat_face:] ')
        
    ex1_b = st.number_input(':violet[**Ans B:**] ในหน่วย $10^{-3}\\;s$')
    if abs(ex1_b - (3.1)) < 0.3:
        st.write(':green[:balloon::balloon:**CongratZ**]:balloon::balloon:')
        st.balloons()
    else:
        st.write(':red[Too bad. . .:crying_cat_face:] ')
      

#---- Exercise 2 -----#
if ex02:
    st.markdown(
        '''
:blue[**Exercise 2:**] ล้ออันหนึ่งมีอัตราเร็วเชิงมุมเป็น :red[$\\; \\omega(t)=2.75 + 1.50t \\;rad/s \\;$]
> จงหามุมที่ล้อนี้หมุนไปได้ในช่วง :red[$2.00\\;s$] แรก
'''
    )
    ex2_a = st.number_input(':violet[**Ans A:**] ในหน่วย $rad$')
    if abs(ex2_a - (9.50)) < 0.3:
        st.write(':green[:balloon::balloon:**CongratZ**]:balloon::balloon:')
        st.balloons()
    else:
        st.write(':red[Too bad. . .:crying_cat_face:] ')

#---- Exercise 3 -----#
if ex03:
    st.markdown(
        '''
:blue[**Exercise 3:**] เด็กคนหนึ่งเล่นม้าหมุน โดยม้าหมุนนี้หมุนได้มุม :red[$\\; \\theta(t)=0.400t+0.0120t^3\\;rad\\;$]
> A: จงหาอัตราเร็วเขิงมุมเฉลี่ยในช่วง :red[$\\; t \\in [0,5.00\\;s]\\;$]   
> B: จงหาอัตราเร็วเชิงมุมที่เวลา :red[$\\;t=5.00\\;s\\;$]
'''
    )
    ex3_a = st.number_input(':violet[**Ans A:**] ในหน่วย $rad/s$')
    if abs(ex3_a - (0.700)) < 0.005:
        st.write(':green[:balloon::balloon:**CongratZ**]:balloon::balloon:')
        st.balloons()
    else:
        st.write(':red[Too bad. . .:crying_cat_face:] ')
    ex3_b = st.number_input(':violet[**Ans B:**] ในหน่วย $rad/s$')
    if abs(ex3_b - (1.30)) < 0.05:
        st.write(':green[:balloon::balloon:**CongratZ**]:balloon::balloon:')
        st.balloons()
    else:
        st.write(':red[Too bad. . .:crying_cat_face:] ')
#---- Exercise 4 -----#
if ex04:
    st.markdown(
        '''
:blue[**Exercise 4:**] จานอันหนึ่งหมุนได้มุม :red[$\\; \\theta(t)=a+bt-ct^3 \\;rad\\;$]
ที่เวลา :red[$\\;t=0;\\;\\theta=\\pi/4,\\;rad\\;\\omega=2.00\\;rad/s\\;$] และที่เวลา
:red[$\\; t=1.50\\;s;\\;\\alpha=1.25\\;rad/s^2 \\;$] 
> จงหาค่าของ :red[a, b, c]
'''
    )
    ex4_a = st.number_input(':violet[**a =**] ในหน่วย $rad$')
    if abs(ex4_a - (np.pi/4)) < 0.03:
        st.write(':green[:balloon::balloon:**CongratZ**]:balloon::balloon:')
        st.balloons()
    else:
        st.write(':red[Too bad. . .:crying_cat_face:] ')
    ex4_b = st.number_input(':violet[**b =**] ในหน่วย $rad/s$')
    if abs(ex4_b - (2.00)) < 0.03:
        st.write(':green[:balloon::balloon:**CongratZ**]:balloon::balloon:')
        st.balloons()
    else:
        st.write(':red[Too bad. . .:crying_cat_face:] ')
    ex4_c = st.number_input(':violet[**c =**] ในหน่วย $rad/s^3$')
    if abs(ex4_c - (-0.139)) < 0.03:
        st.write(':green[:balloon::balloon:**CongratZ**]:balloon::balloon:')
        st.balloons()
    else:
        st.write(':red[Too bad. . .:crying_cat_face:] ')

#---- Exercise 5 -----#
if ex05:
    st.markdown(
        '''
:blue[**Exercise 5:**] ล้ออันหนึ่งหมุนในอัตราเริ่มต้น :red[$1.50\\;rad/s$]
> A: ถ้าความเร่งเชิงมุมคงที่ :red[$0.300\\;rad/s^2$] จงหาความเร็วเชิงมุมที่เวลา :red[$t=2.50\\;s$]   
> B: จงหามุมที่ล้อหมุนได้ในช่วง :red[$t \\in [0,2.50\\;s]$]
'''
    )
    ex5_a = st.number_input(':violet[**Ans A:**] ในหน่วย $rad/s$')
    if abs(ex5_a - (2.25)) < 0.03:
        st.write(':green[:balloon::balloon:**CongratZ**]:balloon::balloon:')
        st.balloons()
    else:
        st.write(':red[Too bad. . .:crying_cat_face:] ')
    ex5_b = st.number_input(':violet[**Ans B:**] ในหน่วย $rad$')
    if abs(ex5_b - (4.69)) < 0.03:
        st.write(':green[:balloon::balloon:**CongratZ**]:balloon::balloon:')
        st.balloons()
    else:
        st.write(':red[Too bad. . .:crying_cat_face:] ')

#---- Exercise 6 -----#
if ex06:
    st.markdown(
        '''
:blue[**Exercise 6:**] ใบมีดของเครื่องปั่นน้ำผลไม้หมุนด้วยความเร่ง :red[$1.50\\;rad/s^2$]
> A: หากเริ่มจากหยุดนิ่ง ต้องรอนานเท่าไหร่ถึงจะมีความเร็วเชิงมุมเป็น :red[$36.0\\;rad/s$]   
> B: ในช่วงนั้น ใบมีดหมุนไปได้ที่รอบ
'''
    )
    ex6_a = st.number_input(':violet[**Ans A:**] ในหน่วย $s$')
    if abs(ex6_a - (24.0)) < 0.3:
        st.write(':green[:balloon::balloon:**CongratZ**]:balloon::balloon:')
        st.balloons()
    else:
        st.write(':red[Too bad. . .:crying_cat_face:] ')
    ex6_b = st.number_input(':violet[**Ans B:**] ในหน่วย $revolution,\\; rev$')
    if abs(ex6_b - (68.8)) < 0.3:
        st.write(':green[:balloon::balloon:**CongratZ**]:balloon::balloon:')
        st.balloons()
    else:
        st.write(':red[Too bad. . .:crying_cat_face:] ')

#---- Exercise 7 -----#
if ex07:
    st.markdown(
        '''
:blue[**Exercise 7:**] โต๊ะตัวหนึ่งกำลังหมุนโดยมีความเร่งเชิงมุม :red[$2.25\\;rad/s^2$]
เมื่อผ่านไป :red[$4.00\\;s$] โต๊ะหมุนไปได้ :red[$60.0\\;rad$]
> จงหาอัตราเร็วเชิงมุมในตอนเริ่มของช่วง :red[$4.00\\;s$] นี้
'''
    )
    ex7_a = st.number_input(':violet[**Ans:**] ในหน่วย $rad/s$')
    if abs(ex7_a - (10.5)) < 0.3:
        st.write(':green[:balloon::balloon:**CongratZ**]:balloon::balloon:')
        st.balloons()
    else:
        st.write(':red[Too bad. . .:crying_cat_face:] ')

#---- Exercise 8 -----#
if ex08:
    st.markdown(
        '''
:blue[**Exercise 8:**] Lift สมัยก่อนทำงานโดยเอากล่อง Lift ผูกกับ Counterweight ผ่านรอก
หากรอกมีเส้นผ่านศูนย์กลาง :red[$2.50\\;m$]
> A: รอกต้องหมุนกี่ :red[$rpm$] จึงจะสามารถยก Lift ขึ้นได้ในอัตรา :red[$25\\; cm/s$]   
> B: ถ้าจะเริ่มให้ Lift ทำงาน ต้องเร่งมันด้วยความเร่ง :red[$\\frac{1}{8}g$] ความเร่งเชิงมุมของรอกต้องเป็นเท่าไหร่ถึงยก Lift ขึ้นได้   
> C: ในช่วงที่ Lift เคลื่อนที่ขึ้นได้ :red[$3.25\\;m$] รอกหมุนได้เท่าไหร่
'''
    )
    ex8_col = st.columns(2)
    ex8_col[1].image('pages/my_storage/lecture_05/ex08_pic1.png',width=200)
    ex8_a = ex8_col[0].number_input(':violet[**Ans A:**] ในหน่วย $rpm$')
    if abs(ex8_a - (1.91)) < 0.03:
        ex8_col[0].write(':green[:balloon::balloon:**CongratZ**]:balloon::balloon:')
        st.balloons()
    else:
        ex8_col[0].write(':red[Too bad. . .:crying_cat_face:] ')
    ex8_b = ex8_col[0].number_input(':violet[**Ans B:**] ในหน่วย $rad/s^2$')
    if abs(ex8_b - (0.98)) < 0.01:
        ex8_col[0].write(':green[:balloon::balloon:**CongratZ**]:balloon::balloon:')
        st.balloons()
    else:
        ex8_col[0].write(':red[Too bad. . .:crying_cat_face:] ')
    ex8_c = ex8_col[0].number_input(':violet[**Ans C:**] ในหน่วย $rad$')
    if abs(ex8_c - (2.60)) < 0.03:
        ex8_col[0].write(':green[:balloon::balloon:**CongratZ**]:balloon::balloon:')
        st.balloons()
    else:
        ex8_col[0].write(':red[Too bad. . .:crying_cat_face:] ')

#---- Exercise 9 -----#
if ex09:
    st.markdown(
        '''
:blue[**Exercise 9:**] ล้ออันหนึ่งมีเส้นผ่านศูนย์กลาง :red[$40.0\\;cm$] เริ่มจากหยุดนิ่งแล้วหมุนด้วยความเร่งคงที่ :red[$3.00\\;rad/s^2$]
> จงหาความเร่งในแนวรัศมี(ความเร่งสู่ศูนย์กลาง) ในขณะที่ล้อนี้หมุนครบสองรอบ
'''
    )
    ex9_a = st.number_input(':violet[**Ans:**] ในหน่วย $m/s^2$')
    if abs(ex9_a - (15.1)) < 0.3:
        st.write(':green[:balloon::balloon:**CongratZ**]:balloon::balloon:')
        st.balloons()
    else:
        st.write(':red[Too bad. . .:crying_cat_face:] ')

#---- Exercise 10 -----#
if ex10:
    st.markdown(
        '''
:blue[**Exercise 10:**] ถ้าเกิดเราเรียนไม่จบ เราอาจจะต้องไปทำงานก่อสร้าง สมมุติว่าในการสร้างตึกอันหนึ่งเราต้องการออกแบบรอก
ที่ใช้ยกถังคอนกรีตหนัก :red[$800\\;N$] จากพื้นขึ้นตึกสูง :red[$78.0\\;m$] 
> A: รอกควรมีเส้นผ่านศูนย์กลางเท่าไหร่ถ้าต้องการยกถังให้เคลื่อนที่ด้วยอัตราเร็ว :red[$2.00\\;cm/s$] ในขณะที่หมุนรอกในอัตรา :red[$7.5\\;rpm$]   
> B: ถ้าต้องการให้ถังเคลื่อนที่ด้วยความเร่ง :red[$0.400\\;m/s^2$] รอกต้องมีความเร่งเชิงมุมเท่าไหร่
'''
    )
    ex10_a = st.number_input(':violet[**Ans A:**] ในหน่วย $cm$')
    if abs(ex10_a - (5.09)) < 0.03:
        st.write(':green[:balloon::balloon:**CongratZ**]:balloon::balloon:')
        st.balloons()
    else:
        st.write(':red[Too bad. . .:crying_cat_face:] ')

    ex10_b = st.number_input(':violet[**Ans B:**] ในหน่วย $rad/s^2$')
    if abs(ex10_b - (15.7)) < 0.03:
        st.write(':green[:balloon::balloon:**CongratZ**]:balloon::balloon:')
        st.balloons()
    else:
        st.write(':red[Too bad. . .:crying_cat_face:] ')

st.divider()

# Music-Player
music = [
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
    'pages/my_storage/music/majesty_by_ben_moon_ft_veela.mp3',
    'pages/my_storage/music/mayuri_sadness_by_steinsgate_ost.mp3',
    'pages/my_storage/music/natural_corruption_by_epica.mp3',
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

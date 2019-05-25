#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhuangxu
@email: zhuangxu0@gmail.com
@time: 2019/5/13 11:28
@desc:
"""


import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
plt.rcParams['font.family'] = ['Times New Roman']


base_time = 1552485036959L
t_all = [
[1552485036959L, 125L, 216L, 122L, 463L],
[1552485037997L, 109L, 213L, 118L, 440L],
[1552485039024L, 117L, 216L, 119L, 452L],
[1552485040051L, 128L, 225L, 117L, 470L],
[1552485041084L, 120L, 236L, 151L, 507L],
[1552485042113L, 119L, 212L, 120L, 451L],
[1552485043134L, 117L, 212L, 125L, 454L],
[1552485044164L, 111L, 217L, 114L, 442L],
[1552485045185L, 121L, 211L, 122L, 454L],
[1552485046215L, 120L, 218L, 124L, 462L],
[1552485047240L, 132L, 227L, 109L, 468L],
[1552485048264L, 119L, 216L, 126L, 461L],
[1552485049296L, 112L, 215L, 117L, 444L],
[1552485050320L, 114L, 226L, 151L, 491L],
[1552485051349L, 123L, 218L, 127L, 468L],
[1552485052374L, 132L, 227L, 117L, 476L],
[1552485053398L, 117L, 215L, 120L, 452L],
[1552485054418L, 116L, 235L, 114L, 465L],
[1552485055439L, 121L, 214L, 121L, 456L],
[1552485056474L, 132L, 221L, 183L, 536L]
]

t_all_mlt = [
[1557718021078L, 114L, 206L, 105L, 425L],
[1557718021295L, 110L, 204L, 104L, 418L],
[1557718021510L, 116L, 203L, 106L, 425L],
[1557718021728L, 109L, 205L, 104L, 418L],
[1557718021956L, 109L, 204L, 104L, 417L],
[1557718022171L, 109L, 203L, 104L, 416L],
[1557718022383L, 109L, 203L, 104L, 416L],
[1557718022596L, 109L, 203L, 104L, 416L],
[1557718022815L, 109L, 205L, 104L, 418L],
[1557718023030L, 110L, 203L, 105L, 418L],
[1557718023245L, 110L, 203L, 105L, 418L],
[1557718023461L, 109L, 203L, 105L, 417L],
[1557718023674L, 109L, 207L, 104L, 420L],
[1557718028894L, 109L, 204L, 105L, 418L],
[1557718029111L, 108L, 204L, 103L, 415L],
[1557718029327L, 110L, 203L, 104L, 417L],
[1557718029543L, 109L, 203L, 103L, 415L],
[1557718029757L, 108L, 203L, 104L, 415L],
[1557718029971L, 107L, 204L, 103L, 414L],
[1557718030205L, 108L, 204L, 104L, 416L],
[1557718030420L, 107L, 203L, 104L, 414L],
[1557718030634L, 107L, 203L, 103L, 413L],
[1557718030845L, 108L, 204L, 105L, 417L],
[1557718031057L, 108L, 203L, 104L, 415L],
[1557718031269L, 107L, 204L, 104L, 415L],
[1557718031482L, 107L, 203L, 104L, 414L],
[1557718031698L, 107L, 206L, 104L, 417L],
[1557718031951L, 110L, 204L, 104L, 418L],
[1557718032166L, 108L, 205L, 104L, 417L],
[1557718032378L, 107L, 203L, 104L, 414L],
[1557718032611L, 108L, 203L, 105L, 416L],
[1557718032824L, 108L, 205L, 104L, 417L],
[1557718033038L, 109L, 206L, 105L, 420L],
[1557718033256L, 108L, 204L, 103L, 415L],
[1557718033470L, 107L, 204L, 104L, 415L],
[1557718033684L, 107L, 204L, 104L, 415L],
[1557718033897L, 107L, 203L, 104L, 414L],
[1557718034109L, 107L, 203L, 104L, 414L],
[1557718034322L, 108L, 210L, 107L, 425L],
[1557718034536L, 107L, 208L, 106L, 421L],
[1557718034759L, 107L, 204L, 105L, 416L],
[1557718034974L, 107L, 203L, 105L, 415L],
[1557718035187L, 107L, 203L, 104L, 414L],
[1557718035401L, 107L, 211L, 104L, 422L],
[1557718035617L, 108L, 203L, 104L, 415L],
[1557718035837L, 107L, 204L, 106L, 417L],
[1557718036065L, 108L, 204L, 104L, 416L],
[1557718036279L, 107L, 204L, 104L, 415L],
[1557718036490L, 107L, 203L, 104L, 414L],
[1557718036703L, 106L, 203L, 105L, 414L],
[1557718036919L, 107L, 205L, 106L, 418L],
[1557718037131L, 107L, 203L, 105L, 415L],
[1557718037355L, 108L, 204L, 106L, 418L],
[1557718037570L, 107L, 214L, 104L, 425L],
[1557718037790L, 107L, 203L, 104L, 414L],
[1557718038003L, 106L, 203L, 104L, 413L],
[1557718038241L, 116L, 203L, 104L, 423L],
[1557718038453L, 107L, 205L, 104L, 416L],
[1557718038666L, 106L, 204L, 104L, 414L],
[1557718038882L, 107L, 203L, 105L, 415L],
[1557718039109L, 107L, 204L, 103L, 414L],
[1557718039323L, 109L, 203L, 103L, 415L],
[1557718039536L, 107L, 203L, 104L, 414L],
[1557718039749L, 109L, 204L, 104L, 417L],
[1557718039965L, 108L, 203L, 104L, 415L],
[1557718040177L, 107L, 203L, 104L, 414L],
[1557718040390L, 106L, 202L, 105L, 413L],
[1557718040609L, 108L, 203L, 104L, 415L],
[1557718040829L, 107L, 203L, 108L, 418L]
]
# service response time
plt.figure(1)

plt.plot([(t[0] - base_time)/1000 for t in t_all], [t[1] for t in t_all], linestyle='--', marker='o', label='Books')
plt.plot([(t[0] - base_time)/1000 for t in t_all], [t[2] for t in t_all], linestyle='-.', marker='o', label='Reviews')
plt.plot([(t[0] - base_time)/1000 for t in t_all], [t[3] for t in t_all], linestyle=':', marker='o', label='Score')
# plt.plot([(t[0] - base_time)/1000 for t in t_all], [t[4] for t in t_all], label='Chain1')

plt.plot([(t[0] - base_time)/1000 for t in t_all], [t[1] for t in t_all], linestyle='--', marker='>', label='Books in cross-regional scenarios')
plt.plot([(t[0] - base_time)/1000 for t in t_all], [t[2] for t in t_all], linestyle='-.', marker='>', label='Reviews in cross-regional scenarios')
plt.plot([(t[0] - base_time)/1000 for t in t_all], [t[3] for t in t_all], linestyle=':', marker='>', label='Score in cross-regional scenarios')

# 设置横纵坐标的名称以及对应字体格式
font1 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 14,
         }
font2 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 13,
         }
plt.xlabel("Time(s)", font1)
plt.ylabel("Response Time(ms)", font1)

plt.tick_params(labelsize=14)
plt.xticks(range(0, 21, 5))
plt.yticks(range(0, 500, 100))
plt.legend(loc='upper center', ncol=2, prop=font2)
plt.tight_layout()
plt.savefig("../fig/fig_9_qps5_chain1_sgl_mtl_responce")



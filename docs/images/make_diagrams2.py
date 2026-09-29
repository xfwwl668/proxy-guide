# -*- coding: utf-8 -*-
"""前置知识新增图解 08/09/10：PIL + Noto Sans CJK。"""
import math, glob, os
from PIL import Image, ImageDraw, ImageFont

OUT = "/home/hatch/workspace/proxy-guide/docs/images"
os.makedirs(OUT, exist_ok=True)

def find_font():
    cands = (glob.glob('/usr/share/fonts/**/NotoSansCJK*.ttc', recursive=True)
             + glob.glob('/usr/share/fonts/**/NotoSansCJK*.otf', recursive=True)
             + glob.glob('/usr/share/fonts/**/NotoSansCJK*.ttf', recursive=True))
    if not cands:
        raise RuntimeError("no CJK font found")
    return sorted(cands)[0]

FONT_PATH = find_font()
FONTS = {}
def font(size):
    if size not in FONTS:
        FONTS[size] = ImageFont.truetype(FONT_PATH, size)
    return FONTS[size]

INK = '#1E293B'; SUB = '#475569'; MUT = '#94A3B8'
BLUE = '#2563EB'; GREEN = '#16A34A'; RED = '#DC2626'; ORANGE = '#EA580C'; PURPLE = '#7C3AED'

def new_canvas():
    img = Image.new('RGB', (1400, 900), 'white')
    return img, ImageDraw.Draw(img)

def title(d, text, sub=None):
    d.text((70, 36), text, font=font(56), fill=INK)
    if sub:
        d.text((70, 112), sub, font=font(32), fill=SUB)

def ctext(d, cx, y, text, size=40, fill=INK):
    f = font(size)
    bb = d.textbbox((0, 0), text, font=f)
    d.text((cx - (bb[2]-bb[0])/2, y), text, font=f, fill=fill)

def box(d, x, y, w, h, title_t, sub_t=None, fill='#EFF6FF', outline=BLUE, ts=44, ss=32):
    d.rounded_rectangle([x, y, x+w, y+h], radius=26, fill=fill, outline=outline, width=5)
    if sub_t:
        ctext(d, x+w/2, y+26, title_t, ts, INK)
        ctext(d, x+w/2, y+26+ts+12, sub_t, ss, SUB)
    else:
        f = font(ts); bb = d.textbbox((0,0), title_t, font=f)
        ctext(d, x+w/2, y+(h-(bb[3]-bb[1]))/2-6, title_t, ts, INK)

def arrow(d, x1, y1, x2, y2, color='#64748B', width=6, label=None, ls=30):
    d.line([x1, y1, x2, y2], fill=color, width=width)
    ang = math.atan2(y2-y1, x2-x1); s = 24
    p1 = (x2 - s*math.cos(ang-0.42), y2 - s*math.sin(ang-0.42))
    p2 = (x2 - s*math.cos(ang+0.42), y2 - s*math.sin(ang+0.42))
    d.polygon([(x2, y2), p1, p2], fill=color)
    if label:
        f = font(ls); bb = d.textbbox((0,0), label, font=f)
        tw, th = bb[2]-bb[0], bb[3]-bb[1]
        mx, my = (x1+x2)/2, (y1+y2)/2
        d.rounded_rectangle([mx-tw/2-16, my-th/2-34, mx+tw/2+16, my+th/2-6],
                            radius=16, fill='white', outline=color, width=3)
        d.text((mx-tw/2, my-th/2-36), label, font=f, fill=INK)

def note(d, y, text, size=32, fill=SUB):
    ctext(d, 700, y, text, size, fill)

def chip(d, x, y, w, h, key, meaning):
    d.rounded_rectangle([x, y, x+w, y+h], radius=20, fill='#EFF6FF', outline=BLUE, width=4)
    ctext(d, x+w/2, y+18, key, 27, BLUE)
    ctext(d, x+w/2, y+18+27+10, meaning, 29, INK)

# ---------- 图8：订阅链接拆解 ----------
img, d = new_canvas()
title(d, "图8 · 读懂一条订阅链接", "以 VLESS + Reality 为例：每一段都有用，缺一段就连不上")
box(d, 70, 200, 200, 130, "vless://", "① 协议", ts=40)
arrow(d, 285, 265, 315, 265, width=5)
box(d, 330, 200, 400, 130, "UUID 一长串", "② 身份证", ts=40)
arrow(d, 745, 265, 775, 265, width=5)
box(d, 790, 200, 110, 130, "@", "分隔", ts=44)
arrow(d, 915, 265, 945, 265, width=5)
box(d, 960, 200, 370, 130, "1.2.3.4 : 443", "③ 地址和端口", ts=40)
d.text((70, 368), "④ 参数区（? 后面跟的一串，每一项都影响能不能连上）", font=font(34), fill=INK)
params = [
    ("security=reality", "伪装层：用 Reality"),
    ("sni=www.iij.ad.jp", "伪装目标：日本网站"),
    ("fp=chrome", "指纹：装成 Chrome"),
    ("pbk=公钥一长串", "服务端公钥：认准这台"),
    ("flow=xtls-rprx-vision", "传输优化模式"),
    ("encryption=none", "本身不加密，靠外层"),
]
xs = [70, 500, 930]
for i, (k, v) in enumerate(params):
    chip(d, xs[i % 3], 430 + (i // 3) * 140, 400, 118, k, v)
box(d, 70, 716, 560, 130, "# 香港-01", "⑤ 备注名（只给你自己看）", ts=40, fill='#F0FDF4', outline=GREEN)
note(d, 856, "整条链接 = 连接这个节点的全部信息 → 谁拿到它，谁就能用你的节点", 30)
img.save(f"{OUT}/08-订阅链接拆解.png")

# ---------- 图9：Reality 伪装 ----------
img, d = new_canvas()
title(d, "图9 · Reality 伪装是怎么骗过检查的", "检查者看到的 vs 实际发生的")
d.rounded_rectangle([40, 180, 660, 650], radius=30, fill='#FEF2F2', outline=RED, width=4)
ctext(d, 350, 208, "检查者看到的", 40, RED)
box(d, 80, 300, 180, 140, "你", "手机/电脑", fill='white', outline=RED, ts=36)
box(d, 420, 300, 200, 140, "日本网站", "真实存在", fill='white', outline=RED, ts=36)
arrow(d, 275, 370, 405, 370, color=RED, width=6)
ctext(d, 350, 398, "TLS 握手", 28, SUB)
ctext(d, 350, 434, "SNI=www.iij.ad.jp", 28, SUB)
ctext(d, 350, 490, "检查者：就是个正常访客", 32, SUB)
ctext(d, 350, 545, "✓ 放行", 38, GREEN)
d.rounded_rectangle([740, 180, 1360, 650], radius=30, fill='#F0FDF4', outline=GREEN, width=4)
ctext(d, 1050, 208, "实际发生的", 40, GREEN)
box(d, 780, 300, 180, 140, "你", "手机/电脑", fill='white', outline=GREEN, ts=36)
box(d, 1120, 300, 200, 140, "你的节点", "境外服务器", fill='white', outline=GREEN, ts=36)
arrow(d, 975, 370, 1105, 370, color=GREEN, width=6)
ctext(d, 1050, 398, "同一条连接", 28, SUB)
ctext(d, 1050, 490, "节点验明正身：是自己人", 32, SUB)
ctext(d, 1050, 545, "→ 解出代理流量，替你访问", 32, SUB)
note(d, 710, "Reality = 借真实网站的身份做掩护", 34)
note(d, 762, "SNI、指纹必须和真网站一致，错一个就露馅", 30)
img.save(f"{OUT}/09-Reality伪装.png")

# ---------- 图10：延迟 / 丢包 / 带宽 ----------
img, d = new_canvas()
title(d, "图10 · 延迟、丢包、带宽是三回事", "测速看这三个数，别只看一个")
panels = [(40, "延迟", BLUE, '#EFF6FF'), (480, "丢包", ORANGE, '#FFF7ED'), (920, "带宽", GREEN, '#F0FDF4')]
for x0, name, color, fill in panels:
    d.rounded_rectangle([x0, 200, x0+400, 650], radius=30, fill=fill, outline=color, width=4)
    ctext(d, x0+200, 226, name, 44, color)
# 延迟
box(d, 110, 300, 260, 145, "80 毫秒", "数据打个来回", fill='white', outline=BLUE, ts=36)
ctext(d, 240, 480, "< 150ms 刷网页够用", 30, SUB)
ctext(d, 240, 530, "> 300ms 明显卡", 30, SUB)
# 丢包：10 个方块，9 绿 1 红
ctext(d, 680, 300, "10 个包裹，丢 1 个", 30, SUB)
for i in range(10):
    sx = 520 + (i % 5) * 74
    sy = 350 + (i // 5) * 74
    if i == 7:
        d.rounded_rectangle([sx, sy, sx+60, sy+60], radius=12, fill='#FECACA', outline=RED, width=4)
        d.line([sx+14, sy+14, sx+46, sy+46], fill=RED, width=7)
        d.line([sx+14, sy+46, sx+46, sy+14], fill=RED, width=7)
    else:
        d.rounded_rectangle([sx, sy, sx+60, sy+60], radius=12, fill='#BBF7D0', outline=GREEN, width=4)
ctext(d, 680, 510, "丢包要重发 → 卡顿转圈", 30, SUB)
ctext(d, 680, 560, "延迟再低也救不了", 30, SUB)
# 带宽：窄路 vs 宽路
ctext(d, 1120, 300, "路有多宽", 30, SUB)
d.rectangle([1070, 350, 1170, 390], fill=GREEN)
ctext(d, 1120, 400, "窄路 10Mbps：慢", 28, SUB)
d.rectangle([990, 460, 1250, 510], fill=GREEN)
ctext(d, 1120, 520, "宽路 200Mbps：快", 28, SUB)
ctext(d, 1120, 575, "看视频吃带宽，聊天不吃", 28, SUB)
note(d, 710, "三者都好 = 体验好；弱网（高铁/电梯）先看丢包", 32)
note(d, 762, "HY2 / TUIC 走 UDP，在弱网下有时体验更好，就这个原因", 30)
img.save(f"{OUT}/10-延迟丢包带宽.png")

# ---------- 图11：假人保活原理 ----------
img, d = new_canvas()
title(d, "图11 · 假人保活原理", "让面板觉得：这服有人在用")
d.rounded_rectangle([40, 180, 660, 660], radius=30, fill='#FEF2F2', outline=RED, width=4)
ctext(d, 350, 210, "没有假人", 42, RED)
box(d, 200, 300, 300, 130, "服务器", "MC 游戏服", fill='white', outline=RED, ts=40)
ctext(d, 350, 470, "在线人数：0", 34, SUB)
ctext(d, 350, 530, "面板判定：僵尸服", 32, RED)
ctext(d, 350, 580, "→ 回收 / 关机", 32, RED)
d.rounded_rectangle([740, 180, 1360, 660], radius=30, fill='#F0FDF4', outline=GREEN, width=4)
ctext(d, 1050, 210, "挂了 2 个假人", 42, GREEN)
box(d, 900, 300, 300, 130, "服务器", "MC 游戏服", fill='white', outline=GREEN, ts=40)
for i, name in enumerate(["Bot_挂机1", "Bot_挂机2"]):
    x = 880 + i * 190
    d.rounded_rectangle([x, 460, x+170, 530], radius=18, fill='#DCFCE7', outline=GREEN, width=3)
    ctext(d, x+85, 478, name, 26, INK)
ctext(d, 1050, 555, "在线人数：2", 34, SUB)
ctext(d, 1050, 605, "面板判定：有人在用 → 保留", 32, GREEN)
note(d, 720, "假人不需要正版账号（插件直接在服务端构造）", 32)
note(d, 772, "1~2 个够用，太多吃内存；服务器重启后假人清零，要重挂", 30)
img.save(f"{OUT}/11-假人保活原理.png")

print("done")

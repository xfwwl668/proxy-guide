# -*- coding: utf-8 -*-
"""画 proxy-guide 前置知识图解：PIL + Noto Sans CJK，保证中文不乱码。"""
import math, glob, os
from PIL import Image, ImageDraw, ImageFont

OUT = "/home/hatch/workspace/proxy-guide/docs/images"
os.makedirs(OUT, exist_ok=True)

def find_font():
    cands = (glob.glob('/usr/share/fonts/**/NotoSansCJK*SC*.ttc', recursive=True)
             + glob.glob('/usr/share/fonts/**/NotoSansCJK*SC*.otf', recursive=True)
             + glob.glob('/usr/share/fonts/**/NotoSansCJK*SC*.ttf', recursive=True)
             + glob.glob('/usr/share/fonts/**/NotoSansCJK-Regular.ttc', recursive=True))
    if not cands:
        raise RuntimeError("no CJK font found")
    return sorted(cands)[0]

FONT_PATH = find_font()
print("font:", FONT_PATH)
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
        ctext(d, x+w/2, y+30, title_t, ts, INK)
        ctext(d, x+w/2, y+30+ts+14, sub_t, ss, SUB)
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

def red_x(d, cx, cy, r=26, width=10):
    d.line([cx-r, cy-r, cx+r, cy+r], fill=RED, width=width)
    d.line([cx-r, cy+r, cx+r, cy-r], fill=RED, width=width)

def green_check(d, cx, cy, s=30, width=10):
    d.line([cx-s, cy, cx-s*0.25, cy+s*0.7], fill=GREEN, width=width)
    d.line([cx-s*0.25, cy+s*0.7, cx+s, cy-s*0.8], fill=GREEN, width=width)

# ---------- 图1：代理是什么 ----------
img, d = new_canvas()
title(d, "图1 · 代理是什么", "左边：直接访问 → 被拦下；右边：请一台境外服务器帮你访问")
# 上半：直接访问
d.text((70, 190), "直接访问", font=font(40), fill=RED)
box(d, 120, 260, 280, 150, "你", "北京 · 手机/电脑", fill='#FEF2F2', outline=RED)
arrow(d, 430, 335, 640, 335, color=RED, width=8, label="想看国外网站")
red_x(d, 745, 335, 30, 12)
d.text((700, 380), "被拦下", font=font(34), fill=RED)
box(d, 850, 260, 400, 150, "国外网站", "打不开 ×", fill='#FEF2F2', outline=RED)
# 下半：走代理
d.text((70, 500), "走代理", font=font(40), fill=GREEN)
box(d, 120, 570, 240, 150, "你", "北京", fill='#F0FDF4', outline=GREEN, ts=40)
arrow(d, 385, 645, 520, 645, color=GREEN, width=8, label="加密隧道")
box(d, 545, 570, 340, 150, "代理节点", "境外服务器", fill='#F0FDF4', outline=GREEN, ts=40)
arrow(d, 910, 645, 1015, 645, color=GREEN, width=8, label="替你访问")
box(d, 1040, 570, 240, 150, "国外网站", "能打开 ✓", fill='#F0FDF4', outline=GREEN, ts=40)
note(d, 800, "一句话：代理 = 请一台境外的服务器，帮你去上网")
img.save(f"{OUT}/01-代理是什么.png")

# ---------- 图2：数据怎么走 ----------
img, d = new_canvas()
title(d, "图2 · 一次上网，数据怎么走", "5 步走完一个来回")
steps = [
    ("① 你点开网站", "手机/电脑", '#EFF6FF', BLUE),
    ("② 客户端加密", "V2RayN 打包", '#F0FDF4', GREEN),
    ("③ 节点转发", "解密再转发", '#FFF7ED', ORANGE),
    ("④ 拿到内容", "目标网站", '#FAF5FF', PURPLE),
    ("⑤ 加密返回", "你看到网页", '#EFF6FF', BLUE),
]
x = 40
for t, s, fill, ol in steps:
    box(d, x, 300, 236, 220, t, s, fill=fill, outline=ol, ts=32, ss=28)
    x += 236
    if x < 1400:
        arrow(d, x-14, 410, x+14, 410, color='#64748B', width=6)
note(d, 620, "中间人只能看到一堆加密乱码，看不到你到底在看什么", 32)
note(d, 680, "这就是为什么全程要加密：防偷看", 32)
img.save(f"{OUT}/02-数据怎么走.png")

# ---------- 图3：订阅是什么 ----------
img, d = new_canvas()
title(d, "图3 · 订阅链接是什么", "1 条链接 = 打包所有节点，自动同步更新")
for i, (name, cc) in enumerate([("节点 A · 香港", BLUE), ("节点 B · 日本", GREEN), ("节点 C · 美国", ORANGE)]):
    y = 230 + i*170
    box(d, 90, y, 300, 130, name, "一个代理服务器", fill='#F8FAFC', outline=cc, ts=38)
    arrow(d, 410, y+65, 520, y+65, color='#64748B', width=5)
d.text((560, 400), "打包", font=font(36), fill=INK)
box(d, 640, 330, 300, 200, "订阅链接", "http://…/sub", fill='#EFF6FF', outline=BLUE, ts=40)
arrow(d, 960, 430, 1060, 430, color=BLUE, width=8, label="客户端导入")
box(d, 1080, 330, 250, 200, "V2RayN", "节点列表自动出现", fill='#F0FDF4', outline=GREEN, ts=40, ss=30)
note(d, 745, "服务端加了新节点 → 客户端点一下「更新订阅」就同步了，不用手动一个个加", 32)
note(d, 805, "⚠️ 订阅链接含你的 UUID/Token，别发给别人", 32, fill=ORANGE)
img.save(f"{OUT}/03-订阅是什么.png")

# ---------- 图4：CDN 与优选 ----------
img, d = new_canvas()
title(d, "图4 · CDN 与优选", "连锁店逻辑：就近拿货最快")
d.text((70, 190), "不用 CDN：跨地域直连，又慢又不稳", font=font(36), fill=RED)
box(d, 120, 260, 240, 140, "你", "北京", fill='#FEF2F2', outline=RED, ts=40)
arrow(d, 390, 330, 950, 330, color=RED, width=8, label="延迟高 · 可能绕远")
box(d, 980, 260, 300, 140, "源站", "广州服务器", fill='#FEF2F2', outline=RED, ts=40)
d.text((70, 470), "用 CDN + 优选：连最近的边缘节点", font=font(36), fill=GREEN)
box(d, 120, 540, 240, 140, "你", "北京", fill='#F0FDF4', outline=GREEN, ts=40)
arrow(d, 390, 610, 560, 610, color=GREEN, width=8, label="延迟低")
box(d, 590, 540, 300, 140, "边缘节点", "北京 · 离你最近", fill='#F0FDF4', outline=GREEN, ts=40)
arrow(d, 920, 610, 1030, 610, color='#64748B', width=6, label="回源")
box(d, 1060, 540, 240, 140, "源站", "广州", fill='#F8FAFC', outline='#64748B', ts=40)
note(d, 740, "优选 = 从一堆边缘节点里，挑离你最近、最快的那一个", 32)
note(d, 800, "可能降低延迟、有时绕开 DNS 污染，但不是万能药", 32)
img.save(f"{OUT}/04-CDN与优选.png")

# ---------- 图5：反代 ----------
img, d = new_canvas()
title(d, "图5 · 反代（中介）", "你只认识中介，不认识真正的卖家")
box(d, 80, 350, 220, 150, "你", "客户端", fill='#EFF6FF', outline=BLUE, ts=40)
arrow(d, 325, 425, 455, 425, color=BLUE, width=8, label="只连中介")
box(d, 480, 330, 340, 190, "反代域名（中介）", "如 abc.workers.dev", fill='#FFF7ED', outline=ORANGE, ts=38, ss=30)
arrow(d, 845, 425, 945, 425, color='#64748B', width=6, label="转交")
box(d, 970, 350, 220, 150, "真实节点", "IP 被藏起来", fill='#F8FAFC', outline='#64748B', ts=40, ss=30)
arrow(d, 1195, 425, 1235, 425, color='#64748B', width=6)
d.text((1245, 402), "目标网站", font=font(30), fill=SUB)
note(d, 620, "好处 1：真实 IP 不暴露，不容易被直接封", 32)
note(d, 680, "好处 2：中介被封就换一个中介，节点本身不用重建", 32)
note(d, 740, "常用中介：Cloudflare Workers（免费版每天 10 万次请求）", 32)
img.save(f"{OUT}/05-反代.png")

# ---------- 图6：Argo 隧道 ----------
img, d = new_canvas()
title(d, "图6 · Argo 隧道", "服务器主动向外打洞，不用开放端口")
box(d, 60, 330, 400, 200, "你的服务器", "无公网端口也行", fill='#FFF7ED', outline=ORANGE, ts=38, ss=30)
arrow(d, 485, 430, 745, 430, color=ORANGE, width=8, label="主动向外建隧道")
box(d, 770, 330, 300, 200, "Cloudflare", "全球边缘网络", fill='#EFF6FF', outline=BLUE, ts=40, ss=30)
arrow(d, 1095, 430, 1185, 430, color=BLUE, width=8, label="你连这里")
box(d, 1210, 350, 130, 150, "你", "", fill='#F0FDF4', outline=GREEN, ts=40)
note(d, 620, "关键：是服务器主动连出去，所以防火墙/内网也不怕，不用开端口", 32)
note(d, 680, "临时隧道：每次重启换域名，适合测试；固定隧道：域名固定，适合长期用", 32)
img.save(f"{OUT}/06-Argo隧道.png")

# ---------- 图7：伪装分层（改成竖条，更清楚） ----------
img, d = new_canvas()
title(d, "图7 · 伪装是怎么做的", "像套娃一样层层包裹，检查者只能看到最外层")
strips = [
    ("最外层 · 看起来像普通 HTTPS 流量", '#F0FDF4', GREEN),
    ("TLS 加密层 · 加密外壳", '#EFF6FF', BLUE),
    ("传输层 WebSocket · 伪装成网页通信", '#FFF7ED', ORANGE),
    ("协议层 VLESS / VMESS · 代理协议", '#FAF5FF', PURPLE),
    ("最内层 · 你的真实数据", '#DC2626', RED),
]
y = 220
for t, fill, ol in strips:
    tc = 'white' if ol == RED else INK
    d.rounded_rectangle([260, y, 1140, y+92], radius=20, fill=fill, outline=ol, width=4)
    ctext(d, 700, y+24, t, 36, tc)
    y += 112
# 左侧大箭头：层层包裹
d.line([150, 240, 150, 240+4*112+72], fill='#64748B', width=6)
for yy in (240, 240+4*112+72):
    pass
ang = math.pi/2; s = 24; x2, y2 = 150, 240+4*112+72
p1 = (x2 - s*math.cos(ang-0.42), y2 - s*math.sin(ang-0.42))
p2 = (x2 - s*math.cos(ang+0.42), y2 - s*math.sin(ang+0.42))
d.polygon([(x2, y2), p1, p2], fill='#64748B')
d.text((36, 430), "层层包裹", font=font(32), fill=SUB)
# 右侧标注
d.text((1160, 236), "← 检查者", font=font(32), fill=GREEN)
d.text((1160, 280), "只能看到这层", font=font(32), fill=GREEN)
note(d, 800, "Reality 更进一步：连 TLS 握手都伪装成在访问某个正常网站", 32)
note(d, 856, "但记住：伪装是“相对隐蔽”，不是“绝对安全”", 32, fill=ORANGE)
img.save(f"{OUT}/07-伪装分层.png")

print("done:", sorted(os.listdir(OUT)))

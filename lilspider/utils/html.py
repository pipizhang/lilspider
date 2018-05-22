# -*- coding: utf-8 -*-
from typing import TypeVar
from lxml.html.clean import Cleaner

__all__ = ['cleaner']

T = TypeVar('T', bound='HtmlCleaner')
class HtmlCleaner(object):

    def __init__(self) -> None:
        self.__style = True
        self.__links = True
        self.__page_structure = False
        self.__safe_attrs_only = True
        self.__allow_tags = None
        self.__kill_tags = None
        self.__remove_tags = None
        self.__safe_attrs = ['href', 'src']
        self.__input = ""

    def input(self: T, content: str) -> T:
        self.__input = content
        return self

    def output(self) -> str:
        return self.__input

    def style(self: T, enable: bool) -> T:
        self.__style = enable
        return self

    def links(self: T, enable: bool) -> T:
        self.__links = enable
        return self

    def page_structure(self: T, enable: bool) -> T:
        self.__page_structure = enable
        return self

    def allow_tags(self: T, *args: str) -> T:
        self.__allow_tags = args
        return self

    def kill_tags(self: T, *args: str) -> T:
        self.__kill_tags = args
        return self

    def remove_tags(self: T, *args: str) -> T:
        self.__remove_tags = args
        return self

    def safe_attrs(self: T, *args: str) -> T:
        self.__safe_attrs = args
        return self

    def safe_attrs_only(self: T, enable: bool) -> T:
        self.__safe_attrs_only = enable
        return self

    def clean_html(self: T) -> T:
        cleaner = Cleaner()
        cleaner.style = self.__style
        cleaner.links = self.__links
        cleaner.page_structure = self.__page_structure
        cleaner.safe_attrs_only = self.__safe_attrs_only

        if self.__allow_tags is not None: cleaner.allow_tags = self.__allow_tags
        if self.__kill_tags is not None: cleaner.kill_tags = self.__kill_tags
        if self.__remove_tags is not None: cleaner.remove_tags = self.__remove_tags
        if self.__safe_attrs is not None: cleaner.safe_attrs = self.__safe_attrs

        self.__input = cleaner.clean_html(self.__input)
        return self

def cleaner() -> HtmlCleaner:
    return HtmlCleaner()

test = """
                <p class="MsoNormal" style="margin-right: 0.0000pt; margin-left: 0.0000pt; mso-para-margin-right: 0.0000gd; mso-para-margin-left: 0.0000gd; text-indent: 21.0000pt; mso-char-indent-count: 2.0000; text-autospace: ideograph-numeric; mso-pagination: none; text-align: justify; text-justify: inter-ideograph;" align="justify"><span style="mso-spacerun: 'yes'; font-family: 宋体; mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: 'Times New Roman'; font-size: 10.5000pt; mso-font-kerning: 1.0000pt;">在我们的生活中</span><span style="mso-spacerun: 'yes'; font-family: 宋体; mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: 'Times New Roman'; font-size: 10.5000pt; mso-font-kerning: 1.0000pt;">，几乎每个人都有过胃痛的经历。你若饮食规律，它轻轻地来轻轻地走；你若三餐不定时，它可以把你折腾得翻江倒海。胃病极为常见，一生中几乎每个人都会患一次以上。</span></p>
<p class="MsoNormal" style="margin-right: 0.0000pt; margin-left: 0.0000pt; mso-para-margin-right: 0.0000gd; mso-para-margin-left: 0.0000gd; text-indent: 21.0000pt; mso-char-indent-count: 2.0000; text-autospace: ideograph-numeric; mso-pagination: none; text-align: justify; text-justify: inter-ideograph;" align="justify"><span style="mso-spacerun: 'yes'; font-family: 宋体; mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: 'Times New Roman'; font-size: 10.5000pt; mso-font-kerning: 1.0000pt;">胃病都有哪些表现？</span></p>
<p class="MsoNormal" style="margin-right: 0.0000pt; margin-left: 0.0000pt; mso-para-margin-right: 0.0000gd; mso-para-margin-left: 0.0000gd; text-indent: 21.0000pt; mso-char-indent-count: 2.0000; text-autospace: ideograph-numeric; mso-pagination: none; text-align: justify; text-justify: inter-ideograph;" align="justify"><span style="mso-spacerun: 'yes'; font-family: 宋体; mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: 'Times New Roman'; font-size: 10.5000pt; mso-font-kerning: 1.0000pt;">胃病，可以是胃部和剑突下疼痛、返酸水，也可以是恶心呕吐、消化不良等症状，这些都是胃病的临床表现。西医认为，感染幽门螺杆菌和长期不适当的药物治疗等因素，会对胃粘膜造成破坏，长期如此就会引发胃病。其次，精神因素和进食刺激性食物也会诱发或者加重胃病的发作。此外，胆汁反流和一些免疫疾病也会引起胃病，但在临床上较为少见。</span></p>
<p class="MsoNormal" style="margin-right: 0pt; margin-left: 0pt; text-indent: 21pt; text-align: center;" align="justify"><span style="mso-spacerun: 'yes'; font-family: 宋体; mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: 'Times New Roman'; font-size: 10.5000pt; mso-font-kerning: 1.0000pt;"><img src="http://blogimg.39.net/photo/2016/11/18/7ac4316e67c0435c8ffd348e86f7d101.jpg" border="0"></span></p>
<p class="MsoNormal" style="margin-right: 0.0000pt; margin-left: 0.0000pt; mso-para-margin-right: 0.0000gd; mso-para-margin-left: 0.0000gd; text-indent: 21.0000pt; mso-char-indent-count: 2.0000; text-autospace: ideograph-numeric; mso-pagination: none; text-align: justify; text-justify: inter-ideograph;" align="justify"><span style="mso-spacerun: 'yes'; font-family: 宋体; mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: 'Times New Roman'; font-size: 10.5000pt; mso-font-kerning: 1.0000pt;">不管情况轻重，若你发现自己或者家人出现这些症状后，应当及时就诊，进行检查和规范性治疗，部分较为严重的胃病还需要定期复查，如：萎缩性胃炎。</span></p>
<p class="MsoNormal" style="margin-right: 0.0000pt; margin-left: 0.0000pt; mso-para-margin-right: 0.0000gd; mso-para-margin-left: 0.0000gd; text-indent: 21.0000pt; mso-char-indent-count: 2.0000; text-autospace: ideograph-numeric; mso-pagination: none; text-align: justify; text-justify: inter-ideograph;" align="justify"><span style="mso-spacerun: 'yes'; font-family: 宋体; mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: 'Times New Roman'; font-size: 10.5000pt; mso-font-kerning: 1.0000pt;">胃病以胃炎和消化性溃疡最为常见</span></p>
<p class="MsoNormal" style="margin-right: 0.0000pt; margin-left: 0.0000pt; mso-para-margin-right: 0.0000gd; mso-para-margin-left: 0.0000gd; text-indent: 21.0000pt; mso-char-indent-count: 2.0000; text-autospace: ideograph-numeric; mso-pagination: none; text-align: justify; text-justify: inter-ideograph;" align="justify"><span style="mso-spacerun: 'yes'; font-family: 宋体; mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: 'Times New Roman'; font-size: 10.5000pt; mso-font-kerning: 1.0000pt;">胃病，以胃炎最为常见，主要分为浅表性胃炎和萎缩性胃炎。浅表性胃炎在人群中极为常见，浅表性胃炎多由饮食不当引起，治疗也较为容易，有的甚至不需要药物治疗仅通过改善不良生活习惯就能得以缓解。萎缩性胃炎稍严重，由于此病有部分癌变的可能，所以患者除常规治疗之外，还需要定期检查。</span></p>
<p class="MsoNormal" style="margin-right: 0.0000pt; margin-left: 0.0000pt; mso-para-margin-right: 0.0000gd; mso-para-margin-left: 0.0000gd; text-indent: 21.0000pt; mso-char-indent-count: 2.0000; text-autospace: ideograph-numeric; mso-pagination: none; text-align: justify; text-justify: inter-ideograph;" align="justify"><span style="mso-spacerun: 'yes'; font-family: 宋体; mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: 'Times New Roman'; font-size: 10.5000pt; mso-font-kerning: 1.0000pt;">中医认为胃病常有如下因素引起：</span></p>
<p class="MsoNormal" style="margin-right: 0.0000pt; margin-left: 0.0000pt; mso-para-margin-right: 0.0000gd; mso-para-margin-left: 0.0000gd; text-indent: 21.0000pt; mso-char-indent-count: 2.0000; text-autospace: ideograph-numeric; mso-pagination: none; text-align: justify; text-justify: inter-ideograph;" align="justify"><span style="mso-spacerun: 'yes'; font-family: 宋体; mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: 'Times New Roman'; font-size: 10.5000pt; mso-font-kerning: 1.0000pt;">1<span style="font-family: 宋体;">、 饮食不节</span></span></p>
<p class="MsoNormal" style="margin-right: 0.0000pt; margin-left: 0.0000pt; mso-para-margin-right: 0.0000gd; mso-para-margin-left: 0.0000gd; text-indent: 21.0000pt; mso-char-indent-count: 2.0000; text-autospace: ideograph-numeric; mso-pagination: none; text-align: justify; text-justify: inter-ideograph;" align="justify"><span style="mso-spacerun: 'yes'; font-family: 宋体; mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: 'Times New Roman'; font-size: 10.5000pt; mso-font-kerning: 1.0000pt;">饮食不规律、暴饮暴食、晚饭过饱、烟酒等因素都会造成胃的伤害；</span></p>
<p class="MsoNormal" style="margin-right: 0.0000pt; margin-left: 0.0000pt; mso-para-margin-right: 0.0000gd; mso-para-margin-left: 0.0000gd; text-indent: 21.0000pt; mso-char-indent-count: 2.0000; text-autospace: ideograph-numeric; mso-pagination: none; text-align: justify; text-justify: inter-ideograph;" align="justify"><span style="mso-spacerun: 'yes'; font-family: 宋体; mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: 'Times New Roman'; font-size: 10.5000pt; mso-font-kerning: 1.0000pt;">2<span style="font-family: 宋体;">、 内伤七情</span></span></p>
<p class="MsoNormal" style="margin-right: 0.0000pt; margin-left: 0.0000pt; mso-para-margin-right: 0.0000gd; mso-para-margin-left: 0.0000gd; text-indent: 21.0000pt; mso-char-indent-count: 2.0000; text-autospace: ideograph-numeric; mso-pagination: none; text-align: justify; text-justify: inter-ideograph;" align="justify"><span style="mso-spacerun: 'yes'; font-family: 宋体; mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: 'Times New Roman'; font-size: 10.5000pt; mso-font-kerning: 1.0000pt;">尤其是发怒，大怒伤肝，肝气犯胃，肝气不和就会影响胃的功能；</span></p>
<p class="MsoNormal" style="margin-right: 0.0000pt; margin-left: 0.0000pt; mso-para-margin-right: 0.0000gd; mso-para-margin-left: 0.0000gd; text-indent: 21.0000pt; mso-char-indent-count: 2.0000; text-autospace: ideograph-numeric; mso-pagination: none; text-align: justify; text-justify: inter-ideograph;" align="justify"><span style="mso-spacerun: 'yes'; font-family: 宋体; mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: 'Times New Roman'; font-size: 10.5000pt; mso-font-kerning: 1.0000pt;">3<span style="font-family: 宋体;">、 先天禀赋不足</span></span></p>
<p class="MsoNormal" style="margin-right: 0.0000pt; margin-left: 0.0000pt; mso-para-margin-right: 0.0000gd; mso-para-margin-left: 0.0000gd; text-indent: 21.0000pt; mso-char-indent-count: 2.0000; text-autospace: ideograph-numeric; mso-pagination: none; text-align: justify; text-justify: inter-ideograph;" align="justify"><span style="mso-spacerun: 'yes'; font-family: 宋体; mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: 'Times New Roman'; font-size: 10.5000pt; mso-font-kerning: 1.0000pt;">这种主要见于遗传性疾病或者先天身体虚弱的患者。</span></p>
<p class="MsoNormal" style="margin-right: 0.0000pt; margin-left: 0.0000pt; mso-para-margin-right: 0.0000gd; mso-para-margin-left: 0.0000gd; text-indent: 21.0000pt; mso-char-indent-count: 2.0000; text-autospace: ideograph-numeric; mso-pagination: none; text-align: justify; text-justify: inter-ideograph;" align="justify"><span style="mso-spacerun: 'yes'; font-family: 宋体; mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: 'Times New Roman'; font-size: 10.5000pt; mso-font-kerning: 1.0000pt;"><span style="font-family: 宋体;">胃病可防</span> 4<span style="font-family: 宋体;">大习惯要养好</span></span><span style="mso-spacerun: 'yes'; font-family: 宋体; mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: 'Times New Roman'; font-size: 10.5000pt; mso-font-kerning: 1.0000pt;">，</span><span style="mso-spacerun: 'yes'; font-family: 宋体; mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: 'Times New Roman'; font-size: 10.5000pt; mso-font-kerning: 1.0000pt;">胃病作为常见病，可治可防，应该根据诱发和加重的原因有针对性地干预：</span></p>
<p class="MsoNormal" style="margin-right: 0.0000pt; margin-left: 0.0000pt; mso-para-margin-right: 0.0000gd; mso-para-margin-left: 0.0000gd; text-indent: 21.0000pt; mso-char-indent-count: 2.0000; text-autospace: ideograph-numeric; mso-pagination: none; text-align: justify; text-justify: inter-ideograph;" align="justify"><span style="mso-spacerun: 'yes'; font-family: 宋体; mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: 'Times New Roman'; font-size: 10.5000pt; mso-font-kerning: 1.0000pt;">1<span style="font-family: 宋体;">、饮食</span></span></p>
<p class="MsoNormal" style="margin-right: 0.0000pt; margin-left: 0.0000pt; mso-para-margin-right: 0.0000gd; mso-para-margin-left: 0.0000gd; text-indent: 21.0000pt; mso-char-indent-count: 2.0000; text-autospace: ideograph-numeric; mso-pagination: none; text-align: justify; text-justify: inter-ideograph;" align="justify"><span style="mso-spacerun: 'yes'; font-family: 宋体; mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: 'Times New Roman'; font-size: 10.5000pt; mso-font-kerning: 1.0000pt;"><span style="font-family: 宋体;">进食时应细嚼慢咽以利于唾液和食物充分反应；饭吃八分饱；每日三餐能量的比例应该遵循</span>4:4:2<span style="font-family: 宋体;">，大多数人应该养成这种习惯。最 后不暴饮暴食，暴饮暴食容易诱发急性胰腺炎或胃扩张。</span></span></p>
<p class="MsoNormal" style="margin-right: 0.0000pt; margin-left: 0.0000pt; mso-para-margin-right: 0.0000gd; mso-para-margin-left: 0.0000gd; text-indent: 21.0000pt; mso-char-indent-count: 2.0000; text-autospace: ideograph-numeric; mso-pagination: none; text-align: justify; text-justify: inter-ideograph;" align="justify"><span style="mso-spacerun: 'yes'; font-family: 宋体; mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: 'Times New Roman'; font-size: 10.5000pt; mso-font-kerning: 1.0000pt;">2<span style="font-family: 宋体;">、 保持良好的情绪</span></span></p>
<p class="MsoNormal" style="margin-right: 0.0000pt; margin-left: 0.0000pt; mso-para-margin-right: 0.0000gd; mso-para-margin-left: 0.0000gd; text-indent: 21.0000pt; mso-char-indent-count: 2.0000; text-autospace: ideograph-numeric; mso-pagination: none; text-align: justify; text-justify: inter-ideograph;" align="justify"><span style="mso-spacerun: 'yes'; font-family: 宋体; mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: 'Times New Roman'; font-size: 10.5000pt; mso-font-kerning: 1.0000pt;">少发怒，是养生保健常规要求，除了胃病，对心脑血管病也多有益处。</span></p>
<p class="MsoNormal" style="margin-right: 0.0000pt; margin-left: 0.0000pt; mso-para-margin-right: 0.0000gd; mso-para-margin-left: 0.0000gd; text-indent: 21.0000pt; mso-char-indent-count: 2.0000; text-autospace: ideograph-numeric; mso-pagination: none; text-align: justify; text-justify: inter-ideograph;" align="justify"><span style="mso-spacerun: 'yes'; font-family: 宋体; mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: 'Times New Roman'; font-size: 10.5000pt; mso-font-kerning: 1.0000pt;">3<span style="font-family: 宋体;">、 戒烟限酒</span></span></p>
<p class="MsoNormal" style="margin-right: 0.0000pt; margin-left: 0.0000pt; mso-para-margin-right: 0.0000gd; mso-para-margin-left: 0.0000gd; text-indent: 21.0000pt; mso-char-indent-count: 2.0000; text-autospace: ideograph-numeric; mso-pagination: none; text-align: justify; text-justify: inter-ideograph;" align="justify"><span style="mso-spacerun: 'yes'; font-family: 宋体; mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: 'Times New Roman'; font-size: 10.5000pt; mso-font-kerning: 1.0000pt;">烟草除了刺激肺部，对全身各器官皆有不良影响；少量饮酒有利于身体健康，但是不应该大量饮酒，这样对身体健康不益。</span></p>
<p class="MsoNormal" style="margin-right: 0.0000pt; margin-left: 0.0000pt; mso-para-margin-right: 0.0000gd; mso-para-margin-left: 0.0000gd; text-indent: 21.0000pt; mso-char-indent-count: 2.0000; text-autospace: ideograph-numeric; mso-pagination: none; text-align: justify; text-justify: inter-ideograph;" align="justify"><span style="mso-spacerun: 'yes'; font-family: 宋体; mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: 'Times New Roman'; font-size: 10.5000pt; mso-font-kerning: 1.0000pt;">4<span style="font-family: 宋体;">、 注意日常饮食禁忌</span></span></p>
<p class="MsoNormal" style="margin-right: 0.0000pt; margin-left: 0.0000pt; mso-para-margin-right: 0.0000gd; mso-para-margin-left: 0.0000gd; text-indent: 21.0000pt; mso-char-indent-count: 2.0000; text-autospace: ideograph-numeric; mso-pagination: none; text-align: justify; text-justify: inter-ideograph;" align="justify"><span style="mso-spacerun: 'yes'; font-family: 宋体; mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: 'Times New Roman'; font-size: 10.5000pt; mso-font-kerning: 1.0000pt;">也就是禁忌生冷寒凉、辛辣刺激、肥甘厚腻，这些类别食物都会对胃造成这样或那样的伤害，在生活中应当加以节制。</span></p>
<p class="MsoNormal" style="margin-right: 0.0000pt; margin-left: 0.0000pt; mso-para-margin-right: 0.0000gd; mso-para-margin-left: 0.0000gd; text-indent: 21.0000pt; mso-char-indent-count: 2.0000; text-autospace: ideograph-numeric; mso-pagination: none; text-align: justify; text-justify: inter-ideograph;" align="justify"><span style="mso-spacerun: 'yes'; font-family: 宋体; mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: 'Times New Roman'; font-size: 10.5000pt; mso-font-kerning: 1.0000pt;">&nbsp;</span></p>
<p class="MsoNormal" style="margin-right: 0.0000pt; margin-left: 0.0000pt; mso-para-margin-right: 0.0000gd; mso-para-margin-left: 0.0000gd; text-indent: 21.0000pt; mso-char-indent-count: 2.0000; text-autospace: ideograph-numeric; mso-pagination: none; text-align: justify; text-justify: inter-ideograph;" align="justify"><span style="mso-spacerun: 'yes'; font-family: 宋体; mso-ascii-font-family: Calibri; mso-hansi-font-family: Calibri; mso-bidi-font-family: 'Times New Roman'; font-size: 10.5000pt; mso-font-kerning: 1.0000pt;">&nbsp;</span></p>
<style>sfadf</style>
<div href="xxh"> adfasdf </div>
<h1>adfa</h1>
<iframe></iframe>
<table></table>
<li>sss</li>
"""

if __name__ == "__main__":
    c = cleaner()
    c.safe_attrs('href', 'src')
    c.remove_tags('span', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6').input(test).clean_html()
    x = c.output()
    print(x)



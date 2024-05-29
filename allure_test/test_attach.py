# -*- coding: utf-8 -*-
# @Time:2024/5/29 17:44
# @Author：huanglijing

import allure


def test_attach_text():
    allure.attach("这是一个纯文本", attachment_type=allure.attachment_type.TEXT)


def test_attach_html():
    allure.attach("<body>这是一段htmlbody块</body>", "html测试块", attachment_type=allure.attachment_type.HTML)


def test_attach_photo():
    allure.attach.file("./ziyuan/Default.jpg", name="这是一张图片", attachment_type=allure.attachment_type.JPG)


def test_attach_video():
    allure.attach.file("./ziyuan/1.Linux系统与Shell环境准备.mp4", name="这是一段MP4视频", attachment_type=allure.attachment_type.MP4)

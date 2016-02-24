#!/usr/bin/env python
#coding=utf-8

from radiuslib import btforms
from radiuslib.btforms import dataform
from radiuslib.btforms import rules
from radiuslib.btforms.rules import button_style, input_style

boolean = {0: u"否", 1: u"是"}

node_add_form = btforms.Form(
    btforms.Textbox("node_name", rules.len_of(2, 32), description=u"区域名称", required="required", **input_style),
    btforms.Textbox("node_desc", rules.len_of(2, 128), description=u"区域描述", required="required", **input_style),
    btforms.Button("submit", type="submit", html=u"<b>提交</b>", **button_style),
    title=u"增加区域",
    action="/admin/node/add"
)

node_update_form = btforms.Form(
    btforms.Hidden("id", description=u"区域ID"),
    btforms.Textbox("node_name", rules.len_of(2, 32), description=u"区域名称", **input_style),
    btforms.Textbox("node_desc", rules.len_of(2, 128), description=u"区域描述", required="required", **input_style),
    btforms.Button("submit", type="submit", html=u"<b>更新</b>", **button_style),
    title=u"修改区域",
    action="/admin/node/update"
)

# -*- coding: utf-8 -*-

test_list = [{'@name': '10分钟内同一网元出现10条BSC-TRANS [101] BER-10E-6 [7]告警',
              'condition': {'exists': {'@name': 'a', '#text': 'alias=="alarm_a"||alias=="alarm_b"||alias=="alarm_c"'},
                            'notexists': {'@name': 'b', '#text': 'alias=="DeriveAlarm"'},
                            'count_alarm': {'@name': 'alarms', '@high': 'a.key[sum]',
                                            '#text': 'alias=="alarm_a"||alias=="alarm_b"||alias=="alarm_c"'}},
              'event': {'alarm_new': {'@alarmname': '网元产生10条BSC-TRANS [101] BER-10E-6 [7]告警', '@alias': 'DeriveAlarm',
                                      '@derivate': 'yes', '@extends': 'a', 'mapset': {
                      'map': [{'@type': 'fixedMap', '@name': 'event_id'},
                              {'@type': 'fieldMap', '@name': 'province_name', '#text': 'a.province_name'},
                              {'@type': 'fieldMap', '@name': 'city_name', '#text': 'a.city_name'},
                              {'@type': 'fieldMap', '@name': 'ne_label', '#text': 'a.ne_label'},
                              {'@type': 'fieldMap', '@name': 'eqp_alias', '#text': 'a.eqp_alias'},
                              {'@type': 'fixedMap', '@name': 'title_text',
                               '#text': '[衍生告警]网元产生10条BSC-TRANS [101] BER-10E-6 [7]告警'},
                              {'@type': 'fixedMap', '@name': 'org_severity', '#text': '3'},
                              {'@type': 'fixedMap', '@name': 'standard_alarm_id', '#text': '400-011-00-101007'},
                              {'@type': 'joinMap', '@name': 'alarm_text',
                               '#text': '"省份:"+a.province_name+\n                                                "\\n地市："+a.city_name+\n                                                "\\n告警标题：[衍生告警]网元产生10条BSC-TRANS [101] BER-10E-6 [7]告警"+\n                                                "\\n告警级别：三级"+\n                                                "\\n告警产生时间："+createTime+\n                                                "\\n量值要求：10分钟"'}]},
                                      'derive_clr_rule': {'clear_rule': {'@type': '1', 'count_alarm': {'@low': '1',
                                                                                                       '#text': 'active_status==1'}}}}}},
             {'@name': 'BSC-TRANS_101_BER-10E-6_7告警压缩', 'condition': {
                 'exists': [{'@name': 'a', '#text': 'alias=="DeriveAlarm"'},
                            {'@name': 'b', '#text': 'alias=="alarm_a"'}]},
              'event': {'alarm_rel': {'main_alarm': 'a', 'child_alarm': 'b'}}}]

list = []
print(test_list[0]['condition'])
print(test_list[1]['event']['alarm_rel'])

"""for i in test_list[0]['condition']:
    list.append(i)"""
list.append(test_list[0]['condition'])
list.append(test_list[1]['condition'])
print(list)

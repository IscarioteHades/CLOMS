# 説明：メインコード。ここからシステムを動かす。
from sub_code import get_report
from sub_code import get_event
from sub_code import insert
from datetime import datetime as dt
from sub_code import some_function
import requests

report_list = get_report.get_report_info()

# GoogleCalendarAPIを使うためのOAuth認証
service = insert.authorize()

events_start = get_event.get_event()

# GoogleCalendar に予定を送る
result = []
for class_name, deadline in report_list:
    # 重複して予定を登録しないため
    if deadline not in events_start:
        insert.set_event(class_name, deadline, service)
        result.append((class_name, deadline))

if result == []:
    print('新しく追加されたレポートはありません')
else:
    print('---新しく追加されたレポート---')
    for class_name, deadline in result:
        print('%s : %s' % (class_name, deadline))
        ('%s:%s' % (class_name, deadline))

def send_line_notify(notification_message):
    """
    LINEに通知する
    """
    try:
        line_notify_token = 'oVcZrQrekz5f4g52kwZaoOVcC9IzrCgDdWIlG91llvo'
        line_notify_api = 'https://notify-api.line.me/api/notify'
        headers = {'Authorization': f'Bearer {line_notify_token}'}
        data = {'message': notification_message}
        requests.post(line_notify_api, headers=headers, data=data)

    except:
        print('失敗')

# エントリーポイントの定義(GCPで使うやつ)
def handler(request):
    return clmos_system(request)

from source.VC import VC
from source.tools.sendQQeMail import QQMail
import datetime
import time


def static_bao_ming():
    '''
    静态地报名，固定化的报名流程，或者叫“死板的”
    :return:
    '''
    vc = VC('emulator-5554')
    qqmail = QQMail()
    vc.click_by_words("我要报名")
    time.sleep(1)
    vc.click_by_words("确定报名")
    qqmail.send_mail("success")
    # while True:
    #     if time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) == "2019-10-9 21:56:20":
    #         vc.click_by_words("我要报名")
    #         vc.click_by_words("确定报名")
    #     time.sleep(600)
    #     print(time.localtime())

def print_all_act( wordsList):
    for itemDict in wordsList:
        print(itemDict)

def zhi_neng_bao_ming():
    '''
    “智能报名”：
    :return:
    '''
    vc = VC('emulator-5554')
    qqmail = QQMail()
    # vc.click_by_words("PU")
    # time.sleep(7)
    # vc.click_by_words("跳过")
    # vc.click_by_words("确定")
    # vc.click_by_words("登录")
    # vc.click_by_words("残忍拒绝")
    # time.sleep(1)
    # vc.click_by_words("本校活动")
    # time.sleep(2)
    # print(vc.get_ui_words())
    # vc.click_by_words("状态")
    # time.sleep(1)
    # vc.click_by_words("未开始")
    # vc.click_by_words("排序")
    # time.sleep(1)
    # vc.click_by_words("最热排序")
    wordsList = vc.get_ui_words()
    print_all_act(wordsList)
    score = []  # 各活动的学时属性字符串组成的列表，待排序
    good_activities = set()  # the define of good is the activity information including '校大礼堂'
    # vc.input_swipe([540, 1600], [540, 1900])  # 刷新页面

    while True:


        before_refresh_activity_count = len(good_activities)
        print(before_refresh_activity_count)

        # 模拟人眼看：信息提取
        wordsList = vc.get_ui_words()
        # 模拟注意力：关注点为【地点:校大礼堂】
        for key_value in wordsList:
            if '校大礼堂' in key_value['words']:
                good_activities.add(key_value['words'])
        # 模拟手指滑动：更新页面信息
        # vc.input_swipe([540, 1800], [540, 1200])
        vc.input_swipe([540, 1600], [540, 1900])  # 刷新页面

        time.sleep(2)
        after_refresh_activity_count = len(good_activities)
        print(after_refresh_activity_count)
        new_activity_count = after_refresh_activity_count - before_refresh_activity_count

        if new_activity_count >= 1:
            print_all_act(good_activities)
            qqmail.send_mail("刚刚有" + str(new_activity_count) + "个校大礼堂活动发布。")

        else:
            print("暂无新活动发布" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

        time.sleep(1800)  # 刷新周期：10分钟
        # while end



def dao_ji_shi():
    '''
    倒计时：用于事先知道报名时间，自动抢报
    h表示设定的小时，m为设定的分钟
    '''
    h = 0
    m = 0
    s = 0
    # 判断是否达到设定时间，例如0:00
    while True:
        now = datetime.datetime.now()
        print(now)
        # 到达设定时间，结束内循环
        if now.hour == h and now.minute == m and now.second == s:
            static_bao_ming()
            break
        # 刷新周期
        time.sleep(1)
        # 做正事，一天做一次
if __name__ == "__main__":
    zhi_neng_bao_ming()

    # for item in sorted(score): 测试默认排序规则
    #     print(item)





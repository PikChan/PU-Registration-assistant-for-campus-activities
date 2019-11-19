from source.VC import VC
from source.tools.sendQQeMail import QQMail
import datetime
import time



def static_bao_ming():
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


def zhi_neng_bao_ming():
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
    vc.click_by_words("状态")
    time.sleep(1)
    vc.click_by_words("未开始")
    wordsList = vc.get_ui_words()
    # for itemDict in wordsList:
    #     print(itemDict)
    # before_refresh_activity_count = len(wordsList)
    # print(before_refresh_activity_count)
    score = []  # 各活动的学时属性字符串组成的列表，待排序
    for itemDict in wordsList:
        if '社会实践活动学时' in itemDict['words']:
            score.append(itemDict['words'])
    before_refresh_activity_count = len(score)
    print(before_refresh_activity_count)

    while True:
        vc.input_swipe([540, 1600], [540, 1900])  # 刷新页面
        time.sleep(1)
        wordsList = vc.get_ui_words()
        # after_refresh_activity_count = len(wordsList)
        # print(after_refresh_activity_count)
        for itemDict in wordsList:
            if '社会实践活动学时' in itemDict['words']:
                score.append(itemDict['words'])
        after_refresh_activity_count = len(score)
        print(after_refresh_activity_count)

        new_activity_count = after_refresh_activity_count - before_refresh_activity_count

        if new_activity_count >= 1:
            qqmail.send_mail("刚刚有" + str(new_activity_count) + "个活动发布。")
            score = []  # 各活动的学时属性字符串组成的列表，待排序
            for itemDict in wordsList:
                if '社会实践活动学时' in itemDict['words']:
                    score.append(itemDict['words'])
            vc.click_by_words(sorted(score)[0])  # 点击最佳活动（学时数最高）
            time.sleep(1)
            vc.click_by_words("我要报名")
            break
        else:
            print("暂无新活动发布" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

        time.sleep(600)  # 刷新周期：10分钟
        # while end


if __name__ == "__main__":
    '''h表示设定的小时，m为设定的分钟'''
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

    # for item in sorted(score): 测试默认排序规则
    #     print(item)





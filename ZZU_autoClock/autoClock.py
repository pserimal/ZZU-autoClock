import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from send_email import send_mail

# 忽略无用的日志信息
options=Options()
options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])

# 小概率出现连接不安全（没配置证书，不会，鸽了！问题不大，暴力重连）的提醒
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(3)
while True:
    try:
        driver.get('https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/first0?fun2=a')
        break
    except:
        print('连接失败')
        driver.close()
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(3)
        continue

# 输入用户名密码并确认
input_user = driver.find_element(By.CSS_SELECTOR, '[type="text"]')
time.sleep(3)
input_user.send_keys('学号')
time.sleep(2)
input_password = driver.find_element(By.CSS_SELECTOR, '[type="password"]')
input_password.send_keys('密码')
time.sleep(1)
input_enter = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
input_enter.click()
time.sleep(2)

# 邮件标题
send_message = '打卡成功'

# 本人填报
try:
    driver.switch_to.frame('zzj_top_6s')
    sure_send = driver.find_element(By.XPATH, '//*[@id="bak_0"]/div[11]/div[3]/div[4]')
    sure_send.click()
    time.sleep(2)
except Exception:
    send_message = '本人填报打卡失败！！！'

# 确认填报
# 健康码颜色，不可以乱搞颜色
# 2022/04/04 系统改了，不需要了
# try:
#     health_mar = Select(driver.find_element(By.CSS_SELECTOR, '#bak_0 > div:nth-child(8) > div:nth-child(2) > div:nth-child(42) > div:nth-child(31) > select:nth-child(1)'))
#     health_mar.select_by_value("g")
# except Exception:
#     send_message = '打卡失败！！！'


# 你是哪（na）省的呀
try:
    na = Select(driver.find_element(By.CSS_SELECTOR, '#myvs_13a'))
    na.select_by_visible_text('省份')
except Exception:
    send_message = '省份打卡失败！！！'

# 你是哪个踏踏儿的
try:
    get_dishi = driver.find_element(By.CSS_SELECTOR, '[value="获取地市"]')
    get_dishi.click()

    dishi = Select(driver.find_element(By.CSS_SELECTOR, '#myvs_13b'))
    dishi.select_by_visible_text('城市')
except Exception:
    send_message = '城市打卡失败！！！'

# 提交表格
try:
    time.sleep
    sure_submit = driver.find_element(By.CSS_SELECTOR, '#btn416b')
    sure_submit.click()
    time.sleep(2)
except Exception:
    send_message = '提交表格打卡失败！！！'

thanks = '获取打卡信息失败'
# 获取成功信息
try:
    thanks = driver.find_element(By.CSS_SELECTOR, '#bak_0 > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2)').text
except Exception:
    print('error')
    send_message = '打卡可能失败了？自行查看'

# 结束退出
# driver.close()

print(send_message)
print(thanks)

# send_mail(send_message, thanks)

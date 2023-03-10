
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as waitfor
from selenium.webdriver.support import expected_conditions as expc

import time
from tkinter import Tk 

import paramiko
from scp import SCPClient

import os

# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}   #Chrome
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62"} # edge


# # # 使用headless 模式只需给webdriver 添加 options 参数即可， headless 模式下剪贴板无法操作！
# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.headless = True
# chrome_options.add_argument("window-size=1920x1080")
# chrome_options.add_argument("User-Agent = Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36")
# browser  = webdriver.Chrome(options=chrome_options)



#지정한 갯수만큼 서버 정보 가져오기
# 구독,  백업서버: 0번
from  ___mdms import get_host,get_server
qty_of_server = 2
hosts   = [get_host(i) for i in range(0,qty_of_server)] 
servers = [get_server(i) for i in range(0,qty_of_server)] 
urls    = [get_host(i)[0] for i in range(0,qty_of_server)]
files   = [get_server(i)[0] for i in range(0,qty_of_server)]


browser  = webdriver.Chrome()
browser.maximize_window()




for index,url in enumerate(urls):
    browser.get(url)
    # 等待页面显示后，再多等待一秒钟
    elem = waitfor(browser, 10).until(expc.presence_of_element_located((By.XPATH,'//*[@id="app"]/main/div[2]/div/form/div[3]/div/div/span/button/span')))
    time.sleep(1)
    # 填写用户名，密码 登录
    namepw = browser.find_elements(By.CLASS_NAME,"ant-input")
    namepw[0].send_keys(hosts[index][1])
    namepw[1].send_keys(hosts[index][2])
    login = browser.find_element(By.TAG_NAME,"button")
    login.click()
    time.sleep(2) # 点击登录后等待


    # 进入入站列表
    url = urls[index] + 'xui/inbounds'
    browser.get(url)
    # browser.save_screenshot('92_inbounds.png')
    # 导出入栈列表到剪贴板
    # expc.presence_of_element_locted():  need only one argument, 때문에 검색조건은 괄호를 쳐서 하나로 만들어야 함
    elem = waitfor(browser, 10).until(expc.presence_of_element_located((By.CLASS_NAME,"copy-btn")))
    time.sleep(1) #页面仙逝后再等待一秒钟
    btn = browser.find_element(By.CLASS_NAME,'copy-btn')
    btn.click()

    time.sleep(1) #点击复制链接按钮以后等待保存到剪贴板
    data = Tk().clipboard_get()

    sublinkfilefolder = './backup/{}/'.format(servers[index][0])
    if not os.path.isdir(sublinkfilefolder):
        os.makedirs(sublinkfilefolder)

    sublinkfile = sublinkfilefolder + files[index] + r'.sh' # full filename
    with open(sublinkfile, "w",encoding="utf8") as f:
        f.write(data)
    print(servers[index][0], "的节点链接文件已成功保存到:  " + sublinkfile)


    # 登出X-ui面板
    menu = browser.find_elements(By.TAG_NAME,'li')
    menu[4].click()

#关闭浏览器
browser.close()


#----------------------

# 定义函数 :建立 ssh链接
def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client
 

# 上传sublink文件到静态站
time.sleep(1)
for index, file in enumerate(files):
    ssh = createSSHClient(servers[0][0], 22, servers[0][1], servers[0][2]) # 上传到订阅server
    scp = SCPClient(ssh.get_transport())  
    sublinkfilefolder = './backup/{}/'.format(servers[index][0])
    sublinkfile = sublinkfilefolder + file + '.sh'
    scp.put(sublinkfile,'/root/myroot/')
    print(file + '.sh 成功上传到' , servers[0][0] + ':/root/myroot/')


# 备份数据库db文件到本地
for index, server in enumerate(servers):
    ssh = createSSHClient(servers[index][0], 22, servers[index][1], servers[index][2]) #与每个server建立连接
    scp = SCPClient(ssh.get_transport()) 
    sublinkfilefolder =  './backup/{}/'.format(servers[index][0])

    scp.get('/etc/x-ui/x-ui.db', sublinkfilefolder) 
    print('{}서버:/etc/x-ui/x-ui.db 파일을./backup/{}/폴더에 백업 완료.'.format(servers[index][0],servers[index][0]))



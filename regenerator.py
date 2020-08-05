from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
t1 = time.time()
for n in range(40):
    names = []
    emails = []
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome("C:\\chromedriver.exe", options=chrome_options)
    driver.get("https://www.name-generator.org.uk/quick/")
    time.sleep(.2)
    elem = driver.find_element_by_name("count")
    generated_names = driver.find_elements_by_xpath('//*[@class="name_heading"]')
    for i in range(len(generated_names)):
        names.append(generated_names[i].text)
    driver.close()

    for i in range(len(names)):
        a, b = names[i].split()
        if '-' in a or '-' in b:
            continue
        emails.append("{}.{}@gmail.com".format(a.lower(), b.lower()))
        emails.append("{}{}@gmail.com".format(a.lower(), b.lower()))
        emails.append("{}{}@gmail.com".format(a[0].lower(), b.lower()))
        emails.append("{}.{}@hotmail.com".format(a.lower(), b.lower()))
        emails.append("{}{}@hotmail.com".format(a.lower(), b.lower()))
        emails.append("{}{}@hotmail.com".format(a[0].lower(), b.lower()))

    f = open("C:\\Users\\neboj\\Desktop\\mailing_list.txt", "r+")

    for email in emails:
        if email in f.read():
            continue
        else:
            f.write(email + '\n')

    f.close()
print(int(time.time() - t1))
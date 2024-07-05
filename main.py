from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select 
import time
import os

def test_create_new_folder():
    os.mkdir('logs')

def test_add_new_file_with_title(driver):
    os.chdir('C:\\Users\\97250\\Desktop\\Practice Automation\\logs')
    
    with open('title.txt', 'w') as file:
        title_element = driver.find_element(By.TAG_NAME, 'title')
        title_text = title_element.get_attribute('textContent')
        file.write(title_text)
        
def test_form(driver):
    
    firstName = driver.find_element(By.ID,'RESULT_TextField-1')
    firstName.clear()
    firstName.send_keys('Daniel')
    
    lastName = driver.find_element(By.ID,'RESULT_TextField-2')
    lastName.clear()
    lastName.send_keys('Razal')
    
    phone = driver.find_element(By.ID,'RESULT_TextField-3')
    phone.clear()
    phone.send_keys('0502242268')
    
    country = driver.find_element(By.ID,'RESULT_TextField-4')
    country.clear()
    country.send_keys('Israel')
    
    city = driver.find_element(By.ID,'RESULT_TextField-5')
    city.clear()
    city.send_keys('Or Yehuda')
    
    email = driver.find_element(By.ID,'RESULT_TextField-6')
    email.clear()
    email.send_keys('mr.danielrazal@gmail.com')
    
    femaleGender = driver.find_element(By.XPATH,'//*[@id="q26"]/table/tbody/tr[2]/td/label')
    femaleGender.click()
    
    time.sleep(2)
    
    maleGender = driver.find_element(By.XPATH,'//*[@id="q26"]/table/tbody/tr[1]/td/label')
    maleGender.click()
    
    time.sleep(2)
    
    checkboxes_xpath = [
        '//*[@id="q15"]/table/tbody/tr[1]/td/label',
        '//*[@id="q15"]/table/tbody/tr[2]/td/label',
        '//*[@id="q15"]/table/tbody/tr[3]/td/label',
        '//*[@id="q15"]/table/tbody/tr[4]/td/label',
        '//*[@id="q15"]/table/tbody/tr[5]/td/label',
        '//*[@id="q15"]/table/tbody/tr[6]/td/label',
        '//*[@id="q15"]/table/tbody/tr[7]/td/label',
    ]
    
    for xpath in checkboxes_xpath:
        checkboxes = driver.find_elements(By.XPATH, xpath)
        for checkbox in checkboxes:
            checkbox.click()
    
    time.sleep(2)
    
    select = Select(driver.find_element(By.ID,'RESULT_RadioButton-9'))
    
    selectsArray = [0,1,2,3]
    for i in selectsArray:
        select.select_by_index(i)
        time.sleep(2)
        
    select.select_by_index(3)
    time.sleep(2)
    select.select_by_value('Radio-1')
    time.sleep(2)
    select.select_by_visible_text('Morning')
    
    """
    file_path = "C:\\Users\\97250\\Desktop\\קורות חיים לבודק תוכנה\\Daniel Razal - English CV.docx"

    # Find the file input element
    chooseFiles = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='file']"))
    )

    # Send the file path to the file input element
    chooseFiles.send_keys(file_path)

    # Optionally, if needed, interact with the submit button or form after uploading
    upload_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'RESULT_FileUpload-10'))
    )
    upload_button.click()
    
    """
    
    

if __name__ == '__main__':
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')
    driver.maximize_window()
    if not os.path.exists('logs'):
        test_create_new_folder()
    if not os.path.exists('logs\\title.txt'):
        test_add_new_file_with_title(driver)
    
    test_form(driver)
    time.sleep(3)
    driver.close()

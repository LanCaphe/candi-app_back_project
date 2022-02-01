from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep 

import os 
print('mon print : ' , os.getcwd())

driver = webdriver.Firefox(executable_path='./Test/driver/geckodriver')

class Selenium_test:
    
    def login_test(user, password) :
        # Insert user and password in the login form 
        driver.find_element_by_id('email').send_keys(user)
        driver.find_element_by_id('password').send_keys(password)
        driver.find_element_by_name('submit').click()
        
        # Assert h1 field is correct in this page
        # Try + assert ou l'un ou l'autre uniquement ? 
        try:
            h1 = driver.find_element_by_tag_name('h1')
            assert h1.text == "CANDIDATURES"
        except AttributeError:
            print('ERROR ----- h1 not found')
        # Assert Flash login success 
        flash_login = driver.find_element_by_class_name('alert')
        assert 'Vous êtes connecté en tant que :' in flash_login.text 
        print('------------------test login user Done----------------------')

    def add_candidacy_test(test_name, contact_test):
        # To click to the button add candidacy
        driver.find_element_by_link_text('Ajouter candidature').click()
        
        # Insert the candidacy in the form 
        driver.find_element_by_id('name').send_keys(test_name) 
        driver.find_element_by_id('place').send_keys('Lille') 
        driver.find_element_by_id('contact').send_keys(contact_test) 

        # Click on the button add candidacy
        driver.find_element_by_name('submit').click()

        # Assert flash element added success 
        flash_succes_xpath = '//div[@class="alert alert-success alter-dismissable fade show"]'
        flash_succes = driver.find_element_by_class_name('alert').text
        assert 'Nouvelle Candidature ajouté' in flash_succes 
        # Assert element is on dashboard's following place => Front test
        td_entreprise_xpath = '//div[@class="tbl-content"]/table/tbody/tr[3]/td[2]'
        td_entreprise = driver.find_element(By.XPATH, td_entreprise_xpath)
        assert td_entreprise.text == test_name
        print('------------------test add candidacy Done----------------------')


    def delete_candidacy_test() :
        # Click on the third button delete item 
        delete_xpath = '//div[@class="tbl-content"]/table/tbody/tr[3]/td[7]/a[2]'
        driver.find_element(By.XPATH, delete_xpath).click()
        # need order dashboard by last added to assert 'word' not in [xpath row[1]] 
        # Or need candidacy id on admin dashboard to assert deleted
        # Or need to use Candidacy.query.filter_by(name=["element to check"]) methods ?
        # 
        print('------------------delete candidacy n°3 done----------------------')
        


    def logout_test():
        # Click on button logout 
        driver.find_element_by_link_text('Log out').click()
        #Assert flash sucess loging 
        flash_logout = driver.find_element_by_class_name('alert')
        assert 'Vous êtes correctement déconnecté' in flash_logout.text
        print ('----------------Test logout done---------------------------')


    def click_login():
        driver.find_element_by_link_text('Log in').click()
        h1 = driver.find_element_by_tag_name('h1').text
        assert h1 == "LOG IN"
        print('---------------Click to login---------------------------')

    def modify_candidacy():
        # Save init status text in status coloumn 
        status_xpath = '//tbody/tr[3]/td[6]'
        status_start = driver.find_element(By.XPATH, status_xpath).text
        
        modify_xpath = '//tbody/tr[3]/td[7]/a[1]'
        driver.find_element(By.XPATH, modify_xpath).click()
      
        status = driver.find_element_by_id('status')
        status.clear()
        status.send_keys('Accepté')
        driver.find_element_by_id('button').click()
        
        status_end = driver.find_element(By.XPATH, status_xpath).text
        assert status_start != status_end
        assert status_end == "Accepté"
        print('----------------Test modify status Candidacy-------------')
        
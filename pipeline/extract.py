from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
import json
import os

def Extract():
    
    #chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()
    
    url = "https://www.bkam.ma/fr/Marches/Principaux-indicateurs/Marche-des-changes/Cours-de-change/Cours-des-billets-de-banque-etrangers?block=98a86bd3205c8223897bbd8d87e3788d&sort=col2,asc"
    driver.get(url) 

    current_date    = datetime.today()
    analysis_period = (current_date - timedelta(days=30))

    results = []

    while True:

        date_str = current_date.strftime('%d/%m/%Y')
        
        driver.execute_script("window.scrollTo(0, 0);")
        form_filter = driver.find_element(By.CLASS_NAME, 'form-filter')
        date_field = form_filter.find_element(By.NAME, 'date')
        date_field.clear()
        date_field.send_keys(date_str)
        
        try:
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='submit']")))
            submit_button = form_filter.find_element(By.XPATH, "//input[@type='submit']")
            submit_button.click()
        except:
            pass

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'block-table'))
        )
        
        bloc_table = driver.find_element(By.CLASS_NAME, 'block-table')

        try:
            p_tag = bloc_table.find_element(By.TAG_NAME, 'p')
            if p_tag:
                Devises = ["1 EURO", "1 DOLLAR U.S.A.", "1 DOLLAR CANADIEN", "1 LIVRE STERLING", "1 LIVRE GIBRALTAR", "1 FRANC SUISSE", "1 RIYAL SAOUDIEN", "1 DINAR KOWEITIEN", "1 DIRHAM E.A.U.", "1 RIYAL QATARI", "1 DINAR BAHREINI", "100 YENS JAPONAIS", "1 RIYAL OMANI"]
                for Devise in Devises:
                    results.append({
                    "date": current_date.strftime('%m/%d/%Y'),
                    "devise_complete": Devise,
                    "taux_achat": None,
                    "taux_vente": None
                    })          
        except: 
            pass 
        
        try:
            result_table  = bloc_table.find_element(By.CLASS_NAME, 'dynamic_contents_ref_19')
            tbody_element = result_table.find_element(By.TAG_NAME, 'tbody')
            tr_elements   = tbody_element.find_elements(By.TAG_NAME, 'tr')

            for tr_element in tr_elements:
                tds = tr_element.find_elements(By.TAG_NAME, "td")
                if len(tds) == 3:
                    Devise    = tds[0].text
                    taux_achat = tds[1].text
                    taux_vente = tds[2].text
                    results.append({
                        "date": current_date.strftime('%m/%d/%Y'),
                        "devise_complete": Devise,
                        "taux_achat": taux_achat,
                        "taux_vente": taux_vente,
                    })
        except:
            pass

        if current_date == analysis_period:
            break  
        current_date -= timedelta(days=1)

    # Fermer le navigateur
    driver.quit()

    current_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(current_dir, '..', 'exchange_data', 'raw_taux_change.json')

    # Enregistrer dans un fichier JSON
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)
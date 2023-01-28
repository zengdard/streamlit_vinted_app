from pyVinted import Vinted
import streamlit as st
vinted = Vinted()



st.title('WeTheCop')
st.markdown('### Estimer n\'importe quel article !' )
st.markdown('#### Notre bot payant : https://mercuresoftware.gumroad.com/l/botVintedDiscord')
text = st.text_input("Quel est votre article ?", '')

def estimation(article):
        
        try:
            null = 0
            false = False
            true = True
            url = f'https://www.vinted.fr/api/v2/catalog/items?search_text={article}&order=newest_first'
            items = vinted.items.search(url, 100, 1, json=True)   

            null = 0
            false = False
            true = True
            price = 0
            max = 0
            min = 100
            for c in range(0, len(items)):
                price_temp = float(items[c]['price'])
                price = price + price_temp

                if price_temp > max :
                    max = price_temp
                if price_temp < min :
                    min = price_temp

            price = price / 100
            price = round(price,2)
            estimation_price=f'{min}-{max}€'
            prix_deux = f'{price}€'
        except:
            estimation_price = 'N/A'
            prix_deux = 'N/A'
        return [prix_deux,estimation_price]


bar = st.progress(0)

if st.button('Estimer'):
    resul = estimation(text)

    bar.progress(20)
    try:
        st.subheader("Résultat.")
        st.subheader('Estimation moyenne : ' + str(resul[0]))
        st.subheader('Répartition : ' + str(resul[1]))
        

        bar.progress(50)
    except:
        st.warning('Le service est temporairement indisponible, merci de votre compréhension.' )
    bar.progress(100) 

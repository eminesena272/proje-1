meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROLE-PLAY":"ROL YAPMAK",
            "FAKE ATMAK":"ŞAŞIRTMAK",
            "COOL":"HAVALI",
            "ROFL":"ŞAKAYA KARŞILIK VERMEK"
            }
kelime = input("kelimeleri girin")            

if kelime in meme_dict.keys():
    print(meme_dict[kelime])
else:
    print("kelime listede yok")

meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "EZ": "Ketika sesuatu sangat mudah dilakukan",
            "BTW": "Omong-Omong",
            "K": "Ok"
            }
            
word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")

if word in meme_dict.keys():
    print('Arti dari kata tersebut adalah "',meme_dict[word], '"')
else:
    print("Maaf, tidak ada kata itu dalam Kamus Meme")

shops = [{
        "shop_id" : "shop-CS-3134",
        "city" : ["東 都","渋谷区","代々木"],
        "category" : ["飲食業","居酒屋","居酒屋"],
        "keywords" : ["飲食業", "football","tennis"]
    },
    {
        "shop_id" : "shop-CS-3124",
        "city" : ["Tokyo","渋谷区","代々木"],
        "category" : ["Tokyo","居酒屋","居酒屋"],
        "keywords" : ["clothes", " hats","sunglasses","rings"]
    },
    {
        "shop_id" : "shop-CS-3144",
        "city" : ["東 都","渋谷区","代々木"],
        "category" : ["飲食業","居酒屋","居酒屋"],
        "keywords" : ["premium clothes", "hoodies","BTS"]
    }]
#print(shops[0]['city'])
for index, shop in enumerate(shops):
    #print(index)
    print(shop["city"])
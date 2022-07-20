database = {
  "sidedish" : {

    "Fries":{
      "price":"50"
    },
    "Salad":{
      "price": "50"
    },
    "Mashed Potato":{
      "price": "50"
    }
  },

  "pizza" : {
    "Cheese Pizza":{
      "price":"50"
    },
    "Pepperoni Pizza":{
      "price": "50"
    },
    "Hawaiian Pizza":{
      "price": "50"
    }
  },

  "drinks" : {
    "Tea":{
      "price":"50"
    },
    "Coffee":{
      "price": "50"
    },
    "Cola":{
      "price": "50"
    }
  }
}




database = {
    "sidedish" : {
        "text" : {
            "font": "Arial",
            "size": "12"
         },
        "position":{
            "x":10,
            "y":100
        },
        "elements" : {
            "Fries":{
               "price":"50",
               "quantity":"0"
            },
                "Salad": {
                    "price": "50",
                    "quantity":"0"
                },
                "Mashed Potato":{
                    "price": "50",
                    "quantity": "0"
                }
        }
    }
}


print("\n\n before")
for key, element in database["sidedish"]["elements"].items():
    print(f'price of {key} : {element["price"]}')
    print(f'quantity of {key} : {element["quantity"]}')

print("\n\n after")
database["sidedish"]["elements"]["Fries"]["price"] = 12

for key, element in database["sidedish"]["elements"].items():
    print(f'price of {key} : {element["price"]}')
    print(f'quantity of {key} : {element["quantity"]}')





def go_pew(answer):
    if answer:
        return True
    if not answer:
        return False



assert go_pew(False)
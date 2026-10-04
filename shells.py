FILE_PRICES="c:/Users/semah/Desktop/polito year 1/fileprices.txt"
FILE_OFFERS="c:/Users/semah/Desktop/polito year 1/fileoffers.txt"
FILE_CHARTS="c:/Users/semah/Desktop/polito year 1/filecharts.txt"

def dict_prices(filename):
    prices=dict()
    try:
        with open(filename) as f:
            for line in f:
                name,price=line.split(":")
                price=float(price.rstrip("\n"))
                prices[name]=price
    except OSError as problem:
        print(problem)
        exit(1)
    return prices

def list_offers(filename):
    offers=list()
    try:
        with open(filename) as f:
            for line in f:
                name,offer=line.split(":")
                offer=offer.rstrip("\n")
                offers.append((name.split(),offer))
    except OSError as problem:
        print(problem)
        exit(1)
    return offers

def dict_charts(filename):
    try:
        carts=dict()
        with open(filename) as file:
            for line in file:
                line=line.rstrip()
                if line not in carts:
                    carts[line]=1
                elif line in carts:
                    carts[line]+=1
        return carts
    except OSError as problem:
        print(problem)
        exit(1)

def main():
    prices=dict_prices(FILE_PRICES)
    offers=list_offers(FILE_OFFERS)
    charts=dict_charts(FILE_CHARTS)
    total_price=0  # Changed 'price' to 'total_price' to match your usage below
    
    for sublist in offers:
        item_name=sublist[0][0]
        
        # --- THIS IS THE FIX ---
        gift_name=sublist[1].strip() 
        # -----------------------
        
        qty_needed=len(sublist[0])
        
        if (item_name in charts) and (gift_name in charts):
            
            # CASE A: Same Item
            if item_name == gift_name:
                total_needed = qty_needed + 1                
                if charts[item_name] >= total_needed:
                    charts[item_name] -= total_needed
                    if item_name in prices:
                        total_price += prices[item_name] * qty_needed
                        
            
            else:
                if charts[item_name] >= qty_needed and charts[gift_name] >= 1:
                    charts[item_name] -= qty_needed
                    charts[gift_name] -= 1
                    
                    if item_name in prices:
                        total_price += prices[item_name] * qty_needed
                        
    
    for item, quantity in charts.items():
        if quantity > 0:
            if item in prices:
                total_price += prices[item] * quantity

    print(charts)
    print("Total Price:", total_price)

if __name__=="__main__":
    main()
    
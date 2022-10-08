#create lists for each variable
products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]
prices=[30,25,40,20,20,35,45,50,35]
last_week=[2,3,5,8,4,4,6,2,9]
newPrices=[]
lessThan30=[]
revenuePerProduct=[]

#calculate total price average
avg=(sum(prices)/len(prices))

#reduce prices by 5
for i in range(0,len(prices)):
    newPrices.append(prices[i]-5)

#find which newPrice is less than 30
    if newPrices[i]<30:
        lessThan30.append(newPrices[i])

#calculate total revenue for each product
    revenuePerProduct.append(prices[i]*last_week[i]) 

#calculate total revenue for all products
revenue=sum(revenuePerProduct)

#display results
print(f'average price: {avg:.2f}\n')
print(f'new prices: {newPrices}\n')
print(f'prices below 30: {lessThan30}\n')
print(f'revenueperproduct: {revenuePerProduct}\n')
print(f'revenue: {revenue}\n')







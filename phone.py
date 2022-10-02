phn=[]

class Phones:
    
    def __init__(self,modl,rm,stg,batt,pric,mno):
        self.model=modl
        self.ram=rm
        self.storage=stg
        self.battery=batt
        self.price=pric
        self.modelno=mno
    
    def viewAllPhones():
        for i in range(len(mobiles)):
            print("\nMobile %d" %(i+1))
            print("Phone model = "+ mobiles[i].model)
            print("Phone ram = "+ str(mobiles[i].ram)+ " GB ")
            print("Phone storage = "+ str(mobiles[i].storage) + " GB ")
            print("Phone battery = "+ str(mobiles[i].battery) + " mAh.")
            print("Phone Price = "+ str(mobiles[i].price)+ " Rs ")
            print("Phone model no = "+ str(mobiles[i].modelno))
    
    def AddNewPhone():  
        modl=input("\nEnter Phone model : ")
        rm=int(input("Enter ram storage : "))
        stg=int(input("Enter the internal storage : "))
        batt=int(input("Enter battery mAh : "))
        pric=int(input("Enter Price of phone in Rs : "))
        mno=int(input("Enter Model number of phone : "))
        mobiles.append(Phones(modl,rm,stg,batt,pric,mno))
    
    def checkDetails(self,mol):
        
        for i in range(len(mobiles)):
            if(mobiles[i].model==mol):
                print("Phone model = "+ mobiles[i].model)
                print("Phone ram = "+ str(mobiles[i].ram)+ " GB ")
                print("Phone storage = "+ str(mobiles[i].storage) + " GB ")
                print("Phone battery = "+ str(mobiles[i].battery) + " mAh.")
                print("Phone Price = "+ str(mobiles[i].price)+ " Rs ")
                print("Phone model no = "+ str(mobiles[i].modelno))
               
    def purchase(self,mol):
         
        for i in range(len(mobiles)):
                if(mobiles[i].model==mol):
                    print(str(mobiles[i].model)+ "       "+ str(mobiles[i].price)+ "Rs")
                    phn.append(mobiles[i].price)            
        print("Total Amount     "+str(sum(phn))+ "Rs")        
        
        
            
mobiles=[Phones("iphone13",6,64,4000,70000,1),Phones("samsungx12",8,128,5000,20000,2)]
x=Phones

print("Menu \na) List all the phones in the shop along with all the details\nb) Add new phones to the list on arrival\nc) Check the details of a particular model\nd) Print invoice when a customer purchases the phone\ne) Exit")

option = 'z'
while(option!='e'):
    option=input("\nChoose an option: ")
    
    if(option=='a'):
        x.viewAllPhones()
        
    elif(option=='b'):
        x.AddNewPhone()
        
    elif(option=='c'):    
        mol=input("\nEnter Phone model : ")
        for i in range(len(mobiles)):
            if(mobiles[i].model==mol):
                mobiles[i].checkDetails(mol)   
                 
        
    elif(option=='d'): 
        mol=input("\nEnter the model of the phone to purchase: ")
        for i in range(len(mobiles)):
            if(mobiles[i].model==mol):
                mobiles[i].purchase(mol) 
        
        
        
        
        
        

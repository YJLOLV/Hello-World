#%%

class VGSM:
    SKU="DAR023"
    Name="VG Skim MIlk"
    Brand="Very Good Brands"
    Manufacturer="Georgia Dairy, Inc."
    Dimensions=[8,8,10,"in"]
    Weight=2.2
    WtUnits="lbs"
    
# Cer12 = Product()
# LDet24 = Product()

#%%    
class Product:
    
    Version =" Ver 1.2 Rev 3"
    
    def __init__(self,sku,name,brand,manu,dims,wt, wtunits):
        self.SKU = sku
        self.Name = name
        self.Brand = brand
        self.Manufactuer = manu
        self.weight = wt
        self.wtunits = wtunits
  
#%%
# Product Structure
#
# SKU
# Product Name
# Brand
# Manufacturer
# As a list [width, depth, height, units]
# Weight
# Units

# Note: the comment line below creates a "cell" for
# the editor in Spyder. Having the curson anywhere in the
# cell allows you to execute the code in the cell (up to
# the next cell boundary) by cntrl-enter

#%%

class Product:
    
    Version = "Ver 1.2 Rev 3"
    
    def __init__(self,sku,name,brand,manu,dims,wt,wtunits):
        self.SKU = sku
        self.Name = name
        self.Brand = brand
        self.Manufacturer = manu
        self.Dimensions = dims
        self.Weight = wt           # Should have been Weight
        self.WtUnits = wtunits
        
    def Print(self):
        out = "\nName:\t\t"+self.Name+"\nSKU:\t\t"+self.SKU+"\n"+ \
            "Brand:\t\t"+self.Brand+"\nManufacturer:\t"+self.Manufacturer+"\n\n"+ \
            "Dimensions\n"+ \
            "\tWidth:\t"+str(self.Dimensions[0])+self.Dimensions[3]+"\n"+ \
            "\tDepth:\t"+str(self.Dimensions[1])+self.Dimensions[3]+"\n"+ \
            "\tHeight:\t"+str(self.Dimensions[2])+self.Dimensions[3]+"\n\n"+ \
            "\tWeight:\t"+str(self.Weight)+self.WtUnits+"\n"
        print (out)

    def SetPhone(self,PhoneNum):
        # Phone number format is XXX-XXX-XXXX
    
        dgts="0123456789"
    
        BadFmt=False
        if type(PhoneNum)!=type("abc") or len(PhoneNum)!=12:
            BadFmt=True
        
        if PhoneNum[3]!="-" or PhoneNum[7]!="-":
            BadFmt=True
        
        if not ( PhoneNum[0] in dgts and PhoneNum[1] in dgts and \
                    PhoneNum[2] in dgts and PhoneNum[4] in dgts and \
                    PhoneNum[5] in dgts and PhoneNum[6] in dgts and\
                    PhoneNum[8] in dgts and PhoneNum[9] in dgts and \
                    PhoneNum[10] in dgts and PhoneNum[11] in dgts):
            BadFmt=True
        
        if BadFmt:
            print ("Wrong phone number format. Use \"xxx-xxx-xxxx\"\n")
            return False
        
        self.__PhoneNumber = PhoneNum
        
        return True
    
    def GetPhone(self):
        return self.__PhoneNumber             
    

#%%

# Create two instances of the class product

Milk23 = Product("DAR023","VG Skim Milk","Very Good Brands","Georgia Dairy",[8,8,10,"in"],2.2,"lbs")
Cer12 = Product("CER012","VG Corn Flakes","Very Good Brands","House Products, Inc.",[9,3,11,"in"],18,"oz")

#%%
# Product Structure
#
# SKU
# Product Name
# Brand
# Manufacturer
# As a list [width, depth, height, units]
# Weight
# Units

#%% Define the Product class

class Product:
    
    Version = "Ver 3.4 Rev 6"
    
    def __init__(self,sku,name,brand,manu,dims,wt,wtunits):
        self.SKU = sku
        self.Name = name
        self.Brand = brand
        self.Manufacturer = manu
        self.Dimensions = dims
        self.Weight = wt           # Should have been Weight
        self.WtUnits = wtunits
    
    def Print(self):
        out = "\nName:\t\t"+self.Name+"\nSKU:\t\t"+self.SKU+"\n"+ \
            "Brand:\t\t"+self.Brand+"\nManufacturer:\t"+self.Manufacturer+"\n\n"+ \
            "Dimensions\n"+ \
            "\tWidth:\t"+str(self.Dimensions[0])+self.Dimensions[3]+"\n"+ \
            "\tDepth:\t"+str(self.Dimensions[1])+self.Dimensions[3]+"\n"+ \
            "\tHeight:\t"+str(self.Dimensions[2])+self.Dimensions[3]+"\n\n"+ \
            "\tWeight:\t"+str(self.Weight)+self.WtUnits+"\n"
        print (out)
    
    def SetPhone(self,PhoneNum):
        # Phone number format is XXX-XXX-XXXX
    
        dgts="0123456789"
    
        BadFmt=False
        if type(PhoneNum)!=type("abc") or len(PhoneNum)!=12:
            BadFmt=True
        
        if PhoneNum[3]!="-" or PhoneNum[7]!="-":
            BadFmt=True
        
        if not ( PhoneNum[0] in dgts and PhoneNum[1] in dgts and \
                    PhoneNum[2] in dgts and PhoneNum[4] in dgts and \
                    PhoneNum[5] in dgts and PhoneNum[6] in dgts and\
                    PhoneNum[8] in dgts and PhoneNum[9] in dgts and \
                    PhoneNum[10] in dgts and PhoneNum[11] in dgts):
            BadFmt=True
        
        if BadFmt:
            print ("Wrong phone number format. Use \"xxx-xxx-xxxx\"\n")
            return False
        
        self.__PhoneNumber = PhoneNum
        
        return True
    
    def GetPhone(self):
        return self.__PhoneNumber
    
    def PrintShelfVolume(self):
        volume = self.Dimensions[0]*self.Dimensions[1]*self.Dimensions[2]
        out = "Shelf Volume = " + str(volume) + " " + \
                self.Dimensions[3] + " cubed\n"
        print (out)
        return volume
    
    def FootprintArea(self):
        return self.Dimensions[0]*self.Dimensions[1]

#%%   Create two instances           

Milk23 = Product("DAR023","VG Skim Milk","Very Good Brands","Georgia Dairy",[8,8,10,"in"],2.2,"lbs")
Cer12 = Product("CER012","VG Corn Flakes","Very Good Brands","House Products, Inc.",[9,3,11,"in"],18,"oz")

#%%    Define the MilkProduct class

class MilkProduct(Product):
    
    Category = "Dairy"
    Storage = "Refrigerated"
    
    def __init__(self,sku,name,brand=None,manu=None,dims=None,wt=None, \
        wtunits=None,vol=None,fatcat="Whole",expir=None,servsize=None, \
        numserve=None,cals=None,fatgrams=None,fatcals=None,phone=None):
        
        Product.__init__(self,sku,name,brand,manu,dims,wt,wtunits)
        
        self.Volume = vol
        self.FatCategory = fatcat
        self.ExpirationDate = expir
        self.ServingSize = servsize
        self.NumberServings = numserve
        self.Calories = cals
        self.FatGrams = fatgrams
        self.FatCalories = fatcals
        
        if phone!=None:
            self.SetPhone(phone)
       
#%%    Define the LaundreyDetergentProduct class   
    
class LaundryDetergentProduct(Product):
    
    Category = "Laundry"

    def __init__(self,sku,name,brand=None,manu=None,dims=None,wt=None, \
        wtunits=None,numloads=None,sudslevel="Not HE",form="Powder", \
        scent=None,phone=None):
        
        Product.__init__(self,sku,name,brand,manu,dims,wt,wtunits)
        
        self.NumberLoads = numloads
        self.SudsingLevel = sudslevel
        self.PhysicalForm = form
        self.Scent = scent
        
        if phone!=None:
            self.SetPhone(phone)

#%%   Create two instances     

Milk23 = MilkProduct("DAR023","VG Skim Milk","Very Good Brands", \
        "Georgia Dairy",[8,8,10,"in"],2.2,"lbs","1Gal","Skim","2014-09-27", \
        8,16,90,0,0,"305-735-4353")
        
Det16 = LaundryDetergentProduct("LAU016","VG Laundry Detergent", \
        "Very Good Brands",dims=[9,3,11,"in"],wt=18,wtunits="oz", \
        numloads=72,sudslevel="HE",form="Liquid")
         
#%%

# The for loop in Python:
#
# for Variable in Iterable:
#    code line 1
#    code line 2
#   etc.
#
# In some other languages:

# for(i=0;i<n;i++) {
#   code line 1
#    code line 2
#    etc.
# }

""" 
#%%
# The 200 highest paid CEOs in 2014, in order, highest to lowest.
# Source: http://www.equilar.com/publications/51-200-highest-paid-CEO-rankings-2015.html

CEOs = ["David M. Zaslav","Michael T. Fries","Mario J. Gabelli",
        "Satya Nadella","Nicholas Woodman","Gregory B. Maffei",
        "Lawrence J. Ellison","Steven M. Mollenkopf","David T. Hamamoto",
        "Leslie Moonves","Philippe P. Dauman","Robert A. Iger",
        "Joseph W. Brown Jr.","Marissa A. Mayer","Leonard S. Schleifer",
        "Joshua W. Sapan","Marc Benioff","Jeffrey M. Leiden",
        "Herve Hoppenot","Jeffrey L. Bewkes","Gary W. Loveman",
        "Eric J. Foss","Zachary Nelson","Martine Rothblatt",
        "William J. McMorrow","W. Nicholas Howley","Steve Ells",
        "Howard M. Lorber","Rex W. Tillerson","Brian C. Cornell",
        "Montgomery F. Moran","James Dimon","Jonathan Oringer",
        "Paul M. Rady","Brian L. Roberts","Craig A. Leavitt",
        "Lamberto Andreotti","Ari Bousbib","Ronald N. Tutor",
        "Stephen A. Wynn","Thomas B. Barker","Stephen P. MacMillan",
        "Wayne T. Smith","Larry J. Merlo","Robert J. Hugin",
        "Michael J. Saylor","John D. Wren","Brian Harris",
        "K. Rupert Murdoch","Laurence D. Fink","Leslie H. Wexner",
        "James L. Dolan","W. James McNerney, Jr","Carol Meyrowitz",
        "James P. Gorman","Peter Liguori","David M. Cote",
        "A. Jayson Adair","Brian D. Jellison","James M. Cracchiolo",
        "Kenneth I. Chenault","Lloyd C. Blankfein","Barry D. Zyskind",
        "Darren R. Huston","Howard Schultz","Kenneth C. Frazier",
        "Randall L. Stephenson","Leonard Bell","Peter M. Carlino",
        "Alex Gorsky","David J. Lesar","Margaret C. Whitman",
        "Richard D. Fairbank","Jay S. Fishman","Andrew N. Liveris",
        "Alan G. Lafley","William R. Berkley","John G. Stumpf",
        "Michael F. Neidorff","Paul C. Saville","Indra K. Nooyi",
        "C. Douglas McMillon","Phebe N. Novakovic","John C. Martin",
        "Jeffrey R. Immelt","John S. Watson","John J. Legere",
        "George A. Scangos","Alan B. Miller","Lowell C. McAdam",
        "Muhtar Kent","Ian C. Read","Virginia M. Rometty",
        "Paul A. Ricci","Stuart A. Miller","Shantanu Narayen",
        "Marillyn A. Hewson","Alan H. Auerbach","Ryan M. Lance",
        "Richard H. Anderson","Richard E. Muncrief","Marc N. Casper",
        "Ronald F. Clarke","Thomas F. Farrell, II","John R. Strangfeld",
        "Samuel R. Allen","Kevin M. Sheehan","Richard A. Gonzalez",
        "Miles S. Nadal","Paal Kibsgaard","Gregory D. Wasson",
        "Brad D. Smith","Hamid R. Moghadam","John T. Chambers",
        "Scott A. McGregor","Dave Schaeffer","Gary E. Dickerson",
        "Alex A. Molinaroli","Marc Holliday","Patricia A. Woertz",
        "Miles D. White","Thomas M. Rutledge","Glenn K. Murphy",
        "Irene B. Rosenfeld","Gregory E. Johnson","Mary T. Barra",
        "John D. Finnegan","Jeffrey Weiner","Martin L. Flanagan",
        "Greg C. Garland","Robert A. Walker","Douglas R. Oberhelman",
        "Mark T. Bertolini","Martin B. Anstice","Fabrizio Freda",
        "Mark Fields","Wesley G. Bush","John Richels",
        "Jay T. Flatley","Stephen J. Hemsley","Richard K. Templeton",
        "Arne M. Sorenson","James T. Prokopanko","Gregory J. Goff",
        "Lorenzo Delpani","David Simon","John J. Koraleski",
        "Richard J. Kramer","Laura J. Alber","Mark G. Parker",
        "Robert D. Lawler","Martin S. Craighead","Brian T. Moynihan",
        "Steven A. Kandarian","Michael L. Corbat","Brian D. Goldner",
        "Mikkel Svane","David M. Cordani","John B. Hess",
        "Daniel S. Glaser","Inge G. Thulin","Robert A. Niblock",
        "Frederick W. Smith, III","Paul L. Berns","Stephen P. Holmes",
        "Joseph L. Hooley","John J. Donahoe","Robert A. Bradway",
        "William P. Sullivan","Kent J. Thiry","Charles E. Bunch",
        "Michael S. Burke","Robert J. Willett","Klaus Kleinfeld",
        "David G. DeWalt","Joseph R. Swedish","Gary R. Heminger",
        "Ajay Banga","Trevor Fetter","Mario Longhi",
        "Ellen J. Kullman","Eric C. Wiseman","Ian M. Cook",
        "Thomas J. Wilson","G. Frederick Wilkinson","Hubert Joly",
        "George Paz","William A. Cooper","Michael I. Roth",
        "Jeff M. Fettig","Donald E. Washkewicz","Robert L. Parkinson, Jr.",
        "Howard W. Lutnick","James D. Taiclet, Jr.","Steven E. Simms",
        "Terry J. Lundgren","James J. Volker","Scott D. Sheffield",
        "John F. Lundgren","Christopher M. Crane"]
#%%
        
CEOFirstNames = ["David","Michael","Mario",
            "Satya","Nicholas","Gregory",
            "Lawrence","Steven","David",
            "Leslie","Philippe","Robert",
            "Joseph","Marissa","Leonard",
            "Joshua","Marc","Jeffrey",
            "Herve","Jeffrey","Gary",
            "Eric","Zachary","Martine",
            "William","Nicholas","Steve",
            "Howard","Rex","Brian",
            "Montgomery","James","Jonathan",
            "Paul","Brian","Craig",
            "Lamberto","Ari","Ronald",
            "Stephen","Thomas","Stephen",
            "Wayne","Larry","Robert",
            "Michael","John","Brian",
            "Rupert","Laurence","Leslie",
            "James","James","Carol",
            "James","Peter","David",
            "Jayson","Brian","James",
            "Kenneth","Lloyd","Barry",
            "Darren","Howard","Kenneth",
            "Randall","Leonard","Peter",
            "Alex","David","Margaret",
            "Richard","Jay","Andrew",
            "Alan","William","John",
            "Michael","Paul","Indra",
            "Douglas","Phebe","John",
            "Jeffrey","John","John",
            "George","Alan","Lowell",
            "Muhtar","Ian","Virginia",
            "Paul","Stuart","Shantanu",
            "Marillyn","Alan","Ryan",
            "Richard","Richard","Marc",
            "Ronald","Thomas","John",
            "Samuel","Kevin","Richard",
            "Miles","Paal","Gregory",
            "Brad","Hamid","John",
            "Scott","Dave","Gary",
            "Alex","Marc","Patricia",
            "Miles","Thomas","Glenn",
            "Irene","Gregory","Mary",
            "John","Jeffrey","Martin",
            "Greg","Robert","Douglas",
            "Mark","Martin","Fabrizio",
            "Mark","Wesley","John",
            "Jay","Stephen","Richard",
            "Arne","James","Gregory",
            "Lorenzo","David","John",
            "Richard","Laura","Mark",
            "Robert","Martin","Brian",
            "Steven","Michael","Brian",
            "Mikkel","David","John",
            "Daniel","Inge","Robert",
            "Frederick","Paul","Stephen",
            "Joseph","John","Robert",
            "William","Kent","Charles",
            "Michael","Robert","Klaus",
            "David","Joseph","Gary",
            "Ajay","Trevor","Mario",
            "Ellen","Eric","Ian",
            "Thomas","Frederick","Hubert",
            "George","William","Michael",
            "Jeff","Donald","Robert",
            "Howard","James","Steven",
            "Terry","James","Scott",
            "John","Christopher"]
            
#%%
            
CEOLastNames = ["Zaslav","Fries","Gabelli",
                "Nadella","Woodman","Maffei",
                "Ellison","Mollenkopf","Hamamoto",
                "Moonves","Dauman","Iger",
                "Brown","Mayer","Schleifer",
                "Sapan","Benioff","Leiden",
                "Hoppenot","Bewkes","Loveman",
                "Foss","Nelson","Rothblatt",
                "McMorrow","Howley","Ells",
                "Lorber","Tillerson","Cornell",
                "Moran","Dimon","Oringer",
                "Rady","Roberts","Leavitt",
                "Andreotti","Bousbib","Tutor",
                "Wynn","Barker","MacMillan",
                "Smith","Merlo","Hugin",
                "Saylor","Wren","Harris",
                "Murdoch","Fink","Wexner",
                "Dolan","McNerney","Meyrowitz",
                "Gorman","Liguori","Cote",
                "Adair","Jellison","Cracchiolo",
                "Chenault","Blankfein","Zyskind",
                "Huston","Schultz","Frazier",
                "Stephenson","Bell","Carlino",
                "Gorsky","Lesar","Whitman",
                "Fairbank","Fishman","Liveris",
                "Lafley","Berkley","Stumpf",
                "Neidorff","Saville","Nooyi",
                "McMillon","Novakovic","Martin",
                "Immelt","Watson","Legere",
                "Scangos","Miller","McAdam",
                "Kent","Read","Rometty",
                "Ricci","Miller","Narayen",
                "Hewson","Auerbach","Lance",
                "Anderson","Muncrief","Casper",
                "Clarke","Farrell","Strangfeld",
                "Allen","Sheehan","Gonzalez",
                "Nadal","Kibsgaard","Wasson",
                "Smith","Moghadam","Chambers",
                "McGregor","Schaeffer","Dickerson",
                "Molinaroli","Holliday","Woertz",
                "White","Rutledge","Murphy",
                "Rosenfeld","Johnson","Barra",
                "Finnegan","Weiner","Flanagan",
                "Garland","Walker","Oberhelman",
                "Bertolini","Anstice","Freda",
                "Fields","Bush","Richels",
                "Flatley","Hemsley","Templeton",
                "Sorenson","Prokopanko","Goff",
                "Delpani","Simon","Koraleski",
                "Kramer","Alber","Parker",
                "Lawler","Craighead","Moynihan",
                "Kandarian","Corbat","Goldner",
                "Svane","Cordani","Hess",
                "Glaser","Thulin","Niblock",
                "Smith","Berns","Holmes",
                "Hooley","Donahoe","Bradway",
                "Sullivan","Thiry","Bunch",
                "Burke","Willett","Kleinfeld",
                "DeWalt","Swedish","Heminger",
                "Banga","Fetter","Longhi",
                "Kullman","Wiseman","Cook",
                "Wilson","Wilkinson","Joly",
                "Paz","Cooper","Roth",
                "Fettig","Washkewicz","Parkinson",
                "Lutnick","Taiclet","Simms",
                "Lundgren","Volker","Sheffield",
                "Lundgren","Crane",
                ]


#%%

def GetItems(InputList,IndexList):
    
    Out = []
    
    for Item in IndexList:
        Out.append(InputList[Item])
    
    return Out

GetItems(CEOs,[1,3,15])

#%%

def mean(Data):
    
    n = len(Data)
    
    Ans = 0.0
    for x in Data:
        Ans += x
    
    Ans /= n
    return Ans
 
#%%
   
def sd(Data):
    
    Xbar = mean(Data)
    n = len(Data)
    
    Ans = 0.0
    for x in Data:
        Ans += (x-Xbar)**2
    
    Ans /= (n-1)
    Ans = Ans**0.5
    
    return Ans
#%%

range(10)
range(len(CEOs))
range(50,len(CEOs))

#%%

def cor(X,Y):
    
    Xbar = mean(X)
    Ybar = mean(Y)
    sdX = sd(X)
    sdY = sd(Y)
    
    Cov = 0.0
    for i in range(len(X)):
        Cov += (X[i]-Xbar)*(Y[i]-Ybar)
    
    Cov /= (len(X)-1)
    
    Ans = Cov/(sdX*sdY)
    return Ans
    
#%%
# map(function,list)   
  
map(len,CEOFirstNames)

cor(map(len,CEOFirstNames),map(len,CEOLastNames))    
        
#%%
"""
# The if statement loop in Python 2.7:

 if logical expression:
    code block
 elif logical expression:                # Optional
    code block
 else:
    code block                          # Optional

# In Excel
# =if(logical expression, value if true, value if false)          

""" 
#%%
# The 200 highest paid CEOs in 2014, in order, highest to lowest.
# Source: http://www.equilar.com/publications/51-200-highest-paid-CEO-rankings-2015.html

CEOs = ["David M. Zaslav","Michael T. Fries","Mario J. Gabelli",
        "Satya Nadella","Nicholas Woodman","Gregory B. Maffei",
        "Lawrence J. Ellison","Steven M. Mollenkopf","David T. Hamamoto",
        "Leslie Moonves","Philippe P. Dauman","Robert A. Iger",
        "Joseph W. Brown Jr.","Marissa A. Mayer","Leonard S. Schleifer",
        "Joshua W. Sapan","Marc Benioff","Jeffrey M. Leiden",
        "Herve Hoppenot","Jeffrey L. Bewkes","Gary W. Loveman",
        "Eric J. Foss","Zachary Nelson","Martine Rothblatt",
        "William J. McMorrow","W. Nicholas Howley","Steve Ells",
        "Howard M. Lorber","Rex W. Tillerson","Brian C. Cornell",
        "Montgomery F. Moran","James Dimon","Jonathan Oringer",
        "Paul M. Rady","Brian L. Roberts","Craig A. Leavitt",
        "Lamberto Andreotti","Ari Bousbib","Ronald N. Tutor",
        "Stephen A. Wynn","Thomas B. Barker","Stephen P. MacMillan",
        "Wayne T. Smith","Larry J. Merlo","Robert J. Hugin",
        "Michael J. Saylor","John D. Wren","Brian Harris",
        "K. Rupert Murdoch","Laurence D. Fink","Leslie H. Wexner",
        "James L. Dolan","W. James McNerney, Jr","Carol Meyrowitz",
        "James P. Gorman","Peter Liguori","David M. Cote",
        "A. Jayson Adair","Brian D. Jellison","James M. Cracchiolo",
        "Kenneth I. Chenault","Lloyd C. Blankfein","Barry D. Zyskind",
        "Darren R. Huston","Howard Schultz","Kenneth C. Frazier",
        "Randall L. Stephenson","Leonard Bell","Peter M. Carlino",
        "Alex Gorsky","David J. Lesar","Margaret C. Whitman",
        "Richard D. Fairbank","Jay S. Fishman","Andrew N. Liveris",
        "Alan G. Lafley","William R. Berkley","John G. Stumpf",
        "Michael F. Neidorff","Paul C. Saville","Indra K. Nooyi",
        "C. Douglas McMillon","Phebe N. Novakovic","John C. Martin",
        "Jeffrey R. Immelt","John S. Watson","John J. Legere",
        "George A. Scangos","Alan B. Miller","Lowell C. McAdam",
        "Muhtar Kent","Ian C. Read","Virginia M. Rometty",
        "Paul A. Ricci","Stuart A. Miller","Shantanu Narayen",
        "Marillyn A. Hewson","Alan H. Auerbach","Ryan M. Lance",
        "Richard H. Anderson","Richard E. Muncrief","Marc N. Casper",
        "Ronald F. Clarke","Thomas F. Farrell, II","John R. Strangfeld",
        "Samuel R. Allen","Kevin M. Sheehan","Richard A. Gonzalez",
        "Miles S. Nadal","Paal Kibsgaard","Gregory D. Wasson",
        "Brad D. Smith","Hamid R. Moghadam","John T. Chambers",
        "Scott A. McGregor","Dave Schaeffer","Gary E. Dickerson",
        "Alex A. Molinaroli","Marc Holliday","Patricia A. Woertz",
        "Miles D. White","Thomas M. Rutledge","Glenn K. Murphy",
        "Irene B. Rosenfeld","Gregory E. Johnson","Mary T. Barra",
        "John D. Finnegan","Jeffrey Weiner","Martin L. Flanagan",
        "Greg C. Garland","Robert A. Walker","Douglas R. Oberhelman",
        "Mark T. Bertolini","Martin B. Anstice","Fabrizio Freda",
        "Mark Fields","Wesley G. Bush","John Richels",
        "Jay T. Flatley","Stephen J. Hemsley","Richard K. Templeton",
        "Arne M. Sorenson","James T. Prokopanko","Gregory J. Goff",
        "Lorenzo Delpani","David Simon","John J. Koraleski",
        "Richard J. Kramer","Laura J. Alber","Mark G. Parker",
        "Robert D. Lawler","Martin S. Craighead","Brian T. Moynihan",
        "Steven A. Kandarian","Michael L. Corbat","Brian D. Goldner",
        "Mikkel Svane","David M. Cordani","John B. Hess",
        "Daniel S. Glaser","Inge G. Thulin","Robert A. Niblock",
        "Frederick W. Smith, III","Paul L. Berns","Stephen P. Holmes",
        "Joseph L. Hooley","John J. Donahoe","Robert A. Bradway",
        "William P. Sullivan","Kent J. Thiry","Charles E. Bunch",
        "Michael S. Burke","Robert J. Willett","Klaus Kleinfeld",
        "David G. DeWalt","Joseph R. Swedish","Gary R. Heminger",
        "Ajay Banga","Trevor Fetter","Mario Longhi",
        "Ellen J. Kullman","Eric C. Wiseman","Ian M. Cook",
        "Thomas J. Wilson","G. Frederick Wilkinson","Hubert Joly",
        "George Paz","William A. Cooper","Michael I. Roth",
        "Jeff M. Fettig","Donald E. Washkewicz","Robert L. Parkinson, Jr.",
        "Howard W. Lutnick","James D. Taiclet, Jr.","Steven E. Simms",
        "Terry J. Lundgren","James J. Volker","Scott D. Sheffield",
        "John F. Lundgren","Christopher M. Crane"]
#%%

def GetItems(InputList,IndexList):
    
    Out = []
    
    for Item in IndexList:
        Out.append(InputList[Item])
    
    return Out

GetItems(CEOs,[1,3,15])

#%%

def GetListItems(InputList,IndexList):
    
    if not isinstance(InputList,list):
        print "Error: InputList is not a list! An empty list is returned."
        return []
    
    if not isinstance(IndexList,list):
        if isinstance(IndexList,int):
            tmp = IndexList
            IndexList = []
            IndexList.append(tmp)
        else:
            print "Error: IndexList is not a list! An empty list is returned."
            return []
 
    Out = []
    
    n = len(InputList)

    for Item in IndexList:
        if isinstance(Item,int):
            if Item >= -n and Item < n:
                Out.append(InputList[Item])
            else:
                print "Warning: Index out of range! The value None is returned."
                Out.append(None)
        else:
            print "Warning: Index is not an integer! The value None is returned."
            Out.append(None)
            

    return Out

GetListItems(CEOs,[1,3,15])

GetListItems(CEOs,"abc")

x = {}
x['a'] = 5
x['b'] = "abc"
GetListItems(x,[1,3,15])
GetListItems(CEOs,[1,3,200])
GetListItems(CEOs,[1,3,-10])
GetListItems(CEOs,[1,-201,-30])
GetListItems([],[1,3,15])
GetListItems(CEOs,15)
GetListItems(CEOs,[15])

#%%        

       
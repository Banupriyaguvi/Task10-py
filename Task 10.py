class User:
  def __init__(self, userld, password):
    self.userld = userld
    self.password = password
    self.loginStatus = "logged out"

  def verifyLogin(self, password):
    if password == self.password:
      self.loginStatus = "logged in"
      return True
    else:
      return False

  def getUser(self):
    return self.userld

class Customer(User):
  def __init__(self, userld, password, customerName, address, email, phoneno, creditcardInfo, shippingInfo):
    super().__init__(userld, password)
    self.customerName = customerName
    self.address = address
    self.email = email
    self.phoneno = phoneno
    self.creditcardInfo = creditcardInfo
    self.shippingInfo = shippingInfo

  def register(self):
    # Implementation for registering a customer
    pass

  def updateProfile(self):
    # Implementation for updating customer profile
    pass

class Administrator(User):
  def __init__(self, userld, password, adminName, departmentName):
    super().__init__(userld, password)
    self.adminName = adminName
    self.departmentName = departmentName

  def updateCatalog(self):
    # Implementation for updating catalog
    pass

  def getdepartment(self):
    return self.departmentName

class Product:
  def __init__(self, productid, name, description, price, imageFileName):
    self.productid = productid
    self.name = name
    self.description = description
    self.price = price
    self.imageFileName = imageFileName

  def displayProduct(self):
    # Implementation for displaying product information
    pass

  def getProductDetails(self):
    # Implementation for getting product details
    pass

class OrderDetail:
  def __init__(self, orderid, productid, quantity, unitCost):
    self.orderid = orderid
    self.productid = productid
    self.quantity = quantity
    self.unitCost = unitCost

  def calcPrice(self):
    self.subtotal = self.quantity * self.unitCost
    return self.subtotal

class Orders:
  def __init__(self, orderid, customerld, shippingid, dateCreated, dateShipped, status):
    self.orderid = orderid
    self.customerld = customerld
    self.shippingid = shippingid
    self.dateCreated = dateCreated
    self.dateShipped = dateShipped
    self.status = status

  def placeOrder(self):
    # Implementation for placing an order
    pass

class ShippingInfo:
  def __init__(self, shippingid, shippingType, shippingCost, shippingRegionld):
    self.shippingid = shippingid
    self.shippingType = shippingType
    self.shippingCost = shippingCost
    self.shippingRegionld = shippingRegionld

  def updateShippinginfo(self):
    # Implementation for updating shipping information
    pass

class Category:
  def __init__(self, categoryid, departmentid, categoryName, description):
    self.categoryid = categoryid
    self.departmentid = departmentid
    self.categoryName = categoryName
    self.description = description

  def getProductsInCategory(self):
    # Implementation for getting products in a category
    pass

class Department:
  def __init__(self, departmentid, name, description):
    self.departmentid = departmentid
    self.name = name
    self.description = description

  def getCategoryInDepartment(self):
    # Implementation for getting categories in a department
    pass

class ShoppingCart:
  def __init__(self, cartid):
    self.cartid = cartid
    # Maybe list or dictionary to hold items
    self.items = []

  def addCartItem(self, item):
    # Implementation for adding a cart item
    pass

  def deleteCartItem(self, item):
    # Implementation for deleting a cart item
    pass

  def updatequantity(self, item, quantity):
    # Implementation for updating the quantity of a cart item
    pass

  def viewCartDetails(self):
    # Implementation for viewing cart details
    pass

  def checkout(self):
    # Implementation for checking out
    pass
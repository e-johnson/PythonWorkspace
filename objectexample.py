class BankAccount: 
	type = 'Normal Account'
	def __init__(self, name): 
		#default variable unique to each object 
		self.userName = name
		self.balance = 2
	#Object Methods: 

	def showBalance(self): 
		print self.balance
		return 
	def withdrawMoney(self, amount): 
		self.balance = self.balance + amount; 
		return 
	def depositMoney(self, amount): 
		self.balance = self.balance + amount
		return 

class ExecutiveAccount(BankAccount): 
	#Overriden attribute
	type = 'Executive Account'

	#Extended functionality
	def requestCredit(self, amount): 
		self.balance += amount

executive = ExecutiveAccount('CEO')

print executive.userName; 
object1 = BankAccount("I'm 1"); 
object2 = BankAccount("Me 2");

#access object properties 
print object1.userName
print object2.userName


object1.depositMoney(5000)  
object2.depositMoney(200)


print object1.balance
print object2.balance

object1.showBalance()
object2.showBalance()

print object1.type
print object2.type
	

object1.discount_code = 'secret'

print object1.discount_code                                                                                                                           

del object1.discount_code
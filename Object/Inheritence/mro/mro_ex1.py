
class A:
	def rk(self):
		print(" In class A")
class B:
	def rk(self):
		print(" In class B")

# classes ordering
class C(A, B):
	def __init__(self):
		print("Constructor C")

r = C()

# it prints the lookup order

print(C.__mro__) # tuple type
print(C.mro()) # list type

# In The Name Of God
# ========================================
# [] File Name : fields.py
#
# [] Creation Date : 05-06-2015
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
__author__ = 'Parham Alvani'


class Fields:
    static_field = 0

    def __init__(self):
        self.non_static_field = 0


Fields.static_field = 10

f1 = Fields()
f1.static_field = 20
print("f1.static_field: " + str(f1.static_field))
f1.non_static_field = 10
print("f1.non_static_field: " + str(f1.non_static_field))

f2 = Fields()
print("f2.static_field: " + str(f2.static_field))
print("f2.non_static_field: " + str(f2.non_static_field))

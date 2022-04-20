import MarksheetBean
from MarksheetBean import *
import MarksheetDao
from MarksheetDao import *


def add():
    
    mb = MarksheetBean()

    mb.setRollNo(7)
    mb.setName("eegejksal")
    mb.setPhy(24)
    mb.setChem(33)
    mb.setMaths(23)

    md = MarksheetDao()
    md.add(mb)
    print(":ADD" )
    # print("{} {} {} {} {}".format(mb.getRollNo, mb.getName, mb.getPhy, mb.getChem, mb.getMaths))


def update():

    mb = MarksheetBean()

    mb.setName("asdeshu")
    mb.setRollNo(4)
    mb.setPhy(3)
    mb.setChem(32)
    mb.setMaths(32)
    # mb.setRollNo(2)

    md = MarksheetDao()
    md.update(mb)
    print("updated")

def delete():
    mb =MarksheetBean()

    mb.setRollNo(2)
    md = MarksheetDao()
    md.delete(mb)
    print("deleted")

# def select():
#     mb =MarksheetBean()
#
#     mb.setRollNo(2)
#     md= MarksheetDao()
#     md.select(mb)
#     print("Select")


def search_all():
    md = MarksheetDao()
    md.search_all()

def merit_list():
    md = MarksheetDao()
    md.merit_list()

def search_single():
    mb = MarksheetBean()
    mb.setRollNo(4)
    md = MarksheetDao()
    md.search_single(mb)



# add()
#update()
# delete()
# select()
# search_all()
# merit_list()
search_single()
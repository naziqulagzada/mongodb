from pymongo import MongoClient

from main import report_collection

students = [{
    "id": "1",
    "name": "nazia",
    "grade": "12"
},{
    "id": "2",
    "name": "zahra",
    "grade": "12"
},{
    "id": "3",
    "name": "ali",
    "grade": "11"
},{
    "id": "4",
    "name": "reza",
    "grade": "10"
}]

teachers = [{
    "name": "ali",
    "class": "12"
},{
    "name": "soghra",
    "class": "11"
}]



client = MongoClient()
db = client.student_list

students_collection = db.students
teachers_collection = db.teachers
info_collection = db.info
updated_collection = db.updated

def store_data():
    students_collection.insert_many(students)
    teachers_collection.insert_many(teachers)

def read_data():
    nazia = students_collection.find_one({"name": "nazia"})
    ali = teachers_collection.find_one({"name": "ali"})


    student_info = info_collection.insert_one({
        "student": nazia,
        "teacher_of_student": ali
    })

def update_and_delete():
    ahmad = students_collection.find_one_and_update({"name": "ali"},
                                                   {"$set": {"name": "ahmad"}},
                                                    return_document=True)
    reza = students_collection.delete_one({"name": "reza"})


    report = updated_collection.insert_one({
        "updated": ahmad,
        "deleted": reza.deleted_count
    })


if __name__ == "__main__":
    # store_data()
    # read_data()
    update_and_delete()
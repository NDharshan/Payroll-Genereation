import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate(r"D:\College\ashrama-website-master\ashrama-website-master\salary-management.json")
firebase_admin.initialize_app(cred)

# Initialize Firestore database
db = firestore.client()

def create_document(collection, document_data):
    db = firestore.client()
    doc_ref = db.collection(collection).document()
    doc_ref.set(document_data)
    print('Document created with ID:', doc_ref.id)

db.collection('employees').add({
    "name": "Kamala Srinivas",
    "mail": "kamala@gmail.com"
})
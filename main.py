import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# --------------------------------------------------------
# Prepare for the connection
# --------------------------------------------------------
# Use a service account.
cred = credentials.Certificate('serviceAccount.json')
app = firebase_admin.initialize_app(cred)

db = firestore.client()

# --------------------------------------------------------
# Prepare data to be imported
# --------------------------------------------------------
new_documents = [
    {
        "name": "Capmu",
        "age": 100
    },
    {
        "name": "Top",
        "age": 25
    }
]

# --------------------------------------------------------
# Import the documents to the Firestore
# --------------------------------------------------------
for new_document in new_documents:
    doc_ref = db.collection(u'users').document(new_document['name'])
    doc_ref.set(new_document)

# --------------------------------------------------------
# Read records from the Firestore
# --------------------------------------------------------
users_ref = db.collection(u'users')
docs = users_ref.stream()

for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')

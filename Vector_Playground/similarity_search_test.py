import chromadb
import os
from sentence_transformers import SentenceTransformer

'''
This document is intended to provide a means of practice and understanding vector databases and similarity searches performed on them.  
'''


# embedding function/model 
embedding_model = SentenceTransformer('all-MiniLM-L6-v2') # paper on SentenceTransformer: https://arxiv.org/abs/1908.10084

# initializes a directory for the chroma database
client = chromadb.PersistentClient(path="my_chroma_db")

# creating a chroma collection
collection = client.get_or_create_collection(name="collection4")


# loads, parses and splits data into chunks.
def getDataFromText(data_file: str) -> list:
    
    try:

        with open(data_file, 'r', encoding="utf-8") as file:
            # parse file. organize contents into list. 
            content: str = file.read()
            divided_content: list = content.split("\n\n\n") # what would be a better way to split data?
            return divided_content
    
    except Exception as e:
    
        print("Read data from text failed : ", e)

# Function to insert embeddings/vectors into db
def addVectorDataToDb(data_file: str) -> None:
    
    # DB Columns
    embeddings: list = []
    metadatas: list = []
    documents: list = []
    ids: list = []
    divided_content: list = getDataFromText(data_file)
    
    try:
        
        # Iterate through data chunks
        for index, data in enumerate(divided_content):
            # Add chunk data to function lists. 
            embeddings.append(embedding_model.encode(data).tolist())
            metadatas.append({"Chapter": str(index+1)}) # whats this
            documents.append(data)
            ids.append(str(index+1))
        
        # Insert collected data into db.
        collection.add(
            embeddings=embeddings,
            metadatas=metadatas,
            documents=documents,
            ids=ids
        )
        
        print("Data added to collection")
    
    except Exception as e:
        
        print("Add data to db failed : ", e)

# Function to Search data by vector
def searchDataByVector(query: str):
    try:
        
        # Convert query to vector
        query_vector = embedding_model.encode(query).tolist()
        
        # Query vector search
        res = collection.query(
            query_embeddings=[query_vector],
            n_results=1,
            include=['distances','embeddings', 'documents', 'metadatas'],
        )
        
        # Original Query
        print("Query", "\n--------------")
        print(query)

        # Resulting documents
        print("Result", "\n--------------")
        print(f"{res['documents'][0][0]}")
        
        # Resulting vectors
        print("Vector", "\n--------------")
        print(f"{res['embeddings'][0][0]}")
        
        #print("Complete Response","\n-------------------------")
        #print(res)

    except Exception as e:
        print("Vector search failed : ", e)


if __name__ == "__main__":

    # Choose a directory that isn't too dense - this takes some time.     
    root_dir = '/home/fer/AICodeGenerator/KMeansCluster_Test_App'#'/home/fer/Projects/edurange-flask'

    # Traverse directory, embed and insert vectors. 
    docs = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for file in filenames:
            try:
                full_path = os.path.join(dirpath, file)
                addVectorDataToDb(full_path)
            except Exception as e:
                pass

    query = "What is an error?"
    searchDataByVector(query=query)
from deepseek import DeepSeek, Document
import sys

def index_initial_documents(ds):
    docs = [
        Document(id="doc1", text="The Communist Revolution in Russia was a pivotal event in history, sparked by widespread discontent and political turmoil."),
        Document(id="doc2", text="The French Revolution reshaped European society with its radical ideas about liberty, equality, and fraternity."),
        Document(id="doc3", text="World War I was a major conflict triggered by the assassination of Archduke Franz Ferdinand, leading to widespread geopolitical changes.")
    ]
    ds.index_documents(docs)

def add_new_document(ds, doc_id, text):
    new_doc = Document(id=doc_id, text=text)
    ds.index_documents([new_doc])

def search_query(ds, query):
    try:
        results = ds.search(query)
        return results
    except Exception as e:
        print("Error during search:", e)
        return []

def format_results(results):
    formatted = ""
    for result in results:
        formatted += "Document ID: {}\nScore: {}\nText: {}\n\n".format(result.id, result.score, result.text)
    return formatted

def main():
    ds = DeepSeek(model_version="r1")
    index_initial_documents(ds)
    user_input = input("Enter your search query: ")
    results = search_query(ds, user_input)
    if not results:
        print("No results found.")
    else:
        print("Search Results:\n")
        print(format_results(results))
    add_more = input("Would you like to add a new document? (yes/no): ").strip().lower()
    if add_more == "yes":
        new_id = input("Enter new document ID: ")
        new_text = input("Enter new document text: ")
        add_new_document(ds, new_id, new_text)
        query2 = input("Enter a search query to verify new document indexing: ")
        new_results = search_query(ds, query2)
        print("Updated Search Results:\n")
        print(format_results(new_results))
    else:
        print("Exiting.")
    sys.exit(0)

if __name__ == "__main__":
    main()

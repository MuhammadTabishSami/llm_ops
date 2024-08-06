import os
import sys
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from logger import logger
from exception import CustomException

#project_root='F:llm_ops'

def load_documents(file_path: str):
    """
    Load Document from a PDF file.

    Args:
        file_path(str): Path to the PDF file

    Returns:
        list: List of documents
    
    """
    try:
        logger.info('Loading Documents')
        loader=PyPDFLoader(file_path)
        documents=loader.load()
        logger.info('Documents Loaded Successfully from %s',file_path)
        return documents
    
    except Exception as e:
        raise CustomException(e,sys)
    
def split_documents(documents: list, chunk_size: int = 2000, chunk_overlap: int = 400):
    """
    Split documents into smaller chunks.

    Args:
        documents (list): List of documents.
        chunk_size (int): Size of each chunk.
        chunk_overlap (int): Overlap between chunks.

    Returns:
        list: List of text chunks.
    """
    try:
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        texts = text_splitter.split
    except Exception as e:
        raise CustomException(e,sys)
    
if __name__ == "__main__":
    file_path = os.path.join("data", "sample.pdf")
    documents = load_documents(file_path)
    texts = split_documents(documents)






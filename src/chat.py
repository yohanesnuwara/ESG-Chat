import numpy as np
import pandas as pd
import tiktoken
import openai
import os
from utils import *

def chat_ESG(key_api, query, show_prompt=False):

    # OpenAI Key
    openai.api_key = key_api

    COMPLETIONS_MODEL = "text-davinci-003"
    EMBEDDING_MODEL = "text-embedding-ada-002"

    # Paths to report tabular and embedding 
    report = "https://github.com/yohanesnuwara/ESG-Chat/blob/main/model/ESG_Report_Database.csv?raw=true"
    embed = "https://github.com/yohanesnuwara/ESG-Chat/blob/main/model/ESG_Report_Embedding.csv?raw=true"

    # Read report tabular and embedding
    embed_df = pd.read_csv(embed)
    embed_df.rename(columns={'Unnamed: 0':'Article_ID'}, inplace=True)

    df = pd.read_csv(report)
    df = df.set_index("Article_ID")

    # Convert embedding dataframe to dictionary
    embed = load_embeddings(embed_df)

    return answer_query_with_context(query, df, embed, show_prompt)
    #return df

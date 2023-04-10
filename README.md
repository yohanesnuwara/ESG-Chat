# ESG-Chat

<img src="https://user-images.githubusercontent.com/51282928/230783659-fbe9b43f-01d2-48fd-84d5-eefd093fb628.png" alt= "esg-chat" width="700">

ESG-Chat is a programmatic chatbot that can answer queries related to ESG (environmental, social, and governance) or sustainability topics. It's like ChatGPT for ESG. For corporates, being engaged in sustainability is important. We can use this chatbot to give us advice and strategy on how to improve sustainability. We can think ESG-Chat like an expert or consultant in sustainability whom we can seek for advice, but now AI does it. 

### Method: Text embedding similarity search using GPT-3

In this method, 15 sustainability reports from various companies (Starbucks, Goldman Sachs, Nestle, Toyota, Xerox, many more) were extracted and decomposed into 5-10 sentences. Then, embedding was calculated using OpenAI's [text-embedding-ada-002](https://openai.com/blog/new-and-improved-embedding-model) model. An embedding is a vector of numbers that helps us understand how semantically similar or different the texts are. The closer two embeddings are to each other, the more similar are their contents. 

Why use this method? Naive GPT models like ChatGPT sometimes can hallucinate because we don't give **context** to it. Because sustainability is core to business, hallucinating is something that we must avoid if we want to implement chat bot for this purpose. 

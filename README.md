# ESG-Chat

<img src="https://user-images.githubusercontent.com/51282928/230783659-fbe9b43f-01d2-48fd-84d5-eefd093fb628.png" alt= "esg-chat" width="700">

ESG-Chat is a programmatic chatbot that can answer queries related to ESG (environmental, social, and governance) or sustainability topics. It's like ChatGPT for ESG. For corporates, being engaged in sustainability is important. We can use this chatbot to give us advice and strategy on how to improve sustainability. We can think ESG-Chat like an expert or consultant in sustainability whom we can seek for advice, but now AI does it. 

### Method: Text embedding similarity search using GPT-3

In this method, sustainability reports from various companies (Starbucks, Goldman Sachs, Nestle, Toyota, Xerox, many more) were extracted and decomposed into multiple parts. Then, embedding was calculated using OpenAI's [text-embedding-ada-002](https://openai.com/blog/new-and-improved-embedding-model) model. An embedding is a vector of numbers that helps us understand how semantically similar or different the texts are. The closer two embeddings are to each other, the more similar are their contents. When the users give their prompt, it will compute the query embedding of the question and use it to find the most similar document sections. These statements with high similarity are used as a context for the [text-davinci-003](https://platform.openai.com/docs/models/gpt-3) GPT model to generate answer. 

Why use this method? Naive GPT models like ChatGPT sometimes can hallucinate because we don't give **context** to it. Because sustainability is core to business, hallucinating is something that we must avoid if we want to implement chat bot for this purpose. 

### Required libraries
* openai 0.27.4
* tiktoken 0.3.3

### How to use ESG-Chat

Install the required libraries and clone this repository. The syntax is very simple. Provide your OpenAI API Key (if you don't have, you need to sign up first and get it [here](https://platform.openai.com/account/api-keys)), create your prompt, and run the following

```
key_api = # Your API key
query = "How to reduce waste? Give long and detail answer."

chat_ESG(key_api, query)
```

Here is sample response from ESG-Chat:

```
Reducing waste can be done in a number of ways, from eliminating paper-based client communications and fully leveraging digital media for internal communications, to reducing reliance on printed promotional material and eliminating single-use plastics such as plastic bottles and straws. Additionally, reducing food waste in cafeterias and micro-market cafes is important, as is encouraging suppliers to set up water and waste reduction targets. Carrefour has set a target to reduce its food waste by 50% by 2025 compared to 2016, and this can be achieved by implementing measures such as crop growing and harvesting, sorting, packaging and transport, quality control, distribution and consumption. Finally, reducing waste, increasing recyclability and circularity, and managing recovered materials effectively are critical for society, and consumer goods companies can play an important role in this.
```

Here it mentions Carrefour as example which indicates that the ESG-Chat response is factual. 

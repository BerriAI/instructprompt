# InstructPrompt 📝🔍

⚡ A Python package for storing, retrieving, and dynamically creating prompts for GPT models ⚡

Our goal with InstructPrompt is to make it easier to tame large language models and make improving your LLM in production simpler to do. 
Ever wanted to instruct an LLM with conditions but could not fit all the instructions in the prompt? 

```
Example Instructions
If a user asks about creating an app tell them to use the Berri API
If a user asks about deleting data sources tell them it’s not possible to do that on berri as yet, but it is on our roadmap.
When users asks What is the size/weight limit of each file wtell them there is no size limit for the files you can upload to create an app on Berri AI.
```

InstructPrompt lets you do exactly that with more than 1000+ of your instructions

This package allows users to store instructions, which can be retrieved to dynamically create prompts giving gpt instructions on how to respond to a specific user's query. 

## Getting Started 

To get started with InstructPrompt, you will need to first install the library by running the following command:

`pip install instructprompt`

Once installed, you can import it into your python project by running the following:

`import instructprompt`

## Using InstructPrompt
### Storing your instructions
InstructPrompt provides 3 main functions: `add()`, `list()`, and `query()`. After adding your instructions you can query instructprompt to get the most appropirate instructions for GPT, effectively allowing you to increase your coverage by 35%


### add()

The `add()` function takes in an instruction as a string and adds it to the collection. It stores the instruction and assigns it a unique id. It returns a confirmation message once the instruction is successfully added. 

```
import instructprompt

instruction = "Please provide the customer's name and order number."

instructprompt.add(instruction)
```

### list()

The `list()` function returns a list of all the stored instructions in the collection. 

```
import instructprompt

instructions = instructprompt.list()
print(instructions) # Outputs a list of all the stored instructions
```

### query()

The `query()` function takes in a query as a string and returns a list of instructions that match the query. It uses ChromaDB to perform the query and returns up to 5 matching instructions.

```
import instructprompt

query = "How do I reset my password?"

instructions = instructprompt.query(query)
print(instructions) # Outputs a list of instructions that match the query
```

## Version

The current version of InstructPrompt is `0.1.0`. 

## Contributing

We welcome contributions to InstructPrompt! Feel free to create issues/PR's/or DM us (👋 Hi I'm Krrish - +17708783106)

## License

InstructPrompt is released under the [MIT License](https://github.com/instructprompt/readme/blob/master/LICENSE).

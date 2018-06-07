###
These files are made available to you on an as-is and restricted basis, and may only be redistributed or sold to any third party as expressly indicated in the Terms of Use for Seed Vault.
###
Seed Vault Code (c) Botanic Technologies, Inc. Used under license.
###

## why .Flow?
- to design and build how a conversation to be between user and bot, is built using node and path as building blocks, where a node represent either a bot message or user input, path represent a possible way from current node to a future node. 


## why should one care about it?
- any one who wishes to come up with a bot, which has some task in it, knows how to execute it in a conversation model, that person can utilize this in representing the conversation in a flow.


## what is a task? 
- task is something like a purpose, it can be related to anything, probably some humorous conversation, or some logical steps to do some task (for eg., transfer money from an account to another account), or some tutor (for eg., a language tutor) etc, an example is given at the end, please have a look for better understanding


## Who builds it?
- any one who is interested in building a bot with some purpose in it, such person can be called a bot developer


## Does a bot developer need to be technically qualified?
- not really, it completely depends on the kind of bot the bot developer wanted to create


## How to build one?
- can be built using author tool, a web client which has beautiful UX required for building a bot
- since it is in json, can write by hand directly in json without any other tool, after writing just one need to validate if it is a valid json or not


## How is it represented?
- is represented in the form of json


## Who consumes it?
- a flow engine, which usually can be built using any language of choice, but as of now Botanic has chosen ChatScript and PHP in writing it. ChatScipt is a rule-based engine, where rules are created by human writers in program scripts through a process called dialog flow scripting


## what does it give?
- a response that need to be shown to the end user, which is set by the bot developer while creating the flow


## what does it expect to continue further?
- user input, once it is received, it will processes it, after understanding the user input, it decides what need to be done next


# Documentation

## Explanation on Flow :
- FlowDocumentation.pdf placed under "documentation\FlowDocumentation" folder. Please go through this for better understanding on FLOW

## Flow Json Schema :
- Flow-schema.json placed under "documentation\FlowJsonSchema" folder. Please go through this for understanding the json schema for FLOW

- Flow-schema-defs.json is having definitions

- FlowJsonSchemaValidator.py is the python script written to validate a given json across json schema

- flow-json-eg-1.json is having sample flow

## an example of a flow
- lets us create a travel flow
- travel can be of international or domestic
- we need to take source and destination
- we need take passenger details
- we need to take payment and book the ticket

## an example of flow in json

    {
      "id": 265,
      "name": "flow265",
      "nodes": [
        {
          "id": "root-node",
          "name": "flow265",
          "type": "root",
          "connections": [
            {
              "default": "4f96"
            }
          ]
        },
        {
          "type": "message",
          "subType": "text",
          "name": "",
          "msg": [
            "Welcome to XYZ travels"
          ],
          "connections": [
            {
              "name": "",
              "if": {
                "context": "userInput",
                "op": "pattern",
                "value": [
                  "*"
                ],
                "then": "3ee3"
              },
              "isButton": false
            },
            {
              "default": "end"
            }
          ],
          "id": "4f96"
        },
        {
          "type": "message",
          "subType": "text",
          "name": "",
          "msg": [
            "Is your travel International or Domestic?"
          ],
          "connections": [
            {
              "name": "",
              "if": {
                "context": "userInput",
                "op": "pattern",
                "value": [
                  "Doemstic"
                ],
                "then": "f15f"
              },
              "isButton": false
            },
            {
              "name": "",
              "if": {
                "context": "userInput",
                "op": "pattern",
                "value": [
                  "International"
                ],
                "then": "0897"
              },
              "isButton": false
            },
            {
              "default": "end"
            }
          ],
          "id": "3ee3"
        },
        {
          "type": "flowId",
          "name": "",
          "msg": [],
          "flowId": 266,
          "connections": [
            {
              "default": "end"
            }
          ],
          "id": "f15f"
        },
        {
          "type": "flowId",
          "name": "",
          "msg": [],
          "flowId": 266,
          "connections": [
            {
              "default": "end"
            }
          ],
          "id": "0897"
        }
      ]
    }

    {
      "id": 266,
      "name": "flow266",
      "nodes": [
        {
          "id": "root-node",
          "name": "flow266",
          "type": "root",
          "connections": [
            {
              "default": "99ec"
            }
          ]
        },
        {
          "type": "message",
          "subType": "text",
          "name": "",
          "msg": [
            "where do you want to go"
          ],
          "connections": [
            {
              "name": "",
              "if": {
                "context": "userInput",
                "op": "pattern",
                "value": [
                  "~city"
                ],
                "then": "7e67"
              },
              "isButton": false
            },
            {
              "default": "end"
            }
          ],
          "id": "99ec"
        },
        {
          "type": "message",
          "subType": "text",
          "name": "",
          "msg": [
            "from where do you want to start?"
          ],
          "connections": [
            {
              "name": "",
              "if": {
                "context": "userInput",
                "op": "pattern",
                "value": [
                  "~city"
                ],
                "then": "08d8"
              },
              "isButton": false
            },
            {
              "default": "end"
            }
          ],
          "id": "7e67"
        },
        {
          "type": "flowId",
          "name": "",
          "msg": [],
          "flowId": 267,
          "connections": [
            {
              "default": "end"
            }
          ],
          "id": "08d8"
        }
      ]
    }

    {
      "id": 267,
      "name": "flow267",
      "nodes": [
        {
          "id": "root-node",
          "name": "flow267",
          "type": "root",
          "connections": [
            {
              "default": "8133"
            }
          ]
        },
        {
          "type": "message",
          "subType": "text",
          "name": "",
          "msg": [
            "What is your name?"
          ],
          "connections": [
            {
              "name": "",
              "if": {
                "context": "userInput",
                "op": "pattern",
                "value": [
                  "*"
                ],
                "then": "c36b"
              },
              "isButton": false
            },
            {
              "default": "end"
            }
          ],
          "id": "8133"
        },
        {
          "type": "message",
          "subType": "text",
          "name": "",
          "msg": [
            "Gender?"
          ],
          "connections": [
            {
              "name": "",
              "if": {
                "context": "userInput",
                "op": "pattern",
                "value": [
                  "*"
                ],
                "then": "9fd0"
              },
              "isButton": false
            },
            {
              "default": "end"
            }
          ],
          "id": "c36b"
        },
        {
          "type": "message",
          "subType": "text",
          "name": "",
          "msg": [
            "Age?"
          ],
          "connections": [
            {
              "name": "",
              "if": {
                "context": "userInput",
                "op": "pattern",
                "value": [
                  "~number"
                ],
                "then": "c812"
              },
              "isButton": false
            },
            {
              "default": "end"
            }
          ],
          "id": "9fd0"
        },
        {
          "type": "flowId",
          "name": "",
          "msg": [],
          "flowId": 268,
          "connections": [
            {
              "default": "end"
            }
          ],
          "id": "c812"
        }
      ]
    }

    {
      "id": 268,
      "name": "flow268",
      "nodes": [
        {
          "id": "root-node",
          "name": "flow268",
          "type": "root",
          "connections": [
            {
              "default": "7ffe"
            }
          ]
        },
        {
          "type": "message",
          "subType": "text",
          "name": "",
          "msg": [
            "please pay the amount"
          ],
          "connections": [
            {
              "name": "",
              "if": {
                "context": "userInput",
                "op": "pattern",
                "value": [
                  "*"
                ],
                "then": "9542"
              },
              "isButton": false
            },
            {
              "default": "end"
            }
          ],
          "id": "7ffe"
        },
        {
          "type": "message",
          "subType": "text",
          "name": "",
          "msg": [
            "ticket booked, itenary is mailed to you, have a happy and safe journey"
          ],
          "connections": [
            {
              "default": "end"
            }
          ],
          "id": "9542"
        }
      ]
    }
# Documentation

This document is related to an old version of .Flow protocol. Please visit [.FLow](https://github.com/SeedVault/flow) repository in order to get the latest version.

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

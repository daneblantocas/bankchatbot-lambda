# BankOne 24/7 Support Chatbot

A proof-of-concept banking support chatbot built using a modular, serverless architecture on AWS.

## Architecture

- **Frontend:** Static HTML/JavaScript hosted on AWS S3
- **Backend:** AWS Lambda functions (Function-as-a-Service)
- **Database:** Amazon DynamoDB (single persistence store)
- **API:** Amazon API Gateway (HTTP API)
- **CI/CD:** GitHub Actions (auto-deploys on push to main branch)

## User Journeys Covered

1. **Check Account Balance** — Customer enters their account ID and retrieves their current balance from DynamoDB
2. **Block a Card** — Customer reports a lost or stolen card, Lambda updates the card status to BLOCKED in DynamoDB
3. **FAQ** — Customer selects a common question and receives an instant answer from the chatbot

## Backend Modules

| Function | Description |
|----------|-------------|
| `getAccountBalance` | Retrieves customer name and balance from DynamoDB |
| `blockCard` | Updates card status to BLOCKED in DynamoDB |
| `getFAQ` | Returns answers to common banking questions |

## API Routes

| Method | Route | Function |
|--------|-------|----------|
| GET | `/balance?accountId=ACC001` | getAccountBalance |
| POST | `/blockcard` | blockCard |
| GET | `/faq?question=reset_pin` | getFAQ |

## Persistence

All data is stored in a single **DynamoDB** table called `ChatBot` using a composite key pattern (PK, SK). Account records are stored with the format `ACCOUNT#<id>` and include name, balance, and card status.

## CI/CD

Backend functions are stored in GitHub and automatically deployed to AWS Lambda via **GitHub Actions** on every push to the `main` branch. The workflow zips each Lambda function and updates the function code using the AWS CLI.

## How to Run

1. Open the frontend: [BankOne Chatbot](http://bankchatbot-frontend-dane.s3-website-us-east-1.amazonaws.com/)
2. Choose an option from the chatbot menu
3. Follow the prompts to check your balance, block a card, or get FAQ answers

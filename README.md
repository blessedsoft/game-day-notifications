# NBA Game Day Notification System

## **Overview**
An alert system that sends real-time NBA game scores to subscribers via SMS/Email using **Amazon SNS**, **AWS Lambda**, **Python**, **EventBridge**, and the **NBA API**.

## **Features**
- Fetches live NBA scores.
- Sends score updates to subscribers via SMS/Email.
- Automates updates using Amazon EventBridge.
- Secure with least privilege IAM policies.

## **Prerequisites**
- Account at [sportsdata.io](https://sportsdata.io/).
- AWS account and basic Python knowledge.

## **Technical Architecture**
![image](https://github.com/user-attachments/assets/fb965771-eba0-4591-91cf-c294eecae55b)


## **Technologies**
- **Cloud Provider**: AWS
- **Services**: SNS, Lambda, EventBridge
- **API**: NBA Game API (SportsData.io)
- **Language**: Python 3.x


## **Project Structure**
```bash
game-day-notifications/
├── src/
│   ├── gd_notifications.py          # Main Lambda function code
├── policies/
│   ├── gb_sns_policy.json           # SNS publishing permissions
│   ├── gd_eventbridge_policy.json   # EventBridge to Lambda permissions
│   └── gd_lambda_policy.json        # Lambda execution role permissions
├── .gitignore
└── README.md                        # Project documentation
```



### **Clone the Repository**
```bash
git clone https://github.com/blessedsoft/game-day-notifications.git
cd game-day-notifications
```

##**Setup Instructions**

**Create an SNS Topic**
-In AWS, navigate to SNS and create a Standard topic.
-Name the topic (e.g., gd_topic) and save the ARN.

**Add Subscriptions**
-In SNS, click the topic and create a subscription.
-Choose Email or SMS protocol, and provide the required contact details.

**Create SNS Publish Policy**
-In IAM, create a policy from gd_sns_policy.json.
-Replace REGION and ACCOUNT_ID with your values.

**Create IAM Role for Lambda**
-In IAM, create a role for Lambda, attaching the SNS Publish and Lambda Basic Execution policies.
-Save the role ARN.

**Deploy Lambda Function**
-In Lambda, create a new function using Python 3.x.
-Attach the IAM role, and paste the code from src/gd_notifications.py.
-Add environment variables (NBA_API_KEY, SNS_TOPIC_ARN).
-Create the function.

**Set Up Automation**
-In EventBridge, create a rule to trigger the Lambda function on a schedule (e.g., hourly) using cron

**Test the System**
-Create a test event in Lambda.
-Run the function and check CloudWatch for logs.
-Ensure notifications are sent, check your email


**What We Learned**
-Design of a notification system with AWS SNS and Lambda.
-Securing services with least privilege policies.
-Automating workflows with EventBridge.
-Integrating external APIs.

**Future Enhancements**
-Add NFL score alerts.
-Store user preferences in DynamoDB for personalized alerts.
-Build a web UI.






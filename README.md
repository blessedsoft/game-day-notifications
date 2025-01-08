# NBA Game Day Notification System

## **Overview**
An alert system that sends real-time NBA game scores to subscribers via SMS/Email using **Amazon SNS**, **AWS Lambda**, **Python**, **EventBridge**, and the **NBA API**.

## **Features**
1. Fetches live NBA scores.
2. Sends score updates to subscribers via SMS/Email.
3. Automate updates using Amazon EventBridge.
4. Secure with least privilege IAM policies.

## **Prerequisites**
1. Account at [sportsdata.io](https://sportsdata.io/).
2, AWS account and basic Python knowledge.

## **Technical Architecture**
![image](https://github.com/user-attachments/assets/fb965771-eba0-4591-91cf-c294eecae55b)


## **Technologies**
1. **Cloud Provider**: AWS
2. **Services**: SNS, Lambda, EventBridge
3. **API**: NBA Game API (SportsData.io)
4. *Language**: Python 3.x


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

**Setup Instructions**

**Create an SNS Topic**
1. In AWS, navigate to SNS and create a Standard topic.
2. Name the topic (e.g., gd_topic) and save the ARN.

**Add Subscriptions**
1. In SNS, click the topic and create a subscription.
2. Choose Email or SMS protocol, and provide the required contact details.

**Create SNS Publish Policy**
1. In IAM, create a policy from gd_sns_policy.json.
2. Replace REGION and ACCOUNT_ID with your values.

**Create IAM Role for Lambda**
-In IAM, create a role for Lambda, attaching the SNS Publish and Lambda Basic Execution policies.
-Save the role ARN.

**Deploy Lambda Function**
1. In Lambda, create a new function using Python 3.x.
2. Attach the IAM role, and paste the code from src/gd_notifications.py.
3. Add environment variables (NBA_API_KEY, SNS_TOPIC_ARN).
3. Create the function.
4. Deploy and Test the function

**Set Up Automation**
1. In EventBridge, create a rule to trigger the Lambda function on a schedule (e.g., hourly) using cron

**Test the System**
1. Create a test event in Lambda.
2. Run the function and check CloudWatch for logs.
3. Ensure notifications are sent, check your email

**Email Notifications**
<img width="712" alt="image" src="https://github.com/user-attachments/assets/ed232274-fadf-4ece-8d31-a43a63f32ad3" />


**What We Learned**
1. Design of a notification system with AWS SNS and Lambda.
2. Securing services with least privilege policies.
3. Automating workflows with EventBridge.
4. Integrating external APIs.

**Future Enhancements**
1. Add NFL score alerts.
2. Store user preferences in DynamoDB for personalized alerts.
3. Build a web UI.






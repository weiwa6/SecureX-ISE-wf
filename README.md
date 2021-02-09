# SecureX-ISE-wf

To demostrate the power of Cisco DevNet and SecuerX,
I've created this use case with two workflows.
1. Cisco [Talos Blog](https://blog.talosintelligence.com/ "Talos Blog") email notification, which triggers CTR investigation with the creation of a new casebook and ServiceNow incident ticket. This is based on the [original workflow](https://github.com/CiscoSecurity/sxo-05-security-workflows/tree/Main/Workflows/0001-Talos-GetNewBlogPosts__definition_workflow_01FX7FQDZRDUX1TWgKJwTPBMaOWrgUOld2q "original workflow"), with enhancement to use email trigger instead of cron-like scheduler.
2. SecureX response workflow, which triggers ISE quarantine/un-quarantine via pxGrid ANC.


------------

## Workflow 1 - New Talos Blog Email Workflow
![](screenshot/workflow1.png)

**Prerequisites:**
1. An email account that supports either POP3 or IMAP. A Gmail account is used as an example in this case.
2. Cisco SecureX Account
3. Import [0002-Talos-SingleBlogPostToCTRCasebook](https://github.com/CiscoSecurity/sxo-05-security-workflows/tree/Main/Workflows/0002-Talos-SingleBlogPostToCTRCasebook__definition_workflow_01KEM2V2JAIPS3zmyEiCmuy3kvr3wxHrEuJ "0002-Talos-SingleBlogPostToCTRCasebook") from github with all dependencies.
4. Cisco Webex Team Account (Optional), this is used to receive messages from the workflow)

### Installation Steps
Please follow the below steps exactly to get started!
1. Subscribe to Talos Blog feed [email notification](https://www.talosintelligence.com/blog_subscription "email notification")

![](screenshot/screenshot_1.png)

2. Import ["Check New Talos Blog Email.json"](https://github.com/weiwa6/SecureX-ISE-wf/blob/main/Check%20New%20Talos%20Blog%20Email.json) to SecureX as a new workflow

3. Update the Email trigger. See documents of [email events](https://ciscosecurity.github.io/sxo-05-security-workflows/events/email) and [triggers](https://ciscosecurity.github.io/sxo-05-security-workflows/workflows/triggers)

4. Send a test email with a Talos blog link and check if the script is triggered.
(Note it could be any security intelligence source url with a little change of the workflow regex)

------------

## Workflow 2 - ISE Quarantine Workflow
![](screenshot/workflow2.png)

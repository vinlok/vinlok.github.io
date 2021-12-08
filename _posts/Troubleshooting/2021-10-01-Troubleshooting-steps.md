

# Steps to handle oncall issue:

1. Assess the severity of the issue:
    1. Do i need to address this now or can this wait?
    2. Is the outage local, regional or global?
    
2. Form hypothesis on possible problem:
    1. Gather data from various monitoring tools.
        1. Follow RED for application
        2. Follow USE for infra.
        3. Is this a false alarm?
        4. What are the dependencies for the service and how are they?
        5. When did this started?
        6. What were the production changes if any?
    2. Validate or dis-approve the hyphthesis
    
3. 
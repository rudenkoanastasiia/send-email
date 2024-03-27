# Send email
<in process> 

A simple Flask applicattion, gets the json file and sending email with this data.  

# Requirenments  

# Usage

## Input JSON Data  
Provide the JSON data containing the information to be included in the email. Ensure that the JSON structure is valid and conforms to the expected schema.
```sh
{  
    'operation_name': {
        'type': 'string',
        'required': True
    },
    'user_name': {
        'type': 'string'
    },
    'list_of_groups': {
        'type': 'list(string)'
    }

}

```

## Provide secrets  

<schema>




## Specify Email Parameters
Specify email parameters such as recipients, subject, and additional message content. This enables personalized communication and ensures that the email content is relevant to the recipients.


## Customize HTML Template  
Optionally, customize the HTML template to define the layout, styling, and presentation of the data. This step allows users to tailor the appearance of the email according to their branding or design preferences.

# Tools

 * flask - https://flask.palletsprojects.com/en/3.0.x/
 * sops - https://github.com/getsops/sops


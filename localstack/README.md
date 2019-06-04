## Criar policy para lambda no IAM

```
aws --endpoint-url=http://localhost:4593 iam create-role --role-name AWSLambdaBasicExecutionRole --assume-role-policy-document file:./iam/AWSLambdaBasicExecutionRole.json
```

output

```
"Role": {
    "Path": "/",
    "RoleName": "AWSLambdaBasicExecutionRole",
    "RoleId": "ypwiebghzj4nd8z7kvhk",
    "Arn": "arn:aws:iam::000000000000:role/AWSLambdaBasicExecutionRole",
    "CreateDate": "2019-06-04 14:24:27.963517+00:00",
    "AssumeRolePolicyDocument": "file:./iam/AWSLambdaBasicExecutionRole.json"
}
```

## Criar lambda

Zipar index.js

```
zip -j ./lambda/function.zip ./lambda/index.js
```

Criar lambda

```
aws --endpoint-url=http://localhost:4574 \
lambda create-function \
--function-name=helloworld \
--runtime nodejs8.10 \
--role arn:aws:iam::000000000000:role/AWSLambdaBasicExecutionRole \
--handler index.handler \
--zip-file fileb://lambda/function.zip

```

Invoke

```
aws --endpoint-url=http://localhost:4574 \
lambda invoke \
--function-name helloworld \
--payload '{"key1":"value1", "key2":"value2", "key3":"value3"}'
```

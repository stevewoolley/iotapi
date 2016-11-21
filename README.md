## schema

### user

	aws dynamodb create-table \
	    --table-name iot-users \
	    --attribute-definitions \
	        AttributeName=username,AttributeType=S \
	    --key-schema AttributeName=username,KeyType=HASH \
	    --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5
	    
#### key

* HASH: username

#### values

* username: string

### domain

	aws dynamodb create-table \
	    --table-name iot-domains \
	    --attribute-definitions \
	        AttributeName=domain,AttributeType=S \
	    --key-schema AttributeName=domain,KeyType=HASH \
	    --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5
	    
#### key

* HASH: domain

#### values

* domain: string

### membership

	aws dynamodb create-table \
	    --table-name iot-memberships \
	    --attribute-definitions \
	        AttributeName=domain,AttributeType=S \
	        AttributeName=username,AttributeType=S \
	    --key-schema AttributeName=domain,KeyType=HASH AttributeName=username,KeyType=RANGE \
	    --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5
	    
#### key

* HASH: domain
* RANGE: username

#### values

* domain: string
* username: string

### thing

	aws dynamodb create-table \
	    --table-name iot-things \
	    --attribute-definitions \
	        AttributeName=domain,AttributeType=S \
	        AttributeName=thing,AttributeType=S \
	    --key-schema AttributeName=domain,KeyType=HASH AttributeName=thing,KeyType=RANGE \
	    --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5

#### key

* HASH: domain
* RANGE: thing

#### values

* domain: string
* thing: string

### metric

	aws dynamodb create-table \
	    --table-name iot-metrics \
	    --attribute-definitions \
	        AttributeName=domain.thing,AttributeType=S \
	        AttributeName=timestamp,AttributeType=S \
	    --key-schema AttributeName=domain.thing,KeyType=HASH AttributeName=timestamp,KeyType=RANGE \
	    --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5

#### key

* HASH: domain.thing
* RANGE: timestamp

#### values

* domain.thing: string
* timestamp: string

